"""Excel ve Markdown çıktıları.

Excel sayfaları:
  Secimler        kategorik tasarım seçimleri
  Varsayimlar     tüm parametreler: değer, aralık, kaynak, kaynak türü, güven, sınıf
  Tarama          güç başına türetilmiş büyüklükler ve $/W (sınıf ve alan bazında)
  Maliyet_dokumu  kalem kalem: birim maliyet × miktar, sınıf, formül
  Duyarlilik_<P>W tornado sıralaması (varsa)
"""
from __future__ import annotations

from pathlib import Path

import pandas as pd

from .params import ParamSet
from .secimler import Secimler

VARSAYIM_SUTUNLARI = [
    "alan", "id", "ad", "birim", "deger", "alt", "ust", "guven", "kaynak_turu", "kaynak",
    "kaynak_alintisi", "kaynak_tarihi", "maliyet_sinifi", "olcek", "senaryoya_uygunluk",
    "aciklama", "dogrulama_deneyi",
]


def varsayim_tablosu(p: ParamSet) -> pd.DataFrame:
    df = pd.DataFrame(p.kayitlar())
    return df[VARSAYIM_SUTUNLARI].sort_values(["alan", "id"]).reset_index(drop=True)


def excel_yaz(yol: Path | str, p: ParamSet, s: Secimler, ozet: pd.DataFrame, dokum: pd.DataFrame,
              duyarlilik: dict[float, pd.DataFrame] | None = None) -> Path:
    yol = Path(yol)
    yol.parent.mkdir(parents=True, exist_ok=True)
    with pd.ExcelWriter(yol, engine="openpyxl") as xw:
        pd.DataFrame(list(s.sozluk().items()), columns=["secim", "deger"]).to_excel(xw, sheet_name="Secimler", index=False)
        varsayim_tablosu(p).to_excel(xw, sheet_name="Varsayimlar", index=False)
        ozet.to_excel(xw, sheet_name="Tarama", index=False)
        dokum.to_excel(xw, sheet_name="Maliyet_dokumu", index=False)
        for P, df in (duyarlilik or {}).items():
            df.to_excel(xw, sheet_name=f"Duyarlilik_{int(P)}W", index=False)
        for ws in xw.book.worksheets:
            ws.freeze_panes = "B2"
            for col in ws.columns:
                genislik = max(len(str(c.value)) if c.value is not None else 0 for c in col[:50])
                ws.column_dimensions[col[0].column_letter].width = min(max(10, genislik + 2), 60)
    return yol


def _md_hucre(x) -> str:
    return str(x).replace("|", "\\|").replace("\n", " ")


def varsayim_markdown(p: ParamSet) -> str:
    df = varsayim_tablosu(p)
    satirlar = ["# Varsayım tablosu", "",
                "Her satır değiştirilebilir bir girdidir (`data/varsayimlar/*.yaml`). "
                "Kaynak türü `tahmin` veya `hafizadan_dogrulanmadi` olanlar doğrulanmamıştır.", ""]
    for alan, g in df.groupby("alan", sort=True):
        satirlar += [f"## {alan}", "",
                     "| id | ad | değer | aralık | birim | güven | kaynak türü | kaynak | sınıf |",
                     "|---|---|---|---|---|---|---|---|---|"]
        for _, r in g.iterrows():
            satirlar.append("| " + " | ".join(_md_hucre(v) for v in (
                r.id, r.ad, f"{r.deger:g}", f"{r.alt:g} – {r.ust:g}", r.birim, r.guven,
                r.kaynak_turu, r.kaynak, r.maliyet_sinifi)) + " |")
        satirlar.append("")
    return "\n".join(satirlar)
