# Araştırma çıktıları (kaynak izi)

`faz1/<alan>.json` — her alan için:
- `revize`: kırmızı takım denetiminden sonra revize edilmiş alan çıktısı (parametreler, formüller,
  tasarım seçimleri, itirazlar, deneyler, arayüzler, doğal sınırlar, kaynaklar, değişiklik günlüğü,
  reddedilen bulgular)
- `kaynak_denetimi`: kaynak denetçisinin raporu (her URL yeniden açıldı; sonuç ve sayfada görülen)
- `fizik_denetimi`: fizik / mühendislik / uygulanabilirlik denetçisinin raporu (bağımsız hesaplar)

Süreç: alan ajanı → (kaynak denetçisi ∥ fizik denetçisi) → alan ajanı revizyonu.
`data/varsayimlar/*.yaml` bu dosyalardan `tools/arastirma_to_yaml.py` ile mekanik olarak üretilir.
