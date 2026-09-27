# Model mimarisi (iskelet)

## Amaç
Entegre mikro PV + sodyum-iyon pil ürününün, polisilikondan son ürüne kadar
kendi makinelerimizle üretildiği bir **ünite** için parametrik maliyet ve
tasarım modeli. Ana değişken: panel gücü `P_panel` = 50–500 W.

## İlkeler
1. **Kodda sayı yok.** Her sayısal varsayım `data/varsayimlar/<alan>.yaml`
   içindedir: değer, alt–üst aralık, kaynak, kaynak türü, güven, maliyet sınıfı,
   senaryoya uygunluk notu ve (belirsizse) doğrulama deneyi.
2. **Kaynak dürüstlüğü.** `kaynak_turu` alanı: `dogrulanmis_url`,
   `arama_ozeti`, `standart_metni_dogrulanmis`, `hafizadan_dogrulanmadi`,
   `fizik_ders_kitabi`, `hesap_turetilmis`, `tahmin`. Kod, kaynak türüne göre
   güven tavanını zorlar (ör. `tahmin` asla `yuksek` olamaz) ve dayanaksız
   tahmini reddeder (`pvbat/params.py`).
3. **Her maliyet kalemi = birim maliyet × sürücü miktarı**, açık formül
   metniyle birlikte (`pvbat/costs.py`). Döküm tablosunda her kalemin neyle
   ölçeklendiği görünür.
4. **Ünite / saha ayrımı.** Saha başına paylaşılan altyapı (gaz kabini +
   yakma, saf su, HF atık arıtma) `saha_sabit` sınıfındadır ve ünite sayısı
   `N_unite`'ye bölünür; basamaklı büyüme (kapasite dolunca yeni modül) formülde.

## Maliyet sınıfları
| sınıf | ölçekleyen | örnek |
|---|---|---|
| `alan` | işlenen m² (veya kalınlık üzerinden Si kütlesi) | cam, enkapsülan, ITO, polisilikon |
| `adet` | wafer / hücre / panel / kutu / pil hücresi | taşıma, ara bağlantı, ünite başı test, bağlantı kutusu |
| `zaman` | ekipman-saat | fırın amortismanı, pota ömrü, baz enerji, vardiya işçiliği |
| `guc_enerji` *(önerilen ek)* | W veya Wh | güç katı (manyetik + MOSFET/GaN), pil hücreleri |
| `urun_sabit` *(önerilen ek)* | ürün varyantı | sertifikasyon, kalıp takımı → hacme bölünür |
| `saha_sabit` | saha | gaz/abatement, UPW, HF arıtma → ünite sayısına bölünür |

Kullanıcının üç sınıfı (alan/adet/zaman) güç katı ve pil gibi W/Wh ile
ölçeklenen kalemleri ve varyant başı sabitleri doğal olarak taşımıyor; bu
yüzden iki ek sınıf öneriliyor (onaya tabi).

## Hesap zinciri (`pvbat/model.py`)
```
P_panel ──► tasarim ──► N_s, N_p, eta_cell(a), A_cell, a_wafer, k_split, D_ingot,
                         n_panel_per_box, P_box, E_batt
        ──► kristal ──► v_cekme(D), çevrim süresi, kg/gün/fırın, kWh/kg, fırın-saat maliyeti
        ──► wafer   ──► kerf, kare kesim, uç kaybı, kırılma(a,t), geri dönüşüm çarpanı
                         → eritilen kg / iyi wafer → wafer/gün; testere sayısı
        ──► hucre   ──► adım adım kapasite (taşıyıcı başına wafer = f(a)), malzeme,
                         kenar kaybı → hücre/gün, hücre verimi
        ──► modul   ──► panel/gün, BOM (alan + çevre + adet), laminatör, testler
        ──► pil     ──► Wh/gün → pil hücresi/gün → pil hattı sayısı (senkron)
        ──► elektronik ► kutu gücüne göre sabit + güç katı + kasa(hacim) + potting
        ──► altyapi ──► saha payı, elektrik, işçilik, bina, ekonomik girdiler
        ──► standart ──► ünite başı zorunlu testler + varyant sertifikası
```
`eta_cell` hücre boyutuna (kenar kaybı) bağlı, hücre boyutu da `eta_cell`'e
bağlı olduğundan tasarım adımı sabit-nokta yinelemesiyle çözülür.

**Ingot çapı ile wafer boyutunu ayırma (`k_split`)**: ingot kesiti k×k
tuğlaya bölünürse küçük wafer'lar büyük (fırın ekonomisi daha iyi) ingottan
kesilebilir. `cap_kurali = wafer_capi` (k=1) veya `sabit_cap` (fırın çapı
sabit, k hesaplanır) seçilir.

## Kategorik seçimler (`pvbat/secimler.py`)
senaryo (A balkon / B taşınabilir), kristal yöntemi (RCz / CCz / FZ), wafer
kaynağı (iç / satın alma — K3), N_s kuralı (SELV-maks / sabit / optimize),
çap kuralı, wafer geometrisi (psödo-kare / kare / altıgen), metalizasyon,
pil kaynağı (satın alınan hücre / iç hat), güç katı (GaN+planar / Si+sarımlı),
kutu kuralı (sabit n / hedef güç).

## Çıktılar
- `Tarama`: her güç için türetilmiş büyüklükler + $/W (sınıf ve alan kırılımı)
- `Maliyet_dokumu`: kalem kalem birim maliyet × miktar ve formül
- `Varsayimlar`: tüm girdiler, kaynak ve güven
- `Duyarlilik_<P>W`: tornado (tek-seferde-bir); Faz 2'de Morris/Monte Carlo
