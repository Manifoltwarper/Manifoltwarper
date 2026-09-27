"""Kategorik tasarım seçimleri (sayısal olmayan varsayımlar).

Sayısal varsayımlar YAML'da; burada yalnızca "hangi yol" seçimleri durur.
Her seçim tabloya ve Excel'e de yazılır.
"""
from __future__ import annotations

from dataclasses import asdict, dataclass, replace

SECENEKLER = {
    "senaryo": ("A_balkon", "B_tasinabilir"),
    "kristal_yontemi": ("RCz", "CCz", "FZ"),
    "wafer_kaynagi": ("ic", "satin_alma"),
    "ns_kurali": ("selv_max", "sabit", "optimize"),
    "cap_kurali": ("wafer_capi", "sabit_cap"),
    "wafer_geometrisi": ("psodo_kare", "kare", "altigen"),
    "metalizasyon": ("ag", "ag_cu", "cu_kaplama"),
    "pil_kaynagi": ("satin_hucre", "ic_hat"),
    "guc_kati": ("gan_planar", "si_sarimli"),
    "kutu_kurali": ("sabit_n", "hedef_guc"),
}


@dataclass(frozen=True)
class Secimler:
    senaryo: str = "A_balkon"
    kristal_yontemi: str = "RCz"
    wafer_kaynagi: str = "ic"
    ns_kurali: str = "selv_max"
    cap_kurali: str = "wafer_capi"
    wafer_geometrisi: str = "psodo_kare"
    metalizasyon: str = "ag"
    pil_kaynagi: str = "satin_hucre"
    guc_kati: str = "gan_planar"
    kutu_kurali: str = "hedef_guc"

    def __post_init__(self):
        for k, izinli in SECENEKLER.items():
            v = getattr(self, k)
            if v not in izinli:
                raise ValueError(f"{k}='{v}' geçersiz; seçenekler: {izinli}")

    def degistir(self, **kw) -> "Secimler":
        return replace(self, **kw)

    def sozluk(self) -> dict:
        return asdict(self)
