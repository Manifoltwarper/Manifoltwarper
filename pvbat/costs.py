"""Maliyet kalemleri ve defter.

Her kalem = birim maliyet × sürücü miktarı (panel başına). Böylece döküm
tablosunda her kalemin "neyle ölçeklendiği" ve formülü açıkça görünür.

Maliyet sınıfları (kullanıcının üç sınıfı + önerilen ekler):
  alan        işlenen alanla (m² wafer/hücre/modül) veya kalınlık üzerinden Si kütlesiyle
  adet        wafer/hücre/panel/kutu/pil hücresi başına
  zaman       ekipman saati başına (amortisman, baz enerji, işçilik, pota ömrü, bakım)
  guc_enerji  W veya Wh ile (güç katı, pil)                      [önerilen ek]
  urun_sabit  ürün varyantı başına sabit (sertifikasyon, kalıp) → hacme bölünür  [önerilen ek]
  saha_sabit  saha başına paylaşılan altyapı → ünite sayısına bölünür
"""
from __future__ import annotations

from dataclasses import asdict, dataclass, field

SINIFLAR = ("alan", "adet", "zaman", "guc_enerji", "urun_sabit", "saha_sabit")
KAPSAMLAR = ("panel", "kutu")  # kutu = elektronik + pil kutusu (n panel besler)


@dataclass(frozen=True)
class CostItem:
    id: str
    ad: str
    alan: str            # hangi alan (kristal, wafer, hucre, ...)
    sinif: str           # SINIFLAR'dan biri
    birim_maliyet: float  # USD / sürücü birimi
    surucu: str          # sürücü birimi: "m2 wafer", "wafer", "firin-saat", "W", "Wh", ...
    miktar: float        # panel başına sürücü miktarı
    formul: str          # insan-okur formül (parametre id'leriyle)
    kapsam: str = "panel"

    def __post_init__(self):
        if self.sinif not in SINIFLAR:
            raise ValueError(f"{self.id}: bilinmeyen maliyet sınıfı '{self.sinif}'")
        if self.kapsam not in KAPSAMLAR:
            raise ValueError(f"{self.id}: bilinmeyen kapsam '{self.kapsam}'")

    @property
    def usd_per_panel(self) -> float:
        return self.birim_maliyet * self.miktar


@dataclass
class Ledger:
    """Bir tasarım noktasının (tek P_panel) maliyet defteri."""

    P_panel_W: float
    kalemler: list[CostItem] = field(default_factory=list)

    def ekle(self, *items: CostItem) -> None:
        ids = {k.id for k in self.kalemler}
        for it in items:
            if it.id in ids:
                raise ValueError(f"Yinelenen maliyet kalemi: {it.id}")
            ids.add(it.id)
            self.kalemler.append(it)

    def extend(self, items) -> None:
        self.ekle(*items)

    def toplam_panel(self, kapsam: str | None = None) -> float:
        return sum(k.usd_per_panel for k in self.kalemler if kapsam is None or k.kapsam == kapsam)

    def usd_per_W(self, kapsam: str | None = None) -> float:
        return self.toplam_panel(kapsam) / self.P_panel_W

    def grupla(self, anahtar: str, per_W: bool = True) -> dict[str, float]:
        """anahtar: 'sinif', 'alan' veya 'kapsam'."""
        out: dict[str, float] = {}
        bolen = self.P_panel_W if per_W else 1.0
        for k in self.kalemler:
            g = getattr(k, anahtar)
            out[g] = out.get(g, 0.0) + k.usd_per_panel / bolen
        return out

    def satirlar(self) -> list[dict]:
        rows = []
        for k in self.kalemler:
            d = asdict(k)
            d["usd_per_panel"] = k.usd_per_panel
            d["usd_per_W"] = k.usd_per_panel / self.P_panel_W
            d["P_panel_W"] = self.P_panel_W
            rows.append(d)
        return rows
