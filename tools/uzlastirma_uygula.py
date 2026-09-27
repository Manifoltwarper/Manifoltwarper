"""Uzlaştırma çıktılarını varsayım düzeltmelerine çevirir → arastirma/duzeltmeler.json

Kaynaklar (varsa):
  arastirma/faz1b/ekonomi.json   ortak ekonomik girdiler: kanonik değer + eşdeğerler
  arastirma/faz1b/zincir.json    teknik ortak büyüklükler: kanonik değer + eşdeğerler
  arastirma/faz1b/dayanak.json   dayanağı boş 'tahmin' parametrelerine dayanak metni
  KAYNAK_ORNEKLEM (aşağıda)      revizyon sonrası kaynak örneklem denetiminin düzeltmeleri

Araştırma kaydı (arastirma/faz1/*.json) değiştirilmez. Çıktı biçimi:
  { "<param_id>": {alan: yeni değer, ...}, ...,
    "_yeni": [ {yeni parametre kaydı + 'alan'} ],
    "_formul_degiskenleri": { "<formüldeki serbest değişken>": "<kanonik id>" },
    "_rapor": [ "insan-okur notlar" ] }
"""
from __future__ import annotations

import json
from pathlib import Path

KOK = Path(__file__).resolve().parent.parent
AR = KOK / "arastirma"
ALANLAR = ["kristal", "wafer", "hucre", "modul", "elektronik", "pil", "altyapi", "standart"]

# Eşdeğer yapılmayacak takma adlar (uzlaştırmanın kendisi farklı kavram olduğunu söylüyor).
ESDEGER_DISI = {
    "el_discount_rate": "Uzlaştırma: yalnız müşteri iskonto oranı olarak kalır (GaN/verim değeri); şirket WACC'ı değil.",
}
# Birim dönüşümü gereken eşdeğerler: takma = kanonik × çarpan
CARPAN = {
    ("xtal_price_argon_usd_nm3", "eco_price_argon_usd_kg"): (1.784, "1 Nm3 Ar = 1,784 kg (0 °C, 1 atm)"),
    ("mod_cu_price_usd_kg", "el_cu_price_usd_kg"): (1.1, "LME × 1,1 örgü/kablolama payı (tahmin)"),
    ("mod_beta_voc_per_K", "hjt_tc_voc_pct_per_K"): (0.01, "%/K → 1/K"),
}
# Teknik zincir görevi 'takma_adlar' listesine ilişkili ama farklı büyüklükleri de (olgun/ilk nesil uçları,
# hücre ve dizi gerilimleri, farklı model biçimleri) koymuş. Bu yüzden zincirde yalnız elle doğrulanmış,
# gerçekten aynı büyüklük olan eşleşmeler eşdeğer yapılır; diğerleri 'ilişkili' notu olarak kalır.
ZINCIR_ESDEGER = {
    "mod_voc_cell_stc_V": "hjt_voc_cell_V",
    "mod_beta_voc_per_K": "hjt_tc_voc_pct_per_K",
    "mod_T_min_design_C": "std_tmin_site_c",
    "el_V_lim_wet_V": "std_dvca_dc_wet_v",
    "mod_classIII_voc_max_V": "std_class3_voc_stc_max_v",
    "mod_classIII_isc_max_A": "std_class3_isc_max_a",
    "wf_texture_removal_um": "hjt_si_etch_removal_um",
    "el_E_cell_Wh": "bat_E_cell_Wh",
    "el_Vcell_max_na_V": "bat_cell_v_max_V",
    "el_Vcell_min_use_V": "bat_v_min_cutoff_V",
    "el_N_batt_series": "bat_ns_cells",
    "el_N_cell_per_year": "bat_line_cells_per_year",
    "wf_tail_h_over_D": "cz_tail_length_ratio",
    "wf_crown_h_over_D": "cz_shoulder_height_ratio",
}
KAYNAK_ORNEKLEM = {
    "saw_wire_price_steel_usd_km": ("hesap_turetilmis", "kaynak 17 RMB/km veriyor (2024, çelik ve tungsten karışık ortalama); 2024 kuruyla ~2,36–2,40 USD/km. 2,5 USD/km bundan %5–6 yüksek; çelik çekirdek için ayrı fiyat kaynakta yok."),
    "hjt_ito_thickness_total_nm": ("hafizadan_dogrulanmadi", "açılan kaynak yüzey başına ~100 nm (toplam ~200 nm) veriyor; 180 nm değeri Louwen 2016'ya dayandırılmış ama URL yok ve doğrulanamadı."),
    "mod_T_min_design_C": ("hesap_turetilmis", "MGM rekorları doğru (İstanbul −9,0; Ankara −24,9; Erzurum −37,2 °C); −20 °C bir tasarım seçimi, sayfalarda yok. Ankara ve Erzurum için muhafazakâr değil; pazara göre seçilmeli (KK3)."),
    "bat_cell_v_nom_nfpp_V": ("hesap_turetilmis", "kaynaklar NFPP için 2,85–3,10 V aralığı veriyor; 2,9 V bu aralıktan seçilmiş muhafazakâr değer, doğrudan yazılı değil."),
    "bat_cycle_life_nfpp_pris": ("hesap_turetilmis", "5000 çevrim kaynaklarda doğrudan yok; 0,5C'de 6000 ile 1C'de 3000 arasından seçilmiş. Highstar'ın 10 000 çevrimi %70 kapasite içindir (%80 değil)."),
}


def _ekle(mevcut: str, yeni: str) -> str:
    return f"{mevcut} | {yeni}" if mevcut and mevcut.strip() not in ("", "-") else yeni


def yukle_parametreler() -> dict[str, dict]:
    P = {}
    for a in ALANLAR:
        r = json.loads((AR / "faz1" / f"{a}.json").read_text(encoding="utf-8"))
        r = r["revize"] or r["ilk"]
        for p in r["parametreler"]:
            P[p["id"]] = {**p, "alan": a}
    return P


def uygula() -> dict:
    P = yukle_parametreler()
    D: dict = {}
    rapor: list[str] = []
    yeni: list[dict] = []
    formul_deg: dict[str, str] = {}

    def duz(pid: str) -> dict:
        return D.setdefault(pid, {})

    def aciklama(pid: str) -> str:
        return D.get(pid, {}).get("aciklama", P[pid].get("not", ""))

    # 1) kaynak örneklemi
    for pid, (kt, nt) in KAYNAK_ORNEKLEM.items():
        g = P[pid]["guven"]
        duz(pid).update({"kaynak_turu": kt, "guven": "orta" if g == "yuksek" else g,
                         "aciklama": _ekle(aciklama(pid), f"Örneklem denetimi (2026-09-27): {nt}")})

    # 2) dayanak
    yol = AR / "faz1b" / "dayanak.json"
    if yol.exists():
        for x in json.loads(yol.read_text(encoding="utf-8"))["sonuc"]["duzeltmeler"]:
            if x["id"] in P:
                duz(x["id"])["aciklama"] = _ekle(aciklama(x["id"]), x["aciklama_yeni"])
                if x.get("oneri", "").strip() and x["oneri"].strip() not in ("-", "Yok", "yok"):
                    rapor.append(f"dayanak/{x['id']}: öneri — {x['oneri']}")
            else:
                rapor.append(f"dayanak: bilinmeyen id {x['id']}")

    # 3) kanonik parametreler (ekonomi, zincir)
    sahip_kaynagi: dict[str, str] = {}
    tum_kanonik = set()
    for gorev in ("ekonomi", "zincir"):
        yol = AR / "faz1b" / f"{gorev}.json"
        if yol.exists():
            tum_kanonik |= {k["kanonik_id"] for k in json.loads(yol.read_text(encoding="utf-8"))["sonuc"]["kanonik_parametreler"]}
    for gorev in ("ekonomi", "zincir"):
        yol = AR / "faz1b" / f"{gorev}.json"
        if not yol.exists():
            continue
        for k in json.loads(yol.read_text(encoding="utf-8"))["sonuc"]["kanonik_parametreler"]:
            kid = k["kanonik_id"]
            if kid in sahip_kaynagi:
                rapor.append(f"{gorev}: {kid} zaten {sahip_kaynagi[kid]} tarafından kanonik; ikinci tanım yok sayıldı")
                continue
            sahip_kaynagi[kid] = gorev
            alanlar = {"deger": k["deger"], "alt": k["alt"], "ust": k["ust"], "kaynak": k["kaynak"],
                       "kaynak_turu": k["kaynak_turu"], "kaynak_alintisi": k["kaynak_alintisi"], "guven": k["guven"]}
            if not (k["alt"] <= k["deger"] <= k["ust"]):
                rapor.append(f"{gorev}: {kid} kanonik değer aralık dışı — atlandı")
                continue
            notu = f"[Uzlaştırma/{gorev}] Kanonik (tek sahip). {k['gerekce_secim']}"
            if kid in P:
                duz(kid).update(alanlar)
                duz(kid)["aciklama"] = _ekle(aciklama(kid), notu)
            else:
                yeni.append({"id": kid, "ad": k["kavram"], "birim": k["birim"], **alanlar, "alan": "altyapi",
                             "maliyet_sinifi": "teknik", "olcek": "genel", "senaryoya_uygunluk": "",
                             "aciklama": notu, "dogrulama_deneyi": ""})
                rapor.append(f"{gorev}: yeni kanonik parametre {kid} (altyapi)")
            for t in k["takma_adlar"]:
                tid = t["id"]
                if tid == kid:
                    continue
                if tid not in P:
                    formul_deg[tid] = kid
                    continue
                if tid in tum_kanonik:  # ayrı rol: kendisi de kanonik, eşdeğer yapılmaz
                    duz(tid)["aciklama"] = _ekle(aciklama(tid), f"[Uzlaştırma/{gorev}] {kid} ile ilişkili ama ayrı kanonik: {t['fark_aciklamasi']}")
                    continue
                if gorev == "zincir" and ZINCIR_ESDEGER.get(tid) != kid:
                    if tid in ZINCIR_ESDEGER:  # doğru sahibine ayrıca bağlanacak
                        continue
                    duz(tid)["aciklama"] = _ekle(aciklama(tid), f"[Uzlaştırma/zincir] İlişkili (eşdeğer değil) → {kid}: {t['fark_aciklamasi']}")
                    continue
                if tid in ESDEGER_DISI:
                    duz(tid)["aciklama"] = _ekle(aciklama(tid), ESDEGER_DISI[tid])
                    continue
                carpan, cnot = CARPAN.get((tid, kid), (1.0, ""))
                duz(tid).update({"esdeger": kid, "esdeger_carpan": carpan,
                                 "aciklama": _ekle(aciklama(tid), f"[Uzlaştırma/{gorev}] Eşdeğer: değer {kid}"
                                                   f"{' × ' + str(carpan) + ' (' + cnot + ')' if carpan != 1.0 else ''}"
                                                   f" üzerinden okunur. Fark: {t['fark_aciklamasi']}")})
    # zincir listesinde yanlış kanonik altında duran doğrulanmış eşleşmeler
    for tid, kid in ZINCIR_ESDEGER.items():
        if tid in P and not D.get(tid, {}).get("esdeger") and (kid in P or any(y["id"] == kid for y in yeni)):
            carpan, cnot = CARPAN.get((tid, kid), (1.0, ""))
            duz(tid).update({"esdeger": kid, "esdeger_carpan": carpan,
                             "aciklama": _ekle(aciklama(tid), f"[Uzlaştırma/zincir, elle doğrulandı] Eşdeğer: değer {kid} üzerinden okunur.")})
    # eşdeğer hedefinin kendisi başka yerde eşdeğer yapıldıysa zinciri kır
    for pid, d in D.items():
        hedef = d.get("esdeger")
        if hedef and D.get(hedef, {}).get("esdeger"):
            rapor.append(f"eşdeğer zinciri: {pid} → {hedef} → {D[hedef]['esdeger']}; {pid} doğrudan son sahibe bağlandı")
            d["esdeger"] = D[hedef]["esdeger"]
    D["_yeni"] = yeni
    D["_formul_degiskenleri"] = formul_deg
    D["_rapor"] = rapor
    (AR / "duzeltmeler.json").write_text(json.dumps(D, ensure_ascii=False, indent=1), encoding="utf-8")
    n_esd = sum(1 for k, v in D.items() if not k.startswith("_") and v.get("esdeger"))
    print(f"{len([k for k in D if not k.startswith('_')])} parametre düzeltmesi, {n_esd} eşdeğer, "
          f"{len(yeni)} yeni parametre, {len(formul_deg)} formül değişkeni eşlemesi, {len(rapor)} rapor notu")
    return D


if __name__ == "__main__":
    uygula()
