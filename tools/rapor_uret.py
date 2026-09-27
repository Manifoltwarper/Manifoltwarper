"""Faz 1 araştırma çıktılarından onay paketi belgelerini üretir.

Kullanım: python tools/rapor_uret.py <arastirma_dizini>
  <arastirma_dizini>/<alan>.json  alan ajanlarının revize çıktıları (+ kırmızı takım raporları)

Üretilenler:
  docs/formul_envanteri.md        her alanın formülleri (girdi, çıktı, birim, sınıf)
  docs/varsayim_tablosu.md        tüm varsayımlar (alan bazında)
  docs/faz1_varsayimlar.xlsx      aynı tablo + formüller + deneyler + itirazlar (filtrelenebilir)
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

import pandas as pd

KOK = Path(__file__).resolve().parent.parent
ALANLAR = ["kristal", "wafer", "hucre", "modul", "elektronik", "pil", "altyapi", "standart"]
ALAN_ADI = {
    "kristal": "Kristal / fırın", "wafer": "Wafer", "hucre": "Hücre (HJT)", "modul": "Modül",
    "elektronik": "Elektronik (MPPT/BMS/inverter)", "pil": "Pil (Na-iyon)",
    "altyapi": "Saha altyapısı, İSG ve ekonomi", "standart": "Standartlar ve mevzuat",
}


def _h(x) -> str:
    return str(x).replace("|", "\\|").replace("\n", " ").strip()


def yukle(dizin: Path) -> dict:
    out = {}
    for a in ALANLAR:
        yol = dizin / f"{a}.json"
        if yol.exists():
            d = json.loads(yol.read_text(encoding="utf-8"))
            out[a] = d["revize"] or d["ilk"]
    return out


def formul_envanteri(R: dict) -> str:
    L = ["# Formül envanteri (Faz 1 iskeleti)", "",
         "Her alanın hesap zinciri. Formüller Python ifadesi olarak yazılmıştır; girdiler "
         "`data/varsayimlar/*.yaml` parametre id'leri ve arayüz değişkenleridir "
         "(`P_panel_W, N_s, N_p, a_wafer_mm, t_wafer_um, D_ingot_mm, k_split, A_cell_m2, eta_cell, "
         "P_box_W, n_panel_per_box, E_batt_Wh, V_lim ...`).", "",
         "> Durum: araştırma ajanlarının önerdiği formüller; kodlanması Faz 2'de (onaydan sonra). "
         "Alanlar arası uzlaştırma notları `docs/uzlastirma.md` içindedir.", ""]
    for a, r in R.items():
        L += [f"## {ALAN_ADI[a]} (`{a}`) — {len(r['formuller'])} formül", "",
              "| id | çıktı | birim | sınıf | ifade | açıklama |", "|---|---|---|---|---|---|"]
        for f in r["formuller"]:
            L.append(f"| {_h(f['id'])} | `{_h(f['cikti'])}` | {_h(f['cikti_birimi'])} | {_h(f['maliyet_sinifi'])} "
                     f"| `{_h(f['ifade'])}` | {_h(f['aciklama'])} |")
        L.append("")
    return "\n".join(L)


def varsayim_df(R: dict) -> pd.DataFrame:
    """Uzlaştırılmış varsayımlar (data/varsayimlar/*.yaml; düzeltmeler ve eşdeğerler uygulanmış)."""
    sys.path.insert(0, str(KOK))
    from pvbat.params import ParamSet
    ps = ParamSet.load(KOK / "data" / "varsayimlar")
    sira = {a: i for i, a in enumerate(ALANLAR)}
    df = pd.DataFrame(ps.kayitlar())
    df["esdeger_carpan"] = df["esdeger_carpan"].where(df["esdeger"] != "", "")
    cols = ["alan", "id", "ad", "birim", "deger", "alt", "ust", "guven", "kaynak_turu", "kaynak", "kaynak_alintisi",
            "kaynak_tarihi", "maliyet_sinifi", "olcek", "esdeger", "esdeger_carpan", "senaryoya_uygunluk",
            "aciklama", "dogrulama_deneyi"]
    return df[cols].sort_values(by="alan", key=lambda s: s.map(sira), kind="stable").reset_index(drop=True)


def varsayim_md(df: pd.DataFrame, R: dict) -> str:
    n = len(df)
    kt = df["kaynak_turu"].value_counts()
    gv = df["guven"].value_counts()
    L = ["# Varsayım tablosu (Faz 1)", "",
         f"Toplam **{n}** parametre. Kaynak türü dağılımı: " +
         ", ".join(f"{k} {v}" for k, v in kt.items()) + ". Güven: " +
         ", ".join(f"{k} {v}" for k, v in gv.items()) + ".", "",
         "Kaynak türleri: `dogrulanmis_url` = sayfa bu çalışmada açıldı ve değer görüldü; "
         "`arama_ozeti` = yalnız arama özeti (güven ≤ orta); `standart_metni_dogrulanmis`; "
         "`hafizadan_dogrulanmadi` (güven ≤ orta); `fizik_ders_kitabi`; `hesap_turetilmis`; "
         "`tahmin` (dayanak yazılı, güven ≤ orta). Uydurma kaynak kural olarak yasaktı; bilinmeyen "
         "'bilmiyoruz + doğrulama deneyi' olarak işaretlidir.", "",
         "**Kaynak denetimi (ölçülen):** kırmızı takım revizyon öncesi 393 kaynağı sayfayı yeniden açarak "
         "kontrol etti: 271 destekliyor, 96 kısmen, 21 erişilemedi, 5 desteklemiyor, 0 uydurma şüphesi; "
         "bulgular revizyonda düzeltildi. Revizyon sonrası bağımsız örneklem denetiminin sonucu "
         "`docs/kaynak_denetimi.md` içindedir. Bu oranlar 'doğrulanmış' etiketli her satırın doğru olduğu "
         "anlamına gelmez; kritik parametreler kullanılmadan önce ayrıca kontrol edilmelidir.",
         "", "Filtrelenebilir tam tablo (kaynak alıntıları, senaryoya uygunluk, doğrulama deneyi dahil): "
         "`docs/faz1_varsayimlar.xlsx`.", ""]
    for a, g in df.groupby("alan", sort=False):
        L += [f"## {ALAN_ADI[a]} (`{a}`) — {len(g)} parametre", "",
              "| id | ad | değer | aralık | birim | güven | kaynak türü | sınıf | eşdeğer | kaynak |",
              "|---|---|---|---|---|---|---|---|---|---|"]
        for _, p in g.iterrows():
            esd = f"→ `{p['esdeger']}`" + (f" × {p['esdeger_carpan']:g}" if p["esdeger"] and p["esdeger_carpan"] != 1 else "") if p["esdeger"] else ""
            L.append(f"| {_h(p['id'])} | {_h(p['ad'])} | {p['deger']:g} | {p['alt']:g} – {p['ust']:g} | {_h(p['birim'])} "
                     f"| {p['guven']} | {p['kaynak_turu']} | {p['maliyet_sinifi']} | {esd} | {_h(str(p['kaynak'])[:140])} |")
        L.append("")
    return "\n".join(L)


def ek_tablolar(R: dict) -> dict[str, pd.DataFrame]:
    f, d, i, s = [], [], [], []
    for a, r in R.items():
        for x in r["formuller"]:
            f.append({"alan": a, **{k: (", ".join(v) if isinstance(v, list) else v) for k, v in x.items()}})
        for x in r["bilinmeyenler_ve_deneyler"]:
            d.append({"alan": a, **{k: (", ".join(v) if isinstance(v, list) else v) for k, v in x.items()}})
        for x in r["itirazlar"]:
            i.append({"alan": a, **x})
        for x in r["dogal_sinirlar"]:
            s.append({"alan": a, **x})
    return {"Formuller": pd.DataFrame(f), "Deneyler_alan": pd.DataFrame(d).sort_values("oncelik"),
            "Itirazlar_alan": pd.DataFrame(i), "Dogal_sinirlar": pd.DataFrame(s)}


def excel(df: pd.DataFrame, ekler: dict, yol: Path) -> None:
    with pd.ExcelWriter(yol, engine="openpyxl") as xw:
        df.to_excel(xw, sheet_name="Varsayimlar", index=False)
        for ad, t in ekler.items():
            t.to_excel(xw, sheet_name=ad, index=False)
        for ws in xw.book.worksheets:
            ws.freeze_panes = "C2"
            ws.auto_filter.ref = ws.dimensions
            for col in ws.columns:
                w = max((len(str(c.value)) for c in col[:60] if c.value is not None), default=8)
                ws.column_dimensions[col[0].column_letter].width = min(max(8, w + 2), 50)


def main(dizin: str) -> None:
    R = yukle(Path(dizin))
    docs = KOK / "docs"
    docs.mkdir(exist_ok=True)
    (docs / "formul_envanteri.md").write_text(formul_envanteri(R), encoding="utf-8")
    df = varsayim_df(R)
    (docs / "varsayim_tablosu.md").write_text(varsayim_md(df, R), encoding="utf-8")
    excel(df, ek_tablolar(R), docs / "faz1_varsayimlar.xlsx")
    print(f"{len(R)} alan, {len(df)} parametre, {sum(len(r['formuller']) for r in R.values())} formül yazıldı")


if __name__ == "__main__":
    main(sys.argv[1])
