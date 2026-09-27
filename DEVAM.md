# Devam promptu (yeni oturum için)

Bu projede önceki bir bulut oturumunda Faz 1 tamamlandı. O oturumun sohbet geçmişi sende yok; bu metin devir teslimdir. Önce bu metni, sonra `README.md`, `docs/mimari.md` ve `arastirma/faz1b/sentez.json` dosyasını oku.

## 0. Depo
- GitHub: `Manifoltwarper/Manifoltwarper`, çalışma dalı `claude/pv-battery-cost-model-bliy1x`, taslak PR #1 (hedef `main`).
- Bu klasör git deposu değilse (ZIP'ten çıkarılmışsa) önce bu dala bağla; yerel dosyaları kaybetmeden.
- Windows ortamı: `py -m pip install -r requirements.txt`, sonra `py -m pytest -q` (10 test geçmeli).

## 1. Proje (kullanıcının özgün isteği, özet)
Gebze'de indüktör üreten bir firma (kendi kalıp/enjeksiyon; manyetik tasarım yetkinliği; indüksiyon ısıtma tecrübesi). Satın alınan polisilikondan son ürüne kadar giden, küçük alanda, kendi tasarladıkları makinelerle çalışan bir üretim ünitesi. Kapasite ünite kopyalanarak artar; ortak altyapı (gaz kabini + yakma, saf su, HF atık arıtma) saha başına paylaşılır. Ürün: güneş paneli + sodyum-iyon pil + MPPT/BMS/inverter entegre. Pazar belirsiz: (A) balkon/şebeke veya (B) taşınabilir/şebeke dışı.

İstenen çıktı:
1. Python parametrik model + Excel aktarımı. Her maliyet kalemi açık formülle, her varsayım değiştirilebilir girdi.
2. Ana değişken panel gücü 50–500 W. Her güç için hücre boyutu, seri hücre sayısı, ingot çapı, fırın kg/gün, wafer/gün, panel/gün, pil ihtiyacı, pil hattı sayısı, W başına maliyet dökümü.
3. Maliyetler alan / adet / zaman ile ölçeklenenlere ayrılsın (+ önerilen `guc_enerji`, `urun_sabit`; `saha_sabit`).
4. Duyarlılık: sonucu en çok değiştiren 5–10 parametre.
5. Her varsayım için değer, aralık, kaynak, güven (yüksek/orta/düşük). Kaynak yoksa "tahmin"; uydurma yok.
6. Doğrulanması gereken deneyler, öncelik sırasıyla.

Kullanıcı kararları (sorgulanabilir): K1 RCz n-tipi P katkılı (alt. FZ); K2 HJT (<250 °C); K3 önce satın alınan wafer; K4 yalnız wafer yolunu kapsayan mini-ortam; K5 pil+elektronik ayrı, gölgede, değiştirilebilir kutuda, bir kutu birden çok paneli besler; K6 DC 60 V SELV altı (soğuk Voc dahil); K7 fırın pota ömrü boyunca sürekli, ingot kilit odasından; K8 kare kesim artıkları ve uçlar asitle temizlenip yeniden eritilir; K9 pil hattı ~150 bin hücre/yıl.
Önceki hatalar (tekrarlanmayacak): H1 sektör sezgisini kontrolsüz aktarma; H2 kasa/kalıp/plastik/potting boyutla ölçeklenir; H3 küçük wafer daha az kırılır; H4 elektronik maliyeti güç katında, küçük güçte planar/GaN; H5 fırın: çıktı ~D²·v, kayıp ~sıcak bölge yüzeyi, büyük fırının avantajı sabit maliyet dağıtımı, enerji izolasyon/kalkanla; H6 uçtan uca proses kontrolü test/servis maliyetini düşürür ama zorunlu ünite başı testler kalır.
Tasarım kuralları: doğal sınırlar esas (fizik, kimya, malzeme, güvenlik, standart); "makinesi yok" sınır değil. Belirsiz olan açıkça belirsiz: "bilmiyoruz, şu deneyle öğrenilir". Kullanıcının varsayımlarına gerekçeyle itiraz et; memnun etmeye çalışma. Kullanıcı Türkçe konuşur; dürüst, süslemesiz, doğruluğa odaklı yanıt ister.
Kullanıcı her araştırma görevi için ayrı ajan istedi (kristal, wafer, hücre, modül, elektronik, pil, entegrasyon, kırmızı takım; önceki oturum saha altyapısı/ekonomi ve standartlar ajanlarını ekledi). Karar veremediğinde kullanıcıya sor.

## 2. Faz 1'de yapılanlar (tamamlandı)
- Süreç: 8 alan ajanı → alan başına 2 kırmızı takım (kaynak + fizik) → revizyon; ardından 5 uzlaştırma görevi (ekonomi, teknik zincir, kapsam, sentez, tahmin dayanakları), her biri denetim + revizyon; 64 parametrelik bağımsız kaynak örneklemi (59 destekliyor, 5 kısmen, 0 desteklemiyor).
- `data/varsayimlar/*.yaml`: 965 varsayım (922 bağımsız sahip + 43 eşdeğer), doğrulama hatası 0.
- `pvbat/`: varsayım kaydı (kaynak türüne göre güven tavanı, dayanaksız tahmin reddi, eşdeğer = tek sahip), maliyet defteri, seçimler, tarama, tornado, Excel/Markdown aktarımı. **Alan modülleri (`pvbat/domains/*.py`) henüz iskelet; formüller kodlanmadı.**
- `docs/`: `mimari.md`, `varsayim_tablosu.md`, `formul_envanteri.md` (505 formül), `faz1_varsayimlar.xlsx`, `kaynak_denetimi.md`, `onay_dosyasi.html` (onay sayfası; yayınlanmış hâli: https://claude.ai/artifact/3uYxibh9GncjNpBumw8tsX).
- `arastirma/`: ham çıktılar ve denetim raporları (`faz1/`), uzlaştırma (`faz1b/`: zincir, ekonomi, kapsam, sentez, dayanak), `duzeltmeler.json` (araştırma kaydını değiştirmeden uygulanan düzeltmeler).
- Araç zinciri: `tools/uzlastirma_uygula.py` → `tools/arastirma_to_yaml.py arastirma/faz1 data/varsayimlar` → `tools/rapor_uret.py arastirma/faz1` → `tools/onay_sayfasi.py docs/onay_dosyasi.html --tek-basina`.

## 3. Ana bulgular (ayrıntı: `arastirma/faz1b/sentez.json`)
- Tahmini talep ~3 MW/yıl (kaynaksız tahmin, ~1–22); en küçük makul HJT hücre hattı 40–50 MW/yıl → bu ölçekte hücre hattının zaman maliyeti ~40 ¢/W. K9 ile senkron tam dikey ünite ekonomik değil.
- Satın alınan n-tipi M10 wafer ~4,9 $/m² teslim; kendi wafer merkez tahminlerde en az ~2 kat pahalı. Kendi pil hücresi (26700, K9) satın almanın 5–8 katı; 50 Ah prizmatik belirsizlik sınırında.
- Tam ölçekte bile satın alınan wafer + kendi hücre + kendi modül ~19–22 ¢/W (saha hariç); ithal HJT modül FOB 11 ¢/W (AB). **Türkiye'de Çin menşeli modüle 20–25 $/m² anti-damping var** (2017'den, 2023'te 5 yıl uzatıldı; Günder sayfası doğrulandı) → TR'de ithal modül ~20–22 ¢/W. Çerçeve (%38–46) ve bağlantı kutusu (%57) anti-dampingi yalnız arama özetinden, doğrulanmadı.
- 60 V PV kurulum standardının SELV sınırı (IEC 60364-7-712); dış ortam dokunma sınırı 30–35 V; 60 V panel Class II olmalı, Class III 35 V / 8 A / 240 W.
- Na-iyon LFP'den genel olarak ucuz değil (formata göre −%14…+%59); bazı Na hücreler 0 °C altında şarj edilmiyor.
- H4 ≤300 W'ta yanlış, ≥500 W'ta kısmen doğru; manyetikler kutunun %4–6'sı.
- 965 varsayımın %66'sı tahmin/hafızadan; ilk 10 deney ~25–100 k$.

## 4. Şu anki durum: kullanıcı onayı ve kararları bekleniyor
Faz 2'ye geçmeden önce kullanıcıdan iste (seçenekler ve öneriler `sentez.json` → `acik_kararlar`):
- **KK1 ünite tanımı** (öneri: (d) wafer ve hücre satın al; ünite = modül + pil paketi + kutu montajı; (b) koşullu: talep ≥40 MW/yıl ve PECVD deneyi başarılı)
- **KK2 poli→wafer'ın stratejik değeri** (kullanıcı sayıyla yazmalı)
- **KK3 V_lim** (öneri: A = 60 V SELV + Class II, B yalnız-DC = 35 V)
- **KK4 pazar** (öneri: modelde A ve B ayrı platform)
- **KK5 pil hücresi yap/al** (öneri: satın al, paketi kendin yap)
- **KK6 kimya** (öneri: model kimyadan bağımsız; Na ve LFP seçenek)
- KK7–KK15: itiraz edilmezse araştırmanın önerisi varsayılan (maliyet sınıfları genişletmesi, kutu kuralı, ayrık varyantlar, Excel = değer + izlenebilir formül metni, öğrenme eğrisi varsayılan, fiyat senaryoları).
Kararları seçenekli sorularla (en fazla 4'er) sor; KK2 için serbest metin iste.

## 5. Onaydan sonra Faz 2
1. `pvbat/secimler.py`'ye zincirin kategorik seçimlerini ekle (ünite tanımı, gerilim rejimi, pazar/T_min, öğrenme durumu, kimya/format, kenar modu…).
2. `pvbat/domains/*.py`: `arastirma/faz1b/zincir.json`'daki 19 adımlık zinciri ve `docs/formul_envanteri.md` formüllerini kodla. Her maliyet kalemi `CostItem` (birim maliyet × sürücü miktarı + formül metni). `duzeltmeler.json` → `_formul_degiskenleri` (42 serbest değişken → kanonik id) eşlemesini uygula.
3. Kapsam eleştirmeninin eksik kalemlerini ve çift sayım çözümlerini uygula (`arastirma/faz1b/kapsam.json`); etiketleme kuralı (fiyatlar `teknik`, sınıfı formül taşır).
4. Tarama 50–500 W, tornado + Morris/Monte Carlo; ilk 10 duyarlı parametrenin kaynağını tek tek yeniden doğrula.
5. Deney listesini kesinleştir; Excel ve onay sayfasını güncelle; PR #1'i güncelle.
Her aşamada: iş başına ayrı ajan, bulguları kırmızı takımla denetle, kaynak uydurma yok.
