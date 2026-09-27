# Kaynak denetimi (Faz 1)

İki aşamalı denetim yapıldı. Amaç, 'doğrulanmış' etiketli kaynakların gerçekten değeri desteklediğini ölçmek.

## 1. Revizyon öncesi — kırmızı takım (alan başına kaynak denetçisi + fizik denetçisi)
393 kaynak yeniden açıldı: **271 destekliyor, 96 kısmen, 21 erişilemedi, 5 desteklemiyor, 0 uydurma şüphesi.** Bulgular alan revizyonunda düzeltildi (kaynak değiştirildi veya kaynak türü/güven düşürüldü). Ayrıntı: `arastirma/faz1/<alan>.json` → `kaynak_denetimi`, `fizik_denetimi`.

## 2. Revizyon sonrası — bağımsız örneklem denetimi
Revize tablodan alan başına 8 olmak üzere **64** parametre seçildi (tabakalı; önce maliyet/fiyat parametreleri, sonra teknik parametreler — rastgele örneklem değil). Her birinin sayfası yeniden açılıp değer arandı.

**Sonuç: 59 destekliyor, 5 kısmen, 0 desteklemiyor, 0 erişilemedi, 0 uydurma şüphesi.**

Yorum: örneklemde uydurma veya desteklenmeyen kaynak bulunmadı. 'Kısmen' sonuçları çoğunlukla birim/kur dönüşümü veya kaynağın daha geniş bir kategoriyi vermesinden kaynaklanıyor (aşağıda). Örneklem tabakalı ve küçük olduğundan bu oran tüm tablo için kesin bir hata oranı değildir; sonucu çok etkileyen parametreler (duyarlılık analizinde ilk 10) Faz 2'de tek tek yeniden kontrol edilecek.

### 'Kısmen' sonuçları

- **wafer / `saw_wire_price_steel_usd_km`** — Ham sayi (17 RMB/km) birebir var. 17 RMB/km, 2024 kuruyla (~7,1-7,2) yaklasik 2,36-2,40 USD/km ediyor; modeldeki 2,5 USD/km bundan ~%5-6 yuksek. Ayrica 17 RMB/km Meichang'in karbon celik ve tungsten karisik ortalama birim fiyati; sayfa celik cekirdek icin ayri bir fiyat vermiyor. Donusum yaklasik olarak makul ama tam ortusmuyor. (Sayfada: '2024年，金刚线单价从上一年的37.64元/公里骤降至17元/公里，同比下滑54.83%'; ayrica Meichang 2024 satisi 12175.10万公里, gelir 21.52亿元; 2025 Q1'de tungsten tel payi %40'in uzerinde)
- **hucre / `hjt_ito_thickness_total_nm`** — Alinti sayfada var, ancak her yuzde 100 nm toplam 200 nm eder; model degeri 180 nm (yaklasik %10 dusuk). 180 nm'nin kaynagi olarak anilan Louwen 2016 icin URL verilmemis ve dogrulanamadi. Deger bu sayfadan dogrudan cikmiyor. (Sayfada: "Taking a cell with 100 nm of ITO applied on both sides as reference" (VON ARDENNE degerlendirmesi). Sayfada baska TCO kalinligi yok.)
- **modul / `mod_T_min_design_C`** — Alintilanan MGM degerleri birebir dogru. Ancak -20 °C degeri sayfalarda yok; bir tasarim secimi. Ankara (-24,9) ve Erzurum (-37,2) rekorlari -20'nin altinda oldugundan -20 bu sahalar icin muhafazakar degil. Almanya verileri (wetterdienst.de, Wikipedia) icin URL verilmedi, kontrol edilmedi. (Sayfada: Istanbul (1950-2025) En Dusuk Sicaklik Subat -9,0; Ankara (1927-2025) Ocak -24,9; Erzurum (1929-2025) Aralik -37,2 °C.)
- **pil / `bat_cell_v_nom_nfpp_V`** — Alintilarin ucu de sayfalarda mevcut. Ancak 2.9 V degeri kaynaklarin hicbirinde NFPP icin dogrudan yazmiyor; 2.85-3.10 V araligindan secilmis muhafazakar bir deger (2.9 V yalnizca kimyasi belirtilmemis 75Ah hucrede geciyor). EVLithium URL'si bu parametrenin olasi_urller listesinde yok, baska parametreden acildi. egroup curl ile engellendi (Mod_Security), WebFetch ile okundu. (Sayfada: egroup: 'SIB-50160118-NFPP-50Ah ... 50Ah capacity and 2.85V platform voltage'; ayrica 'SIB 50160118-75Ah ... 75Ah at 2.9V'. OGSolar: 'SIB-P71173208-160Ah ... Nominal Voltage 3.0 V'. EVLithium 210Ah: 'Nominal Voltage ≈3.10V')
- **pil / `bat_cycle_life_nfpp_pris`** — 5000 degeri hicbir sayfada dogrudan yok; 0.5C'de 6000 ile 1C'de 3000 arasinda muhafazakar bir secim. Ayrica kaynak_alintisi Highstar'in '10,000 cycles'ini %80 cercevesinde sunuyor, oysa sayfada bu deger %70 kapasite icin; Highstar'in %80 icin 0.5P degeri 6000. (Sayfada: OGSolar 160Ah: '0.5C charge ... 0.5C discharge ... at 25 °C. Spec calls out: ≥6000 cycles to 80% of initial capacity; ≥10000 cycles to 70%'. Highstar: 'Charge/discharge energy retention rate≥80% at 6000 times; ≥70% at 10000 times' (0.5P, 25 ℃); '≥80% at 3000 times' (1P, 25 ℃); '≥80% at 2000 times' ()

### Tüm kontroller

| alan | id | sonuç | açılan URL |
|---|---|---|---|
| kristal | cz_crucible_freight_36in_usd | destekliyor | https://solaralliance.eu/wp-content/uploads/2024/03/ESIA-Report-Ingots-and-Wafers.pdf |
| kristal | cz_hotzone_life_h | destekliyor | https://solaralliance.eu/wp-content/uploads/2024/03/ESIA-Report-Ingots-and-Wafers.pdf |
| kristal | xtal_ref_wafer_price_usd_pc | destekliyor | https://www.infolink-group.com/spot-price |
| kristal | xtal_ref_poly_price_usd_kg | destekliyor | https://www.infolink-group.com/spot-price |
| kristal | xtal_si_melting_point_C | destekliyor | https://en.wikipedia.org/wiki/Silicon |
| kristal | cz_seg_coeff_Fe | destekliyor | https://www.cityu.edu.hk/phy/appkchu/AP6120/2.PDF |
| kristal | cz_tau_over_rho_min_us_per_ohmcm | destekliyor | https://taiyangnews.info/technology/constraints-on-wafer-size-for-hjt |
| kristal | cz_t_unload_load_h | destekliyor | https://archive.org/stream/NASA_NTRS_Archive_19780008498/NASA_NTRS_Archive_19780008498_djvu.txt |
| wafer | saw_wire_price_steel_usd_km | kismen | https://mp.ofweek.com/solar/a856714294547 |
| wafer | wf_price_m10_usd | destekliyor | https://www.infolink-group.com/spot-price/ |
| wafer | wf_price_210r_usd | destekliyor | https://www.pv-magazine.com/2026/09/11/china-wafer-prices-fall-as-august-rally-fades-polysilicon-outlook-remains-uncertain/ |
| wafer | wf_poly_price_nonchina_usd_kg | destekliyor | https://www.trendforce.com/price/pv/cell |
| wafer | wf_t_ascut_mature_um | destekliyor | https://taiyangnews.info/technology/wafer-developments-continue-to-support-hjt-adoption |
| wafer | saw_wire_core_um | destekliyor | https://strathprints.strath.ac.uk/94630/1/Ge-etal-MSSP-2025-Progress-and-critical-challenges-in-slicing-of-thin-semiconductor-wafers.pdf |
| wafer | saw_feed_mature_mm_min | destekliyor | https://pmc.ncbi.nlm.nih.gov/articles/PMC11279129/ |
| wafer | wf_weibull_m | destekliyor | https://pmc.ncbi.nlm.nih.gov/articles/PMC9692905/ |
| hucre | hjt_ag_mg_per_W_itrpv_2025 | destekliyor | https://taiyangnews.info/technology/itrpv-sees-pv-shipments-stabilize-at-706-gw-in-2025 |
| hucre | hjt_ito_thickness_total_nm | kismen | https://taiyangnews.info/technology/reducing-indium-in-hjt-tco-processing |
| hucre | hjt_in_price_usd_per_kg | destekliyor | https://tradingeconomics.com/commodity/indium ; https://www.procurementresource.com/resource-center/indium-price-trends ; https://pubs.usgs.gov/periodicals/mcs2025/mcs2025-indium.pdf |
| hucre | hjt_capex_industry_usd_per_Wyr | destekliyor | https://images.assettype.com/taiyangnews/2024-06/4d81d4e5-ecda-429e-92d4-359d5806e4b5/TaiyangNews_Report_Heterojunction_Solar_Technology_2023_download_EN_v2.pdf |
| hucre | cell_eta_industry_2025_pct | destekliyor | https://taiyangnews.info/technology/heterojunction-efficiency-roadmaps-approach-27 |
| hucre | hjt_edge_j02_native_nA_cm | destekliyor | https://d-nb.info/1355800013/34 |
| hucre | hjt_queue_time_max_min | destekliyor | https://www.scientific.net/SSP.187.345 |
| hucre | hjt_breakage_ref | destekliyor | https://www.tradingview.com/news/eqs:c199be9e4094b:0-from-concept-to-mass-production-risen-energy-s-journey-with-ultra-thin-wafers/ ; https://taiyangnews.info/technology/the-supply-side-of-pecvd-tools-for-hjt-part-1 |
| modul | mod_fx_cny_per_usd | destekliyor | https://www.federalreserve.gov/releases/h10/hist/dat00_ch.htm |
| modul | mod_glass_price_usd_m2_per_mm | destekliyor | https://www.energytrend.com/solar-price.html ; https://www.montagtech.com/solar-glass-prices-rebound-what-20mm-and-32mm-buyers-should-know-september-2026 |
| modul | mod_glass_rear_price_usd_m2_per_mm | destekliyor | https://www.energytrend.com/solar-price.html |
| modul | mod_encap_price_usd_m2 | destekliyor | https://faxiangongchang.com/en/reports/china-pv-encapsulation-film-2026 |
| modul | mod_T_min_design_C | kismen | https://www.mgm.gov.tr/veridegerlendirme/il-ve-ilceler-istatistik.aspx?m=ISTANBUL ; ...m=ANKARA ; ...m=ERZURUM |
| modul | mod_classIII_voc_max_V | destekliyor | https://www.sis.se/api/document/preview/8022082/ |
| modul | mod_isc_max_factor | destekliyor | yerel-onbellek://scratchpad/712_2017.txt (web URL degil); alternatif: https://lsp.global/wp-content/uploads/2025/10/IEC-60364-7-712-2017-Part-7-712-Requirements-for-special-installations-or-locations-Solar-photovoltaic-PV-power-supply-systems.pdf |
| modul | mod_gamma_Q | destekliyor | https://www.phd.eng.br/wp-content/uploads/2015/12/en.1990.2002.pdf |
| elektronik | el_fx_usd_try | destekliyor | https://tradingeconomics.com/turkey/currency |
| elektronik | el_cu_price_usd_kg | destekliyor | https://www.westmetall.com/en/markdaten.php?action=table&field=LME_Cu_cash |
| elektronik | el_mcu_usd | destekliyor | https://www.lcsc.com/product-detail/C730123.html |
| elektronik | el_afe_usd | destekliyor | https://www.lcsc.com/product-detail/C2862742.html |
| elektronik | el_Qoss_gan_nC | destekliyor | https://epc-co.com/epc/Portals/0/epc/documents/datasheet/EPC2218_datasheet.pdf |
| elektronik | el_T_charge_max_C | destekliyor | https://ecoteardown.top/wp-content/uploads/2024/01/71173204E-220-220Ah-3.1V-Sodium-ion-Na-ion-Prismatic-Battery-Cell-Specification-Datasheet.pdf |
| elektronik | el_C_charge_cold_C | destekliyor | https://ecoteardown.top/wp-content/uploads/2024/01/71173204E-220-220Ah-3.1V-Sodium-ion-Na-ion-Prismatic-Battery-Cell-Specification-Datasheet.pdf |
| elektronik | el_grid_limit_VA | destekliyor | https://www.dke.de/de/arbeitsfelder/energy/normenhinweise/faq-zur-dinvdev012695 ; https://www.solakon.de/blogs/rechtliches/neue-vde-ar-n-4105-norm |
| pil | bat_fx_cny_per_usd | destekliyor | https://tradingeconomics.com/china/currency |
| pil | bat_cell_price_na_prismatic_usd_Wh | destekliyor | https://www-old.metal.com/price/New-Energy/Sodium-ion-Battery |
| pil | bat_cell_price_lfp_50ah_usd_Wh | destekliyor | https://www-old.metal.com/price/New-Energy/Battery-Cell-And-Module |
| pil | bat_prod_energy_kWh_per_kWh | destekliyor | https://www.nature.com/articles/s41560-023-01355-z |
| pil | bat_cn_li_consumption_tax_frac | destekliyor | https://www.mysteel.net/analysis/5139214-china-lithium-industry-in-h2-2026-from-aggregate-surplus-to-structural-rebalancing |
| pil | bat_cell_v_nom_nfpp_V | kismen | https://egroup18650.com/73-sodium-ion-cells ; https://ogsolarstore.com/blogs/news/cell-review-sodium-ion-nfpp-18650 ; https://www.evlithium.com/sodium-ion-battery/210ah-sodium-prismatic-battery-cell.html |
| pil | bat_cycle_life_nfpp_pris | kismen | https://ogsolarstore.com/blogs/news/cell-review-sodium-ion-nfpp-18650 ; https://www.highstar-sodium.com/technical-characteristics-of-prismatic-sodium-battery-cells/ |
| pil | bat_charge_c_max_subzero | destekliyor | https://www.tycorun.com/products/sodium-ion-26700-battery ; https://www.evlithium.com/sodium-ion-battery/210ah-sodium-prismatic-battery-cell.html |
| altyapi | eco_fx_try_per_usd | destekliyor | https://finans.mynet.com/haber/detay/doviz/26-eylul-2026-dolar-bugun-kac-tl-serbest-piyasa-dolar-kuru-dolar-tl-gunluk-sinirli-yukselis-haftalik-yukselis/577072/ ; https://www.tcmb.gov.tr/kurlar/today.xml |
| altyapi | eco_tr_eurobond_usd_10y | destekliyor | https://hibya.com/eurobond-getirilerinde-yukselis-goruldu-1027379 |
| altyapi | eco_water_isu_sanayi_usd_m3 | destekliyor | https://www.isu.gov.tr/sufiyatlari |
| altyapi | eco_water_isu_osb_usd_m3 | destekliyor | https://www.isu.gov.tr/sufiyatlari |
| altyapi | eco_tr_erp | destekliyor | https://pages.stern.nyu.edu/~adamodar/New_Home_Page/datafile/ctryprem.html |
| altyapi | eco_elec_ptf_try_mwh | destekliyor | https://www.enerjigunlugu.net/spot-elektrik-fiyati-26-08-2026-icin-3634-98-tl-69541h.htm |
| altyapi | site_f_discharge_limit_mg_l | destekliyor | https://web.deu.edu.tr/atiksu/ana39/skkypdf.pdf |
| altyapi | site_seveso_ph3_lower_t | destekliyor | https://www.legislation.gov.uk/uksi/2015/483/schedule/1 ; https://www.resmigazete.gov.tr/eskiler/2019/03/20190302-1.htm (+ ek: 20190302-1-1.pdf) |
| standart | std_selv_pv_uocmax_limit_v | destekliyor | https://lsp.global/wp-content/uploads/2025/10/IEC-60364-7-712-2017-Part-7-712-Requirements-for-special-installations-or-locations-Solar-photovoltaic-PV-power-supply-systems.pdf |
| standart | std_class3_pmax_w | destekliyor | https://www.sis.se/api/document/preview/8022082/ |
| standart | std_lvd_dc_lower_v | destekliyor | https://single-market-economy.ec.europa.eu/sectors/electrical-and-electronic-engineering-industries-eei/low-voltage-directive-lvd_en |
| standart | std_batt_due_diligence_turnover_eur | destekliyor | http://publications.europa.eu/resource/cellar/d0065c31-2ce3-11ee-95a2-01aa75ed71a1.0006.03/DOC_1 ; http://publications.europa.eu/resource/cellar/fe1163e4-6cdd-11f0-bf4e-01aa75ed71a1.0006.03/DOC_1 |
| standart | std_austria_selv_pv_v | destekliyor | https://lsp.global/wp-content/uploads/2025/10/IEC-60364-7-712-2017-Part-7-712-Requirements-for-special-installations-or-locations-Solar-photovoltaic-PV-power-supply-systems.pdf |
| standart | std_selv_dry_no_basic_protection_dc_v | destekliyor | http://erlerdesign.com/download/ESD/old_iec60364-4-41_protection_shock_inst_buildings.pdf |
| standart | std_selv_wet_no_basic_protection_dc_v | destekliyor | http://erlerdesign.com/download/ESD/old_iec60364-4-41_protection_shock_inst_buildings.pdf |
| standart | std_elv_band1_dc_max_v | destekliyor | http://erlerdesign.com/download/ESD/old_iec60364-4-41_protection_shock_inst_buildings.pdf |