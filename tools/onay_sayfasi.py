"""Faz 1 onay dosyasını (tek sayfa HTML) üretir.

Kullanım: python tools/onay_sayfasi.py <cikti.html> [--tek-basina]
Girdiler: arastirma/faz1/*.json, arastirma/faz1b/*.json, arastirma/kaynak_orneklem_denetimi.json,
          tools/onay_sablon.html
"""
from __future__ import annotations

import html
import json
import sys
from pathlib import Path

KOK = Path(__file__).resolve().parent.parent
AR = KOK / "arastirma"
ALANLAR = ["kristal", "wafer", "hucre", "modul", "elektronik", "pil", "altyapi", "standart"]
ALAN_ADI = {
    "kristal": "Kristal / fırın", "wafer": "Wafer", "hucre": "Hücre (HJT)", "modul": "Modül",
    "elektronik": "Elektronik", "pil": "Pil (Na-iyon)", "altyapi": "Saha altyapısı ve ekonomi",
    "standart": "Standartlar ve mevzuat",
}
KILIT_KARARLAR = ["KK1", "KK2", "KK3", "KK4", "KK5", "KK6"]

LEAD = (
    "Bu dosya Faz 1'in sonucu: modelin iskeleti ve tüm varsayımların tablosu. Sekiz alan ajanı (kristal, wafer, "
    "hücre, modül, elektronik, pil, saha altyapısı, standartlar) araştırdı. Her alanın çıktısını iki kırmızı takım "
    "denetçisi (kaynak ve fizik) denetledi, alan ajanı revize etti. Ardından beş uzlaştırma görevi alanlar arası "
    "çelişkileri, eksik kalemleri, itirazları ve deneyleri birleştirdi. Alan formüllerinin kodlanması, W başına "
    "maliyet dökümü ve duyarlılık analizi Faz 2'de, onayınızdan sonra yapılacak."
)
ANA_SONUC = (
    "Araştırma, projenin bugünkü kurgusunu desteklemiyor. Her ünitede polisilikondan başlayıp pil hattıyla senkron "
    "çalışan tam dikey üretim, bugünkü fiyatlar ve tahmini talep altında satın almaktan belirgin pahalı. Wafer'ı "
    "kendimiz üretmek merkez tahminlerde satın almanın en az ~2 katı; pil hücresinde formata göre 1,3–8 katı. En küçük "
    "makul HJT hücre hattı (40–50 MW/yıl) tahmini talebin (~3 MW/yıl) 10 katından büyük. Bu hüküm henüz ölçülmemiş iki "
    "şeye bağlı: talep (kaynaksız bir tahmin) ve stratejik gerekçelerin parasal değeri (menşe, tedarik güvenliği, "
    "Türkiye'deki anti-damping vergileri, Çin fiyatlarının yükselmesi). Faz 2'nin yapısını belirleyen ilk karar bu "
    "yüzden ‘ünite’nin ne olduğu (KK1)."
)
# Sentezdeki 12 bulgu için kısa satırlar (aynı sırayla) + doğrulanmış Türkiye anti-damping bulgusu.
KISA = [
    "Tahmini talep ~3 MW/yıl (belirsiz: ~1–22). En küçük makul HJT hattı 40–50 MW/yıl. Bu ölçekte hücre hattının zaman maliyeti tek başına ~40 ¢/W.",
    "Satın alınan wafer + kendi hücre + kendi modül, 45 MW/yıl ve olgun proseste ~19–22 ¢/W (saha payı hariç). Çin'den FOB HJT modül 11 ¢/W.",
    "Satın alınan n-tipi M10 wafer ~4,9 $/m² teslim. Kendi wafer dönüşümünün merkez tahmini tek başına 7,2 $/m². Stratejik gerekçeler sayıya dökülmedi.",
    "26700 formatında 150 bin hücre/yıl ≈ 1,4 MWh/yıl ve ~1,03 $/Wh: satın almanın 5–8 katı. 50 Ah prizmatik hat belirsizlik sınırında (1,3–1,6 kat).",
    "Na/LFP fiyat farkı formata göre −%14 ile +%59. Bazı Na hücreler 0 °C altında şarj edilemiyor. LFP ile aynı koşulda soğuk kıyas verisi yok.",
    "Kutu elektroniği 50 W'ta 1,84 $/W, 500 W'ta 0,25 $/W. Öneri: balkonda ≥200 W panel ve kutu başına 2–4 panel.",
    "60 V, PV kurulum standardının SELV sınırı. Dış ortam dokunma sınırı 30–35 V. 60 V'luk panel Class II olmalı; Class III 35 V / 8 A / 240 W ile sınırlı.",
    "AB Pil Tüzüğü (SBESS, 5 kg, 2 kWh), Almanya'da 800 VA / 960 Wp, fişli panellerde RoHS ve Makine Tüzüğü ürün mimarisini basamaklı biçimde belirliyor.",
    "Evde enerji depolayan kutu büyük olasılıkla SBESS sayılır (Ek V güvenlik testleri). Model bunu varsayılan alıyor.",
    "HJT hatlarında gettering ön tavlaması (550–950 °C) yaygın; ‘tümüyle <250 °C’ tam doğru değil. Küçük hücrede TOPCon'a üstünlük ölçülmedi.",
    "Manyetikler kutu maliyetinin %4–6'sı. İndüksiyon yetkinliği FZ'nin MHz RF'ine değil, indüksiyonlu susseptör CZ'ye uyuyor. Kendi makine maliyetleri ölçülmedi.",
    "954 varsayımın 637'si tahmin veya hafızadan. İlk 10 deney yaklaşık 25–100 k$ ile Faz 2 kararlarının çoğunu açıyor.",
]
TR_BULGU = {
    "baslik": "Türkiye pazarında ithal Çin modülüne 20–25 $/m² anti-damping var; AB'de yok",
    "kisa": "1 Nisan 2017'den beri uygulanıyor, 2023'te 5 yıl uzatıldı. ~%22 verimli modülde +9–11 ¢/W: Türkiye'de ithal modül ~20–22 ¢/W. Kendi modül montajı bu pazarda rekabetçi olabilir.",
    "aciklama": (
        "Önlem ‘bir modül halinde birleştirilmiş veya panolarda düzenlenmiş fotovoltaik hücreler’ için: 16 Çinli "
        "üreticiye 20 $/m², diğerlerine 25 $/m². Bu, 2 numaralı bulgudaki ‘ithal modül 11 ¢/W’ kıyasının yalnız AB "
        "pazarı için geçerli olduğu anlamına geliyor. Doğrulanmamış (yalnız arama özeti): 2026'da Çin menşeli panel "
        "çerçevelerine %38–46, bağlantı kutularına %57 anti-damping. Doğruysa bu parçaların kendi enjeksiyon "
        "kapasitesiyle üretilmesi avantaj olur. Bilinmeyen: hücrelerin kendisine ayrı önlem olup olmadığı ve ihracat "
        "için dahilde işleme rejiminin girdileri vergiden muaf tutup tutmadığı (Deney 3, gümrük müşaviri)."
    ),
    "kanit": "https://www.gunder.org.tr/cin-menseli-gunes-paneli-ithalatinda-anti-damping-vergisi-5-yil-daha-uzatildi/ (bu çalışmada açıldı ve metin görüldü). Çerçeve/bağlantı kutusu: arama özeti, doğrulanmadı.",
    "guven": "yuksek",
}
GRAFIK = {
    "not": ("Aralıklar belirsizlik bandı değil, hesaplardaki alt–üst değerler. Tahmini merkez talepte (~3 MW/yıl) "
            "yalnız hücre hattının zaman maliyeti ~40 ¢/W olduğundan kendi zincir bu grafiğin dışına çıkar."),
    "eksen_max": 30,
    "satirlar": [
        {"etiket": "İthal HJT modül, FOB Çin (AB pazarı)", "alt": 11.0, "ust": 11.0,
         "kaynak": "InfoLink spot fiyatı, 23.09.2026 (doğrulanmış)"},
        {"etiket": "İthal HJT modül, Türkiye'ye (FOB + anti-damping)", "alt": 19.7, "ust": 22.4,
         "kaynak": "Hesap: 11 ¢/W + 20–25 $/m² ÷ 220–230 W/m². Navlun ve gümrük vergisi hariç."},
        {"etiket": "Satın alınan wafer + kendi hücre ve modül (45 MW/yıl, olgun, saha hariç)", "alt": 19.4, "ust": 21.6,
         "kaynak": "Uzlaştırma sentezi hesabı; girdilerin çoğu tahmin."},
        {"etiket": "Aynı zincir + saha payı (tek ünite)", "alt": 25.0, "ust": 27.0,
         "kaynak": "Uzlaştırma sentezi hesabı; saha capex'inin çoğu tahmin."},
    ],
}


def e(x) -> str:
    return html.escape(str(x))


def yukle():
    R = {a: json.loads((AR / "faz1" / f"{a}.json").read_text(encoding="utf-8")) for a in ALANLAR}
    B = {p.stem: json.loads(p.read_text(encoding="utf-8")) for p in (AR / "faz1b").glob("*.json")}
    K = json.loads((AR / "kaynak_orneklem_denetimi.json").read_text(encoding="utf-8"))
    return R, B, K


def parametreler(R, duzeltme: dict) -> list[dict]:
    out = []
    for a in ALANLAR:
        r = R[a]["revize"] or R[a]["ilk"]
        for p in r["parametreler"]:
            q = {k: p.get(k, "") for k in ("id", "ad", "birim", "deger", "alt", "ust", "guven", "kaynak_turu", "kaynak",
                                          "kaynak_alintisi", "kaynak_tarihi", "maliyet_sinifi", "olcek",
                                          "senaryoya_uygunluk", "dogrulama_deneyi")}
            q["alan"] = a
            q["aciklama"] = p.get("not", "")
            q.update(duzeltme.get(p["id"], {}))
            out.append(q)
        for y in duzeltme.get("_yeni", []):
            if y.get("alan") == a:
                out.append(dict(y))
    return out


def iskelet_html(B) -> str:
    parts = []
    z = B.get("zincir", {}).get("sonuc")
    parts.append("""<div class="two">
<div class="stack"><h3>Maliyet sınıfları</h3>
<p class="small" style="color:var(--ink-2)">Her maliyet kalemi = birim maliyet × sürücü miktarı, açık formül metniyle. Sizin üç sınıfınıza (alan / adet / zaman) iki ek öneriliyor; uzlaştırma bunları ve birkaç alt ayrımı destekledi (KK7).</p>
<div class="tablewrap"><table><thead><tr><th>Sınıf</th><th>Ölçekleyen</th><th>Örnek</th></tr></thead><tbody>
<tr><td class="id">alan</td><td>işlenen m² (veya kalınlık üzerinden Si kütlesi)</td><td>cam, enkapsülan, ITO, gümüş, polisilikon</td></tr>
<tr><td class="id">adet</td><td>wafer / hücre / panel / kutu / pil hücresi</td><td>ara bağlantı, bağlantı kutusu, ünite başı test</td></tr>
<tr><td class="id">zaman</td><td>ekipman-saat (sabit + değişken)</td><td>fırın amortismanı, pota ömrü, vardiya işçiliği</td></tr>
<tr><td class="id">guc_enerji <span class="chip acc">ek</span></td><td>W veya Wh</td><td>güç katı (manyetik + FET), pil hücresi</td></tr>
<tr><td class="id">urun_sabit <span class="chip acc">ek</span></td><td>ürün varyantı → hacme bölünür</td><td>sertifika, kalıp takımı, hücre boyutu kalifikasyonu</td></tr>
<tr><td class="id">saha_sabit</td><td>saha → ünite sayısına bölünür (basamaklı)</td><td>gaz odası + yakma, UPW, HF arıtma</td></tr>
</tbody></table></div></div>
<div class="stack"><h3>Kodda ne hazır, ne kalıyor</h3>
<ul class="small" style="margin:0;padding-left:18px;color:var(--ink-2);display:flex;flex-direction:column;gap:4px">
<li><b>Hazır:</b> varsayım kaydı (kaynak türüne göre güven tavanı ve dayanaksız tahmin kodda reddediliyor), maliyet defteri, kategorik seçimler, güç taraması, tornado duyarlılığı, Excel ve Markdown aktarımı, 954 varsayımlık YAML.</li>
<li><b>Faz 2:</b> dokuz alan modülünün formülleri (505 formül envanteri hazır), ortak girdilerin tek sahibe bağlanması (eşdeğer parametreler), tasarım adımının sabit-nokta yinelemesi, deney listesinin kesinleşmesi.</li>
<li><b>Ana değişken:</b> P_panel 50–500 W. Her güç için hücre boyutu, seri hücre sayısı, ingot çapı, fırın kg/gün, wafer/gün, panel/gün, pil ihtiyacı, pil hattı sayısı ve W başına maliyet dökümü (sınıf ve alan kırılımıyla).</li>
</ul></div></div>""")
    if z:
        adim = "".join(
            f"""<div class="step"><span><b>{e(s['alan'])}</b> · {e(s['adim'])}</span>
<span class="io">Girdi: {', '.join(f'<code>{e(g)}</code>' for g in s['girdiler'][:10])}{' …' if len(s['girdiler']) > 10 else ''}</span>
<span class="io">Çıktı: {', '.join(f'<code>{e(c["anahtar"])}</code> [{e(c["birim"])}]' for c in s['ciktilar'][:8])}{' …' if len(s['ciktilar']) > 8 else ''}</span></div>"""
            for s in sorted(z["zincir"], key=lambda s: s["sira"]))
        parts.append(f'<h3 style="margin-top:10px">Hesap zinciri</h3><div class="chain">{adim}</div>')
        parts.append(f'<details><summary>P → geometri tasarım kuralı (uzlaştırılmış)</summary><div class="body"><p style="white-space:pre-line">{e(z["tasarim_kurali_P_geometri"])}</p></div></details>')
        ops = "".join(
            f"""<div class="opt"><span class="code mono" style="color:var(--accent)">{e(o['kod'])}</span><h3>{e(o['ad'])}</h3>
<p class="small" style="color:var(--ink-2)">{e(o['tanim'])}</p>
<p class="small"><b>Darboğaz:</b> {e(o['capa_darbogaz'])}</p>
<p class="small"><b>Sayısal:</b> {e(o['sayisal_ipuclari'])}</p>
<details><summary>Artı / eksi</summary><div class="body"><ul>{''.join(f'<li>+ {e(x)}</li>' for x in o['artilar'])}{''.join(f'<li>− {e(x)}</li>' for x in o['eksiler'])}</ul></div></details></div>"""
            for o in z["unite_tanimi_secenekleri"])
        parts.append(f'<h3 style="margin-top:10px">Ünite tanımı seçenekleri (KK1)</h3><div class="options">{ops}</div>')
        cel = "".join(f"<tr><td>{e(c['konu'])}</td><td class='small'>{e(', '.join(c['alanlar']))}</td><td class='small'>{e(c['cozum'])}</td><td>{e(c['ciddiyet'])}</td></tr>" for c in z["celiskiler"])
        parts.append(f'<details><summary>Alanlar arası teknik çelişkiler ve çözümleri ({len(z["celiskiler"])})</summary><div class="body"><div class="tablewrap"><table><thead><tr><th>Konu</th><th>Alanlar</th><th>Çözüm</th><th>Ciddiyet</th></tr></thead><tbody>{cel}</tbody></table></div></div></details>')
    ek = B.get("ekonomi", {}).get("sonuc")
    if ek:
        rows = "".join(f"<tr><td>{e(k['kavram'])}</td><td class='id'>{e(k['kanonik_id'])}</td><td class='num'>{k['deger']:g}</td><td class='small'>{e(k['birim'])}</td><td class='small'>{e(', '.join(t['id'] for t in k['takma_adlar']))}</td></tr>" for k in ek["kanonik_parametreler"])
        parts.append(f'<details><summary>Ortak ekonomik girdiler: tek sahipli kanonik değerler ({len(ek["kanonik_parametreler"])})</summary><div class="body"><p>{e(ek["sermaye_yuku_yontemi"])}</p><div class="tablewrap"><table><thead><tr><th>Kavram</th><th>Kanonik id</th><th>Değer</th><th>Birim</th><th>Eşdeğer (yerine geçer)</th></tr></thead><tbody>{rows}</tbody></table></div></div></details>')
    k = B.get("kapsam", {}).get("sonuc")
    if k:
        eks = "".join(f"<tr><td>{e(x['kalem'])}</td><td class='small'>{e(x['onerilen_alan'])}</td><td class='id'>{e(x['sinif'])}</td><td class='small'>{e(x['kaba_buyukluk'])}</td></tr>" for x in k["eksik_kalemler"])
        cift = "".join(f"<tr><td>{e(x['kalem'])}</td><td class='small'>{e(', '.join(x['alanlar']))}</td><td class='small'>{e(x['cozum'])}</td></tr>" for x in k["cift_sayimlar"])
        parts.append(f'<details><summary>Eksik maliyet kalemleri — Faz 2\'de eklenecek ({len(k["eksik_kalemler"])})</summary><div class="body"><div class="tablewrap"><table><thead><tr><th>Kalem</th><th>Alan</th><th>Sınıf</th><th>Kaba büyüklük</th></tr></thead><tbody>{eks}</tbody></table></div></div></details>')
        parts.append(f'<details><summary>Çift sayım riskleri ve tek sahip önerisi ({len(k["cift_sayimlar"])})</summary><div class="body"><div class="tablewrap"><table><thead><tr><th>Kalem</th><th>Alanlar</th><th>Çözüm</th></tr></thead><tbody>{cift}</tbody></table></div></div></details>')
        parts.append(f'<details><summary>Maliyet sınıfı etiketleme kuralı (önerilen)</summary><div class="body"><p style="white-space:pre-line">{e(k["etiketleme_kurali"])}</p></div></details>')
    return "\n".join(parts)


def kaynak_html(R, K) -> str:
    from collections import Counter
    c = Counter()
    for a in ALANLAR:
        for rt in ("kaynak_denetimi", "fizik_denetimi"):
            b = R[a][rt]
            if b:
                c.update(x["sonuc"] for x in b["kaynak_kontrolleri"])
    kismen = "".join(f"<li><b>{e(x['alan'])} / <code>{e(x['id'])}</code></b> — {e(x['not'])}</li>" for x in K["kontroller"] if x["sonuc"] != "destekliyor")
    d = K["dagilim"]
    return f"""<div class="two">
<div class="stack"><h3>1. Revizyon öncesi: kırmızı takım</h3>
<p class="small" style="color:var(--ink-2)">Alan başına kaynak denetçisi ve fizik denetçisi {sum(c.values())} kaynağı sayfayı yeniden açarak kontrol etti. Bulgular revizyonda düzeltildi: kaynak değiştirildi ya da kaynak türü ve güven düşürüldü.</p>
<div class="stats"><div><span class="label">Destekliyor</span><span class="big">{c['destekliyor']}</span></div><div><span class="label">Kısmen</span><span class="big">{c['kismen']}</span></div><div><span class="label">Erişilemedi</span><span class="big">{c['erisilemedi']}</span></div><div><span class="label">Desteklemiyor</span><span class="big">{c['desteklemiyor']}</span></div><div><span class="label">Uydurma şüphesi</span><span class="big">{c.get('uydurma_supheli', 0)}</span></div></div></div>
<div class="stack"><h3>2. Revizyon sonrası: bağımsız örneklem</h3>
<p class="small" style="color:var(--ink-2)">Alan başına 8, toplam {K['toplam']} ‘doğrulanmış’ parametre seçildi (tabakalı: önce fiyat/maliyet, sonra teknik; rastgele değil). Her sayfa yeniden açılıp değer arandı.</p>
<div class="stats"><div><span class="label">Destekliyor</span><span class="big">{d.get('destekliyor', 0)}</span></div><div><span class="label">Kısmen</span><span class="big">{d.get('kismen', 0)}</span></div><div><span class="label">Desteklemiyor</span><span class="big">{d.get('desteklemiyor', 0)}</span></div><div><span class="label">Uydurma şüphesi</span><span class="big">{d.get('uydurma_supheli', 0)}</span></div></div></div></div>
<p>Örneklemde uydurma ya da desteklenmeyen kaynak çıkmadı. ‘Kısmen’ sonuçlarında değer, kaynağın verdiği aralıktan seçilmiş veya kaynaktan hesapla türetilmiş, ama ‘doğrulanmış’ diye etiketlenmiş. Bu beş parametrenin kaynak türü ‘hesap_turetilmis’ olarak düzeltildi. Örneklem küçük ve tabakalı olduğundan bu oran tablonun tamamı için kesin hata oranı değil. Sonucu en çok etkileyen parametreler (duyarlılıkta ilk 10) Faz 2'de tek tek yeniden kontrol edilecek.</p>
<details><summary>‘Kısmen’ çıkan 5 parametre</summary><div class="body"><ul>{kismen}</ul></div></details>
<p class="small muted">Tablonun %67'si ‘tahmin’ veya ‘hafızadan’. Bunlar uydurma değil, kaynağı olmayan ya da doğrulanamayan değerler; her birinin dayanağı ve doğrulama yolu satır ayrıntısında yazılı.</p>"""


def uret(cikti: Path, tek_basina: bool = False) -> None:
    R, B, K = yukle()
    s = B["sentez"]["sonuc"]
    duz = json.loads((AR / "duzeltmeler.json").read_text(encoding="utf-8")) if (AR / "duzeltmeler.json").exists() else {}
    P = parametreler(R, duz)
    kt = {}
    for p in P:
        kt[p["kaynak_turu"]] = kt.get(p["kaynak_turu"], 0) + 1
    dogrulanmis = kt.get("dogrulanmis_url", 0) + kt.get("standart_metni_dogrulanmis", 0)
    tahmin = kt.get("tahmin", 0) + kt.get("hafizadan_dogrulanmadi", 0)
    n_formul = sum(len((R[a]["revize"] or R[a]["ilk"])["formuller"]) for a in ALANLAR)
    bulgular = []
    for i, b in enumerate(s["ana_bulgular"]):
        bulgular.append({**b, "kisa": KISA[i] if i < len(KISA) else ""})
        if i == 1:
            bulgular.append(TR_BULGU)
    V = {
        "lead": LEAD, "ana_sonuc": ANA_SONUC,
        "stats": [["Varsayım", str(len(P)), "8 alan, hepsi değiştirilebilir"],
                  ["Formül", str(n_formul), "alan formülleri (envanter)"],
                  ["Doğrulanmış kaynak", str(dogrulanmis), "URL veya standart metni açıldı"],
                  ["Tahmin / hafızadan", str(tahmin), f"%{round(100 * tahmin / len(P))}; deneyle doğrulanacak"],
                  ["Kaynak örneklemi", f"{K['dagilim'].get('destekliyor', 0)}/{K['toplam']}", "destekliyor; 0 desteklemiyor"]],
        "grafik": GRAFIK, "bulgular": bulgular,
        "kararlar": s["acik_kararlar"], "kilit_kararlar": KILIT_KARARLAR,
        "itirazlar": s["itirazlar"], "deneyler": sorted(s["deneyler"], key=lambda d: d["sira"]),
        "parametreler": P, "alan_adlari": ALAN_ADI,
        "iskelet_html": iskelet_html(B), "kaynak_html": kaynak_html(R, K),
    }
    sablon = (KOK / "tools" / "onay_sablon.html").read_text(encoding="utf-8")
    veri = json.dumps(V, ensure_ascii=False).replace("</", "<\\/")
    sayfa = sablon.replace("/*__VERI__*/", veri, 1)
    if tek_basina:  # yerelde çift tıklayarak açılabilen tam belge (yayın sürümünü iskeleti platform ekler)
        sayfa = ('<!doctype html>\n<html lang="tr">\n<head>\n<meta charset="utf-8">\n'
                 '<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">\n'
                 '<style>body{margin:0}[hidden]{display:none!important}</style>\n</head>\n<body>\n'
                 + sayfa + "\n</body>\n</html>\n")
    cikti.parent.mkdir(parents=True, exist_ok=True)
    cikti.write_text(sayfa, encoding="utf-8")
    print(f"{cikti} yazıldı ({cikti.stat().st_size // 1024} KB, {len(P)} parametre)")


if __name__ == "__main__":
    # --tek-basina: yerelde açmak için <!doctype>, <meta charset> vb. ile tam HTML belgesi yazar
    uret(Path(sys.argv[1]), tek_basina="--tek-basina" in sys.argv[2:])
