"""Parametre (varsayım) kaydı.

Her varsayım `data/varsayimlar/<alan>.yaml` içinde bir kayıttır: değer, aralık,
kaynak, kaynak türü, güven düzeyi ve maliyet sınıfı. Model hiçbir sayıyı kod
içinde sabit tutmaz; her sayı buradan okunur ve değiştirilebilir.
"""
from __future__ import annotations

from dataclasses import asdict, dataclass, fields
from pathlib import Path
from typing import Iterable, Iterator, Mapping

import yaml

KAYNAK_TURLERI = (
    "dogrulanmis_url",
    "arama_ozeti",
    "standart_metni_dogrulanmis",
    "hafizadan_dogrulanmadi",
    "fizik_ders_kitabi",
    "hesap_turetilmis",
    "tahmin",
)
GUVEN_DUZEYLERI = ("yuksek", "orta", "dusuk")
MALIYET_SINIFLARI = ("alan", "adet", "zaman", "guc_enerji", "urun_sabit", "saha_sabit", "teknik")
OLCEKLER = ("unite", "saha", "urun", "genel")

# Kaynak türüne göre izin verilen en yüksek güven düzeyi.
_GUVEN_TAVANI = {
    "arama_ozeti": "orta",
    "hafizadan_dogrulanmadi": "orta",
    "tahmin": "orta",
}
_GUVEN_SIRASI = {g: i for i, g in enumerate(reversed(GUVEN_DUZEYLERI))}  # dusuk=0 .. yuksek=2

VARSAYILAN_DIZIN = Path(__file__).resolve().parent.parent / "data" / "varsayimlar"


@dataclass(frozen=True)
class Param:
    id: str
    ad: str
    birim: str
    deger: float
    alt: float
    ust: float
    alan: str
    kaynak: str = "tahmin"
    kaynak_turu: str = "tahmin"
    kaynak_alintisi: str = ""
    kaynak_tarihi: str = ""
    guven: str = "dusuk"
    maliyet_sinifi: str = "teknik"
    olcek: str = "unite"
    senaryoya_uygunluk: str = ""
    aciklama: str = ""
    dogrulama_deneyi: str = ""
    # Eşdeğer (takma ad): bu kavramın tek sahibi başka bir parametredir. Değer her zaman
    # esdeger × esdeger_carpan olarak okunur; kendi 'deger' alanı yalnızca kayıt içindir.
    esdeger: str = ""
    esdeger_carpan: float = 1.0

    def hatalar(self) -> list[str]:
        """Kayıt tutarlılık hataları (boş liste = geçerli)."""
        h = []
        if not (self.alt <= self.deger <= self.ust):
            h.append(f"{self.id}: aralık dışı (alt={self.alt}, deger={self.deger}, ust={self.ust})")
        if self.kaynak_turu not in KAYNAK_TURLERI:
            h.append(f"{self.id}: bilinmeyen kaynak_turu '{self.kaynak_turu}'")
        if self.guven not in GUVEN_DUZEYLERI:
            h.append(f"{self.id}: bilinmeyen guven '{self.guven}'")
        if self.maliyet_sinifi not in MALIYET_SINIFLARI:
            h.append(f"{self.id}: bilinmeyen maliyet_sinifi '{self.maliyet_sinifi}'")
        if self.olcek not in OLCEKLER:
            h.append(f"{self.id}: bilinmeyen olcek '{self.olcek}'")
        tavan = _GUVEN_TAVANI.get(self.kaynak_turu)
        if tavan and _GUVEN_SIRASI.get(self.guven, 0) > _GUVEN_SIRASI[tavan]:
            h.append(f"{self.id}: '{self.kaynak_turu}' kaynağıyla güven '{self.guven}' olamaz (tavan: {tavan})")
        if self.kaynak_turu == "tahmin" and not self.aciklama.strip():
            h.append(f"{self.id}: 'tahmin' için dayanak (aciklama) boş")
        return h


class ParamSet(Mapping[str, float]):
    """Parametre değerleri + meta veri. `p.cz_pull_rate_mm_min` ile okunur.

    `override()` yeni bir ParamSet döndürür; orijinal değişmez (duyarlılık
    analizi ve senaryolar bunu kullanır). Okunan anahtarlar `kullanilan`
    kümesinde tutulur; hiç okunmayan varsayımlar raporlanabilir.
    """

    def __init__(self, params: Mapping[str, Param], values: Mapping[str, float] | None = None):
        object.__setattr__(self, "_meta", dict(params))
        object.__setattr__(self, "_values", dict(values) if values is not None else {k: v.deger for k, v in params.items()})
        object.__setattr__(self, "kullanilan", set())

    # --- okuma ---
    def __getattr__(self, name: str) -> float:
        values = object.__getattribute__(self, "_values")
        if name in values:
            object.__getattribute__(self, "kullanilan").add(name)
            m = object.__getattribute__(self, "_meta").get(name)
            if m is not None and m.esdeger:
                return self.__getattr__(m.esdeger) * m.esdeger_carpan
            return values[name]
        raise AttributeError(f"Tanımsız parametre: {name}")

    def __setattr__(self, name, value):
        raise AttributeError("ParamSet değişmezdir; override() kullanın")

    def __getitem__(self, key: str) -> float:
        try:
            return self.__getattr__(key)
        except AttributeError as e:
            raise KeyError(key) from e

    def __contains__(self, key: object) -> bool:
        return key in self._values

    def __iter__(self) -> Iterator[str]:
        return iter(self._values)

    def __len__(self) -> int:
        return len(self._values)

    def meta(self, key: str) -> Param:
        return self._meta[key]

    def metas(self) -> Iterable[Param]:
        return self._meta.values()

    # --- değiştirme ---
    def override(self, **values: float) -> "ParamSet":
        bilinmeyen = set(values) - set(self._values)
        if bilinmeyen:
            raise KeyError(f"Tanımsız parametre(ler): {sorted(bilinmeyen)}")
        takma = [k for k in values if self._meta[k].esdeger]
        if takma:
            raise KeyError(f"Eşdeğer parametre değiştirilemez; sahibini değiştirin: "
                           f"{ {k: self._meta[k].esdeger for k in takma} }")
        new = dict(self._values)
        new.update(values)
        return ParamSet(self._meta, new)

    # --- yükleme / doğrulama ---
    @classmethod
    def load(cls, dizin: Path | str = VARSAYILAN_DIZIN) -> "ParamSet":
        dizin = Path(dizin)
        params: dict[str, Param] = {}
        izinli = {f.name for f in fields(Param)}
        for yol in sorted(dizin.glob("*.yaml")):
            veri = yaml.safe_load(yol.read_text(encoding="utf-8")) or {}
            alan = veri.get("alan", yol.stem)
            for kayit in veri.get("parametreler", []):
                kayit = dict(kayit)
                kayit.setdefault("alan", alan)
                fazla = set(kayit) - izinli
                if fazla:
                    raise ValueError(f"{yol.name}:{kayit.get('id')}: bilinmeyen alan(lar) {sorted(fazla)}")
                p = Param(**kayit)
                if p.id in params:
                    raise ValueError(f"Yinelenen parametre id: {p.id} ({yol.name} ve {params[p.id].alan})")
                params[p.id] = p
        return cls(params)

    def dogrula(self) -> list[str]:
        hatalar: list[str] = []
        for p in self._meta.values():
            hatalar.extend(p.hatalar())
            if p.esdeger:
                hedef = self._meta.get(p.esdeger)
                if hedef is None:
                    hatalar.append(f"{p.id}: eşdeğer hedefi tanımsız '{p.esdeger}'")
                elif hedef.esdeger:
                    hatalar.append(f"{p.id}: eşdeğer zinciri ({p.esdeger} de eşdeğer); tek sahibe bağlanmalı")
        return hatalar

    def sahipler(self) -> list[str]:
        """Eşdeğer olmayan (bağımsız) parametreler — duyarlılık analizi bunları gezer."""
        return [k for k, m in self._meta.items() if not m.esdeger]

    def kayitlar(self) -> list[dict]:
        """Varsayım tablosu satırları (güncel değerle)."""
        out = []
        for k, p in self._meta.items():
            d = asdict(p)
            d["deger"] = self._values[k]
            out.append(d)
        return out
