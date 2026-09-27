"""Faz 1 araştırma çıktısını (alan JSON) data/varsayimlar/<alan>.yaml'a çevirir.

Kullanım: python tools/arastirma_to_yaml.py <faz1_dizini> <cikti_dizini>
Dönüşüm mekaniktir; değerler değiştirilmez. 'not' alanı 'aciklama' olur.
"""
import json
import sys
from pathlib import Path

import yaml

ALAN_SIRASI = ["kristal", "wafer", "hucre", "modul", "elektronik", "pil", "altyapi", "standart"]


def donustur(kaynak: Path, hedef: Path) -> None:
    hedef.mkdir(parents=True, exist_ok=True)
    for alan in ALAN_SIRASI:
        yol = kaynak / f"{alan}.json"
        if not yol.exists():
            print(f"atlandı (yok): {alan}")
            continue
        a = json.loads(yol.read_text(encoding="utf-8"))
        r = a["revize"] or a["ilk"]
        params = []
        for p in r["parametreler"]:
            q = {k: p.get(k, "") for k in ("id", "ad", "birim", "deger", "alt", "ust", "kaynak", "kaynak_turu",
                                          "kaynak_alintisi", "kaynak_tarihi", "guven", "maliyet_sinifi", "olcek",
                                          "senaryoya_uygunluk")}
            q["aciklama"] = p.get("not", "")
            q["dogrulama_deneyi"] = p.get("dogrulama_deneyi", "")
            params.append(q)
        out = {"alan": alan, "ozet": r["ozet"], "parametreler": params}
        (hedef / f"{alan}.yaml").write_text(
            yaml.safe_dump(out, allow_unicode=True, sort_keys=False, width=110), encoding="utf-8")
        print(f"{alan}: {len(params)} parametre")


if __name__ == "__main__":
    donustur(Path(sys.argv[1]), Path(sys.argv[2]))
