"""Model orkestratörü: tek bir panel gücü için tüm zinciri hesaplar.

Akış (her adım bir alan modülü; hepsi `d` türetilmiş-değer sözlüğünü doldurur
ve maliyet kalemlerini `L` defterine yazar):

  tasarim   P_panel → N_s, N_p, hücre/wafer boyutu, ingot çapı, kutu gücü, pil Wh
  kristal   ingot çapı → fırın kg/gün, kWh/kg, fırın-saat maliyeti
  wafer     kütle/adet dengesi, geri dönüşüm döngüsü → wafer/gün, testere
  hucre     HJT adımları → hücre/gün, verim, malzeme, ekipman sayısı
  modul     panel/gün, BOM, laminasyon, test
  pil       Wh/gün ihtiyacı → pil hücresi/gün, hat sayısı, pil maliyeti
  elektronik kutu gücü → MPPT/BMS/inverter maliyeti
  altyapi   saha-paylaşımlı altyapı + ekonomik girdiler → ünite payı
  standart  ünite başı zorunlu testler + varyant başı sertifikasyon
"""
from __future__ import annotations

from dataclasses import dataclass, field

from .costs import Ledger
from .params import ParamSet
from .secimler import Secimler
from .domains import altyapi, elektronik, hucre, kristal, modul, pil, standart, tasarim, wafer

ADIMLAR = (
    ("tasarim", tasarim.hesapla),
    ("kristal", kristal.hesapla),
    ("wafer", wafer.hesapla),
    ("hucre", hucre.hesapla),
    ("modul", modul.hesapla),
    ("pil", pil.hesapla),
    ("elektronik", elektronik.hesapla),
    ("altyapi", altyapi.hesapla),
    ("standart", standart.hesapla),
)


@dataclass
class Sonuc:
    P_panel_W: float
    secimler: Secimler
    turetilmis: dict = field(default_factory=dict)
    defter: Ledger | None = None
    uyarilar: list[str] = field(default_factory=list)

    @property
    def usd_per_W(self) -> float:
        return self.defter.usd_per_W()

    def ozet_satiri(self) -> dict:
        row = {"P_panel_W": self.P_panel_W}
        row.update({k: v for k, v in self.turetilmis.items() if isinstance(v, (int, float, str))})
        row["usd_per_W_panel"] = self.defter.usd_per_W("panel")
        row["usd_per_W_kutu"] = self.defter.usd_per_W("kutu")
        row["usd_per_W_sistem"] = self.defter.usd_per_W()
        for g, v in self.defter.grupla("sinif").items():
            row[f"sinif_{g}_usd_per_W"] = v
        for g, v in self.defter.grupla("alan").items():
            row[f"alan_{g}_usd_per_W"] = v
        row["uyarilar"] = " | ".join(self.uyarilar)
        return row


def degerlendir(p: ParamSet, s: Secimler, P_panel_W: float) -> Sonuc:
    d: dict = {"P_panel_W": float(P_panel_W)}
    L = Ledger(P_panel_W=float(P_panel_W))
    uyarilar: list[str] = []
    d["_uyarilar"] = uyarilar
    for _ad, fn in ADIMLAR:
        fn(p, s, d, L)
    d.pop("_uyarilar")
    return Sonuc(P_panel_W=float(P_panel_W), secimler=s, turetilmis=d, defter=L, uyarilar=uyarilar)
