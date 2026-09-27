# Varsayım tablosu (Faz 1)

Toplam **965** parametre. Kaynak türü dağılımı: tahmin 592, dogrulanmis_url 165, hesap_turetilmis 117, hafizadan_dogrulanmadi 51, standart_metni_dogrulanmis 27, fizik_ders_kitabi 7, arama_ozeti 6. Güven: dusuk 659, orta 205, yuksek 101.

Kaynak türleri: `dogrulanmis_url` = sayfa bu çalışmada açıldı ve değer görüldü; `arama_ozeti` = yalnız arama özeti (güven ≤ orta); `standart_metni_dogrulanmis`; `hafizadan_dogrulanmadi` (güven ≤ orta); `fizik_ders_kitabi`; `hesap_turetilmis`; `tahmin` (dayanak yazılı, güven ≤ orta). Uydurma kaynak kural olarak yasaktı; bilinmeyen 'bilmiyoruz + doğrulama deneyi' olarak işaretlidir.

**Kaynak denetimi (ölçülen):** kırmızı takım revizyon öncesi 393 kaynağı sayfayı yeniden açarak kontrol etti: 271 destekliyor, 96 kısmen, 21 erişilemedi, 5 desteklemiyor, 0 uydurma şüphesi; bulgular revizyonda düzeltildi. Revizyon sonrası bağımsız örneklem denetiminin sonucu `docs/kaynak_denetimi.md` içindedir. Bu oranlar 'doğrulanmış' etiketli her satırın doğru olduğu anlamına gelmez; kritik parametreler kullanılmadan önce ayrıca kontrol edilmelidir.

Filtrelenebilir tam tablo (kaynak alıntıları, senaryoya uygunluk, doğrulama deneyi dahil): `docs/faz1_varsayimlar.xlsx`.

## Kristal / fırın (`kristal`) — 128 parametre

| id | ad | değer | aralık | birim | güven | kaynak türü | sınıf | eşdeğer | kaynak |
|---|---|---|---|---|---|---|---|---|---|
| xtal_si_melting_point_C | Si erime noktasi | 1414 | 1410 – 1414 | C | yuksek | dogrulanmis_url | teknik |  | https://en.wikipedia.org/wiki/Silicon |
| xtal_si_latent_heat_kJ_kg | Si erime gizli isisi | 1787 | 1655 – 1790 | kJ/kg | yuksek | dogrulanmis_url | teknik |  | https://en.wikipedia.org/wiki/Silicon |
| xtal_si_enthalpy_RT_to_liquid_kWh_kg | Si'yi 25 C'den eriyige getirmenin minimum entalpisi | 0.852 | 0.84 – 0.86 | kWh/kg | yuksek | hesap_turetilmis | teknik |  | https://webbook.nist.gov/cgi/cbook.cgi?ID=C7440213&Mask=2 |
| xtal_si_density_solid_kg_m3 | Kati Si yogunlugu | 2329 | 2328 – 2330 | kg/m3 | yuksek | dogrulanmis_url | teknik |  | https://en.wikipedia.org/wiki/Silicon |
| xtal_si_density_liquid_kg_m3 | Sivi Si yogunlugu (erime noktasinda) | 2570 | 2550 – 2580 | kg/m3 | yuksek | dogrulanmis_url | teknik |  | https://en.wikipedia.org/wiki/Silicon |
| xtal_si_freeze_expansion_frac | Si donarken hacim genlesmesi | 0.103 | 0.09 – 0.105 | - | yuksek | hesap_turetilmis | teknik |  | https://en.wikipedia.org/wiki/Silicon |
| xtal_si_k_solid_Tm_W_mK | Kati Si isil iletkenligi (erime noktasi yakininda) | 22 | 20 – 25 | W/(m.K) | orta | hafizadan_dogrulanmadi | teknik |  | Hafizadan (Si k(T) literatur egrileri); Wikipedia oda sicakligi degeri 149 W/mK |
| cz_vmax_theory_coeff_mm15_min | Isinim sinirli teorik cekme hizi katsayisi C_v (v_th = C_v/sqrt(D_mm)) | 50 | 44 – 56 | mm^1.5/min | orta | hesap_turetilmis | teknik |  | https://www.slideserve.com/devin/crystal-growth-wafer-fabrication-and-basic-properties-of-silicon-wafers |
| cz_fv_nojacket | Ceketsiz pratik govde hizi / teorik v_th orani | 0.36 | 0.28 – 0.5 | - | orta | hesap_turetilmis | teknik |  | https://archive.org/stream/NASA_NTRS_Archive_19780008498/NASA_NTRS_Archive_19780008498_djvu.txt ; https://archive.org/stream/NASA_NTRS_Archi |
| cz_jacket_speed_gain | Su sogutmali ceket ve isi kalkaninin hiz kazanci carpani | 1.25 | 1 – 2 | - | dusuk | tahmin | teknik |  | https://patents.google.com/patent/US11708643B2/en ; TI 1977 (archive.org NTRS 19780008498) |
| cz_pull_rate_cap_mm_min | Kucuk capta govde hizi ust siniri | 3 | 2.2 – 3.7 | mm/min | orta | dogrulanmis_url | teknik |  | https://archive.org/stream/NASA_NTRS_Archive_19780008498/NASA_NTRS_Archive_19780008498_djvu.txt |
| xtal_voronkov_crit_mm2_minK | Voronkov kritik v/G orani | 0.13 | 0.1 – 0.2 | mm2/(min.K) | dusuk | hafizadan_dogrulanmadi | teknik |  | Voronkov kriteri (hafizadan, ~1.3e-3 cm2/(min.K)) |
| cz_seg_coeff_P | Fosfor denge segregasyon katsayisi k0 | 0.35 | 0.3 – 0.35 | - | yuksek | dogrulanmis_url | teknik |  | https://www.cityu.edu.hk/phy/appkchu/AP6120/2.PDF |
| cz_seg_coeff_Fe | Demir segregasyon katsayisi (metal temsilcisi) | 8e-06 | 1e-06 – 1e-05 | - | yuksek | dogrulanmis_url | teknik |  | https://www.cityu.edu.hk/phy/appkchu/AP6120/2.PDF |
| cz_seg_coeff_C | Karbon segregasyon katsayisi | 0.07 | 0.05 – 0.07 | - | yuksek | dogrulanmis_url | teknik |  | https://www.cityu.edu.hk/phy/appkchu/AP6120/2.PDF |
| cz_rho_window_min_ohmcm | HJT wafer ozdirenc penceresi alt siniri | 0.3 | 0.3 – 1 | ohm.cm | orta | dogrulanmis_url | teknik |  | https://taiyangnews.info/technology/wafer-developments-continue-to-support-hjt-adoption |
| cz_rho_window_max_ohmcm | HJT wafer ozdirenc penceresi ust siniri | 2.1 | 1.5 – 5 | ohm.cm | orta | dogrulanmis_url | teknik |  | https://taiyangnews.info/technology/wafer-developments-continue-to-support-hjt-adoption |
| cz_rho_seed_tail_ratio_batch | Batch Cz'de n-tipi tohum/kuyruk ozdirenc orani (kalibrasyon kontrolu) | 7 | 5 – 10 | - | orta | dogrulanmis_url | teknik |  | https://www.linkedin.com/pulse/limiting-factors-n-type-solar-technologies-dr-balachander-krishnan |
| cz_oxygen_interstitial_ppma | Cz ingot ara-yer oksijeni (Oi), beklenen | 15 | 8 – 25 | ppma | dusuk | dogrulanmis_url | teknik |  | https://taiyangnews.info/technology/constraints-on-wafer-size-for-hjt ; https://www.linkedin.com/pulse/limiting-factors-n-type-solar-technol |
| cz_tau_over_rho_min_us_per_ohmcm | n-tipi wafer kalite gostergesi: etkin omur / ozdirenc | 2000 | 1000 – 3000 | us/(ohm.cm) | dusuk | dogrulanmis_url | teknik |  | https://taiyangnews.info/technology/constraints-on-wafer-size-for-hjt |
| xtal_poly_purity_min_N | n-tipi icin asgari poly safligi | 10 | 9 – 11 | N (dokuzlar) | orta | dogrulanmis_url | teknik |  | https://www.linkedin.com/pulse/limiting-factors-n-type-solar-technologies-dr-balachander-krishnan |
| xtal_feed_Fe_ppbw | Beslemedeki (poly) Fe | 0.05 | 0.01 – 0.5 | ppbw | dusuk | tahmin | teknik |  | Kaynak yok |
| xtal_Fe_lim_crystal_cm3 | Kristalde izin verilen Fe (n-tipi HJT omru icin) | 3e+11 | 1e+10 – 1e+12 | cm-3 | dusuk | hafizadan_dogrulanmadi | teknik |  | SRH kaba hesabi, hafizadan: tau = 1/(sigma_p*v_th*N); Fe_i icin sigma_p ~7e-17 cm2 |
| cz_metal_flux_rel_per_ingot | Ingot cevrimi basina pota/sicak bolgeden eriyige gecen metal / taze sarjin getirdigi metal | 1 | 0 – 100 | - | dusuk | tahmin | teknik |  | https://www.cityu.edu.hk/phy/appkchu/AP6120/2.PDF (kuvars pota Fe icerigi) |
| xtal_feed_C_ppma | Besleme ve Cz kristalinde tipik karbon | 0.2 | 0.05 – 0.5 | ppma | orta | dogrulanmis_url | teknik |  | https://pv-manufacturing.org/silicon-production/cz-monocrystalline-silicon-production/ |
| xtal_C_lim_crystal_ppma | Kristalde izin verilen karbon | 1 | 0.5 – 8 | ppma | dusuk | hafizadan_dogrulanmadi | teknik |  | https://archive.org/stream/NASA_NTRS_Archive_19780008498/NASA_NTRS_Archive_19780008498_djvu.txt (buyume siniri); kalite siniri hafizadan |
| cz_C_flux_rel_per_ingot | Ingot cevrimi basina sicak bolgeden (CO) eriyige gecen karbon / taze sarjin getirdigi karbon | 1 | 0 – 10 | - | dusuk | tahmin | teknik |  | Kaynak yok; nitel dayanak TI 1977 |
| cz_crucible_life_h | Kuvars pota omru (sicak saat) | 300 | 150 – 500 | h | dusuk | tahmin | zaman |  | https://solaralliance.eu/wp-content/uploads/2024/03/ESIA-Report-Ingots-and-Wafers.pdf |
| cz_crucible_price_36in_usd | 36 inc PV kuvars pota fiyati | 918 | 600 – 4000 | USD/adet | dusuk | arama_ozeti | zaman |  | https://www.metal.com/Solar/202403270003 |
| cz_crucible_price_fixed_usd | Pota fiyatinin boyuttan bagimsiz kismi | 150 | 80 – 400 | USD/adet | dusuk | tahmin | zaman |  | Kaynak yok |
| cz_crucible_freight_36in_usd | 36 inc pota navlunu (hacimle olceklenir) | 600 | 300 – 1000 | USD/adet | orta | dogrulanmis_url | zaman |  | https://solaralliance.eu/wp-content/uploads/2024/03/ESIA-Report-Ingots-and-Wafers.pdf |
| cz_crucible_diameter_ratio | Pota capi / ingot capi r_cr | 3 | 2 – 3.8 | - | orta | hesap_turetilmis | teknik |  | https://archive.org/stream/NASA_NTRS_Archive_19780008498/NASA_NTRS_Archive_19780008498_djvu.txt ; https://www.pvatepla.com/fileadmin/sitepac |
| cz_ccz_crucible_cost_mult | CCz cift pota/weir maliyet carpani | 1.8 | 1.3 – 3 | - | dusuk | tahmin | zaman |  | Kaynak yok |
| cz_radial_gap_m | Pota duvari ile izolasyon ic yuzu arasi radyal bosluk (susseptor + isitici + bosluklar) | 0.09 | 0.06 – 0.14 | m | dusuk | tahmin | teknik |  | https://www.pvatepla.com/fileadmin/sitepackage/pdf/brochures/PVA_CGS1218.pdf (kisit) |
| cz_insulation_thickness_m | Yan izolasyon kalinligi | 0.12 | 0.08 – 0.25 | m | dusuk | tahmin | teknik |  | Tasarim degiskeni; PVA hazne olcusu kisiti |
| cz_hotzone_height_ratio | Sicak bolge ic yuksekligi / pota capi (RCz) | 1.5 | 1.1 – 2 | - | dusuk | tahmin | teknik |  | https://www.pvatepla.com/fileadmin/sitepackage/pdf/brochures/PVA_CGS1218.pdf (kisit) |
| cz_ccz_hotzone_height_ratio | Sicak bolge ic yuksekligi / pota capi (CCz, sig eriyik) | 1.1 | 0.9 – 1.4 | - | dusuk | tahmin | teknik |  | Kaynak yok |
| cz_hotzone_height_fixed_m | Sicak bolge sabit yukseklik ofseti | 0.3 | 0.2 – 0.5 | m | dusuk | tahmin | teknik |  | Kaynak yok |
| xtal_ins_k_mat_W_mK | Temiz grafit kecenin malzeme isil iletkenligi (sicak yuz 1600 C ile soguk yuz 330-450 C arasi integral ortalama, inert gaz) | 0.13 | 0.1 – 0.2 | W/(m.K) | orta | hesap_turetilmis | teknik |  | https://www.sglcarbon.com/pdf/SGL-Datasheet-SIGRATHERM-GFA-EN.pdf |
| cz_ins_loss_mult | Izolasyon etkin kayip carpani (derz, gecisler, SiO bozunmasi, gaz; k_eff = k_mat * carpan) | 3.8 | 1.5 – 8 | - | dusuk | tahmin | teknik |  | Buyuk firin kalibrasyonu (arama ozeti 59-110 kW) ve CPIA/IEA kWh/kg araligi |
| cz_T_hot_face_K | Izolasyon sicak yuz sicakligi | 1873 | 1800 – 1950 | K | dusuk | tahmin | teknik |  | Kaynak yok |
| cz_T_cold_face_K | Izolasyon soguk yuz sicakligi | 600 | 450 – 800 | K | dusuk | tahmin | teknik |  | Kaynak yok |
| cz_topbottom_penetration_factor | Ust/alt izolasyonda gecis kayip carpani | 1.3 | 1.1 – 1.8 | - | dusuk | tahmin | teknik |  | Kaynak yok |
| cz_q_open_W_m2 | Eriyik serbest yuzeyinden isi kalkani acikligi uzerinden kacan etkin aki (kalkanli) | 30000 | 15000 – 60000 | W/m2 | dusuk | tahmin | teknik |  | Kaynak yok (kara cisim siniri sigma*T_m^4 = 459 kW/m2) |
| cz_q_melt_to_crystal_W_m2 | Eriyikten kristale iletilen isi akisi | 80000 | 40000 – 150000 | W/m2 | dusuk | hafizadan_dogrulanmadi | teknik |  | Sivi Si k~60 W/mK ve sivi gradyan 1-2.5 K/mm (hafizadan) |
| cz_P_electrode_kW | Su sogutmali elektrot ve mil isi kayiplari | 3 | 1 – 6 | kW | dusuk | tahmin | teknik |  | Kaynak yok |
| cz_P_parasitic_fixed_kW | Diger sabit parazitik kayiplar (gozetleme pencereleri, cekme haznesi, besleyici portu) | 2 | 0.5 – 6 | kW | dusuk | tahmin | teknik |  | Kaynak yok |
| cz_jacket_loss_kW_per_m | Su sogutmali ceketin ek isi yuku (kristal capi basina) | 12 | 4 – 30 | kW/m | dusuk | tahmin | teknik |  | Kaynak yok; nitel dayanak TI 1977 |
| cz_gas_exit_dT_K | Argonun sicak bolgeyi terk ederken sicaklik artisi | 1000 | 600 – 1300 | K | dusuk | tahmin | teknik |  | Kaynak yok; Ar cp = 520 J/(kg.K), yogunluk 1.784 kg/Nm3 (fizik) |
| cz_supply_hold_margin | Guc kaynagi boyutlandirmasinda tutma gucu emniyet payi | 1.3 | 1 – 2 | - | dusuk | tahmin | teknik |  | https://archive.org/stream/NASA_NTRS_Archive_19780008498/NASA_NTRS_Archive_19780008498_djvu.txt (kontrol degeri) |
| cz_recharge_melt_target_h | Tasarim resarj ergitme suresi hedefi | 3 | 2 – 6 | h | dusuk | tahmin | teknik |  | https://archive.org/stream/NASA_NTRS_Archive_19790018325/NASA_NTRS_Archive_19790018325_djvu.txt (kontrol) |
| cz_melt_efficiency | Ergitmeye eklenen gucun eriyige gecen orani | 0.7 | 0.5 – 0.85 | - | dusuk | tahmin | teknik |  | Kaynak yok |
| cz_heater_voltage_V | Grafit isitici calisma gerilimi (dusuk basinc Ar'da ark siniri) | 60 | 30 – 100 | V | dusuk | hafizadan_dogrulanmadi | teknik |  | Paschen egrisi, Ar 1-4 kPa (hafizadan) |
| cz_melt_depth_ratio | Eriyik derinligi / pota capi (RCz) | 0.55 | 0.4 – 0.7 | - | dusuk | tahmin | teknik |  | Kaynak yok |
| cz_ccz_melt_depth_ratio | Eriyik derinligi / pota capi (CCz) | 0.25 | 0.15 – 0.35 | - | dusuk | tahmin | teknik |  | Kaynak yok |
| cz_crucible_fill | Pota doluluk orani | 0.85 | 0.75 – 0.9 | - | dusuk | tahmin | teknik |  | Kaynak yok |
| cz_g_pull | RCz'de ingot basina cekilen eriyik orani g | 0.8 | 0.6 – 0.9 | - | orta | tahmin | teknik |  | https://archive.org/stream/NASA_NTRS_Archive_19780008498/NASA_NTRS_Archive_19780008498_djvu.txt (kontrol) |
| cz_L_body_max_mm | Hazne ile sinirli azami govde boyu | 2500 | 1200 – 3800 | mm | orta | dogrulanmis_url | teknik |  | https://www.trinasolar.com/us/resources/newsroom/first-210mm-ingot-production-2023 ; https://www.pvatepla.com/fileadmin/sitepackage/pdf/broc |
| cz_ccz_L_ingot_mm | CCz ingot boyu | 2000 | 1200 – 3000 | mm | dusuk | tahmin | teknik |  | Kaynak yok |
| cz_t_stabilize_h | Ilk ergitme sonrasi eriyik sabitleme suresi | 1.5 | 1 – 3 | h | dusuk | tahmin | teknik |  | Kaynak yok |
| cz_t_seed_neck_h | Ingot basina tohum daldirma, sabitleme ve Dash boyun suresi (omuz haric) | 1 | 0.5 – 2 | h | orta | hesap_turetilmis | teknik |  | https://archive.org/stream/NASA_NTRS_Archive_19780008498/NASA_NTRS_Archive_19780008498_djvu.txt |
| cz_shoulder_speed_mm_min | Omuz (crown) buyutme hizi | 1 | 0.83 – 1.33 | mm/min | orta | dogrulanmis_url | teknik |  | https://patents.google.com/patent/US11708643B2/en |
| cz_shoulder_height_ratio | Omuz yuksekligi / D | 0.4 | 0.2 – 0.6 | - | dusuk | tahmin | teknik |  | Kaynak yok |
| cz_tail_speed_mm_min | Kuyruk konisi hizi | 1 | 0.5 – 1.33 | mm/min | orta | dogrulanmis_url | teknik |  | https://patents.google.com/patent/US11708643B2/en |
| cz_tail_length_ratio | Kuyruk konisi boyu / D | 0.6 | 0.4 – 1 | - | dusuk | tahmin | teknik |  | Kristal tahmini; wafer tahmini 0.8 |
| cz_t_cool_base_h | Ingot sogutma suresi, sabit kisim | 0.5 | 0.25 – 1 | h | dusuk | tahmin | teknik |  | Isinimla soguma kaba hesabi (fizik denetcisi: 120 mm icin ideal ~0.9 h) |
| cz_t_cool_per_mm_h | Sogutma suresinin capla artan kismi | 0.005 | 0.003 – 0.01 | h/mm | dusuk | tahmin | teknik |  | Isinimla soguma ~D |
| cz_t_unload_load_h | Kristali vanadan alma ve besleyiciyi yukleme (ergitme haric) | 1 | 0.5 – 2 | h | orta | dogrulanmis_url | teknik |  | https://archive.org/stream/NASA_NTRS_Archive_19780008498/NASA_NTRS_Archive_19780008498_djvu.txt |
| cz_t_turnaround_h | Pota degisimi toplam durus (soguma, temizlik, montaj, pompalama, isitma) | 24 | 12 – 40 | h | dusuk | tahmin | teknik |  | https://solaralliance.eu/wp-content/uploads/2024/03/ESIA-Report-Ingots-and-Wafers.pdf |
| cz_heatup_h | Pota degisimi sonrasi isitma suresi (durus icinde) | 4 | 2 – 6 | h | dusuk | tahmin | teknik |  | Kaynak yok |
| cz_heatup_power_frac | Isitma sirasinda ortalama guc / guc kaynagi | 0.7 | 0.5 – 1 | - | dusuk | tahmin | teknik |  | Kaynak yok |
| cz_aux_turnaround_frac | Durus suresinin yardimci yuklerin calistigi kismi | 0.5 | 0.3 – 1 | - | dusuk | tahmin | teknik |  | Kaynak yok |
| cz_turnaround_crew_person_h | Pota degisimi iscilik | 16 | 8 – 48 | kisi.h/kampanya | dusuk | tahmin | zaman |  | https://solaralliance.eu/wp-content/uploads/2024/03/ESIA-Report-Ingots-and-Wafers.pdf |
| cz_availability_unplanned | Plansiz durus sonrasi kullanilabilirlik | 0.9 | 0.8 – 0.97 | - | dusuk | tahmin | teknik |  | Kaynak yok |
| cz_zd_yield | Dislokasyonsuz (ZD) kutle verimi, olgun isletme | 0.8 | 0.6 – 0.95 | - | dusuk | tahmin | teknik |  | https://archive.org/stream/NASA_NTRS_Archive_19790018325/NASA_NTRS_Archive_19790018325_djvu.txt (ogrenme noktasi); olgun deger tahmin |
| cz_ccz_zd_mult | CCz'de ZD verim carpani (besleme sicramasi, partikul) | 0.9 | 0.7 – 1 | - | dusuk | tahmin | teknik |  | Kaynak yok |
| cz_P_aux_fixed_kW | Yardimci yuk, sabit kisim (kontrol, tahrikler, kucuk pompa) | 4 | 2 – 8 | kW | dusuk | tahmin | teknik |  | Kaynak yok |
| cz_P_aux_per_m2_kW | Yardimci yukun pota alaniyla olceklenen kismi (vakum pompasi, gaz) | 8 | 4 – 15 | kW/m2 | dusuk | tahmin | teknik |  | Kaynak yok |
| cz_cooling_energy_frac | Sogutma sistemi enerjisi / isitici enerjisi | 0.08 | 0.03 – 0.25 | - | dusuk | arama_ozeti | teknik |  | https://www.sciencedirect.com/science/article/pii/S0022024825000545 (acilamadi) |
| cz_argon_slpm_ref_36in | Argon debisi referansi (36 inc pota esdegeri) | 100 | 50 – 150 | slpm | dusuk | tahmin | zaman |  | https://www.comsol.com/blogs/thermal-analysis-of-a-czochralski-crystal-growth-furnace (yalnizca mertebe) |
| cz_argon_scaling_exp | Argon debisinin pota capiyla olcekleme usteli | 1 | 0.5 – 2 | - | dusuk | tahmin | teknik |  | Kaynak yok |
| cz_chamber_pressure_Pa | Hazne basinci | 2500 | 1300 – 4000 | Pa | orta | dogrulanmis_url | teknik |  | https://archive.org/stream/NASA_NTRS_Archive_19780008498/NASA_NTRS_Archive_19780008498_djvu.txt ; https://www.comsol.com/blogs/thermal-analy |
| cz_capex_fixed_usd | Kendi tasarimi cekicinin sabit capex'i (cekme kafasi, kontrol, kamera/pirometre, pompa, gaz paneli, izolasyon vanasi, besleyici, cerceve) | 120000 | 60000 – 350000 | USD | dusuk | tahmin | zaman |  | Kaynak yok; tarihi referans TI 1977 |
| cz_capex_per_crucible_area_usd_m2 | Boyutla olceklenen capex / D_cr^2 (hazne, pota mekanizmasi) | 150000 | 80000 – 300000 | USD/m2 | dusuk | tahmin | zaman |  | Kaynak yok |
| cz_capex_power_usd_per_kW | Isitici guc kaynagi capex'i | 250 | 150 – 500 | USD/kW | dusuk | tahmin | zaman |  | Kaynak yok |
| cz_ccz_feeder_capex_usd | CCz surekli besleyici ek capex'i | 40000 | 15000 – 100000 | USD | dusuk | tahmin | zaman |  | Kaynak yok |
| xtal_safety_capex_frac | Guvenlik ve deprem ek capex'i (dokulme tavasi, ankraj, sismik anahtar, O2 monitoru, su kacak algilama) | 0.05 | 0.02 – 0.12 | - | dusuk | tahmin | zaman |  | Kaynak yok |
| xtal_puller_nre_usd | Cekici tasarim gelistirme maliyeti (NRE: muhendislik, prototip, iterasyon) | 600000 | 250000 – 1.5e+06 | USD/makine tipi | dusuk | tahmin | urun_sabit |  | Kaynak yok |
| xtal_puller_ce_usd | Makine tipi basina CE uygunluk dosyasi (risk analizi, teknik dosya, EN 60204-1 testleri) | 40000 | 15000 – 100000 | USD/makine tipi | dusuk | hafizadan_dogrulanmadi | urun_sabit |  | Makine Emniyeti Yonetmeligi (2006/42/AT uyumlu); AB 2023/1230'un 2027-01-20'de yururluge girmesi (hafizadan) |
| cz_hotzone_cost_usd_m2 | Grafit sicak bolge seti maliyeti / sicak bolge ic yuzeyi | 6000 | 3000 – 20000 | USD/m2 | dusuk | tahmin | zaman |  | Kaynak yok |
| cz_hotzone_life_h | Sicak bolge seti omru | 5800 | 3000 – 8000 | h | dusuk | dogrulanmis_url | zaman |  | https://solaralliance.eu/wp-content/uploads/2024/03/ESIA-Report-Ingots-and-Wafers.pdf |
| cz_puller_life_yr | Cekici amortisman omru | 7 | 2 – 15 | yil | dusuk | tahmin | zaman | → `eco_life_machine_yr` | https://solaralliance.eu/wp-content/uploads/2024/03/ESIA-Report-Ingots-and-Wafers.pdf ; TI 1977 |
| cz_maint_frac | Yillik bakim / capex | 0.04 | 0.02 – 0.08 | 1/yil | dusuk | tahmin | zaman | → `eco_maint_frac_capex_yr` | Kaynak yok |
| xtal_operator_hours_per_furnace_hour | Firin saati basina operator saati (kucuk unite) | 0.5 | 0.2 – 1 | h/h | dusuk | tahmin | zaman |  | https://archive.org/stream/NASA_NTRS_Archive_19780008498/NASA_NTRS_Archive_19780008498_djvu.txt ; https://solaralliance.eu/wp-content/upload |
| xtal_outage_events_per_yr | Eriyik kaybina yol acan kesinti sayisi (yedek guc yoksa) | 2 | 0.5 – 10 | 1/yil | dusuk | tahmin | zaman |  | Kaynak yok |
| xtal_outage_loss_usd_per_event | Kesinti basina kayip (pota, eriyik hurdasi, kirik susseptor, durus) | 3000 | 1000 – 15000 | USD/olay | dusuk | tahmin | zaman |  | Kaynak yok |
| xtal_price_electricity_usd_kwh | Elektrik fiyati (YER TUTUCU) | 0.1 | 0.07 – 0.16 | USD/kWh | dusuk | tahmin | zaman | → `eco_elec_price_usd_kwh` | Kaynak yok |
| xtal_price_argon_usd_nm3 | Argon fiyati (YER TUTUCU) | 0.8 | 0.3 – 2 | USD/Nm3 | dusuk | tahmin | zaman | → `eco_price_argon_usd_kg` × 1.784 | Kaynak yok |
| xtal_wage_usd_h | Teknisyen tam yuklu saat ucreti (YER TUTUCU) | 12 | 8 – 20 | USD/h | dusuk | tahmin | zaman | → `eco_labor_technician_usd_h` | Kaynak yok |
| xtal_wacc | Sermaye maliyeti (YER TUTUCU) | 0.1 | 0.06 – 0.2 | 1/yil | dusuk | tahmin | zaman | → `eco_wacc_usd` | Kaynak yok |
| xtal_recycle_remelt_frac | Kare kesim artigi ve uclarin tekrar eritilebilir orani | 0.85 | 0.6 – 0.95 | - | dusuk | tahmin | alan |  | Kaynak yok |
| xtal_recycle_etch_loss_frac | Geri donusum dagliamada kutle kaybi | 0.01 | 0.003 – 0.03 | - | dusuk | tahmin | alan |  | Kaynak yok |
| xtal_pot_scrap_frac_of_charge | Kampanya sonu pota artigi / pota sarji | 0.05 | 0.02 – 0.2 | - | dusuk | tahmin | alan |  | Kaynak yok |
| cz_mcz_field_T | MCZ manyetik alan siddeti (kullanilirsa) | 0.15 | 0 – 0.4 | T | dusuk | tahmin | teknik |  | https://www.pvatepla.com/fileadmin/sitepackage/pdf/brochures/PVA_CGS1218.pdf (ust referans) |
| fz_rf_frequency_MHz | FZ RF induksiyon frekansi | 3 | 1.7 – 3 | MHz | orta | dogrulanmis_url | teknik |  | https://arxiv.org/pdf/1102.3800 |
| fz_diameter_max_mm | FZ cap siniri | 200 | 150 – 200 | mm | yuksek | dogrulanmis_url | teknik |  | https://en.wikipedia.org/wiki/Float-zone_silicon |
| fz_pull_rate_ref_mm_min | FZ govde hizi @100 mm | 3.2 | 2.5 – 3.6 | mm/min | dusuk | arama_ozeti | teknik |  | https://publica.fraunhofer.de/bitstreams/35c55b63-af15-4b78-b7b8-5ff210b2e69a/download (erisilemedi) |
| fz_pull_rate_diam_exponent | FZ hiz-cap usteli b | -0.33 | -0.5 – -0.2 | - | dusuk | hesap_turetilmis | teknik |  | fz_pull_rate_ref ile ayni iki noktadan |
| fz_power_ref_kW | FZ toplam guc @100 mm | 44 | 35 – 60 | kW | dusuk | arama_ozeti | teknik |  | https://publica.fraunhofer.de/bitstreams/35c55b63-af15-4b78-b7b8-5ff210b2e69a/download (erisilemedi) |
| fz_power_diam_exponent | FZ guc-cap usteli a | 2 | 1.5 – 2.2 | - | dusuk | hesap_turetilmis | teknik |  | Iki noktadan hesap |
| fz_overhead_per_crystal_h | FZ kristal basina ek sure | 5 | 3 – 8 | h | dusuk | tahmin | teknik |  | Kaynak yok |
| fz_standby_power_frac | FZ ek sure boyunca ortalama guc / buyutme gucu | 0.4 | 0.2 – 0.6 | - | dusuk | tahmin | teknik |  | Kaynak yok |
| fz_zd_yield | FZ dislokasyonsuz verim | 0.75 | 0.5 – 0.9 | - | dusuk | tahmin | teknik |  | Kaynak yok |
| fz_crystal_length_mm | FZ kristal boyu | 1500 | 1000 – 2000 | mm | dusuk | tahmin | teknik |  | Kaynak yok |
| fz_oxygen_cm3 | FZ Si oksijen ve karbon konsantrasyonu (ust sinir) | 5e+15 | 1e+15 – 5e+15 | cm-3 | yuksek | dogrulanmis_url | teknik |  | https://sinovoltaics.com/learning-center/solar-cells/float-zone-silicon-cells-fz/ |
| fz_feed_rod_premium_usd_kg | FZ kalitesi besleme cubugunun parca poly'ye gore fiyat primi | 20 | 5 – 50 | USD/kg | dusuk | tahmin | alan |  | https://www.csp.fraunhofer.de/en/areas-of-research/crystallization/Float-Zone-Solar-Cells-Low-Cost-Feed-Material.html (yalnizca nitel) |
| fz_capex_fixed_usd | Kendi tasarimi FZ makinesi sabit capex'i (hazne, mekanik, kontrol) | 250000 | 150000 – 600000 | USD | dusuk | tahmin | zaman |  | Kaynak yok |
| fz_capex_rf_usd_per_kW | MHz RF jenerator capex'i | 400 | 200 – 1000 | USD/kW | dusuk | tahmin | zaman |  | Kaynak yok |
| fz_argon_slpm | FZ argon tuketimi | 30 | 10 – 80 | slpm | dusuk | tahmin | zaman |  | Kaynak yok |
| fz_consumables_usd_h | FZ sarf (bobin asinmasi, reflektorler) | 1 | 0.5 – 3 | USD/h | dusuk | tahmin | zaman |  | Kaynak yok |
| xtal_industry_kwh_per_kg | Sektor Cz cekme elektrik tuketimi (kalibrasyon referansi) | 22.3 | 13.5 – 25 | kWh/kg | yuksek | dogrulanmis_url | teknik |  | https://taiyangnews.info/technology/china-updates-solar-pv-energy-consumption-efficiency-standards ; https://iea-pvps.org/wp-content/uploads |
| xtal_industry_MWp_per_puller_yr | Sektor cekici basina cikti (kalibrasyon) | 16 | 15 – 17 | MWp/yil | orta | dogrulanmis_url | teknik |  | https://solaralliance.eu/wp-content/uploads/2024/03/ESIA-Report-Ingots-and-Wafers.pdf |
| xtal_calib_heater_power_large_kW | Buyuk endustriyel cekici govde buyutme isitici gucu (kalibrasyon) | 80 | 59 – 110 | kW | dusuk | arama_ozeti | teknik |  | ScienceDirect/Springer ozetleri (acilamadi) |
| xtal_calib_TI1977_hold_kW | Kucuk olcek olculmus isletme gucu (TI 1977; 12 cm kristal, 12 kg pota, yaricap 12.3 cm) | 45 | 45 – 80 | kW | orta | dogrulanmis_url | teknik |  | https://archive.org/stream/NASA_NTRS_Archive_19780008498/NASA_NTRS_Archive_19780008498_djvu.txt |
| xtal_graphite_ash_ppm | Sicak bolge grafit/kece kul icerigi (saflastirilmis) | 20 | 5 – 1000 | ppm | yuksek | dogrulanmis_url | teknik |  | https://www.sglcarbon.com/pdf/SGL-Datasheet-SIGRATHERM-GFA-EN.pdf |
| xtal_ref_wafer_price_usd_pc | Satin alinan n-tipi wafer spot fiyati (182-183.75 mm, 130 um) | 0.148 | 0.141 – 0.25 | USD/adet | yuksek | dogrulanmis_url | alan | → `wf_price_m10_usd` | https://www.infolink-group.com/spot-price |
| xtal_ref_wafer_area_m2 | 182 mm wafer alani | 0.033 | 0.0328 – 0.0335 | m2 | orta | hesap_turetilmis | teknik |  | Geometriden hesap |
| xtal_ref_poly_price_usd_kg | Mono sinifi poly fiyati | 18.5 | 5 – 27 | USD/kg | yuksek | dogrulanmis_url | alan | → `wf_poly_price_nonchina_usd_kg` | https://www.infolink-group.com/spot-price |

## Wafer (`wafer`) — 95 parametre

| id | ad | değer | aralık | birim | güven | kaynak türü | sınıf | eşdeğer | kaynak |
|---|---|---|---|---|---|---|---|---|---|
| wf_si_density_kg_m3 | Silisyum yogunlugu (oda sicakligi) | 2329 | 2329 – 2329 | kg/m3 | yuksek | fizik_ders_kitabi | teknik |  | https://en.wikipedia.org/wiki/Silicon |
| wf_t_ascut_mature_um | HJT as-cut wafer kalinligi, olgun hat | 110 | 100 – 120 | um | orta | dogrulanmis_url | teknik |  | https://taiyangnews.info/technology/wafer-developments-continue-to-support-hjt-adoption |
| wf_t_ascut_firstgen_um | HJT as-cut wafer kalinligi, ilk nesil (varsayilan) | 125 | 115 – 135 | um | dusuk | tahmin | teknik |  | Wafer: ilk nesil tahmin (satin alinan n-tipi 130 um'den TTV payi); olgun 110 um TaiyangNews; nihai alt sinir 80 um |
| wf_t_final_min_um | Nihai (dokulama sonrasi) HJT wafer kalinligi alt siniri | 80 | 75 – 90 | um | orta | dogrulanmis_url | teknik |  | https://taiyangnews.info/technology/low-temperature-hjt-manufacturing-adapts-to-wider-wafer-variants |
| wf_texture_removal_um | Hasar daglama + dokulamada toplam kalinlik kaybi (iki yuz) | 15 | 8 – 25 | um | dusuk | hafizadan_dogrulanmadi | teknik | → `hjt_si_etch_removal_um` | hafiza; hucre ajaniyla ortak |
| saw_wire_core_um | Elmas tel cekirdek capi (ilk nesil: karbon celik) | 36 | 28 – 40 | um | orta | dogrulanmis_url | teknik |  | https://strathprints.strath.ac.uk/94630/1/Ge-etal-MSSP-2025-Progress-and-critical-challenges-in-slicing-of-thin-semiconductor-wafers.pdf |
| saw_wire_coating_add_um | Elmas kaplamanin tel capina ekledigi (dis cap eksi cekirdek) | 15 | 12 – 20 | um | orta | dogrulanmis_url | teknik |  | https://strathprints.strath.ac.uk/94630/1/Ge-etal-MSSP-2025-Progress-and-critical-challenges-in-slicing-of-thin-semiconductor-wafers.pdf |
| saw_kerf_excess_um | Tel titresimi/sapmasi kaynakli ek kerf (dis cap ustu) | 6 | 2 – 12 | um | dusuk | tahmin | teknik |  | tahmin |
| saw_kerf_firstgen_um | Kerf, ilk nesil kendi testeremiz (varsayilan) | 57 | 48 – 65 | um | orta | hesap_turetilmis | teknik |  | Wafer: tel geometrisi 36 + 15 + 6 = 57 um (saw_kerf_calc); capa qualenergia/ITRPV 2023 |
| saw_kerf_mature_um | Kerf, olgun testere + ~30 um tungsten tel | 50 | 45 – 55 | um | orta | hesap_turetilmis | teknik |  | https://cdn.qualenergia.it/wp-content/uploads/2023/05/itrpv_2023.pdf ; https://strathprints.strath.ac.uk/94630/1/Ge-etal-MSSP-2025-Progress- |
| wf_ttv_um | Toplam kalinlik degiskenligi (TTV), ilk nesil | 15 | 8 – 25 | um | dusuk | tahmin | teknik |  | tahmin (olgun capa ITRPV 2023) |
| saw_wire_speed_m_s | Tel hizi, ilk nesil | 25 | 15 – 40 | m/s | dusuk | tahmin | teknik |  | tahmin (endustri capasi Ge 2025) |
| saw_feed_firstgen_mm_min | Besleme hizi, ilk nesil (~182 mm temas) | 1.2 | 0.8 – 1.75 | mm/dk | dusuk | tahmin | teknik |  | tahmin |
| saw_feed_mature_mm_min | Besleme hizi, olgun endustri (~182 mm temas) | 1.75 | 1.5 – 2 | mm/dk | orta | dogrulanmis_url | teknik |  | https://pmc.ncbi.nlm.nih.gov/articles/PMC11279129/ |
| saw_feed_contact_exp | Besleme hizinin tel basina Si temas uzunluguna bagimlilik ussu (beta) | 0.5 | 0 – 1 | - | dusuk | tahmin | teknik |  | tahmin |
| saw_L_load_mm | Yuklu tugla boyu (tel agi uzunlugu), kendi tasarim | 600 | 300 – 950 | mm | orta | tahmin | teknik |  | tasarim secimi |
| saw_W_web_mm | Kullanilabilir tel agi genisligi (yan yana tugla icin) | 250 | 200 – 450 | mm | dusuk | tahmin | teknik |  | tasarim tahmini |
| saw_brick_gap_mm | Yan yana tuglalar arasi bosluk | 5 | 3 – 10 | mm | dusuk | tahmin | teknik |  | tahmin |
| saw_overcut_mm | Asiri kesim (recine plakaya giris) ve yaklasma | 3 | 2 – 6 | mm | dusuk | tahmin | teknik |  | tahmin |
| saw_t_overhead_h | Kesim disi cevrim suresi (yukleme, bosaltma, tel agi, temizlik), ilk nesil | 1 | 0.5 – 1.5 | saat/cevrim | dusuk | tahmin | teknik |  | tahmin |
| saw_uptime | Testere kullanilabilirlik orani, ilk nesil | 0.85 | 0.75 – 0.95 | - | dusuk | tahmin | teknik |  | tahmin |
| saw_wire_use_ref_m_per_m2 | Tel tuketimi, kesilen wafer alani basina (referans kerf 57 um, olgun endustri) | 115 | 105 – 121 | m/m2 | orta | hesap_turetilmis | alan |  | https://www.infolink-group.com/energy-article/quest-for-thinner-wafers-and-wires-ramp-up-tungsten-diamond-wire-application |
| saw_wire_use_mult_firstgen | Ilk nesil testerede tel tuketimi carpani | 1.8 | 1 – 2.5 | - | dusuk | tahmin | alan |  | tahmin |
| saw_wire_price_steel_usd_km | Elmas tel fiyati (celik cekirdek agirlikli ortalama) | 2.5 | 1.8 – 5.5 | USD/km | dusuk | hesap_turetilmis | alan |  | https://mp.ofweek.com/solar/a856714294547 |
| saw_wire_price_w_usd_km | Tungsten cekirdekli elmas tel fiyati | 3.5 | 2.5 – 6 | USD/km | dusuk | tahmin | alan |  | tahmin; alt capa https://finance.sina.com.cn/roll/2025-01-07/doc-ineecmqz1633344.shtml |
| saw_coolant_usd_m2 | Sogutma sivisi ve katki maliyeti | 0.3 | 0.1 – 1 | USD/m2 | dusuk | tahmin | alan |  | tahmin |
| saw_beam_usd_m2 | Recine plaka + tutkal maliyeti (plaka alani basina) | 150 | 50 – 400 | USD/m2 plaka | dusuk | tahmin | adet |  | tahmin |
| saw_power_kW | Testere ortalama elektrik gucu (600 mm yuk) | 25 | 10 – 60 | kW | dusuk | tahmin | zaman |  | tahmin |
| saw_capex_usd | Kendi yapim cok telli testere yatirimi | 200000 | 80000 – 500000 | USD | dusuk | tahmin | zaman |  | tahmin |
| saw_filtration_capex_usd | Sogutma sivisi filtrasyonu ve kerf camuru susuzlastirma yatirimi | 50000 | 20000 – 150000 | USD | dusuk | tahmin | zaman |  | tahmin |
| saw_maint_usd_per_h | Testere bakim sarfi (makara PU kaplama yenileme, rulman, filtre) | 8 | 3 – 20 | USD/calisma saati | dusuk | tahmin | zaman |  | tahmin |
| saw_life_yr | Wafer ekipmanlari amortisman omru | 8 | 5 – 12 | yil | dusuk | tahmin | zaman | → `eco_life_machine_yr` | tahmin |
| saw_labor_h_per_cycle | Testere cevrimi basina iscilik | 1 | 0.5 – 2 | adam-saat/cevrim | dusuk | tahmin | zaman |  | tahmin |
| wf_staff_min_per_shift | Wafer alani asgari vardiya personeli (kare kesim, testere, ayirma, temizlik, muayene, geri donusum) | 1.5 | 1 – 3 | kisi/vardiya | dusuk | tahmin | zaman |  | tahmin |
| sq_kerf_mm | Kare kesim / tugla bolme kerfi | 0.4 | 0.25 – 1.5 | mm | dusuk | tahmin | teknik |  | tahmin |
| sq_grind_margin_mm | As-grown ile kullanilabilir cap arasi radyal pay | 2 | 1 – 5 | mm | dusuk | tahmin | teknik |  | tahmin |
| sq_D_over_a_pseudo | Psodo-kare (tek parca veya kxk blok): taslanmis cap / blok kenari | 1.3557 | 1.2 – 1.4142 | - | orta | hafizadan_dogrulanmadi | teknik |  | M10 (182.2 mm, cap 247 mm); G12 (210 mm, cap 295 mm) |
| sq_chamfer_max_frac | Izin verilen kose pahi bacagi / wafer kenari | 0.1 | 0.04 – 0.2 | - | dusuk | tahmin | teknik |  | tahmin |
| sq_capex_usd | Kare kesim + silindirik taslama + tugla bolme makinesi yatirimi | 150000 | 60000 – 400000 | USD | dusuk | tahmin | zaman |  | tahmin |
| sq_cut_rate_m2_h | Kare kesim / bolme makinesi kesim yuzeyi hizi | 2 | 0.5 – 5 | m2 kesim yuzeyi/saat | dusuk | tahmin | teknik |  | tahmin |
| sq_consumable_usd_m2cut | Kare kesim sarfi (tel/serit), kesim yuzeyi basina | 1 | 0.3 – 5 | USD/m2 kesim | dusuk | tahmin | alan |  | tahmin |
| wf_crown_h_over_D | Tac/omuz konisi yuksekligi / ingot capi | 0.35 | 0.15 – 0.6 | - | dusuk | tahmin | teknik | → `cz_shoulder_height_ratio` | tahmin |
| wf_tail_h_over_D | Kuyruk konisi yuksekligi / ingot capi | 0.8 | 0.4 – 1.2 | - | dusuk | tahmin | teknik | → `cz_tail_length_ratio` | tahmin |
| wf_crop_mm | Govdeden kesilen uc ve test dilimleri | 20 | 10 – 50 | mm/ingot | dusuk | tahmin | teknik |  | tahmin |
| wf_brick_end_mm | Tugla ucu basina kayip (yarim/kirik ilk-son wafer'lar) | 3 | 1 – 8 | mm/uc | dusuk | tahmin | teknik |  | tahmin |
| wf_break_wafering_ref_firstgen | Kesim + tutkal cozme + on temizlik kirilma orani, ilk nesil (182 mm, 130 um referansi) | 0.02 | 0.005 – 0.06 | - | dusuk | tahmin | teknik |  | tahmin |
| wf_break_wafering_ref_mature | Kesim + tutkal cozme + on temizlik kirilma orani, olgun (182 mm, 130 um) | 0.005 | 0.002 – 0.015 | - | dusuk | tahmin | teknik |  | tahmin |
| wf_break_cell_ref_mature | HJT hucre hatti kirilma orani, olgun hat (110 um) | 0.0025 | 0.001 – 0.005 | - | orta | dogrulanmis_url | teknik |  | https://www.prnewswire.co.uk/news-releases/from-concept-to-mass-production-risen-energys-journey-with-ultra-thin-wafers-302711087.html |
| wf_break_cell_ref_firstgen | HJT hucre hatti kirilma orani, ilk nesil (110 um referansi) | 0.02 | 0.005 – 0.1 | - | dusuk | tahmin | teknik |  | tahmin; capalar https://pmc.ncbi.nlm.nih.gov/articles/PMC11076549/ ve https://arxiv.org/pdf/1906.06770 |
| wf_break_exp_thickness | Kesim kirilmasinin kalinlik ussu n_t: P ~ (t_ref/t)^n_t | 3.8 | 2.5 – 5 | - | dusuk | hesap_turetilmis | teknik |  | https://pmc.ncbi.nlm.nih.gov/articles/PMC9692905/ |
| wf_break_exp_thickness_cell | Hucre adimlari kirilmasinin kalinlik ussu | 3.8 | 1.5 – 6 | - | dusuk | tahmin | teknik |  | tahmin |
| wf_break_exp_size | Kirilmanin boyut ussu n_a: P ~ (a/a_ref)^n_a | 3 | 1 – 8 | - | dusuk | tahmin | teknik |  | Wafer tahmini (Weibull + plak teorisi sinirlari); hucre tahmini us 1 (0.5-2) |
| wf_weibull_m | As-cut wafer Weibull modulu | 3.5 | 3 – 10 | - | orta | dogrulanmis_url | teknik |  | https://pmc.ncbi.nlm.nih.gov/articles/PMC9692905/ |
| wf_weibull_sigma0_MPa | As-cut wafer Weibull karakteristik dayanimi | 151 | 100 – 300 | MPa | orta | dogrulanmis_url | teknik |  | https://pmc.ncbi.nlm.nih.gov/articles/PMC9692905/ |
| wf_break_floor_frac | Kirilmanin boyut ve kalinliktan bagimsiz taban payi (referansa oran) | 0.25 | 0.1 – 0.5 | - | dusuk | tahmin | teknik |  | tahmin |
| wf_reject_quality | Kirilma disi kalite ret orani | 0.015 | 0.005 – 0.05 | - | dusuk | tahmin | teknik |  | tahmin |
| wf_learn_half_m2 | Ogrenme egrisi: ilk nesil-olgun farkinin yarilandigi kumulatif iyi wafer alani | 50000 | 10000 – 300000 | m2 | dusuk | tahmin | teknik |  | tahmin |
| wf_etch_depth_um | Geri donusum parcalari icin yuzey daglama derinligi | 30 | 10 – 100 | um | dusuk | tahmin | teknik |  | tahmin |
| wf_scrap_chunk_mm | Besleyici icin geri donusum parca boyu (kirma sonrasi) | 20 | 5 – 50 | mm | dusuk | tahmin | teknik |  | tahmin |
| wf_etch_util_factor | Asit kullanimi / stokiyometrik ihtiyac orani | 3 | 1.5 – 6 | - | dusuk | tahmin | teknik |  | tahmin |
| wf_hf_stoich_kg_per_kg | Daglanan kg Si basina HF (100% baz) | 4.27 | 4.27 – 4.27 | kg/kg Si | yuksek | hesap_turetilmis | teknik |  | 3Si + 4HNO3 + 18HF -> 3H2SiF6 + 4NO + 8H2O |
| wf_hno3_stoich_kg_per_kg | Daglanan kg Si basina HNO3 (100% baz) | 2.99 | 2.99 – 8.97 | kg/kg Si | orta | hesap_turetilmis | teknik |  | stokiyometri (NO ve NO2 yollari) |
| wf_hf_price_usd_kg | HF fiyati (100% baz, teslim) | 2.5 | 1 – 6 | USD/kg | dusuk | tahmin | alan |  | tahmin |
| wf_hno3_price_usd_kg | HNO3 fiyati (100% baz, teslim) | 0.6 | 0.3 – 1.5 | USD/kg | dusuk | tahmin | alan |  | tahmin |
| wf_waste_treat_usd_per_kg_si | Daglama atigi notralizasyon ve bertarafi (daglanan kg Si basina) | 4 | 1.5 – 10 | USD/kg Si | dusuk | tahmin | alan |  | tahmin |
| wf_crusher_capex_usd | Kontaminasyonsuz kirici (WC/Si kaplamali) ve eleme yatirimi | 60000 | 20000 – 200000 | USD | dusuk | tahmin | zaman |  | tahmin |
| wf_etch_station_capex_usd | Geri donusum daglama tezgahi + lokal gaz yikayici yatirimi | 120000 | 40000 – 400000 | USD | dusuk | tahmin | zaman |  | tahmin |
| wf_slab_recovery_frac | Kare kesim artiginin geri kazanilabilir payi (taslama tozu ve kerf haric) | 0.886 | 0.8 – 0.97 | - | orta | hesap_turetilmis | teknik |  | hesap (geometri) |
| wf_kerf_recovery_frac | Kerf tozunun HJT kalitesinde unite icinde geri kazanim payi | 0 | 0 – 0.1 | - | orta | tahmin | teknik |  | tahmin (varsayim); en yakin kanit https://circulareconomy.europa.eu/platform/sites/default/files/remelting_and_purification_of_si-kerf_for_p |
| wf_kerf_value_usd_kg | Kerf camurunun degeri (+ satis, - bertaraf maliyeti) | 0 | -0.5 – 1 | USD/kg Si | dusuk | tahmin | alan |  | tahmin |
| wf_price_m10_usd | Satin alinan n-tipi M10 (182-183.75 mm, 130 um) wafer, FOB Cin | 0.148 | 0.13 – 0.3 | USD/adet | orta | dogrulanmis_url | adet |  | https://www.infolink-group.com/spot-price |
| wf_price_210r_usd | Satin alinan n-tipi 210R (182x210 mm) wafer, FOB Cin | 0.156 | 0.14 – 0.3 | USD/adet | orta | dogrulanmis_url | adet |  | https://www.pv-magazine.com/2026/09/11/china-wafer-prices-fall-as-august-rally-fades-polysilicon-outlook-remains-uncertain/ |
| wf_price_g12_usd | Satin alinan n-tipi G12 (210 mm, 130 um) wafer | 0.17 | 0.15 – 0.33 | USD/adet | orta | hesap_turetilmis | adet |  | https://www.trendforce.com/price/pv/cell |
| wf_price_traceable_m10_usd | Izlenebilir (Cin disi poli/zincir) M10 esdegeri wafer fiyati | 0.35 | 0.25 – 0.6 | USD/adet | dusuk | tahmin | adet |  | tahmin |
| wf_A_m10_m2 | M10 wafer alani (psodo-kare) | 0.03309 | 0.033 – 0.0331 | m2 | yuksek | hesap_turetilmis | teknik |  | hesap (sq_A_ps, a=182.2, D_g=247) |
| wf_import_logistics_usd_per_wafer | Ithalat nakliye + sigorta + ambalaj (wafer basina) | 0.005 | 0.002 – 0.015 | USD/adet | dusuk | tahmin | adet |  | tahmin |
| wf_import_duty_frac | Turkiye ithalat vergisi + ilave vergiler (wafer degerine oran) | 0.05 | 0 – 0.3 | - | dusuk | tahmin | adet |  | tahmin |
| wf_incoming_qc_usd_per_wafer | Satin alinan wafer giris kontrolu (orneklemeli) | 0.002 | 0.0005 – 0.006 | USD/adet | dusuk | tahmin | adet |  | tahmin |
| wf_poly_price_nonchina_usd_kg | Poli-Si fiyati, Cin disi mense | 17.5 | 11 – 27 | USD/kg | orta | dogrulanmis_url | alan |  | https://www.trendforce.com/price/pv/cell ; https://www.infolink-group.com/spot-price |
| wf_poly_price_china_rmb_kg | Poli-Si fiyati, Cin ic piyasa (n-tipi recharge, KDV dahil) | 33.5 | 31 – 45 | RMB/kg | orta | dogrulanmis_url | alan |  | https://www.trendforce.com/price/pv/cell |
| wf_cn_vat | Cin KDV orani (ic fiyatlari KDV haric USD'ye cevirmek icin) | 0.13 | 0.13 – 0.13 | - | orta | hafizadan_dogrulanmadi | teknik |  | wafer alani (hafiza); dolayli teyit https://www.pv-magazine.com/2026/01/09/china-to-abolish-solar-export-tax-rebates-from-april/ |
| wf_fx_cny_per_usd | Kur varsayimi | 6.8 | 6.6 – 7.3 | CNY/USD | orta | hesap_turetilmis | teknik | → `bat_fx_cny_per_usd` | https://www.pv-magazine.com/2026/09/11/china-wafer-prices-fall-as-august-rally-fades-polysilicon-outlook-remains-uncertain/ |
| wf_resistivity_ohm_cm | HJT n-tipi wafer ozdirenci | 1 | 0.3 – 2.1 | ohm.cm | yuksek | dogrulanmis_url | teknik |  | https://taiyangnews.info/technology/wafer-developments-continue-to-support-hjt-adoption |
| wf_lifetime_min_ms | HJT icin minimum wafer tasiyici omru (spesifikasyon) | 1 | 0.3 – 3 | ms | dusuk | hafizadan_dogrulanmadi | teknik |  | hafiza; nitel destek https://taiyangnews.info/technology/low-temperature-hjt-manufacturing-adapts-to-wider-wafer-variants |
| wf_oxygen_cm3 | CZ wafer tipik oksijen konsantrasyonu | 1e+18 | 3e+17 – 1.2e+18 | atom/cm3 | orta | dogrulanmis_url | teknik |  | https://en.wikipedia.org/wiki/Czochralski_method |
| wf_inspect_capex_usd | Wafer muayene/siniflandirma istasyonu yatirimi | 150000 | 50000 – 600000 | USD | dusuk | tahmin | zaman |  | tahmin |
| wf_inspect_wph | Muayene ve ayirma istasyonu kapasitesi | 3600 | 1500 – 8000 | wafer/saat | dusuk | tahmin | teknik |  | tahmin |
| wf_inspect_uptime | Muayene ve ayirma istasyonu kullanilabilirligi | 0.9 | 0.8 – 0.95 | - | dusuk | tahmin | teknik |  | tahmin |
| wf_handling_capex_usd | Tutkal cozme + ayirma + on temizlik hatti yatirimi | 250000 | 80000 – 800000 | USD | dusuk | tahmin | zaman |  | tahmin |
| wf_brick_metrology_capex_usd | Tugla seviyesinde olcum (girdap akimi ozdirenc, PL/omur haritasi, IR inkluzyon) | 80000 | 30000 – 250000 | USD | dusuk | tahmin | zaman |  | tahmin |
| wf_preclean_chem_usd_m2 | On temizlik kimyasal + su maliyeti | 0.2 | 0.05 – 0.6 | USD/m2 | dusuk | tahmin | alan |  | tahmin |
| wf_split_tls_wph | Termal lazer ayirma (TLS) kapasitesi | 6000 | 3000 – 6000 | wafer/saat | dusuk | dogrulanmis_url | teknik |  | https://3d-micromac.com/microcell |
| wf_split_capex_usd | Wafer bolme istasyonu yatirimi (TLS veya lazer cizme + yarma) | 400000 | 60000 – 1e+06 | USD | dusuk | tahmin | zaman |  | tahmin |
| wf_split_edge_loss_rel | Hucre oncesi bolunmus HJT parcasinda kenar kaynakli goreli verim kaybi (91 mm ceyrek) | 0.01 | 0.002 – 0.04 | - | dusuk | tahmin | teknik |  | tahmin |
| wf_poly_ratio_itrpv | Endustri referansi: taze poli / wafer Si kutlesi (M10, 2026, 130 um) - kalibrasyon | 1.42 | 1.33 – 1.58 | - | orta | hesap_turetilmis | teknik |  | https://taiyangnews.info/technology/itrpv-expects-topcon-to-lead-as-bc-and-tandem-technologies-expand |

## Hücre (HJT) (`hucre`) — 118 parametre

| id | ad | değer | aralık | birim | güven | kaynak türü | sınıf | eşdeğer | kaynak |
|---|---|---|---|---|---|---|---|---|---|
| cell_eta_industry_2025_pct | Endustriyel HJT seri uretim hucre verimi (2025) | 25.7 | 25.3 – 26.2 | % | yuksek | dogrulanmis_url | teknik |  | TaiyangNews 'Heterojunction Efficiency Roadmaps Approach 27%' (ITRPV/CPIA) |
| hjt_ref_PA_per_mm | Endustri referans hucresinin cevre/alan orani (kalibrasyon formati) | 0.0286 | 0.019 – 0.033 | 1/mm | orta | hesap_turetilmis | teknik |  | Geometri + TaiyangNews HJT 2023 (islem oncesi yarim wafer yaygin) |
| cell_eta_core_mature_pct | Kenarsiz cekirdek verim, olgun proses, tau_SRH = tau_ref | 26.1 | 25.5 – 26.8 | % | orta | hesap_turetilmis | teknik |  | f_hjt_eta_core_calib ile cell_eta_industry_2025_pct'ten turetildi |
| cell_eta_core_start_pct | Kendi hattimizda ilk 12 ayin kenarsiz cekirdek verimi (satin alinan wafer, K3) | 22.5 | 19 – 24.5 | % | dusuk | tahmin | teknik |  | Tahmin; dayanak Ballif vd. 2019 PVI: ticari araclarla pilot hat 10 ayda %20.5'ten %22.8'e |
| hjt_w_eq_start_mm | Baslangic hattinda esdeger olu kenar genisligi | 0.75 | 0.5 – 1.2 | mm | dusuk | tahmin | teknik |  | Tahmin: olgun B-arka degeri 0.61 mm + genis maske ve kaba kenar islemesi payi |
| hjt_tau_ref_ms | Referans wafer SRH omru (yalniz SRH; intrinsik ve yuzey haric) | 7 | 5 – 10 | ms | orta | dogrulanmis_url | teknik |  | Giglia, Varache, Veirman, Fourmond, SOLMAT 238 (2022) 111605 (HAL) |
| hjt_eta_tau_A_pctabs | Verim-omur duyarlilik katsayisi A | 1.18 | 1.13 – 1.23 | %abs | dusuk | hesap_turetilmis | teknik |  | Kendi toplu hucre modelimiz: Richter intrinsik + enjeksiyondan bagimsiz SRH + J0s + Rs; bu gorevde python ile yeniden fit |
| hjt_eta_tau_c_ms | Verim-omur fit sabiti c | 3.35 | 2.3 – 4.6 | ms | dusuk | hesap_turetilmis | teknik |  | Ayni fit (A ile korele) |
| hjt_tau_srh_target_ms | Kristal ajanina verilen hucre hedefi: izin verilen kayip icin asgari SRH omru | 3.7 | 2.7 – 4.9 | ms | dusuk | hesap_turetilmis | teknik |  | f_hjt_tau_target (A=1.18, c=3.35, tau_ref=7) |
| hjt_wafer_tau_over_rho_min | Ballif asgari esigi tau/rho (gettering/termal donor yok etme gerekmeyen sinir; kayipsiz DEGIL) | 1 | 0.5 – 2 | ms/(Ohm cm) | orta | dogrulanmis_url | teknik |  | Ballif vd. 2019, Photovoltaics International |
| hjt_preanneal_recovery_frac | On-tavlama (gettering) ile metal kaynakli SRH rekombinasyonunun giderilen orani r | 0.5 | 0 – 0.9 | - | dusuk | tahmin | teknik |  | Tahmin. Nitel dayanak: TaiyangNews HJT 2023 (bu gorevde PDF okundu) |
| hjt_preanneal_capex_usd | On-tavlama firini capex'i (kendi yapim bant/tup; induksiyon secenegi) | 250000 | 100000 – 600000 | USD | dusuk | tahmin | zaman |  | Tahmin (firin govdesi + isitici + atmosfer kontrolu + tasima) |
| hjt_preanneal_kWh_per_m2 | On-tavlama marjinal enerjisi | 1.5 | 0.5 – 4 | kWh/m2 | dusuk | tahmin | alan |  | Tahmin (Si + tasiyici isil kutlesinin 700-900 C'ye isitilmasi + kayiplar) |
| hjt_edge_j02_native_nA_cm | Dogal (islenmis, a-Si/TCO sarili) kenar icin cizgisel j02 | 2.41 | 1 – 5 | nA/cm | yuksek | dogrulanmis_url | teknik |  | Wohler, Greulich, Bett, SOLMAT 278 (2024) 113192 (Fraunhofer ISE), acik erisim PDF |
| hjt_edge_j02_tls_nA_cm | TLS (termal lazer ayirma) kesik kenar icin j02 | 7.77 | 5 – 12 | nA/cm | yuksek | dogrulanmis_url | teknik |  | Wohler vd. 2024 |
| hjt_edge_weq_native_mm | Dogal kenarin esdeger olu genisligi (rekombinasyon) | 0.26 | 0.12 – 0.55 | mm | orta | hesap_turetilmis | teknik |  | Iki diyotlu toplu model, Wohler verisine kalibre; fizik denetcisi bagimsiz 0.24-0.25 mm |
| hjt_edge_weq_tls_mm | TLS kesik kenarin esdeger olu genisligi (TCO kenara kadar, bant yok) | 0.8 | 0.5 – 1.3 | mm | orta | hesap_turetilmis | teknik |  | Wohler j02 orani ve model; kaynak denetcisi bagimsiz 0.73-0.76 mm (%22.8 hucre) |
| hjt_edge_weq_scribe_mm | Lazer cizik-kir kesik kenarin esdeger olu genisligi | 3.8 | 2.5 – 6 | mm | orta | hesap_turetilmis | teknik |  | Wohler: scribe half -1.1%, shingle -5.5%; iki denetcinin bagimsiz hesabi 3.6-4.0 mm |
| hjt_edge_weq_repass_mm | Islem sonrasi kesik kenarin 250 C altinda yeniden pasivasyon sonrasi esdeger olu genisligi (D secenegi) | 0.35 | 0.2 – 0.8 | mm | dusuk | tahmin | teknik |  | Tahmin; dayanak Giglia 2022 SIMULASYONU (Dit=3e10 ile yeniden pasivasyon) |
| hjt_tco_excl_mm | TCO kenar dislama (TCO'suz bant) genisligi | 1 | 0.3 – 1.5 | mm | orta | dogrulanmis_url | teknik |  | Giglia vd. 2022 (HAL) |
| hjt_tco_dead_frac_rear | Arka (emitor) yuzde TCO'suz bandin etkin olu alan orani | 0.35 | 0.25 – 0.5 | - | orta | hesap_turetilmis | teknik |  | Giglia 2022 simulasyonu: M6'da 1 mm TCO'suz kenar -0.17 (Dit=0) / -0.22 %abs |
| hjt_tco_dead_frac_front | On (n) yuzde TCO'suz bandin etkin olu alan orani (yalniz optik + yanal akis) | 0.12 | 0.05 – 0.3 | - | dusuk | tahmin | teknik |  | Tahmin: kayip esasen yansima (ARC yok); elektronlar n-bulk uzerinden yanal akar |
| hjt_tco_wrap_weq_mm | On yuz dislamasinda arka p-TCO'nun on n-katmanina sarilmasinin esdeger kenar kaybi (sont/kuyu) | 0.1 | 0 – 0.5 | mm | dusuk | tahmin | teknik |  | Tahmin (fizik muhakemesi; fizik denetcisi bulgusu) |
| hjt_queue_time_max_min | HF-son -> PECVD izin verilen bekleme suresi (kayipsiz) | 30 | 20 – 60 | dk | orta | dogrulanmis_url | teknik |  | Danel vd. 2012, Solid State Phenomena 187:345 |
| hjt_queue_penalty_rel_per_min | Bekleme siniri asildiginda bagil verim kaybi | 0.0008 | 0.0003 – 0.002 | 1/dk | dusuk | hesap_turetilmis | teknik |  | Danel 2012'den: 90 dk'da %5 bagil, 30 dk'da 0 -> 0.05/60 |
| hjt_ag_mg_per_W_itrpv_2025 | SHJ endustri ortalamasi Ag tuketimi (2025, ITRPV) - capraz referans | 12 | 10 – 14 | mg/W | orta | dogrulanmis_url | alan |  | TaiyangNews 'ITRPV Sees PV Shipments Stabilize At 706 GW In 2025' |
| hjt_paste_laydown_start_g_per_m2 | Dusuk sicaklik Ag pastasi yas kutle yogunlugu - baslangic (kendi yazicimiz, ilk yil) | 5.5 | 4.5 – 7.5 | g/m2 | dusuk | hesap_turetilmis | alan |  | TaiyangNews HJT 2023 (bu gorevde PDF okundu): laydown 18-23 mg/W; M6 basina 180 -> 120 mg |
| hjt_paste_laydown_mature_g_per_m2 | Dusuk sicaklik Ag pastasi yas kutle yogunlugu - olgun (SMBB/0BB, cift baski) | 4.3 | 3.5 – 5 | g/m2 | orta | hesap_turetilmis | alan |  | TaiyangNews HJT 2023 (bu gorevde PDF okundu): Huasun M6 basina 126 mg pasta |
| hjt_paste_ag_frac | Dusuk sicaklik pastasinda Ag kutle orani | 0.88 | 0.8 – 0.93 | - | dusuk | hafizadan_dogrulanmadi | alan |  | Hafizadan (dusuk-T pastalar ~%85-92 Ag) |
| hjt_ag_g_per_m2_agcu | Ag kapli Cu (AgCu) pasta + 0BB ile saf Ag yuzey yogunlugu | 1.5 | 1 – 2.6 | g/m2 | orta | hesap_turetilmis | alan |  | TaiyangNews 'Silver-Coated Copper Drives HJT Metallization Roadmap' (2026-06-10); Fraunhofer ISE (pv magazine 2025) 1.4 mg/W |
| hjt_ag_price_usd_per_g | Gumus fiyati | 2.066 | 1.6 – 2.8 | USD/g | yuksek | dogrulanmis_url | alan |  | https://tradingeconomics.com/commodity/silver |
| hjt_ag_paste_premium_usd_per_g | Pasta imalat primi (Ag icerigi basina) | 0.3 | 0.1 – 0.7 | USD/g Ag | dusuk | tahmin | alan |  | Tahmin (pasta ureticisi marji; dogrulanmis kaynak yok) |
| hjt_ito_thickness_total_nm | Toplam TCO kalinligi (on+arka) | 180 | 140 – 220 | nm | orta | hafizadan_dogrulanmadi | alan |  | TaiyangNews 'Reducing Indium In HJT TCO Processing' (VON ARDENNE 100 nm her iki yuz); Louwen 2016 |
| hjt_ito_density_g_cm3 | ITO yogunlugu | 7.1 | 6.8 – 7.2 | g/cm3 | orta | fizik_ders_kitabi | teknik |  | Malzeme ozelligi (hafizadan) |
| hjt_ito_target_util | ITO hedef kullanim orani (asinan / satin alinan) | 0.85 | 0.25 – 0.9 | - | orta | dogrulanmis_url | alan |  | TaiyangNews 'TCO Deposition' (doner hedef %90); duzlemsel icin hafizadan 0.25-0.4 |
| hjt_ito_transfer_frac | Asinan ITO'nun tasiyici alanina ulasan payi | 0.53 | 0.35 – 0.7 | - | dusuk | hesap_turetilmis | alan |  | PV-Tech Maxwell (2023-07-24) 12-13.5 mg/W'den geri hesap |
| hjt_in_mass_frac_target | ITO hedefte indiyum kutle orani | 0.75 | 0.74 – 0.8 | - | yuksek | hesap_turetilmis | alan |  | Stokiyometri: In2O3 0.827; ITO 90:10 -> 0.744; 97:3 -> 0.80 |
| hjt_in_price_usd_per_kg | Indiyum fiyati | 800 | 350 – 1100 | USD/kg | orta | dogrulanmis_url | alan |  | https://tradingeconomics.com/commodity/indium ; Procurement Resource ; USGS MCS 2025 (hucre) |
| hjt_ito_target_fab_adder_usd_per_kg | ITO hedef imalat ucreti (In degeri disinda) | 450 | 300 – 700 | USD/kg hedef | orta | hesap_turetilmis | alan |  | Ballif vd. 2019 PVI |
| hjt_ito_spent_in_recovery_frac | Kullanilmis hedefte kalan In degerinin geri satista kredilenen orani | 0.7 | 0.4 – 0.9 | - | dusuk | tahmin | alan |  | Tahmin (geri donusumcu marji) |
| hjt_sih4_g_per_m2 | Silan tuketimi | 2 | 0.8 – 5 | g/m2 | orta | hesap_turetilmis | alan |  | Louwen vd. 2016 SOLMAT 147 Tablo A4 (Ref-SHJ 0.039 g/wafer, 239 cm2) |
| hjt_h2_g_per_m2 | Hidrojen tuketimi (PECVD) | 10 | 2.5 – 40 | g/m2 | dusuk | tahmin | alan |  | Louwen 2016 Ref-SHJ 0.059 g/wafer (2.5 g/m2, a-Si); nc-Si icin H2 seyreltme 50-200x -> tahmin |
| hjt_ph3_mg_per_m2 | Fosfin tuketimi (saf esdeger) | 10 | 2 – 50 | mg/m2 | dusuk | tahmin | alan |  | Tahmin: katkili katmanda PH3/SiH4 ~%0.5-2; katkili katman silanin ~yarisi |
| hjt_bdopant_mg_per_m2 | Bor kaynagi (TMB veya B2H6) tuketimi | 10 | 2 – 50 | mg/m2 | dusuk | tahmin | alan |  | Tahmin (PH3 ile ayni gerekce) |
| hjt_nf3_g_per_m2 | NF3 (in-situ oda temizligi) tuketimi | 3 | 0 – 10 | g/m2 | dusuk | tahmin | alan |  | Tahmin: 4NF3+3Si -> 3SiF4+2N2 (3.4 g NF3/g Si), %30-60 verim, odada biriken Si 0.3-1 g/m2 |
| hjt_sih4_price_usd_per_kg | Silan fiyati (tup olcegi, teslim) | 80 | 30 – 300 | USD/kg | dusuk | tahmin | alan | → `eco_price_sih4_usd_kg` | Tahmin |
| hjt_h2_price_usd_per_kg | Hidrojen fiyati (tup/demet) | 10 | 4 – 25 | USD/kg | dusuk | tahmin | alan | → `eco_price_h2_usd_kg` | Tahmin (tup olcegi H2; elektrolizor secenegi altyapi ajaninda) |
| hjt_dopant_gas_usd_per_m2 | Katki gazlari (PH3, TMB/B2H6 karisimlari) maliyeti | 0.03 | 0.01 – 0.1 | USD/m2 | dusuk | tahmin | alan |  | Tahmin: 10 mg/m2 saf esdeger; %1 karisim tupu fiyati belirleyici |
| hjt_n2_Nm3_per_h | Hucre hatti N2 tuketimi (pompa purge, kurutma, N2 tampon) | 15 | 5 – 40 | Nm3/h | dusuk | tahmin | zaman |  | Tahmin: 6-8 kuru pompa x 30-50 slm purge = 11-24 Nm3/h + kurutma |
| hjt_si_etch_removal_um | SDE + dokulama toplam Si asindirma (iki yuz) | 12 | 8 – 25 | um | dusuk | tahmin | teknik |  | Hucre tahmini (piramit 2-5 um + hasar giderme); wafer hafizadan 15 um; alt capa Ge 2025 |
| hjt_koh_excess | KOH stokiyometri fazlasi (banyo yenileme/bosaltma) | 1.3 | 1 – 2 | - | dusuk | tahmin | alan |  | Tahmin |
| hjt_hf_g_per_m2 | HF tuketimi (temizlik + HF-son) | 20 | 8 – 40 | g/m2 | dusuk | hesap_turetilmis | alan |  | Louwen 2016 Tablo A2 (0.918 g/wafer -> 38 g/m2, RCA donemi); ozonla azalma |
| hjt_upw_L_per_m2 | Ultra saf su tuketimi | 30 | 15 – 60 | L/m2 | orta | hesap_turetilmis | alan |  | Louwen 2016 Tablo A2 (0.745 kg/wafer, 239 cm2) |
| hjt_koh_price_usd_per_kg | KOH fiyati (%100 KOH bazinda, yari iletken sinifi) | 1.5 | 0.8 – 3 | USD/kg | dusuk | tahmin | alan |  | Tahmin (endustriyel pul ~1 $/kg mertebesi, hafizadan; saflik primi) |
| hjt_hf_price_usd_per_kg | HF fiyati (%100 HF bazinda, %49 elektronik sinif) | 4 | 2 – 8 | USD/kg | dusuk | tahmin | alan |  | Tahmin |
| hjt_misc_chem_usd_per_m2 | Diger islak kimya (dokulama katkisi, HCl, H2O2/O3, tasiyici temizlik kimyasi) | 0.15 | 0.05 – 0.4 | USD/m2 | dusuk | tahmin | alan |  | Tahmin |
| hjt_wet_consumables_usd_per_W_ref | Islak kimya sarf maliyeti referansi (capraz kontrol) | 0.0055 | 0.002 – 0.006 | USD/W | orta | dogrulanmis_url | alan |  | Ballif vd. 2019 PVI (Singulus) |
| hjt_elec_marginal_kWh_per_m2 | Proses marjinal elektrigi (uretimle artan kisim) | 2.5 | 1 – 4 | kWh/m2 | dusuk | tahmin | alan |  | Tahmin: RF 0.03-0.1, PVD puskurtme 0.3-1, islak isitma/yenileme 0.5-2, kurleme 0.2-0.5 kWh/m2 |
| hjt_base_load_kW | Hucre hatti calisirken uretimden bagimsiz taban yuk | 120 | 60 – 250 | kW | dusuk | tahmin | zaman |  | Tahmin: PECVD 4 oda + kilitler kuru/roots pompalar ~40 kW, isiticilar 15 kW, RF bekleme; PVD turbo+on pompa+isitici ~20 kW; islak banyo isit |
| hjt_idle_base_load_kW | Hat bekleme (vakum ve sicaklik korunur) yuku | 40 | 15 – 80 | kW | dusuk | tahmin | zaman |  | Tahmin (pompalar dusuk devir, isiticilar bekleme) |
| hjt_carrier_side_mm | PECVD/PVD tasiyici kenar boyu L | 1000 | 500 – 1720 | mm | orta | tahmin | teknik |  | Tasarim; endustri tepsileri 10x10 M6 / 8x8 210 mm cep (~1.7 m) (TaiyangNews PECVD) |
| hjt_carrier_gap_mm | Cepler arasi agi + tutma cikintisi g | 4 | 2 – 8 | mm | dusuk | tahmin | teknik |  | Tahmin: kenar basina 1-2 mm tutma/maske cikintisi + cep duvari |
| hjt_carrier_margin_mm | Tasiyici cevre payi | 10 | 5 – 30 | mm | dusuk | tahmin | teknik |  | Tahmin: tasima rayi/sikistirma cercevesi |
| hjt_pecvd_n_process_ch | PECVD proses odasi sayisi (i-on, n, i-arka, p) | 4 | 2 – 4 | adet | dusuk | tahmin | teknik |  | Tasarim secimi; katki capraz kirlenmesine karsi ayri odalar |
| hjt_pecvd_takt_s | PECVD takt suresi: tam iki yuzlu 4 katmanli yiginin tasiyici cikis araligi | 120 | 60 – 300 | s | dusuk | tahmin | zaman |  | Tahmin: en yavas oda = nc-Si katkili 10-20 nm @0.1-0.2 nm/s (50-200 s) + transfer/pompa/gaz stabilizasyonu 30-60 s |
| hjt_pvd_takt_s | PVD (TCO, iki yuz) tasiyici takt suresi | 90 | 45 – 200 | s | dusuk | tahmin | zaman |  | Tahmin; endustri PVD 7,200-12,800 wafer/h (TaiyangNews TCO) |
| hjt_wet_bath_W_mm | Islak tezgah banyo ic genisligi (kaset kesiti) | 500 | 300 – 700 | mm | dusuk | tahmin | teknik |  | Tasarim/tahmin |
| hjt_wet_bath_H_mm | Islak tezgah kullanilabilir derinlik (wafer sirasi) | 250 | 220 – 400 | mm | dusuk | tahmin | teknik |  | Tasarim/tahmin |
| hjt_wet_slots | Kaset yuva sayisi (derinlik yonunde) | 100 | 50 – 100 | adet | dusuk | tahmin | teknik |  | Tahmin (standart kaset yuva sayisi) |
| hjt_wet_lane_gap_mm | Kasette seritler arasi bosluk | 10 | 5 – 20 | mm | dusuk | tahmin | teknik |  | Tahmin (sivi akisi, kabarcik tahliyesi) |
| hjt_wet_takt_s | Islak tezgah parti takt suresi | 600 | 300 – 1200 | s | dusuk | tahmin | zaman |  | Tahmin: KOH+katki dokulama ~15 dk, 2 paralel dokulama tanki |
| hjt_print_pallet_side_mm | Serigrafi paleti kenar boyu | 330 | 160 – 400 | mm | dusuk | tahmin | teknik |  | Tasarim/tahmin |
| hjt_print_cycle_s | Palet basina baski cevrimi (bir yuz) | 4 | 2 – 8 | s | dusuk | tahmin | zaman |  | Tahmin (baski hizi 200-250 mm/s, TaiyangNews 2023 + yukleme) |
| hjt_cure_temp_C | Pasta kurleme sicakligi | 200 | 180 – 250 | C | orta | dogrulanmis_url | teknik |  | PV-Manufacturing.org SHJ |
| hjt_iv_test_s_per_cell | IV test islem suresi (bir flas) | 0.75 | 0.3 – 3 | s | orta | hesap_turetilmis | adet |  | TaiyangNews HJT 2023 (WAVELABS) |
| hjt_cells_per_op | Tek islemde (tutucu/flas) islenen hucre sayisi | 1 | 1 – 16 | adet | dusuk | tahmin | adet |  | Tasarim secimi |
| hjt_handling_ops_per_wafer | Wafer basina tasima (al-birak) islemi | 6 | 4 – 10 | adet | dusuk | tahmin | adet |  | Tahmin: kaset yukle/bosalt, tasiyici yukle/bosalt, yazici, IV/siniflama |
| hjt_handling_s_per_pick | Robot al-birak cevrim suresi | 1 | 0.5 – 2 | s | dusuk | tahmin | adet |  | Tahmin (SCARA/delta robot) |
| hjt_adet_var_usd_per_op | Islem basina capex disi degisken maliyet (enerji, vakum, pin/tutucu asinmasi) | 0.0001 | 3e-05 – 0.0005 | USD/islem | dusuk | tahmin | adet |  | Tahmin: robot 0.5 kW x 1 s ~0.00002 $; IV pini ~5 $/pin, ~1e6 temas, ~20 pin -> 0.0001 $ |
| hjt_line_uptime | Hat kullanilabilirligi | 0.85 | 0.7 – 0.92 | - | dusuk | tahmin | zaman |  | TaiyangNews HJT 2023: endustri hedefi >%90; bizim icin tahmin |
| hjt_line_yield_mature | Olgun HJT hat verimi (kirilma haric) | 0.985 | 0.97 – 0.995 | - | orta | dogrulanmis_url | teknik |  | Risen (TradingView/EQS 2026-03-11); TaiyangNews 2023 hedef >=98.5% |
| hjt_line_yield_start | Baslangic hat verimi | 0.9 | 0.75 – 0.96 | - | dusuk | tahmin | teknik |  | Hucre tahmini; Ballif 2019 (ilk hatlarda tasima/bekleme sorunlari); olgun 0.985 (Risen) |
| hjt_breakage_ref | Hucre hatti kirilma orani (referans 210-yarim, 110 um) | 0.0025 | 0.001 – 0.01 | - | orta | dogrulanmis_url | teknik |  | Risen 2026 (fragment <0.25%); Maxwell PECVD spec 0.25% |
| hjt_breakage_size_exp | Kirilmanin wafer boyutu ussu (H3) | 1 | 0.5 – 2 | - | dusuk | tahmin | teknik |  | Tahmin, mekanizma dayanakli |
| hjt_capex_industry_usd_per_Wyr | Endustriyel HJT hucre hatti ekipman capex (yillik kapasite basina) - referans | 0.055 | 0.037 – 0.065 | USD/(W/yil) | orta | dogrulanmis_url | zaman |  | TaiyangNews HJT 2023 (350-400 M RMB/GW, hedef 250) |
| hjt_capex_pecvd_base_usd | PECVD sabit capex (yukleme/bosaltma kilitleri, tasima, kontrol, gaz paneli arayuzu) | 300000 | 150000 – 600000 | USD | dusuk | tahmin | zaman |  | Tahmin (parca BOM mantigi) |
| hjt_capex_pecvd_ch_fix_usd | PECVD oda basina sabit capex (RF jenerator+esleme, pompa, MFC seti, vana, isitici) | 120000 | 70000 – 250000 | USD/oda | dusuk | tahmin | zaman |  | Tahmin |
| hjt_capex_pecvd_ch_per_m2_usd | PECVD oda basina tasiyici alani ile olceklenen capex (govde, elektrot/dus basligi, isitici boyu) | 100000 | 50000 – 250000 | USD/(oda m2) | dusuk | tahmin | zaman |  | Tahmin |
| hjt_capex_pvd_base_usd | PVD sabit capex (kilitler, turbo pompalar, tasima, kontrol) | 350000 | 200000 – 700000 | USD | dusuk | tahmin | zaman |  | Tahmin |
| hjt_capex_pvd_per_m_usd | PVD katod genisligi ile olceklenen capex (4 katod + DC guc kaynaklari, oda boyu) | 300000 | 150000 – 600000 | USD/m | dusuk | tahmin | zaman |  | Tahmin |
| hjt_capex_wet_usd | Islak tezgah capex (8-12 tank, isitici, ozon, durulama, kurutma, egzoz baglantisi) | 350000 | 200000 – 700000 | USD | dusuk | tahmin | zaman |  | Tahmin |
| hjt_capex_print_cure_usd | Baski + kurleme + isik iyilestirme capex (2 yazici, bant firin, LED isik bandi) | 350000 | 200000 – 600000 | USD | dusuk | tahmin | zaman |  | Tahmin |
| hjt_capex_iv_station_usd | IV test/siniflama istasyonu capex (LED simulator + coklu kontak) | 120000 | 60000 – 250000 | USD/istasyon | dusuk | tahmin | adet |  | Tahmin |
| hjt_capex_handling_cell_usd | Tasima robot hucresi capex (robot + tutucu + kontrol) | 80000 | 40000 – 150000 | USD/hucre | dusuk | tahmin | adet |  | Tahmin |
| hjt_capex_metrology_usd | Metroloji capex (QSSPC, PL goruntuleme, elipsometre, 4 nokta sonda, mikroskop) | 350000 | 200000 – 700000 | USD | dusuk | tahmin | zaman |  | Tahmin (QSSPC ~50-100 k$, PL 100-300 k$, elipsometre 50-150 k$) |
| hjt_capex_selfbuilt_line_usd | Kendi yapim HJT hucre hatti toplam capex (L=1 m, 4 oda, a=105, 16'li tutucu; on-tavlama haric) | 3.08e+06 | 2e+06 – 6.5e+06 | USD | dusuk | hesap_turetilmis | zaman |  | f_hjt_capex bilesenlerinin toplami |
| hjt_pecvd_capex_share | Endustri hucre hatti capex'inde 'core layer deposition' payi | 0.4 | 0.3 – 0.5 | - | orta | dogrulanmis_url | teknik |  | TaiyangNews HJT 2023 |
| hjt_maint_frac_capex_per_yr | Bakim + yedek parca (kuru pompa revizyonu, RF, conta, tank) - capex orani/yil | 0.05 | 0.03 – 0.08 | 1/yil | dusuk | tahmin | zaman | → `eco_maint_frac_capex_yr` | Tahmin |
| hjt_carrier_cost_usd | PECVD/PVD tasiyici birim maliyeti (1 m2) | 3000 | 1000 – 8000 | USD | dusuk | tahmin | alan |  | Tahmin (grafit/CFC/Al levha + cep isleme) |
| hjt_carrier_life_cycles | Tasiyici omru (temizlik dahil cevrim) | 5000 | 1000 – 20000 | cevrim | dusuk | tahmin | alan |  | Tahmin (bilinmiyor) |
| hjt_tool_nre_usd | Kendi yapim hucre araclarinin tasarim/devreye alma NRE'si (muhendislik + prototip iterasyonu) | 2.5e+06 | 1.2e+06 – 5e+06 | USD | dusuk | tahmin | urun_sabit |  | Tahmin: 15-40 muhendis-yili x 40-80 k$ + 0.5-1 M$ prototip donanimi |
| hjt_tooling_per_size_usd | Hucre boyutuna (a) ozgu takim seti (tasiyici cepleri, palet/elekler, IV tutuculari, kasetler, robot tutuculari) | 150000 | 60000 – 400000 | USD/boyut | dusuk | tahmin | urun_sabit |  | Tahmin (10-20 tasiyici x 3-8 k$ + elek/palet 10-20 k$ + IV 10-30 k$ + kaset 10-20 k$) |
| hjt_requal_cost_usd | Yeni hucre boyutu icin proses yeniden kalifikasyonu (kenar, paketleme, TCO dislama, IV) | 80000 | 30000 – 200000 | USD/boyut | dusuk | tahmin | urun_sabit |  | Tahmin (2-3 ay muhendislik + test waferlari) |
| hjt_fte_per_shift | Vardiya basina operator | 3 | 2 – 5 | FTE | dusuk | tahmin | zaman |  | Tahmin (islak+PECVD/PVD+baski/IV) |
| hjt_shift_crews | 7/24 icin ekip sayisi | 4.2 | 3.7 – 4.6 | - | dusuk | tahmin | zaman | → `eco_fte_per_24x7_position` | Tahmin: 168 h / 45 h haftalik + izin payi |
| hjt_fte_support | Gunduz destek kadrosu (proses muhendisi, bakim, kalite) | 4 | 2 – 6 | FTE | dusuk | tahmin | zaman |  | Tahmin |
| hjt_labor_cost_usd_per_fte_yr | Harmanlanmis yuklu iscilik maliyeti (Gebze, operator+muhendis) | 20000 | 13000 – 35000 | USD/(FTE yil) | dusuk | tahmin | zaman |  | TradingEconomics Turkiye asgari ucret ve USD/TRY (bu gorevde acildi) x carpanlar (tahmin) |
| hjt_campaign_startup_h | Kampanya baslangici isinma/pompalama/kosullama suresi | 8 | 4 – 24 | h | dusuk | tahmin | zaman |  | Tahmin |
| hjt_seasoning_m2_per_start | Baslangicta PECVD oda kosullama icin kukla tasiyici alani | 3 | 1 – 10 | m2/baslangic | dusuk | tahmin | zaman |  | Tahmin |
| cell_fx_usd_cny | Kur varsayimi USD/CNY | 6.72 | 6.5 – 7.3 | CNY/USD | yuksek | dogrulanmis_url | teknik | → `bat_fx_cny_per_usd` | TradingEconomics China currency |
| cell_fx_usd_try | Kur varsayimi USD/TRY | 48.92 | 45 – 60 | TRY/USD | yuksek | dogrulanmis_url | teknik | → `eco_fx_try_per_usd` | TradingEconomics Turkey currency (bu gorevde acildi) |
| hjt_voc_cell_V | Hucre acik devre gerilimi (25 C) | 0.745 | 0.72 – 0.77 | V | orta | dogrulanmis_url | teknik |  | Hucre: Wohler 2024 endustriyel M6 olcumu 739-740 mV; LONGi sampiyon 749-755 mV. Modul: Waaree Plexus BiH-11-730 veri sayfasi 50.62 V / 66 se |
| hjt_jsc_mA_cm2 | Hucre kisa devre akim yogunlugu | 40 | 38 – 41.4 | mA/cm2 | orta | dogrulanmis_url | teknik |  | Hucre: Wohler 2024 endustriyel M6 olcumu 38.02-38.05; LONGi sampiyon 41.4 |
| hjt_tc_pmax_pct_per_K | Pmax sicaklik katsayisi | -0.26 | -0.3 – -0.24 | %/K | orta | dogrulanmis_url | teknik |  | TaiyangNews HJT 2023 (bu gorevde PDF okundu) |
| hjt_tc_voc_pct_per_K | Voc sicaklik katsayisi (SELV soguk Voc hesabi) | -0.244 | -0.28 – -0.2 | %/K | orta | hesap_turetilmis | teknik |  | Hucre: PVEducation 'Effect of Temperature' formulu; Modul: Waaree veri sayfasi beta_Voc -0.22 %/C ve fizik tahmini -0.22..-0.24 |
| hjt_voc_irr_margin_mV | Soguk Voc icin isinim (>1000 W/m2, bulut kenari) ve cift yuzlu kazanc payi, hucre basina | 6 | 3 – 10 | mV | dusuk | hesap_turetilmis | teknik |  | Hesap: n*Vt*ln(1.2) (-20 C, n=1) = 4 mV + arka yuz kazanci ~2 mV |
| hjt_bifaciality | Cift yuzluluk orani | 0.85 | 0.8 – 0.95 | - | orta | dogrulanmis_url | teknik |  | TaiyangNews HJT 2023 |
| hjt_sputter_damage_dVoc_mV | Kendi PVD'mizde ITO puskurtme iyon hasari kaynakli Voc kaybi (kurleme sonrasi kalan) | 5 | 0 – 20 | mV | dusuk | tahmin | teknik |  | Tahmin (hafizadan: puskurtme hasari a-Si:H pasivasyonunu bozar, tavlamayla kismen geri gelir) |

## Modül (`modul`) — 99 parametre

| id | ad | değer | aralık | birim | güven | kaynak türü | sınıf | eşdeğer | kaynak |
|---|---|---|---|---|---|---|---|---|---|
| mod_voc_cell_stc_V | HJT hücre Voc (STC, modül içinde, hücre başı) | 0.745 | 0.72 – 0.77 | V | orta | hesap_turetilmis | teknik | → `hjt_voc_cell_V` | Waaree Plexus HJT BiH-11-730 veri sayfası: Voc 50.62 V / 66 seri pozisyon (132 yarım G12, 11x6\|\|11x6) = 0.767 V. Yeni hat için nominal 0.745 |
| mod_beta_voc_per_K | Voc bağıl sıcaklık katsayısı | -0.0024 | -0.0028 – -0.002 | 1/K | orta | hesap_turetilmis | teknik | → `hjt_tc_voc_pct_per_K` × 0.01 | Veri sayfası β = -0.22 %/°C. Fizik tahmini: β = -(Eg0/q − Voc + γkT/q)/(T·Voc), Eg0 = 1.206 V, γ = 1-3 → Voc 0.745 V için -0.22 ile -0.24; 0 |
| mod_vmp_cell_stc_V | HJT hücre Vmp (STC) | 0.64 | 0.62 – 0.66 | V | orta | hesap_turetilmis | teknik |  | Waaree BiH-11-730 veri sayfasi: Vmp 42.52 V / 66 = 0.644 V; beta_Vmp = gamma_Pmax (-0.24) - alfa_Isc (0.04) |
| mod_beta_vmp_per_K | Vmp sıcaklık katsayısı | -0.0028 | -0.0033 – -0.0024 | 1/K | orta | hesap_turetilmis | teknik |  | Waaree: γ_Pmax -0.24, α_Isc +0.04 %/°C; β_Vmp ≈ γ − α_Imp ≈ -0.28 %/K |
| mod_jsc_A_per_cm2 | Modül içi hücre Jsc (STC, ön yüz) | 0.0413 | 0.038 – 0.042 | A/cm2 | orta | hesap_turetilmis | teknik |  | Waaree BiH-11-730 veri sayfasi Isc 18.22 A / 441 cm2 (G12) |
| mod_T_min_design_C | En düşük tasarım sıcaklığı (UOC MAX için sahanın en düşük ortam sıcaklığı) | -20 | -40 – -9 | C | orta | hesap_turetilmis | teknik | → `std_tmin_site_c` | MGM (bu revizyonda açıldı): İstanbul Şubat -9.0 (1950-2025), Ankara Ocak -24.9 (1927-2025), Erzurum Aralık -37.2 °C (1929-2025). Almanya: Hü |
| mod_voc_margin | Voc tasarım marjı (ölçüm belirsizliği, 1000 W/m² üstü ışınım, binleme) | 1.03 | 1 – 1.08 | - | dusuk | tahmin | teknik |  | Modul tahmini; Waaree veri sayfasi +-%3 guc olcum belirsizligi; 1.2 kW/m2'de Voc ~+%0.6 |
| mod_T_cell_max_C | MPPT penceresi için en yüksek hücre sıcaklığı | 85 | 75 – 90 | C | orta | dogrulanmis_url | teknik |  | Waaree veri sayfası çalışma aralığı -40..85 °C. MGM en yüksek ortam sıcaklıkları: İstanbul 40.6 °C (Temmuz), Ankara 41.0 °C (Temmuz). |
| mod_T_p98_class_C | Modül çalışma sıcaklığı sınıf eşiği (P98) | 70 | 70 – 70 | C | yuksek | standart_metni_dogrulanmis | teknik |  | IEC 61730-1:2023 ED3 kapsamı (iTeh örnek sayfaları, bu revizyonda açıldı) |
| mod_ctm_optical | CTM'nin optik ve diğer kısmı (ara bağlantı kaybı hariç) | 1.01 | 0.99 – 1.03 | - | dusuk | tahmin | teknik |  | Tahmin. Dayanak: sektörde CTM ~%98-100 (hafızadan) ve bu değer 182/210 yarım hücrede ~%2-4 ara bağlantı kaybını içerir; bu kayıp ayrı modell |
| mod_classIII_voc_max_V | Class III modül: STC'de en yüksek Voc | 35 | 35 – 35 | V | orta | standart_metni_dogrulanmis | teknik | → `std_class3_voc_stc_max_v` | IEC 61730-1:2016 madde 4.4.1 (SIS önizlemesi, bu revizyonda açıldı). 2023 baskısında Class III madde 5.4'e taşınmış; değişiklik listesinde y |
| mod_classIII_isc_max_A | Class III modül: STC'de en yüksek Isc | 8 | 8 – 8 | A | orta | standart_metni_dogrulanmis | teknik | → `std_class3_isc_max_a` | IEC 61730-1:2016 madde 4.4.1. 2023 değişiklik listesi h(2): bifacial modüllerin yüksek akımı için testler değiştirildi. |
| mod_classIII_p_max_W | Class III modül: en yüksek güç | 240 | 240 – 240 | W | orta | standart_metni_dogrulanmis | teknik |  | IEC 61730-1:2016 madde 4.4.1 |
| mod_isc_margin | Class III için Isc üretim/ölçüm marjı | 1.03 | 1 – 1.05 | - | dusuk | tahmin | teknik |  | Tahmin. Dayanak: Voc'ye konan %3 marjın simetriği; flaş ölçüm belirsizliği ve hücre binleme toleransı. |
| mod_bifacial_isc_factor | Arka yüz ışınımından Isc artış çarpanı | 1 | 1 – 1.26 | - | dusuk | hesap_turetilmis | teknik |  | Türetildi: opak veya beyaz arka yüzde 1.0; şeffaf arka camda BSI koşulu (1000 + 300 W/m², hafızadan) ve bifasiyalite 0.85 ile 1 + 0.85·0.3 = |
| mod_isc_max_factor | ISC MAX / ISC STC (kablo, konnektör, baypas boyutlandırma) | 1.25 | 1.25 – 1.25 | - | orta | standart_metni_dogrulanmis | teknik |  | IEC 60364-7-712:2017 Ek B.2. Tam metin bu oturumun paylaşılan önbelleğinde okundu; özgün URL kayıtlı değil. |
| mod_cells_per_bypass_max | Baypas elemanı başına en fazla seri hücre | 24 | 14 – 28 | adet | dusuk | tahmin | teknik |  | Tahmin. Dayanak: Waaree 132 yarım hücre / 3 diyot = 22 seri pozisyon (doğrulandı). Gölgeli hücreye binen ters gerilim ≈ (n−1)·Vmp; n = 24'te |
| mod_bypass_vf_V | Schottky baypas diyotu ileri gerilimi (Isc'de) | 0.45 | 0.35 – 0.55 | V | dusuk | tahmin | teknik |  | Tahmin: 15-20 A Schottky diyotta tipik Vf (hafızadan) |
| mod_gap_cell_mm | Dizi içi hücre aralığı | 2 | 0.5 – 3 | mm | dusuk | tahmin | teknik |  | Tahmin. Dayanak: tel ara bağlantıda telin iki hücre arasında bükülme payı 1.5-2.5 mm (hafızadan). |
| mod_gap_string_mm | Diziler arası aralık | 3 | 2 – 5 | mm | dusuk | tahmin | teknik |  | Tahmin. Dayanak: laminasyonda dizi kayması ±1 mm + yerleştirme toleransı ±0.5 mm + kısa devre güvenlik payı. |
| mod_edge_side_mm | Yan kenar boşluğu (hücreden cam kenarına) | 12 | 6 – 18 | mm | dusuk | tahmin | teknik |  | Tahmin. Class III'te yalnız fonksiyonel yalıtım gerekir (IEC 61730-1:2016 4.4.2). 2023 baskısında ≤ 35 V çalışma gerilimli Class II modüller |
| mod_edge_end_mm | Uç bölge (bara + kenar), her uçta | 20 | 12 – 35 | mm | dusuk | tahmin | teknik |  | Tahmin. Dayanak: U-bara şeridi 5-8 mm + bara-hücre boşluğu 3-5 mm + kenar contası 10-12 mm. |
| mod_aspect_target | Hedef panel en-boy oranı (W/L) | 1.4 | 1.2 – 1.8 | - | dusuk | tahmin | teknik |  | Tahmin. Dayanak: ~1 m korkuluğa yatay montaj ve ambalaj/taşıma oranı. |
| mod_a_cell_min_mm | Üretilebilir en küçük hücre kenarı | 60 | 40 – 100 | mm | dusuk | tahmin | teknik |  | Tahmin. Dayanak: hücre başı işlem maliyeti, aralık kaybı ve kenar rekombinasyonu (~4/a ile artar). |
| mod_a_cell_max_mm | En büyük hücre kenarı (tam hücre, N_p = 1) | 210 | 182 – 230 | mm | orta | hafizadan_dogrulanmadi | teknik |  | G12 = 210 mm endüstri formatı (hafızadan; Waaree 'G12' diyor) |
| mod_glass_density_kg_m2_per_mm | Cam birim alan kütlesi (mm kalınlık başına) | 2.5 | 2.45 – 2.55 | kg/m2/mm | yuksek | fizik_ders_kitabi | teknik |  | Soda-kireç camı ~2500 kg/m³. Çapraz kontrol: Waaree 2+2 çerçeveli modül 39 kg / (2.384 × 1.303) = 12.6 kg/m². |
| mod_glass_t_min_mm | PV camı için en düşük kalınlık (yarı temperli) | 2 | 1.6 – 3.2 | mm | orta | dogrulanmis_url | teknik |  | Waaree HJT: ön ve arka cam 2 mm yarı temperli. 1.6 mm PV camının varlığı hafızadan. |
| mod_glass_ft_min_mm | Havayla tam temperlenebilen en ince cam | 2.5 | 2 – 3.2 | mm | dusuk | hafizadan_dogrulanmadi | teknik |  | Hafızadan: ~2.5-3 mm altında tam temperleme (FT) zordur; ince PV camı yarı temperli (HS) üretilir (Waaree 2 mm 'semi-tempered' ile tutarlı). |
| mod_glass_ct_GG_mm_per_m | Cam-cam (HS) toplam kalınlık / kısa kenar kalibrasyonu (5400 Pa, çerçeveli, 4 kenar mesnet) | 2.8 | 2.2 – 3.1 | mm/m | dusuk | hesap_turetilmis | teknik |  | Türetildi: Waaree 2+2 HS çerçeveli cam-cam, b = 1.303 m, 5400 Pa sertifikalı → c ≤ 4/1.303 = 3.07 mm/m. Sektör tasarım marjı için nominal 2. |
| mod_glass_ct_GB_mm_per_m | Cam-arka tabaka (tek FT cam) kalınlık / kısa kenar kalibrasyonu (5400 Pa, çerçeveli) | 2.82 | 2 – 3.4 | mm/m | dusuk | hesap_turetilmis | teknik |  | Türetildi: 3.2 mm FT cam / 1.134 m (5400 Pa sertifikalı 182 GB modül; 2278×1134 ölçüsü hafızadan). |
| mod_glass_temper_factor_HS | Yarı temperli camın kalınlık gereksinimi çarpanı (FT'ye göre) | 1.4 | 1.3 – 1.5 | - | dusuk | hafizadan_dogrulanmadi | teknik |  | Hafızadan: EN 12150-1 FT ~120 MPa, EN 1863-1 HS ~70 MPa karakteristik dayanım; t ∝ σ^-0.5 (doğrusal) ile σ^-0.75 (membran) → 1.31-1.50. Wiki |
| mod_glass_mount_factor_frameless | Çerçevesiz 4 kelepçeli montajda kalınlık çarpanı (4 kenar mesnede göre) | 1.25 | 1.1 – 1.45 | - | dusuk | tahmin | teknik |  | Tahmin. Dayanak: nokta mesnette eğilme momenti 4 kenar mesnetten ~1.3-1.6 kat (plaka tabloları, hafızadan); kalınlıkta karekökü 1.15-1.26, m |
| mod_glass_nq_exp | Cam kalınlığının yüke bağımlılık üssü | 0.75 | 0.5 – 1 | - | orta | fizik_ders_kitabi | teknik |  | Plaka teorisi: küçük sehimde t ∝ q^0.5, büyük sehimde (membran) t ∝ q^1 |
| mod_q_test_Pa | Ürünün beyan test yükü (ön/arka) | 2400 | 1600 – 5400 | Pa | yuksek | dogrulanmis_url | teknik |  | IEC 61215-2 MQT 16: her iki yüze 2400 Pa, 1 saat, 3 çevrim (pv-tech, 27.03.2026). 5400 Pa ön yüz kar seçeneği (Synapsun). |
| mod_load_safety_factor | IEC 61215 test yükü / tasarım yükü katsayısı (γM) | 1.5 | 1.5 – 1.5 | - | orta | arama_ozeti | teknik |  | IEC 61215'te en düşük tasarım yükü 1600 Pa ve güvenlik katsayısı 1.5 (ilk analizde arama özetinde görüldü; ecogeneration sayfası iki denetçi |
| mod_gamma_Q | Değişken etki kısmi güvenlik katsayısı (rüzgâr, EN 1990) | 1.5 | 1 – 1.5 | - | orta | standart_metni_dogrulanmis | teknik |  | EN 1990:2002+A1 Tablo A1.2(B) Not 2 (phd.eng.br'deki BS EN kopyası, bu revizyonda açıldı) |
| mod_wind_qp_Pa | Balkon yüksekliğinde tepe hız basıncı qp(z) | 850 | 370 – 1450 | Pa | orta | hesap_turetilmis | teknik |  | EN 1991-1-4 formülleri (4.5)-(4.8) (PDF ve SkyCiv, açıldı) + DIN NA vb0 22.5-30 m/s (designforms, açıldı) + TS 498 (insapedia, açıldı): 0-8 |
| mod_wind_cp_net | Korkuluğa monte panel için net basınç katsayısı | 1.8 | 1.2 – 3.4 | - | orta | standart_metni_dogrulanmis | teknik |  | EN 1991-1-4:2005+A1 Tablo 7.9 (PDF açıldı). φ = 1, dönüşsüz: l/h ≤ 3 için A 2.3 / B 1.4 / C 1.2 / D 1.2; l/h = 5 için 2.9/1.8/1.4/1.2; l/h ≥ |
| mod_railing_height_m | Balkon korkuluk yüksekliği | 1 | 0.9 – 1.2 | m | dusuk | hafizadan_dogrulanmadi | teknik |  | Hafızadan: yönetmeliklerde ~0.9-1.1 m (doğrulanmadı) |
| mod_mass_max_portable_kg | Taşınabilir panel için kabul edilebilir en yüksek kütle | 12 | 8 – 20 | kg | dusuk | tahmin | teknik |  | Tahmin. Dayanak: tek kişi taşıma ergonomisi (ISO 11228-1'deki 25 kg referansı, hafızadan) ile ürün kullanılabilirliği. |
| mod_frame_kg_per_m_ref | Al çerçeve birim kütlesi (büyük modül referansı, 5400 Pa) | 0.4 | 0.33 – 0.48 | kg/m | orta | hesap_turetilmis | teknik |  | SMM (26.09.2024): 0.45-0.48万吨/GW. Cinda raporu (2023-09, bu revizyonda açıldı): 182 mm modülde 2.60 kg/takım, 210 mm'de 2.90 kg/takım → 2.60 |
| mod_frame_kg_per_m_min | Çerçeve profilinin üretilebilir en küçük birim kütlesi | 0.2 | 0.12 – 0.3 | kg/m | dusuk | tahmin | teknik |  | Tahmin. Dayanak: 1.0-1.2 mm et kalınlığı, 25-30 mm yükseklik ve cam kanalı; ~75 mm² kesit × 2.7 g/cm³ ≈ 0.2 kg/m. |
| mod_encap_mass_kg_m2 | Enkapsülan film birim kütlesi (tek kat) | 0.46 | 0.42 – 0.5 | kg/m2 | orta | dogrulanmis_url | teknik |  | Tianxia Gongchang Research (bu revizyonda açıldı): HJT POE 500 µm 460 g/m²; EVA ~450 µm 420 g/m² |
| mod_backsheet_mass_kg_m2 | Arka tabaka birim kütlesi | 0.4 | 0.3 – 0.5 | kg/m2 | dusuk | tahmin | teknik |  | Tahmin. Dayanak: ~300 µm PET esaslı katman × ~1.4 g/cm³ ≈ 0.42 kg/m². |
| mod_jbox_mass_kg | Bağlantı kutusu + kısa lead kütlesi | 0.3 | 0.15 – 0.5 | kg | dusuk | tahmin | teknik |  | Tahmin. Dayanak: PPO gövde ~60-100 g + potting + terminal + 2 × 0.3 m kablo. |
| mod_fx_cny_per_usd | Kur varsayımı CNY/USD | 6.7 | 6.5 – 7.3 | CNY/USD | yuksek | dogrulanmis_url | teknik | → `bat_fx_cny_per_usd` | Federal Reserve H.10 (ham HTML curl ile okundu; WebFetch özetleyicisi bu sayfada yanlış değer üretiyor) |
| mod_glass_price_usd_m2_per_mm | Ön yüz PV camı fiyatı (çift kaplamalı, Çin spot) | 0.71 | 0.55 – 1.3 | USD/m2/mm | orta | hesap_turetilmis | alan |  | EnergyTrend (23.09.2026) ; Montagtech/SCI (03.09.2026) (modul) |
| mod_glass_rear_price_usd_m2_per_mm | Arka PV camı fiyatı (cam-cam arka cam) | 0.63 | 0.45 – 1 | USD/m2/mm | orta | dogrulanmis_url | alan |  | EnergyTrend (23.09.2026, bu revizyonda açıldı): 2.0 mm arka cam ortalama 8.5 RMB/m² → 8.5/6.70/2 |
| mod_landed_factor_glass | Cam için TR'ye teslim ve küçük hacim çarpanı | 1.4 | 1.15 – 2.5 | - | dusuk | tahmin | teknik |  | Tahmin. Dayanak: cam ağır (2 mm ≈ 5 kg/m²); 40' konteyner ~26 t ≈ 5000 m² 2 mm ve ~2-3 k$ navlunla (hafızadan) +0.2-0.3 $/m²/mm; artı gümrük |
| mod_encap_price_usd_m2 | POE (veya EPE) enkapsülan fiyatı, tek kat | 1.94 | 0.95 – 2.6 | USD/m2 | dusuk | dogrulanmis_url | alan |  | Tianxia Gongchang Research (24.06.2026, bu revizyonda açıldı; Infolink, PVInsights ve SolarMedia endekslerine dayanır): 2025 sonu POE RMB 13 |
| mod_encap_eva_price_usd_m2 | Şeffaf EVA enkapsülan fiyatı, tek kat (60 V PID'siz dal) | 1.31 | 0.9 – 1.8 | USD/m2 | dusuk | dogrulanmis_url | alan |  | Tianxia Gongchang Research: şeffaf EVA RMB 8.8 /m² (2025 sonu) / 6.70 |
| mod_landed_factor_film | Enkapsülan için TR teslim ve küçük hacim çarpanı | 1.4 | 1.15 – 2 | - | dusuk | tahmin | teknik |  | Tahmin. Dayanak: film hafif (0.46 kg/m²) olduğundan navlun küçük; ağırlık rulo MOQ, raf ömrü (POE ~6 ay, hafızadan) ve distribütör marjında. |
| mod_backsheet_price_usd_m2 | Arka tabaka fiyatı (yalnız GB) | 1.1 | 0.7 – 1.8 | USD/m2 | dusuk | hafizadan_dogrulanmadi | alan |  | Hafızadan: 2024-2025'te RMB ~6-10/m² (doğrulanmadı) |
| mod_al_lme_usd_kg | Alüminyum LME fiyatı | 3.254 | 2.8 – 3.8 | USD/kg | yuksek | dogrulanmis_url | adet |  | https://www.westmetall.com/en/markdaten.php?action=table&field=LME_Al_cash |
| mod_al_premium_usd_kg | Bölgesel alüminyum primi (Avrupa/TR teslim) | 0.35 | 0.15 – 0.6 | USD/kg | dusuk | tahmin | adet |  | Tahmin. Hafızadan: Rotterdam gümrüklü primi 2024-25'te ~250-450 $/t. |
| mod_frame_processing_cn_usd_kg | Çerçeve işleme ücreti (Çin, GW ölçek) | 0.78 | 0.63 – 0.93 | USD/kg | dusuk | hesap_turetilmis | adet |  | Türetildi, Cinda (信达证券) 光伏边框行业深度报告, 2023-09 (bu revizyonda açıldı): çerçeve 'külçe fiyatı + işleme ücreti' ile fiyatlanır; 2022 ortalama çer |
| mod_landed_factor_frame | Çerçeve işleme için TR kısa seri çarpanı | 1.9 | 1.2 – 3.2 | - | dusuk | tahmin | teknik |  | Tahmin. Dayanak: özel profil kalıbı amortismanı, kısa seri eloksal, kesim/delme ve köşe montajı. |
| mod_cu_interconnect_price_usd_kg | Kaplamalı Cu ara bağlantı teli fiyatı | 15 | 10 – 25 | USD/kg | dusuk | dogrulanmis_url | alan |  | Made-in-China ilanı (bu revizyonda açıldı): 100-999 kg için 20 $/kg, 1000+ kg için 10 $/kg. Ürün Cu+Sn+Pb kalay kaplı; SnBi(Ag) değil. |
| mod_wire_d_mm | Ara bağlantı teli çapı | 0.25 | 0.18 – 0.35 | mm | orta | dogrulanmis_url | teknik |  | TaiyangNews (15.12.2023, bu revizyonda açıldı): 0BB/ZBB ~0.2 mm, eski 0.29-0.4 mm |
| mod_wire_shading_k | Yuvarlak telin optik etkin gölgeleme oranı | 0.4 | 0.25 – 0.7 | - | dusuk | tahmin | teknik |  | Tahmin. Dayanak: yuvarlak tel ışığın bir kısmını cam içi toplam yansımayla hücreye geri gönderir. |
| mod_wire_n_min | Hücre başına en az tel sayısı | 4 | 3 – 6 | adet | dusuk | tahmin | teknik |  | Tahmin. Dayanak: mekanik tutunma ve tek tel kopmasına karşı yedeklilik. |
| mod_finger_k_ohm | Parmak (finger) kayıp katsayısı f_yüz·ρ_f·s_f/(3·A_f) | 0.21 | 0.08 – 0.6 | ohm | dusuk | tahmin | teknik |  | Tahmin: f_yüz 1.5 (ön ve arka ızgara) × ρ_f 6e-8 Ω·m (düşük sıcaklık Ag, 4e-8..1.2e-7) × s_f 1.5 mm / (3 × A_f 2.1e-10 m², 25×12 µm × 0.7). |
| mod_cu_resistivity_op_ohm_m | Bakır özdirenci (çalışma sıcaklığında) | 1.9e-08 | 1.8e-08 – 2e-08 | ohm*m | yuksek | fizik_ders_kitabi | teknik |  | 1.72e-8 Ω·m (20 °C) × (1 + 0.0039·(T − 20)), T = 45-65 °C |
| mod_interconnect_fixed_usd_per_cell | Hücre başı sabit ara bağlantı sarfiyatı (lehim/film/ECA, bara payı) | 0.01 | 0.003 – 0.04 | USD/hücre | dusuk | tahmin | adet |  | Tahmin. Dayanak: SnBi flux/film ve bara payı ~0.2-0.5 g malzeme/hücre; ECA gümüş içerdiği için üst sınır. |
| mod_edge_seal_usd_per_m | Butil kenar contası + kalıplı kenar koruyucu (GG çerçevesiz) | 0.3 | 0.1 – 0.8 | USD/m | dusuk | tahmin | adet |  | Tahmin. Dayanak: butil 12 × 0.6 mm × 1.3 g/cm³ ≈ 9 g/m × ~5 $/kg ≈ 0.05 $/m; kendi enjeksiyonumuzla PP/TPE koruyucu 30-60 g/m × 2-3 $/kg ≈ 0 |
| mod_edge_seal_gb_usd_per_m | Çerçeve silikonu (GB veya GG çerçeveli) | 0.1 | 0.05 – 0.2 | USD/m | dusuk | tahmin | adet |  | Tahmin. Dayanak: 10-15 g/m silikon × 5-8 $/kg. |
| mod_jbox_base_usd | Bağlantı kutusu gövdesi + terminal + kısa lead (kendi kalıbımız, diyot hariç) | 1.5 | 0.8 – 3 | USD/adet | dusuk | tahmin | adet |  | Tahmin. Dayanak: PPO ~80 g × 3-4 $/kg ≈ 0.3 $ + terminal/bakır 0.3-0.5 + potting 0.2-0.4 + montaj. Karşılaştırma: Çin 1500 V 3 diyotlu kutu |
| mod_bypass_device_usd | Baypas elemanı maliyeti (Schottky veya aktif MOSFET) | 0.3 | 0.1 – 0.8 | USD/adet | dusuk | tahmin | adet |  | Tahmin. Dayanak: 15-20 A SMD Schottky distribütör fiyatı ~0.1-0.3 $ (hafızadan); aktif baypas (IC + MOSFET) 0.5-0.8 $. |
| mod_pack_fixed_usd | Ambalaj, etiket, belge (panel başı sabit) | 0.6 | 0.3 – 1.5 | USD/adet | dusuk | tahmin | adet |  | Tahmin. Dayanak: etiket ~0.1, kılavuz 0.1-0.2, bant/köşe elemanları 0.2-0.4 $. |
| mod_pack_area_usd_m2 | Ambalajın alanla ölçeklenen kısmı | 1.5 | 0.8 – 3 | USD/m2 | dusuk | tahmin | alan |  | Tahmin. Dayanak: çift oluklu karton ~0.5-0.8 $/m² × ~2.2 m² karton/m² panel + köşe koruyucu. |
| mod_cable_length_m | Panelden kutuya tek yön kablo uzunluğu | 3 | 1 – 15 | m | dusuk | tahmin | teknik |  | Tahmin. Dayanak: K5'e göre kutu gölgede ve ayrı; balkonda korkuluk ile zemin arası 1-3 m; çok panelli kutuda 3-10 m. |
| mod_cable_cross_min_mm2 | En küçük PV kablo kesiti | 1.5 | 1.5 – 4 | mm2 | orta | hafizadan_dogrulanmadi | teknik |  | Hafızadan: EN 50618 PV kablo kesitleri 1.5 mm²'den başlar. Waaree 4 mm² kullanıyor (doğrulandı). |
| mod_cable_core_fixed_usd_per_m | PV kablo damarının bakır dışı maliyeti (yalıtım + kılıf + üretim) | 0.2 | 0.1 – 0.4 | USD/m | dusuk | tahmin | adet |  | Tahmin. Dayanak: XLPO yalıtım + kılıf 20-40 g/m × 3-5 $/kg + üretim payı. |
| mod_cu_price_usd_kg | Kablo için etkin bakır fiyatı (örgü payı dahil) | 12 | 9.5 – 15 | USD/kg | dusuk | hafizadan_dogrulanmadi | adet | → `el_cu_price_usd_kg` × 1.1 | Hafızadan: LME bakır 2025'te ~9.5-10 k$/t; 2026 değeri doğrulanmadı. ×1.1 örgü/kablolama payı. |
| mod_connector_pair_usd | PV konnektör çifti (MC4 uyumlu, IEC 62852) | 0.6 | 0.3 – 1.5 | USD/adet | dusuk | tahmin | adet |  | Tahmin. Dayanak: Çin'de hacimde konnektör çifti ~0.2-0.4 $ (hafızadan) + küçük hacim ve teslim. |
| mod_cable_loss_target | Kablo kesit seçimi için STC kayıp hedefi | 0.01 | 0.005 – 0.02 | - | dusuk | tahmin | teknik |  | Tahmin (tasarım kuralı; optimizasyonla değiştirilebilir) |
| mod_cable_loss_energy_factor | Yıllık enerji ağırlıklı I² kaybı / STC kaybı | 0.55 | 0.4 – 0.75 | - | dusuk | hesap_turetilmis | teknik |  | Türetildi: güneşli günde sinüs profilinde ∫G²/∫G = (π/4)·Gmax; dikey balkonda Gmax 600-900 W/m² (tahmin) → 0.47-0.71. |
| mod_lam_cycle_min | Laminatör çevrim süresi (POE, cam-cam) | 15 | 10 – 22 | min | dusuk | hafizadan_dogrulanmadi | teknik |  | Hafızadan: EVA 8-12, POE 12-18 dk. Ooitech: POE işleme sıcaklığı 145-155 °C (açıldı; çevrim süresi sayfada yok). |
| mod_lam_area_m2 | Laminatör etkin alanı (kendi tasarım) | 3 | 1.5 – 6 | m2 | dusuk | tahmin | teknik |  | Tasarım seçimi (tahmin) |
| mod_lam_packing_factor | Laminatörde panel başına alan payı | 1.15 | 1.05 – 1.3 | - | dusuk | tahmin | teknik |  | Tahmin. Dayanak: paneller arası 30-50 mm ve kenar payı. |
| mod_lam_capex_usd | Laminatör yatırımı (kendi yapım) | 60000 | 25000 – 150000 | USD | dusuk | tahmin | zaman |  | Tahmin. Dayanak: ısıtma plakası (indüksiyon/yağ) 10-25 k$, vakum sistemi 5-15 k$, membran ve kasa 5-15 k$, kontrol 5-10 k$, mühendislik. |
| mod_lam_energy_kWh_m2 | Laminasyon duyulur ısı enerjisi (işlenen m² başına) | 0.3 | 0.25 – 0.45 | kWh/m2 | orta | hesap_turetilmis | alan |  | Türetildi: 2+2 cam 10 kg/m² × 0.84 kJ/kgK × 125 K = 1050 kJ = 0.29 kWh/m² |
| mod_lam_standby_kW | Laminatör bekleme/ısıl kayıp gücü | 4 | 2 – 8 | kW | dusuk | tahmin | zaman |  | Tahmin. Dayanak: 3 m² plaka 150 °C'de; yalıtım + yükleme sırasında açık yüzey kaybı ~0.7-2.5 kW/m². |
| mod_stringer_capex_usd | Düşük sıcaklık dizgi makinesi yatırımı | 120000 | 40000 – 400000 | USD | dusuk | tahmin | zaman |  | Tahmin. Dayanak: hücre besleme + görüntüleme 20-40 k$, tel çekme/kesme 15-30 k$, indüksiyon/IR lehim başlığı 15-40 k$, taşıma ve kontrol 20- |
| mod_test_capex_usd | Test ekipmanı yatırımı (IV flaş + EL + yalıtım/hipot + süreklilik) | 70000 | 30000 – 170000 | USD | dusuk | tahmin | zaman |  | Tahmin. Dayanak: IV 20-120 k$, EL 5-40 k$, hipot 2-12 k$ (hafızadan). |
| mod_misc_capex_usd | Diğer modül hattı donanımı (kenar/çerçeve aparatı, kutu yapıştırma, taşıma) | 30000 | 10000 – 80000 | USD | dusuk | tahmin | zaman |  | Tahmin. Dayanak: kenar koruyucu pres/aparatı 5-15 k$, kutu dozajlama 5-15 k$, arabalar ve raflar 5-10 k$. |
| mod_equip_life_y | Ekipman amortisman ömrü | 7 | 5 – 10 | yıl | dusuk | tahmin | teknik | → `eco_life_machine_yr` | Tahmin. Dayanak: üretim makinelerinde tipik 5-10 yıl; teknoloji eskimesi. |
| mod_maint_frac_per_y | Yıllık bakım ve yedek parça / yatırım | 0.05 | 0.02 – 0.08 | 1/yıl | dusuk | tahmin | zaman | → `eco_maint_frac_capex_yr` | Tahmin. Dayanak: membran, conta, flaş lambası ve vakum pompası sarfları. |
| mod_test_time_s_per_panel | Panel başı test makine süresi (EL + IV + gerekirse hipot) | 90 | 40 – 240 | s | dusuk | tahmin | teknik |  | Tahmin. Dayanak: EL 10-30 s, IV 10-20 s, hipot ve süreklilik 30-120 s, taşıma dahil. |
| mod_labor_min_per_panel | Panel başı elle yapılan iş (dizim, bara, kutu, kenar/çerçeve, temizlik, test yükleme, ambalaj) | 22 | 10 – 50 | min | dusuk | tahmin | teknik |  | Tahmin. Dayanak: yarı otomatik küçük hat; GW hatlarında ~2-5 dk (hafızadan). Test makine süresi hariç. |
| mod_labor_s_per_cell | Hücre başı işçilik (besleme, onarım, EL hatası) | 3 | 1 – 8 | s | dusuk | tahmin | teknik |  | Tahmin. Dayanak: otomatik dizgide hücre başı müdahale olasılığı %5-10 × 30-60 s. |
| mod_labor_rate_usd_h | Tam yüklü işçilik maliyeti (Gebze) | 7 | 5 – 12 | USD/h | dusuk | tahmin | zaman | → `eco_labor_operator_usd_h` | Tahmin. Dayanak: TR asgari ücretin işveren maliyeti (hafızadan, 2025'te ~1100-1300 $/ay) × vasıf primi 1.2-1.5 / ~190 saat. |
| mod_crew_min | Modül hattında vardiya başına asgari operatör | 1 | 1 – 2 | kişi | dusuk | tahmin | zaman |  | Tahmin. Dayanak: laminatör + dizgi + test tek operatörle yürüyebilir; iş güvenliği için 2 kişi gerekebilir. |
| mod_shift_h_per_day | Modül hattı çalışma saati | 8 | 8 – 24 | h/gün | dusuk | tahmin | teknik |  | Tahmin (tasarım seçimi) |
| mod_module_yield | Modül hattı verimi (kırılma, EL ret, yeniden işleme) | 0.98 | 0.94 – 0.995 | - | dusuk | tahmin | teknik |  | Tahmin. Dayanak: pilot hatta EL ret %1-3 + kırılma %0.5-2 (hafızadan, benzer küçük hatlar). |
| mod_mold_small_parts_usd | Küçük plastik parça kalıp seti (kutu, köşe takozu, kenar koruyucu ucu), varyant başına | 12000 | 4500 – 35000 | USD | dusuk | tahmin | urun_sabit |  | Tahmin (kendi kalıphanemiz). Dayanak: 3-4 kalıp × 1.5-8 k$. |
| mod_mold_frame_base_usd | Tek parça çerçeve kalıbının boyuttan bağımsız kısmı | 15000 | 5000 – 30000 | USD | dusuk | tahmin | urun_sabit |  | Tahmin. Dayanak: yolluk, soğutma, itici sistemi ve tasarım. |
| mod_mold_frame_usd_per_m2 | Tek parça çerçeve kalıbının panel ayak izi başına maliyeti (pay dahil) | 30000 | 10000 – 80000 | USD/m2 | dusuk | tahmin | urun_sabit |  | Tahmin. Dayanak: kalıp çeliği/alüminyum hacmi ve tabla ölçüsü ayak iziyle büyür. |
| mod_mold_cavity_pressure_MPa | Kalıp boşluk basıncı (pres tonajı için) | 50 | 0.5 – 80 | MPa | dusuk | hafizadan_dogrulanmadi | teknik |  | Hafızadan: termoplastik 30-80 MPa, RIM-PU ~0.5-1 MPa |

## Elektronik (MPPT/BMS/inverter) (`elektronik`) — 181 parametre

| id | ad | değer | aralık | birim | güven | kaynak türü | sınıf | eşdeğer | kaynak |
|---|---|---|---|---|---|---|---|---|---|
| el_fx_usd_try | USD/TRY kuru | 48.92 | 47 – 56 | TRY/USD | yuksek | dogrulanmis_url | teknik | → `eco_fx_try_per_usd` | https://tradingeconomics.com/turkey/currency |
| el_fx_eur_usd | EUR/USD | 1.139 | 1.05 – 1.25 | USD/EUR | yuksek | dogrulanmis_url | teknik |  | https://www.tcmb.gov.tr/kurlar/today.xml ; https://tradingeconomics.com/turkey/currency |
| el_discount_rate | Iskonto orani (USD, reel) | 0.08 | 0.04 – 0.12 | - | dusuk | tahmin | teknik |  | Kaynak yok |
| el_n_amort_yr | Ekipman amortisman suresi | 5 | 3 – 8 | yil | dusuk | tahmin | teknik |  | Kaynak yok (elektronik); dayanak: elektronik test ekipmani muhasebe pratigi (hafiza) |
| el_price_kWh_DE_usd | Almanya hane elektrik fiyati | 0.42 | 0.34 – 0.46 | USD/kWh | orta | hesap_turetilmis | teknik |  | https://www.bdew.de/service/daten-und-grafiken/bdew-strompreisanalyse/ |
| el_price_kWh_TR_usd | Turkiye mesken elektrik fiyati | 0.07 | 0.04 – 0.12 | USD/kWh | dusuk | hafizadan_dogrulanmadi | teknik |  | EPDK tarife sayfasi acildi, tablo gorulmedi; deger hafizadan (2025 mesken ~2.5-3 TL/kWh) |
| el_value_kWh_B_usd | Sebeke disi enerjinin ikame degeri (B) | 0.3 | 0.1 – 1 | USD/kWh | dusuk | tahmin | teknik |  | Kaynak yok |
| el_warranty_years_A | A garanti suresi | 10 | 5 – 12 | yil | dusuk | tahmin | teknik |  | https://balkon-kraft-werke.de/magazin/hoymiles-hms-800w-2t-test-daten-check/ (pazar referansi) |
| el_warranty_years_B | B garanti suresi | 3 | 2 – 5 | yil | dusuk | tahmin | teknik |  | Kaynak yok |
| el_years_life_B | B enerji degeri hesap suresi | 5 | 3 – 8 | yil | dusuk | tahmin | teknik |  | Kaynak yok |
| el_cu_price_usd_kg | LME bakir nakit | 14.74 | 11 – 16.5 | USD/kg | yuksek | dogrulanmis_url | teknik |  | https://www.westmetall.com/en/markdaten.php?action=table&field=LME_Cu_cash |
| el_enamel_premium | Emaye tel / LME bakir fiyat orani | 1.25 | 1.1 – 1.5 | - | dusuk | tahmin | teknik |  | Kaynak yok |
| el_tiw_premium | Uc kat yalitimli tel (TIW) / LME bakir orani | 2 | 1.5 – 3.5 | - | dusuk | tahmin | teknik |  | Kaynak yok |
| el_ferrite_price_usd_kg | MnZn guc ferriti | 6 | 3 – 12 | USD/kg | dusuk | tahmin | teknik |  | Kaynak yok |
| el_mag_ref_Ap_m4 | Referans cekirdek alan carpimi (PQ35/35) | 1.9e-08 | 1.6e-08 – 2.2e-08 | m^4 | orta | hesap_turetilmis | teknik |  | https://www.ferroxcube.com/upload/media/product/file/Pr_ds/PQ35_35.pdf |
| el_mag_ref_mass_kg | Referans manyetik kutlesi (PQ35/35 ferrit + bakir) | 0.1 | 0.09 – 0.12 | kg | orta | hesap_turetilmis | teknik |  | https://www.ferroxcube.com/upload/media/product/file/Pr_ds/PQ35_35.pdf |
| el_mag_fe_frac | Manyetik kutlesinde ferrit payi | 0.73 | 0.6 – 0.8 | - | dusuk | hesap_turetilmis | teknik |  | PQ35/35 73 g / 100 g |
| el_mag_labor_usd_per_piece | Sarimli induktor iscilik + bobin | 0.65 | 0.35 – 1.4 | USD/adet | orta | hesap_turetilmis | adet |  | https://www.alomaliye.com/2025/12/23/2026-yili-asgari-ucreti-2026-yili-asgari-ucret-bilgilendirme/ |
| el_xfmr_labor_usd | Guclendirilmis yalitimli trafo iscilik + bobin (TIW, bant, hipot) | 1.15 | 0.6 – 2.2 | USD/adet | dusuk | hesap_turetilmis | adet |  | Iscilik saat maliyetinden |
| el_planar_core_premium | Planar cekirdek fiyat primi | 1.3 | 1.1 – 1.8 | - | dusuk | tahmin | teknik |  | Kaynak yok |
| el_planar_winding_usd_per_m2 | Planar sargi maliyeti (sqrt(Ap) basina etkin PCB) | 1350 | 700 – 2500 | USD/m^2 | dusuk | tahmin | teknik |  | Kaynak yok |
| el_planar_labor_usd | Planar induktor montaj iscilik | 0.25 | 0.1 – 0.5 | USD/adet | dusuk | tahmin | adet |  | Kaynak yok |
| el_mag_market_markup | Manyetik piyasa fiyati / firma ici maliyet | 2 | 1.4 – 3 | - | dusuk | tahmin | teknik |  | Kaynak yok |
| el_K_R_si100_usd_mohm | Si 100 V MOSFET fiyat x Rds(on,maks) | 2.18 | 1.5 – 3.5 | USD·mΩ | orta | hesap_turetilmis | teknik |  | https://www.lcsc.com/product-detail/MOSFET_Infineon-Technologies-BSC070N10NS5_C534364.html |
| el_K_R_gan100_usd_mohm | GaN 100 V FET fiyat x Rds(on) | 8 | 3 – 14 | USD·mΩ | dusuk | tahmin | teknik |  | https://www.lcsc.com/product-detail/MOSFETs_EPC-EPC2218_C3288335.html (ust referans) |
| el_fet_floor_si_usd | Si FET paket taban fiyati | 0.18 | 0.08 – 0.3 | USD/adet | dusuk | tahmin | adet |  | Kaynak yok |
| el_fet_floor_gan_usd | GaN FET taban fiyati | 0.7 | 0.4 – 1.5 | USD/adet | dusuk | tahmin | adet |  | Kaynak yok |
| el_k_T_rdson | Rds(on) sicak/25 °C orani | 1.6 | 1.4 – 1.9 | - | orta | hafizadan_dogrulanmadi | teknik |  | Hafiza (Si ve GaN veri sayfalarinda 100-125 °C'de 1.5-1.8x) |
| el_alpha_cond_per_switch | Anahtar basina iletim kaybi butcesi (gucun orani) | 0.0025 | 0.0015 – 0.005 | - | dusuk | tahmin | teknik |  | Tasarim butcesi |
| el_K_R_hv650_usd_mohm | 600/650 V SJ MOSFET fiyat x Rds(on) | 242 | 80 – 300 | USD·mΩ | orta | hesap_turetilmis | teknik |  | https://www.lcsc.com/product-detail/MOSFET_Infineon-Technologies-IPB65R125C7_C536638.html |
| el_fet_floor_hv_usd | 650 V FET taban fiyati | 0.8 | 0.4 – 1.9 | USD/adet | dusuk | tahmin | adet |  | Kaynak yok |
| el_drv_si_usd | Si yarim kopru surucusu | 0.45 | 0.25 – 0.8 | USD/adet | dusuk | tahmin | adet |  | Kaynak yok |
| el_drv_gan_usd | GaN yarim kopru surucusu | 0.8 | 0.4 – 1.5 | USD/adet | dusuk | tahmin | adet |  | Kaynak yok |
| el_drv_iso_usd | Izoleli yarim kopru surucusu (HV) | 1 | 0.6 – 2 | USD/adet | dusuk | tahmin | adet |  | Kaynak yok |
| el_Qoss_gan_nC | GaN 100 V cikis yuku (EPC2218, 50 V) | 46 | 46 – 69 | nC | yuksek | dogrulanmis_url | teknik |  | https://epc-co.com/epc/Portals/0/epc/documents/datasheets/EPC2218_datasheet.pdf |
| el_Qoss_si_nC | Si 100 V cikis yuku (BSC070N10NS5 sinifi, 50 V) | 40 | 25 – 60 | nC | dusuk | tahmin | teknik |  | LCSC: Coss 340 pF |
| el_Qrr_si_nC | Si 100 V govde diyodu ters toparlanma yuku | 50 | 20 – 150 | nC | dusuk | tahmin | teknik |  | Hafiza |
| el_fsw_si_kHz | Si secenegi anahtarlama frekansi (MPPT ve LV DC-DC) | 100 | 50 – 150 | kHz | orta | tahmin | teknik |  | Muhendislik pratigi |
| el_fsw_gan_kHz | GaN secenegi anahtarlama frekansi | 400 | 200 – 1000 | kHz | dusuk | tahmin | teknik |  | Kaynak yok |
| el_fsw_grid_kHz | H koprusu PWM frekansi (Si SJ) | 20 | 16 – 50 | kHz | dusuk | tahmin | teknik |  | Kaynak yok |
| el_Bac_xfmr_si_T | Trafo tepe AC aki, 100 kHz (3C95) | 0.12 | 0.08 – 0.15 | T | orta | hesap_turetilmis | teknik |  | https://www.ferroxcube.com/upload/media/product/file/Pr_ds/PQ35_35.pdf |
| el_Bac_xfmr_gan_T | Trafo tepe AC aki, 400-500 kHz (3F36/3C96) | 0.05 | 0.03 – 0.08 | T | orta | hesap_turetilmis | teknik |  | https://www.ferroxcube.com/upload/media/product/file/Pr_ds/PQ35_35.pdf |
| el_Bpk_L_si_T | Induktor tepe aki (DC ongerilimli, 100 kHz) | 0.3 | 0.25 – 0.33 | T | orta | hesap_turetilmis | teknik |  | https://www.ferroxcube.com/upload/media/product/file/Pr_ds/PQ35_35.pdf |
| el_Bpk_L_gan_T | Induktor tepe aki, 400 kHz | 0.25 | 0.2 – 0.3 | T | dusuk | tahmin | teknik |  | Kaynak yok |
| el_B_grid_L_T | Sebeke filtre induktoru tepe aki | 0.3 | 0.2 – 0.5 | T | dusuk | tahmin | teknik |  | Kaynak yok |
| el_J_A_m2 | Sargi akim yogunlugu | 4.5e+06 | 3e+06 – 6e+06 | A/m^2 | orta | tahmin | teknik |  | Muhendislik pratigi |
| el_Ku_L | Induktor pencere doluluk | 0.35 | 0.25 – 0.45 | - | dusuk | tahmin | teknik |  | Kaynak yok |
| el_Ku_xfmr_reinforced | Guclendirilmis yalitimli trafo doluluk | 0.2 | 0.15 – 0.3 | - | dusuk | tahmin | teknik |  | Kaynak yok |
| el_ripple_L | Induktor dalgacik orani | 0.3 | 0.2 – 0.4 | - | orta | tahmin | teknik |  | Pratik |
| el_ripple_grid | Sebeke induktoru dalgacik orani | 0.3 | 0.2 – 0.4 | - | orta | tahmin | teknik |  | Pratik |
| el_V_mp_min_V | Panel Vmp alt (sicak) — modul arayuzu | 30 | 26 – 34 | V | dusuk | tahmin | teknik |  | Kaynak yok (HJT N_s≈66 varsayimi) |
| el_V_mp_max_V | Panel Vmp ust (soguk) | 46 | 40 – 52 | V | dusuk | tahmin | teknik |  | Kaynak yok |
| el_V_mp_nom_V | Panel Vmp nominal | 40 | 35 – 45 | V | dusuk | tahmin | teknik |  | Kaynak yok |
| el_n_panel_per_mppt | MPPT kanali basina paralel panel sayisi | 1 | 1 – 8 | - | orta | tahmin | teknik |  | Tasarim secimi el_ds_mppt_grouping |
| el_P_ch_max_W | MPPT kanal azami gucu | 500 | 400 – 800 | W | dusuk | tahmin | teknik |  | Tasarim |
| el_I_rev_module_A | Modul azami seri sigorta degeri (ters akim) | 15 | 5 – 25 | A | dusuk | hafizadan_dogrulanmadi | teknik |  | IEC 62548 ters akim kurali (N-1)·1.25·Isc (hafiza) |
| el_cap_base_usd | MPPT kanal kondansator tabani | 0.5 | 0.3 – 1 | USD/kanal | dusuk | tahmin | adet |  | Kaynak yok |
| el_cap_per_W_usd | MPPT kondansator egimi | 0.003 | 0.0015 – 0.006 | USD/W | dusuk | tahmin | guc_enerji |  | Kaynak yok |
| el_isense_usd | Kanal akim olcumu | 0.4 | 0.2 – 0.8 | USD/kanal | dusuk | tahmin | adet |  | Kaynak yok |
| el_pv_conn_pair_usd | Panel basina PV giris konnektor cifti (kutu) | 1.5 | 0.8 – 3 | USD/panel | dusuk | tahmin | adet |  | Kaynak yok |
| el_str_fuse_usd | Dizi sigortasi | 1.5 | 0.8 – 3 | USD/panel | dusuk | tahmin | adet |  | Kaynak yok |
| el_ovp_usd | Bagimsiz donanim asiri gerilim korumasi (SELV tek ariza) | 1 | 0.5 – 1.5 | USD/kutu | dusuk | tahmin | adet |  | Kaynak yok |
| el_N_batt_series | Na-ion seri hucre sayisi | 14 | 14 – 15 | - | yuksek | hesap_turetilmis | teknik | → `bat_ns_cells` | floor(60/3.95) = 15; 14 onerilen |
| el_Vcell_max_na_V | Na-ion sarj ust gerilimi | 3.95 | 3.9 – 4.1 | V | yuksek | dogrulanmis_url | teknik | → `bat_cell_v_max_V` | https://ecoteardown.top/wp-content/uploads/2024/01/71173204E-220-220Ah-3.1V-Sodium-ion-Na-ion-Prismatic-Battery-Cell-Specification-Datasheet |
| el_Vcell_min_use_V | Kullanilan alt hucre gerilimi | 2 | 1.5 – 2.5 | V | dusuk | tahmin | teknik | → `bat_v_min_cutoff_V` | Datasheet 1.50 V + tasarim |
| el_T_charge_max_C | Na-ion sarj ust sicakligi | 45 | 40 – 55 | °C | yuksek | dogrulanmis_url | teknik |  | https://ecoteardown.top/wp-content/uploads/2024/01/71173204E-220-220Ah-3.1V-Sodium-ion-Na-ion-Prismatic-Battery-Cell-Specification-Datasheet |
| el_C_charge_max_C | Azami surekli sarj hizi (0-45 °C) | 0.5 | 0.5 – 3 | 1/h | yuksek | dogrulanmis_url | teknik |  | https://ecoteardown.top/wp-content/uploads/2024/01/71173204E-220-220Ah-3.1V-Sodium-ion-Na-ion-Prismatic-Battery-Cell-Specification-Datasheet |
| el_C_charge_cold_C | Azami sarj hizi (-10 ile 0 °C) | 0.2 | 0.1 – 1 | 1/h | yuksek | dogrulanmis_url | teknik |  | https://ecoteardown.top/wp-content/uploads/2024/01/71173204E-220-220Ah-3.1V-Sodium-ion-Na-ion-Prismatic-Battery-Cell-Specification-Datasheet |
| el_E_cell_Wh | Hucre enerjisi (pil arayuzu) | 20 | 10 – 71 | Wh | dusuk | tahmin | teknik | → `bat_E_cell_Wh` | Kaynak yok |
| el_h_store_h | Istenen depolama suresi E_batt/P_box | 1.5 | 0.5 – 4 | h | dusuk | tahmin | teknik |  | Referans: Solarbank 3 E2700 Pro 2.68 kWh / 800-1200 W |
| el_rhoE_pack_Wh_L | Pil bolmesi hacimsel enerji yogunlugu | 150 | 100 – 250 | Wh/L | dusuk | hesap_turetilmis | teknik |  | Datasheet hucre: 682 Wh / 2.52 L |
| el_eta_batt_rt | Na-ion DC cevrim verimi | 0.92 | 0.88 – 0.95 | - | orta | dogrulanmis_url | teknik |  | https://en.wikipedia.org/wiki/Sodium-ion_battery |
| el_grid_limit_VA | Almanya fis-tak besleme siniri | 800 | 600 – 800 | VA | yuksek | standart_metni_dogrulanmis | teknik |  | https://www.dke.de/de/arbeitsfelder/energy/normenhinweise/faq-zur-dinvdev012695 |
| el_V_grid_V | Sebeke nominal gerilimi | 230 | 220 – 240 | V | orta | hafizadan_dogrulanmadi | teknik |  | IEC 60038 (hafiza) |
| el_V_dc_link_V | HV DC ara devre gerilimi | 400 | 380 – 420 | V | orta | hesap_turetilmis | teknik |  | 230 V tepe 325 V + pay |
| el_dV_dc_link_V | DC ara devre 100 Hz tepe-tepe dalgacik | 40 | 20 – 60 | V | dusuk | tahmin | teknik |  | Tasarim |
| el_capJ_hv_usd_per_J | 450 V elektrolitik fiyat / depolanan enerji | 0.08 | 0.04 – 0.2 | USD/J | dusuk | tahmin | teknik |  | Kaynak yok |
| el_hv_diode_usd | 600 V hizli diyot (tek yonlu HV dogrultucu) | 0.15 | 0.08 – 0.4 | USD/adet | dusuk | tahmin | adet |  | Kaynak yok |
| el_inv_misc_usd | Inverter diger (rezonans L, izoleli geri besleme, HV kond. tabani) | 1.6 | 1 – 3 | USD/kutu | dusuk | tahmin | adet |  | Kaynak yok |
| el_bidir_sense_usd | Cift yonlu ek olcum/koruma | 1 | 0.5 – 2 | USD/kutu | dusuk | tahmin | adet |  | Kaynak yok |
| el_P_inv_B_max_W | B inverter ust gucu | 600 | 300 – 1000 | W | dusuk | tahmin | teknik |  | Tasarim |
| el_pcb_m2_per_W | Guc kati PCB alani | 1.5e-05 | 1e-05 – 2.5e-05 | m^2/W | dusuk | tahmin | teknik |  | Kaynak yok |
| el_pcb_usd_m2 | 2 oz 4 katman PCB fiyati | 110 | 70 – 160 | USD/m^2 | dusuk | hesap_turetilmis | teknik |  | https://jlcpcb.com/blog/special-discount-on-quality-4-layers-pcbs |
| el_asm_per_W_usd | Guc kati montaj egimi | 0.002 | 0.001 – 0.004 | USD/W | dusuk | tahmin | guc_enerji |  | Kaynak yok |
| el_bms_bar_per_W_usd | BMS bara/sigorta egimi | 0.002 | 0.001 – 0.004 | USD/W | dusuk | tahmin | guc_enerji |  | Kaynak yok |
| el_mcu_usd | MCU (STM32G474, inverterli) | 3.01 | 2.5 – 4.3 | USD/kutu | yuksek | dogrulanmis_url | adet |  | https://www.lcsc.com/product-detail/C730123.html |
| el_mcu_B_usd | MCU (B, inverter yok) | 1.5 | 0.8 – 3 | USD/kutu | dusuk | tahmin | adet |  | Kaynak yok |
| el_fixed_common_usd | Ortak sabit elektronik (yardimci guc, olcum/koruma, PCB tabani, SMT tabani, etiket) | 9.9 | 6.5 – 15 | USD/kutu | dusuk | tahmin | adet |  | Kaynak yok |
| el_ac_interface_usd | A AC arayuzu (4 NA-koruma rolesi, EMI filtre, X/Y, varistor, sigorta, AC konnektor) | 10 | 6 – 16 | USD/kutu | dusuk | tahmin | adet |  | Kaynak yok |
| el_comm_monitor_A_usd | A WiFi + yedekli sebeke izleme | 4 | 2.5 – 6 | USD/kutu | dusuk | tahmin | adet |  | Kaynak yok |
| el_fixed_B_extra_usd | B ek sabit (BLE, 2x USB-PD 100 W, 12 V cikis, ekran/tus) | 16 | 9 – 24 | USD/kutu | dusuk | tahmin | adet |  | https://www.lcsc.com/product-detail/C20415848.html (kismi) |
| el_afe_usd | BMS AFE (BQ76952) | 2.01 | 1.8 – 3.3 | USD/kutu | yuksek | dogrulanmis_url | adet |  | https://www.lcsc.com/product-detail/C2862742.html |
| el_bms_support_usd | BMS destek + sigorta/on-sarj | 4.5 | 3 – 8 | USD/kutu | dusuk | tahmin | adet |  | Kaynak yok |
| el_rho_stage_si_W_per_L | Kat basina guc yogunlugu (Si, dolgulu, dogal sogutma) | 500 | 300 – 800 | W/L | dusuk | hesap_turetilmis | teknik |  | https://www.chargerlab.com/teardown-of-enphase-iq8p-480w-microinverter-iq8p-72-2-int/ |
| el_rho_stage_gan_W_per_L | Kat basina guc yogunlugu (GaN + planar) | 800 | 500 – 1400 | W/L | dusuk | tahmin | teknik |  | Kaynak yok |
| el_V0_box_A_L | Gucten bagimsiz hacim (A) | 0.25 | 0.15 – 0.5 | L | dusuk | tahmin | teknik |  | Kaynak yok |
| el_V0_box_B_L | Gucten bagimsiz hacim (B) | 0.35 | 0.2 – 0.6 | L | dusuk | tahmin | teknik |  | Kaynak yok |
| el_box_void_factor | Kutu bosluk katsayisi | 1.1 | 1.05 – 1.25 | - | dusuk | tahmin | teknik |  | Kaynak yok |
| el_resin_price_usd_kg | UV kararli FR PC/ASA recine | 4.5 | 3.4 – 8 | USD/kg | orta | hesap_turetilmis | teknik |  | https://www.intratec.us/solutions/primary-commodity-prices/commodity/polycarbonate-prices |
| el_wall_thickness_mm | Kasa et kalinligi | 3 | 2.2 – 4 | mm | dusuk | tahmin | teknik |  | Kaynak yok |
| el_resin_density_kg_m3 | PC yogunlugu | 1200 | 1150 – 1250 | kg/m^3 | yuksek | fizik_ders_kitabi | teknik |  | Malzeme ozelligi (hafiza) |
| el_rib_factor | Nervur/bosluk malzeme katsayisi | 1.3 | 1.1 – 1.5 | - | dusuk | tahmin | teknik |  | Kaynak yok |
| el_k_shape | Yuzey/hacim^(2/3) (1:0.75:0.35) | 6.6 | 6 – 8 | - | yuksek | hesap_turetilmis | teknik |  | Geometri |
| el_gasket_usd_per_m2 | Conta/cevre maliyeti | 8 | 4 – 15 | USD/m^2 | dusuk | tahmin | guc_enerji |  | Kaynak yok |
| el_enclosure_fixed_usd | Kasa sabit (vida, valf, rakor) | 3.1 | 2 – 6 | USD/kutu | dusuk | tahmin | adet |  | Kaynak yok |
| el_n_mold_parts | Enjeksiyon parca sayisi (govde + kapak) | 2 | 2 – 3 | - | orta | tahmin | teknik |  | Tasarim |
| el_t_cycle_s | Enjeksiyon cevrim suresi | 60 | 40 – 90 | s | dusuk | tahmin | teknik |  | Kaynak yok |
| el_press_rate_a_usd_h | Pres saat ucreti sabit kismi | 15 | 8 – 30 | USD/h | dusuk | tahmin | zaman |  | Kaynak yok |
| el_press_rate_b_usd_h_per_t | Pres saat ucreti tonaj egimi | 0.06 | 0.03 – 0.12 | USD/(h·t) | dusuk | tahmin | zaman |  | Kaynak yok |
| el_clamp_t_per_cm2 | Kapama kuvveti / izdusum alani | 0.4 | 0.3 – 0.5 | t/cm^2 | dusuk | tahmin | teknik |  | Denetci: 3-5 kN/cm² |
| el_mold_c0_usd | Kalip takimi sabit | 12000 | 6000 – 25000 | USD/varyant | dusuk | tahmin | urun_sabit |  | Kaynak yok |
| el_mold_c1_usd_per_cm2 | Kalip takimi izdusum egimi | 30 | 15 – 60 | USD/cm^2 | dusuk | tahmin | urun_sabit |  | Kaynak yok |
| el_potting_price_usd_kg | Dolgu recinesi (PU/silikon, dolgulu) | 8 | 5 – 15 | USD/kg | dusuk | tahmin | teknik |  | Kaynak yok |
| el_potting_fill_frac | Elektronik bolmesi dolgu orani | 0.35 | 0.2 – 0.6 | - | dusuk | hesap_turetilmis | teknik |  | https://www.chargerlab.com/teardown-of-enphase-iq8p-480w-microinverter-iq8p-72-2-int/ |
| el_potting_density_kg_L | Dolgu yogunlugu | 1.5 | 1.3 – 1.8 | kg/L | dusuk | tahmin | teknik |  | Kaynak yok |
| el_hv_volume_frac | HV/sebeke bolumu hacim payi (kismi dolgu) | 0.4 | 0.25 – 0.6 | - | dusuk | tahmin | teknik |  | Kaynak yok |
| el_varnish_usd | Vernik (dolgusuz) | 1 | 0.5 – 2 | USD/kutu | dusuk | tahmin | adet |  | Kaynak yok |
| el_h_conv_rad_W_m2K | Dogal tasinim + isinim katsayisi | 9 | 6 – 12 | W/(m^2·K) | orta | fizik_ders_kitabi | teknik |  | h_rad = 4εσT³ |
| el_dT_box_allow_K | Elektronik yuzey - ortam ΔT | 20 | 10 – 30 | K | dusuk | tahmin | teknik |  | Kaynak yok |
| el_fin_cost_usd_per_m2 | Ek Al kanatcik (etkin alan basina) | 35 | 20 – 60 | USD/m^2 | dusuk | tahmin | teknik |  | Kaynak yok |
| el_fin_base_usd | Termal arayuz tabani | 1 | 0.5 – 2 | USD/kutu | dusuk | tahmin | adet |  | Kaynak yok |
| el_pad_usd_per_W | Termal ped egimi | 0.0015 | 0.0008 – 0.003 | USD/W | dusuk | tahmin | guc_enerji |  | Kaynak yok |
| el_P_aux_W | Gunduz yardimci tuketim | 3 | 1.5 – 5 | W | dusuk | tahmin | teknik |  | Kaynak yok |
| el_eta_mppt | MPPT agirlikli verimi (Si, 4 anahtarli buck-boost) | 0.975 | 0.96 – 0.98 | - | orta | hesap_turetilmis | teknik |  | https://www.victronenergy.com/solar-charge-controllers/smartsolar-mppt-75-10-75-15-100-15-100-20 |
| el_eta_inv | Izoleli DC-DC + H koprusu agirlikli verim (Si) | 0.95 | 0.93 – 0.965 | - | dusuk | hesap_turetilmis | teknik |  | https://balkon-kraft-werke.de/magazin/hoymiles-hms-800w-2t-test-daten-check/ |
| el_gan_eta_gain_pts | GaN'in zincir verimine katkisi | 0.8 | 0 – 1.5 | puan | dusuk | tahmin | teknik |  | Kaynak yok (IQ9N %97.5 tepe/agirlikli belirsiz, Si karsilastirmasi yok) |
| el_eta_dc_out_B | B DC cikis verimi | 0.95 | 0.92 – 0.97 | - | dusuk | tahmin | teknik |  | Kaynak yok |
| el_P_standby_A_W | A gece oz tuketimi | 2 | 0.5 – 10 | W | dusuk | tahmin | teknik |  | https://reduco.ai/blog/solar/anker-solix-solarbank-3-test (ust referans) |
| el_P_standby_B_W | B bekleme tuketimi | 0.5 | 0.1 – 2 | W | dusuk | tahmin | teknik |  | Kaynak yok |
| el_night_frac | Yil icinde PV'siz saat payi | 0.55 | 0.45 – 0.65 | - | orta | tahmin | teknik |  | Kaynak yok |
| el_Y_spec_kWh_per_kWp | Ozgul yillik uretim | 1000 | 600 – 1500 | kWh/kWp/yil | dusuk | tahmin | teknik |  | Kaynak yok (sistem arayuzu) |
| el_cap_L0_h | Elektrolitik anma omru (105 °C) | 5000 | 2000 – 10000 | h | dusuk | tahmin | teknik |  | https://www.chemi-con.co.jp/en/faq/detail.php?id=alLifetime (formul) |
| el_V_lim_dry_V | DVC-A / SELV DC siniri, kuru | 60 | 60 – 60 | V | yuksek | standart_metni_dogrulanmis | teknik |  | http://erlerdesign.com/download/ESD/old_iec60364-4-41_protection_shock_inst_buildings.pdf ; https://en.eastups.com/u/cms/en/202012/221419145 |
| el_V_lim_wet_V | Islak ortam siniri (urun DVC-A 35 V / tesisat 30 V) | 35 | 30 – 35 | V | yuksek | standart_metni_dogrulanmis | teknik | → `std_dvca_dc_wet_v` | https://cdn.standards.iteh.ai/samples/101797/42a8cc90b5da400b94a3684c1c75b0a0/IEC-TS-62257-9-8-2020.pdf ; IEC 60364-4-41 (yukarida); eastups |
| el_labor_usd_h | Teknisyen saat maliyeti (isveren) | 6.17 | 4.1 – 10 | USD/h | orta | hesap_turetilmis | teknik | → `eco_labor_operator_usd_h` | https://www.alomaliye.com/2025/12/23/2026-yili-asgari-ucreti-2026-yili-asgari-ucret-bilgilendirme/ |
| el_test_time_A_s | A unite testi suresi (hipot, fonksiyon, NA-koruma, kalibrasyon) | 180 | 90 – 400 | s | dusuk | tahmin | teknik |  | https://cdn.standards.iteh.ai/samples/9666/8b57d360961d4b7bb89ff9cbd04db3a6/IEC-62109-1-2010.pdf (zorunluluk) |
| el_test_time_B_s | B unite testi suresi | 90 | 45 – 240 | s | dusuk | tahmin | teknik |  | Kaynak yok |
| el_final_asm_A_min | A son montaj | 12 | 6 – 25 | dk | dusuk | tahmin | teknik |  | Kaynak yok |
| el_final_asm_B_min | B son montaj | 10 | 5 – 20 | dk | dusuk | tahmin | teknik |  | Kaynak yok |
| el_test_station_capex_A_usd | A test istasyonu yatirimi (sebeke simulatoru, PV/DC kaynak, guvenlik test cihazi, fikstur) | 90000 | 50000 – 150000 | USD | dusuk | tahmin | zaman |  | Kaynak yok |
| el_test_station_capex_B_usd | B test istasyonu yatirimi | 35000 | 15000 – 60000 | USD | dusuk | tahmin | zaman |  | Kaynak yok |
| el_hours_per_year_h | Yillik vardiya saati | 4000 | 2000 – 6000 | h/yil | orta | hesap_turetilmis | teknik |  | 2 vardiya x 8 h x 250 gun; altyapi eco_shift_pattern onerisi (firin ve HJT 24/7, modul/pil/kutu 2 vardiya + ara stok) |
| el_station_util_max | Istasyon azami kullanim | 0.7 | 0.5 – 0.85 | - | dusuk | tahmin | teknik |  | Kaynak yok |
| el_site_lab_capex_usd | Saha laboratuvari (EMC on-uyum, iklim kabini, HALT) | 200000 | 80000 – 400000 | USD/saha | dusuk | tahmin | saha_sabit |  | Kaynak yok |
| el_n_units_site | Sahadaki unite sayisi (paylasim) | 1 | 1 – 5 | - | orta | tahmin | teknik |  | Proje tanimi |
| el_packaging_A_usd | A ambalaj + kilavuz | 4 | 2.5 – 7 | USD/kutu | dusuk | tahmin | adet |  | Kaynak yok |
| el_packaging_B_usd | B ambalaj + kilavuz | 3.5 | 2 – 6 | USD/kutu | dusuk | tahmin | adet |  | Kaynak yok |
| el_ac_cable_plug_usd | A AC cikis kablosu + fis | 5 | 3 – 9 | USD/kutu | dusuk | tahmin | adet |  | Kaynak yok |
| el_scrap_frac | Hurda orani (malzeme) | 0.015 | 0.005 – 0.04 | - | dusuk | tahmin | teknik |  | Kaynak yok |
| el_fpy | Ilk gecis verimi | 0.95 | 0.85 – 0.99 | - | dusuk | tahmin | teknik |  | Kaynak yok |
| el_rework_min | Yeniden isleme suresi | 20 | 10 – 40 | dk/ariza | dusuk | tahmin | teknik |  | Kaynak yok |
| el_moq_attrition_frac | Dusuk hacimde MOQ/makara firesi | 0.03 | 0.01 – 0.08 | - | dusuk | tahmin | teknik |  | Kaynak yok |
| el_smt_setup_usd_per_lot | SMT kurulum maliyeti (lot basina) | 300 | 150 – 800 | USD/lot | dusuk | tahmin | adet |  | Kaynak yok |
| el_lot_size | Lot buyuklugu | 500 | 200 – 2000 | adet | dusuk | tahmin | teknik |  | Kaynak yok |
| el_weee_usd_per_kg | WEEE/EPR ucreti (elektronik + kasa) | 0.3 | 0.1 – 1 | USD/kg | dusuk | tahmin | teknik |  | Kaynak yok |
| el_elec_density_kg_L | Elektronik bolmesi kutle yogunlugu (dolgusuz) | 0.5 | 0.3 – 0.9 | kg/L | dusuk | tahmin | teknik |  | Kaynak yok |
| el_cloud_usd_per_box_yr | Bulut/uygulama isletimi (A) | 0.5 | 0.2 – 2 | USD/kutu/yil | dusuk | tahmin | adet |  | Kaynak yok |
| el_field_fail_rate_pct_yr | Saha ariza orani | 0.5 | 0.1 – 2 | %/yil | dusuk | tahmin | teknik |  | Kaynak yok |
| el_logistics_swap_usd | Ariza basina degisim lojistigi | 40 | 20 – 80 | USD/ariza | dusuk | tahmin | adet |  | Kaynak yok |
| el_eng_cost_usd_per_py | Muhendis isveren maliyeti (Gebze) | 40000 | 25000 – 60000 | USD/kisi-yil | dusuk | tahmin | teknik |  | Kaynak yok |
| el_py_A | A gelistirme eforu | 6 | 4 – 10 | kisi-yil | dusuk | tahmin | teknik |  | Kaynak yok |
| el_py_B | B gelistirme eforu | 3 | 2 – 5 | kisi-yil | dusuk | tahmin | teknik |  | Kaynak yok |
| el_nre_other_A_usd | A diger NRE (fikstur, prototip, dis kaynak on-uyum) | 85000 | 50000 – 150000 | USD/varyant | dusuk | tahmin | urun_sabit |  | Kaynak yok |
| el_nre_other_B_usd | B diger NRE | 45000 | 25000 – 80000 | USD/varyant | dusuk | tahmin | urun_sabit |  | Kaynak yok |
| el_cert_cost_A_usd | A sertifikasyon (IEC 62109-1/-2, VDE-AR-N 4105, EMC, RED) | 150000 | 80000 – 300000 | USD/varyant | dusuk | tahmin | urun_sabit |  | Kaynak yok |
| el_cert_cost_B_usd | B sertifikasyon (IEC 62368-1, EMC, RED) | 60000 | 25000 – 120000 | USD/varyant | dusuk | tahmin | urun_sabit |  | Kaynak yok |
| el_un383_usd | UN 38.3 tip testleri (Na-ion, UN 3551) | 15000 | 8000 – 30000 | USD/paket tasarimi | dusuk | tahmin | urun_sabit |  | https://www.iata.org/contentassets/05e6d8742b0047259bf3a700bc9d42b9/lithium-battery-guidance-document.pdf (gereklilik) |
| el_cra_usd_per_yr_A | Siber guvenlik/zafiyet yonetimi (A, WiFi) | 12000 | 5000 – 30000 | USD/yil | dusuk | tahmin | urun_sabit |  | AB Siber Dayaniklilik Tuzugu (hafiza) |
| el_cra_usd_per_yr_B | Siber guvenlik (B, BLE) | 6000 | 2000 – 15000 | USD/yil | dusuk | tahmin | urun_sabit |  | Kaynak yok |
| el_cra_support_years | Guvenlik destek suresi | 5 | 5 – 10 | yil | dusuk | hafizadan_dogrulanmadi | teknik |  | CRA en az 5 yil (hafiza) |
| el_N_demand_per_yr | Varyant basina yillik talep | 3000 | 1000 – 20000 | kutu/yil | dusuk | tahmin | teknik |  | Kaynak yok |
| el_Y_product_life | Varyant pazar omru | 5 | 3 – 8 | yil | dusuk | tahmin | teknik |  | tahmin (elektronik) |
| el_N_cell_per_year | Pil hatti hucre kapasitesi (K9) | 150000 | 100000 – 200000 | hucre/yil | orta | tahmin | teknik | → `bat_line_cells_per_year` | Kullanici karari K9 |
| el_n_batt_lines | Pil hatti sayisi | 1 | 1 – 3 | - | orta | tahmin | teknik |  | Proje |
| el_cable_len_m | Panel-kutu kablo uzunlugu | 5 | 2 – 15 | m | dusuk | tahmin | teknik |  | Kaynak yok |
| el_cable_loss_frac | Izin verilen kablo kaybi | 0.01 | 0.005 – 0.02 | - | orta | tahmin | teknik |  | https://www.staubli.com/content/dam/ecs/technical-documentation/assembly-instructions/RE/PV_SOL-LVDC-en.pdf (akim siniri baglami) |
| el_cable_price_factor | Kablo fiyati / bakir metal degeri | 2.5 | 1.8 – 4 | - | dusuk | tahmin | teknik |  | Kaynak yok |
| el_ref_microinv_retail_usd_per_W | Referans: 800 W balkon mikroinverteri perakende | 0.157 | 0.128 – 0.185 | USD/W | orta | dogrulanmis_url | teknik |  | https://balkon-kraft-werke.de/magazin/hoymiles-hms-800w-2t-test-daten-check/ |
| el_ref_pps_retail_usd_per_Wh | Referans: tasinabilir guc istasyonu medyan | 0.6 | 0.44 – 0.89 | USD/Wh | orta | dogrulanmis_url | teknik |  | https://www.solarwaypoint.com/portable-power-station-price-index/ |
| el_E_batt_reg_threshold_Wh | AB Pil Tuzugu 2 kWh esigi (karbon ayak izi, pasaport) | 2000 | 2000 – 2000 | Wh | dusuk | hafizadan_dogrulanmadi | teknik |  | Tuzuk 2023/1542 (hafiza); EUR-Lex bu gorevde bos dondu |
| el_portable_batt_mass_kg | Tasinabilir pil kutle siniri | 5 | 5 – 5 | kg | dusuk | hafizadan_dogrulanmadi | teknik |  | https://environment.ec.europa.eu/topics/waste-and-recycling/batteries_en (kismi) + hafiza |

## Pil (Na-iyon) (`pil`) — 111 parametre

| id | ad | değer | aralık | birim | güven | kaynak türü | sınıf | eşdeğer | kaynak |
|---|---|---|---|---|---|---|---|---|---|
| bat_fx_cny_per_usd | USD/CNY kuru | 6.72 | 6.5 – 7.3 | CNY/USD | yuksek | dogrulanmis_url | teknik |  | https://tradingeconomics.com/china/currency ; https://www.tcmb.gov.tr/kurlar/today.xml |
| bat_cell_price_na_cyl_usd_Wh | Na-iyon silindirik 26700 (LO) Cin fiyati | 0.084 | 0.079 – 0.088 | USD/Wh | orta | dogrulanmis_url | guc_enerji |  | https://www-old.metal.com/price/New-Energy/Sodium-ion-Battery |
| bat_cell_price_na_prismatic_usd_Wh | Na-iyon NFPP prizmatik 50-200 Ah Cin fiyati | 0.085 | 0.079 – 0.09 | USD/Wh | orta | dogrulanmis_url | guc_enerji |  | https://www-old.metal.com/price/New-Energy/Sodium-ion-Battery |
| bat_cell_price_na_pris_small_usd_Wh | Na-iyon NFPP kucuk prizmatik 10-28 Ah Cin fiyati | 0.073 | 0.07 – 0.076 | USD/Wh | orta | dogrulanmis_url | guc_enerji |  | https://www-old.metal.com/price/New-Energy/Sodium-ion-Battery |
| bat_cell_price_lfp_50ah_usd_Wh | LFP 50 Ah depolama (ESS) hucresi Cin fiyati | 0.0565 | 0.0543 – 0.0588 | USD/Wh | orta | dogrulanmis_url | guc_enerji |  | https://www-old.metal.com/price/New-Energy/Battery-Cell-And-Module |
| bat_cell_price_lfp_small_usd_Wh | LFP kucuk prizmatik 20-25 Ah Cin fiyati | 0.072 | 0.069 – 0.09 | USD/Wh | orta | dogrulanmis_url | guc_enerji |  | https://www-old.metal.com/price/New-Energy/Battery-Cell-And-Module |
| bat_cn_li_consumption_tax_frac | Cin Li-iyon pil tuketim vergisi (Na-iyon muaf) | 0.02 | 0 – 0.04 | - | orta | dogrulanmis_url | teknik |  | https://www.mysteel.net/analysis/5139214-china-lithium-industry-in-h2-2026-from-aggregate-surplus-to-structural-rebalancing |
| bat_cn_export_vat_cost_frac | Ihracatta iade edilmeyen KDV payi (Cin ic fiyatin ustune) | 0.13 | 0.07 – 0.13 | - | orta | hesap_turetilmis | guc_enerji |  | https://www.pv-magazine.com/2026/01/09/china-to-abolish-solar-export-tax-rebates-from-april/ + wf_cn_vat |
| bat_small_lot_markup | Kucuk alim primi — fabrikadan dogrudan alim | 0.3 | 0.1 – 0.8 | - | dusuk | tahmin | guc_enerji |  | tahmin |
| bat_small_lot_markup_pilot | Kucuk alim primi — distributor/pilot kanal (Faz 1 prototip) | 2 | 1 – 4 | - | dusuk | tahmin | guc_enerji |  | https://ogsolarstore.com/products/sodium-ion-nfpp-cylindrical-cells-rechargeable-battery-cell |
| bat_moq_cells | Fabrikadan dogrudan alim icin asgari siparis (MOQ) | 5000 | 1000 – 50000 | hucre | dusuk | tahmin | teknik |  | tahmin |
| bat_import_logistics_usd_Wh | Ithalat lojistigi + gumruk + EGV + giris | 0.012 | 0.005 – 0.05 | USD/Wh | dusuk | tahmin | guc_enerji |  | tahmin |
| bat_wh_usable_per_wp_A | Senaryo A: KULLANILABILIR Wh / panel Wp | 1.6 | 0.9 – 2.6 | Wh/Wp | orta | hesap_turetilmis | teknik |  | Pil: rakip urunlerin nominal 0.96-2.8 Wh/Wp orani x LFP kullanilabilir 0.92 |
| bat_wh_usable_per_wp_B | Senaryo B: KULLANILABILIR Wh / panel Wp | 3.2 | 1.8 – 5.5 | Wh/Wp | orta | hesap_turetilmis | teknik |  | Pil: EcoFlow River 3 245 Wh + 110 W; Jackery 1000 v2 1070 Wh + 200 W; nominal 2.2-5.35 x 0.92 |
| bat_cell_v_max_lo_V | LO hucre sarj ust gerilimi | 3.95 | 3.9 – 4 | V | yuksek | dogrulanmis_url | teknik |  | https://www.tycorun.com/products/sodium-ion-26700-battery |
| bat_cell_v_min_lo_V | LO veri sayfasi desarj alt gerilimi | 1.5 | 1.5 – 2 | V | yuksek | dogrulanmis_url | teknik |  | https://www.tycorun.com/products/sodium-ion-26700-battery ; https://www.evlithium.com/sodium-ion-battery/10ah-32140-sodium-ion-battery-for-s |
| bat_cell_v_nom_lo_V | LO nominal gerilim | 3.1 | 3 – 3.1 | V | yuksek | dogrulanmis_url | teknik |  | https://www.tycorun.com/products/sodium-ion-26700-battery |
| bat_cell_v_max_nfpp_V | Polianyon (NFPP etiketli) sarj ust gerilimi | 3.8 | 3.7 – 3.95 | V | orta | dogrulanmis_url | teknik |  | https://ogsolarstore.com/blogs/news/cell-review-sodium-ion-nfpp-18650 |
| bat_cell_v_min_nfpp_V | Polianyon desarj alt gerilimi | 1.5 | 1.5 – 2 | V | orta | dogrulanmis_url | teknik |  | https://ogsolarstore.com/blogs/news/cell-review-sodium-ion-nfpp-18650 |
| bat_cell_v_nom_nfpp_V | Polianyon nominal gerilim | 2.9 | 2.85 – 3.1 | V | orta | hesap_turetilmis | teknik |  | https://egroup18650.com/73-sodium-ion-cells ; https://ogsolarstore.com/blogs/news/cell-review-sodium-ion-nfpp-18650 |
| bat_cell_v_max_lfp_V | LFP sarj ust gerilimi (referans) | 3.65 | 3.55 – 3.65 | V | orta | hafizadan_dogrulanmadi | teknik |  | hafiza (LFP veri sayfalari) |
| bat_cell_v_min_lfp_V | LFP desarj alt gerilimi (referans) | 2.5 | 2 – 2.8 | V | orta | hafizadan_dogrulanmadi | teknik |  | hafiza |
| bat_cell_v_nom_lfp_V | LFP nominal gerilim | 3.2 | 3.2 – 3.22 | V | orta | hafizadan_dogrulanmadi | teknik |  | hafiza |
| bat_v_min_cutoff_V | Tasarimda secilen hucre desarj kesimi (Na) | 2 | 1.5 – 2.5 | V | dusuk | tahmin | teknik |  | Pil tasarim onerisi; veri sayfasi alt siniri 1.50 V (Tycorun) |
| bat_usable_fraction_lo | LO kullanilabilir enerji / anma enerjisi (2.0 V kesimde) | 0.8 | 0.72 – 0.88 | - | dusuk | tahmin | teknik |  | https://arxiv.org/pdf/2403.13759 (Bolum 16.1, Natron CEO yorumu) |
| bat_usable_fraction_nfpp | NFPP kullanilabilir enerji orani (2.0 V kesimde) | 0.9 | 0.8 – 0.95 | - | dusuk | tahmin | teknik |  | tahmin |
| bat_usable_fraction_lfp | LFP kullanilabilir oran (rakip urunler ve LFP secenegi) | 0.92 | 0.88 – 0.96 | - | dusuk | tahmin | teknik |  | tahmin |
| bat_cell_26700_capacity_Ah | 26700 Na-iyon kapasite | 3.3 | 3.2 – 3.5 | Ah | yuksek | dogrulanmis_url | teknik |  | https://www.tycorun.com/products/sodium-ion-26700-battery |
| bat_cell_prismatic_capacity_Ah | Buyuk prizmatik kapasite (tasarim secimi) | 50 | 50 – 200 | Ah | yuksek | dogrulanmis_url | teknik |  | https://www-old.metal.com/price/New-Energy/Sodium-ion-Battery |
| bat_cell_pris_small_capacity_Ah | Kucuk prizmatik kapasite (tasarim secimi) | 20 | 10 – 28 | Ah | orta | dogrulanmis_url | teknik |  | https://www-old.metal.com/price/New-Energy/Sodium-ion-Battery |
| bat_cell_grav_lo_Wh_kg | LO hucre ozgul enerjisi | 127 | 110 – 175 | Wh/kg | yuksek | dogrulanmis_url | teknik |  | https://www.tycorun.com/products/sodium-ion-26700-battery ; https://www.catl.com/en/news/6720.html |
| bat_cell_grav_nfpp_Wh_kg | Polianyon hucre ozgul enerjisi | 115 | 80 – 140 | Wh/kg | orta | hesap_turetilmis | teknik |  | https://ogsolarstore.com/blogs/news/cell-review-sodium-ion-nfpp-18650 ; https://www.evlithium.com/sodium-ion-battery/210ah-sodium-prismatic- |
| bat_cell_grav_lfp_Wh_kg | LFP hucre ozgul enerjisi (referans) | 160 | 140 – 190 | Wh/kg | dusuk | hafizadan_dogrulanmadi | teknik |  | hafiza |
| bat_cycle_life_lo_cyl | LO silindirik cevrim omru (%80, 25 C) | 3000 | 2000 – 5000 | cevrim | dusuk | dogrulanmis_url | teknik |  | https://www.tycorun.com/products/sodium-ion-26700-battery ; https://www.evlithium.com/sodium-ion-battery/10ah-32140-sodium-ion-battery-for-s |
| bat_cycle_life_nfpp_pris | NFPP prizmatik cevrim omru (%80, 25 C) | 5000 | 2000 – 10000 | cevrim | dusuk | hesap_turetilmis | teknik |  | https://ogsolarstore.com/blogs/news/cell-review-sodium-ion-nfpp-18650 ; https://www.highstar-sodium.com/technical-characteristics-of-prismat |
| bat_cycle_life_nfpp_cyl | Polianyon kucuk silindirik cevrim omru | 1500 | 1000 – 4000 | cevrim | dusuk | dogrulanmis_url | teknik |  | https://ogsolarstore.com/blogs/news/cell-review-sodium-ion-nfpp-18650 |
| bat_cycle_life_lfp | LFP cevrim omru (referans, %80) | 6000 | 3000 – 8000 | cevrim | dusuk | hafizadan_dogrulanmadi | teknik |  | hafiza |
| bat_cal_fade_k_per_sqrt_yr | Takvim yaslanmasi katsayisi (25 C, orta SOC) | 0.02 | 0.01 – 0.04 | 1/yil^0.5 | dusuk | tahmin | teknik |  | tahmin |
| bat_aging_accel_per_10C | Yaslanma hizlanma carpani (her +10 C) | 1.58 | 1.3 – 2 | - | dusuk | hesap_turetilmis | teknik |  | https://www.highstar-sodium.com/technical-characteristics-of-prismatic-sodium-battery-cells/ |
| bat_eol_soh | Garanti sonu vaat edilen SOH | 0.7 | 0.6 – 0.8 | - | dusuk | tahmin | teknik |  | tahmin |
| bat_capacity_oversize | Garanti icin nominal buyutme carpani | 1 | 1 – 1.25 | - | dusuk | tahmin | teknik |  | tasarim secimi |
| bat_charge_temp_min_C | En dusuk sarj sicakligi | -10 | -20 – 0 | C | orta | dogrulanmis_url | teknik |  | https://www.tycorun.com/products/sodium-ion-26700-battery ; https://www.evlithium.com/sodium-ion-battery/210ah-sodium-prismatic-battery-cell |
| bat_charge_temp_max_C | En yuksek sarj sicakligi | 45 | 45 – 60 | C | orta | dogrulanmis_url | teknik |  | https://www.tycorun.com/products/sodium-ion-26700-battery ; https://ogsolarstore.com/blogs/news/cell-review-sodium-ion-nfpp-18650 |
| bat_charge_c_max_cyl | Silindirik surekli sarj C-orani (0-45 C) | 1 | 0.5 – 1 | 1/h | orta | dogrulanmis_url | teknik |  | https://www.tycorun.com/products/sodium-ion-26700-battery |
| bat_charge_c_max_pris | Prizmatik surekli sarj C-orani (0-45 C) | 0.5 | 0.3 – 1 | 1/h | orta | dogrulanmis_url | teknik |  | EVLithium 210 Ah prizmatik veri sayfasi; 26700 icin bat_charge_c_max_cyl 1.0 (Tycorun); sifir alti 0.2C |
| bat_charge_c_max_subzero | Sifir alti sarj C-orani | 0.2 | 0.1 – 0.2 | 1/h | orta | dogrulanmis_url | teknik |  | https://www.tycorun.com/products/sodium-ion-26700-battery ; https://www.evlithium.com/sodium-ion-battery/210ah-sodium-prismatic-battery-cell |
| bat_discharge_c_max_subzero | Sifir alti desarj C-orani siniri | 0.2 | 0.2 – 1 | 1/h | orta | dogrulanmis_url | teknik |  | https://www.tycorun.com/products/sodium-ion-26700-battery ; https://ogsolarstore.com/blogs/news/cell-review-sodium-ion-nfpp-18650 |
| bat_discharge_retention_m20C | -20 C desarj kapasite orani (dusuk akim) | 0.85 | 0.8 – 0.9 | - | orta | dogrulanmis_url | teknik |  | https://ogsolarstore.com/blogs/news/cell-review-sodium-ion-nfpp-18650 ; https://www.catl.com/en/news/6720.html |
| bat_pv_peak_factor | PV en yuksek gucunun Wp'ye orani (sarj akimi icin) | 0.85 | 0.7 – 0.95 | - | dusuk | tahmin | teknik |  | tahmin |
| bat_roundtrip_eff | Hucre DC gidis-donus verimi | 0.94 | 0.9 – 0.97 | - | orta | dogrulanmis_url | teknik |  | https://www.highstar-sodium.com/technical-characteristics-of-prismatic-sodium-battery-cells/ |
| bat_v_lim_margin | SELV sinirina gore tasarim payi | 0.97 | 0.93 – 0.99 | - | dusuk | tahmin | teknik |  | tahmin |
| bat_cycles_per_year_A | A yillik esdeger tam cevrim | 300 | 200 – 365 | cevrim/yil | dusuk | tahmin | teknik |  | tahmin |
| bat_cycles_per_year_B | B yillik esdeger tam cevrim | 60 | 20 – 150 | cevrim/yil | dusuk | tahmin | teknik |  | tahmin |
| bat_design_life_years | Hedef urun omru/garanti | 10 | 5 – 15 | yil | dusuk | tahmin | teknik |  | tahmin (pazar referansi: Anker 5 yil dogrulandi; Zendure 10 yil kaynak denetcisince dogrulandi) |
| bat_mech_per_cell_cyl_usd | Silindirik hucre basina paket PARCALARI (tutucu, serit, yalitim) | 0.08 | 0.04 – 0.18 | USD/hucre | dusuk | tahmin | adet |  | tahmin |
| bat_mech_per_cell_pris_usd | Prizmatik hucre basina paket parcalari (bara, yalitim, sikistirma payi) | 0.8 | 0.4 – 1.6 | USD/hucre | dusuk | tahmin | adet |  | tahmin |
| bat_enclosure_fixed_usd | Kutu sabit parca maliyeti (conta, kapak, valf) | 15 | 8 – 30 | USD/kutu | dusuk | tahmin | adet |  | tahmin |
| bat_enclosure_ref_usd | Kutu boyutla olceklenen maliyet (1 kWh referansta) | 20 | 10 – 50 | USD/kutu | dusuk | tahmin | adet |  | tahmin |
| bat_enclosure_exp | Kutu maliyeti olcekleme ussu | 0.85 | 0.67 – 1 | - | dusuk | tahmin | teknik |  | hesap/tahmin |
| bat_box_misc_usd | Kutu basina diger parcalar (DC konnektor, sigorta, rakor, kablo) | 12 | 6 – 25 | USD/kutu | dusuk | tahmin | adet |  | tahmin |
| bat_pack_mass_overhead_factor | Paket kutlesi / hucre kutlesi | 1.35 | 1.2 – 1.6 | - | dusuk | tahmin | teknik |  | tahmin |
| bat_pack_yield | Paket montaj verimi | 0.99 | 0.97 – 0.998 | - | dusuk | tahmin | teknik |  | tahmin |
| bat_eol_test_usd_per_box | Pil tarafi hat sonu testi (OCV, IR, izolasyon, koruma kesme kontrolu) | 1.5 | 0.5 – 4 | USD/kutu | dusuk | tahmin | adet |  | tahmin |
| bat_incoming_insp_usd_per_cell | Hucre giris muayenesi (yalniz satin alma yolunda) | 0.02 | 0.005 – 0.05 | USD/hucre | dusuk | tahmin | adet |  | tahmin |
| bat_pack_line_capex_usd | Paket montaj hatti yatirimi (ayiklama, kaynak, fikstur; EOL testi haric) | 250000 | 100000 – 600000 | USD/hat | dusuk | tahmin | zaman |  | tahmin |
| bat_pack_cells_per_h_cyl | Paket hatti hizi — silindirik | 400 | 200 – 900 | hucre/saat | dusuk | tahmin | teknik |  | tahmin |
| bat_pack_cells_per_h_pris | Paket hatti hizi — prizmatik | 60 | 30 – 120 | hucre/saat | dusuk | tahmin | teknik |  | tahmin |
| bat_pack_min_per_box | Kutu basina sabit montaj iscilik suresi (kapatma, kablaj, BMS baglantisi, etiket) | 15 | 8 – 30 | dk/kutu | dusuk | tahmin | zaman |  | tahmin |
| bat_pack_line_hours_yr | Paket hatti yillik calisma saati | 3600 | 3000 – 5500 | saat/yil | dusuk | tahmin | teknik |  | tahmin |
| bat_fte_hours_yr | FTE basina yillik calisma saati | 1800 | 1700 – 2200 | saat/yil | dusuk | tahmin | teknik | → `eco_productive_hours_fte_yr` | tahmin |
| bat_tooling_fixed_usd | Kutu ve tutucu kalip takimi — sabit kisim (tasarim basina) | 20000 | 8000 – 50000 | USD/tasarim | dusuk | tahmin | urun_sabit |  | tahmin |
| bat_tooling_ref_usd | Kalip takimi boyut terimi (1 kWh referansta) | 15000 | 5000 – 40000 | USD/tasarim | dusuk | tahmin | urun_sabit |  | tahmin |
| bat_warranty_reserve_frac | Garanti karsiligi (hucre + mekanik maliyetine oran) | 0.03 | 0.01 – 0.08 | - | dusuk | tahmin | adet |  | tahmin |
| bat_epr_fee_usd_per_kg | Genisletilmis uretici sorumlulugu / atik pil ucreti | 1 | 0.3 – 3 | USD/kg | dusuk | tahmin | adet |  | tahmin |
| bat_heater_usd_per_box | Isitici film + kontrol (opsiyonel, B) | 4 | 2 – 10 | USD/kutu | dusuk | tahmin | adet |  | tahmin |
| bat_line_cells_per_year | Kendi hucre hatti montaj/formasyon kapasitesi (K9) | 150000 | 100000 – 200000 | hucre/yil | orta | tahmin | teknik |  | Kullanici karari K9 |
| bat_line_capex_cyl_usd | Kendi hucre hatti yatirimi — 26700 (0.25 m kaplama makinesi, kuru oda dahil) | 2e+06 | 1e+06 – 4e+06 | USD | dusuk | tahmin | zaman |  | tahmin (olcek referansi: https://www.ess-news.com/2025/12/19/moll-batterien-garners-more-than-25-million-for-sodium-ion-battery-plant-in-ger |
| bat_line_capex_pris_usd | Kendi hucre hatti yatirimi — 50 Ah prizmatik (0.6 m kaplama makinesi) | 5e+06 | 2.5e+06 – 1e+07 | USD | dusuk | tahmin | zaman |  | tahmin |
| bat_coat_area_cyl_m2_yr | Kaplama kapasitesi — 26700 hatti (tek yuz gecis alani) | 108000 | 50000 – 250000 | m2/yil | dusuk | tahmin | teknik |  | tahmin |
| bat_coat_area_pris_m2_yr | Kaplama kapasitesi — prizmatik hat | 605000 | 300000 – 1.2e+06 | m2/yil | dusuk | tahmin | teknik |  | tahmin |
| bat_coat_side_factor | Hucre basina kaplanan yuz alani / tek yuz esdeger katot alani | 2.1 | 2 – 2.3 | - | orta | hesap_turetilmis | teknik |  | hesap |
| bat_line_life_years | Hat ekonomik omru | 7 | 5 – 10 | yil | dusuk | tahmin | zaman | → `eco_life_machine_yr` | tahmin |
| bat_line_maint_frac | Yillik bakim / yatirim | 0.05 | 0.03 – 0.08 | 1/yil | dusuk | tahmin | zaman | → `eco_maint_frac_capex_yr` | tahmin |
| bat_line_staff_fte_cyl | Hucre hatti personeli — 26700 | 12 | 8 – 20 | FTE | dusuk | tahmin | zaman |  | tahmin |
| bat_line_staff_fte_pris | Hucre hatti personeli — prizmatik | 16 | 10 – 24 | FTE | dusuk | tahmin | zaman |  | tahmin |
| bat_line_overhead_cyl_usd_yr | Hat genel giderleri — 26700 | 130000 | 60000 – 250000 | USD/yil | dusuk | tahmin | zaman |  | tahmin |
| bat_line_overhead_pris_usd_yr | Hat genel giderleri — prizmatik | 180000 | 90000 – 350000 | USD/yil | dusuk | tahmin | zaman |  | tahmin |
| bat_dryroom_power_cyl_kW | Kuru ortam surekli gucu — 26700 hatti | 60 | 30 – 120 | kW | dusuk | tahmin | zaman |  | tahmin |
| bat_dryroom_power_pris_kW | Kuru ortam surekli gucu — prizmatik hat | 90 | 45 – 180 | kW | dusuk | tahmin | zaman |  | tahmin |
| bat_prod_energy_kWh_per_kWh | Hucre uretim enerjisi (GWh olcek, SIB, kWh_cell basina) | 23 | 15 – 30 | kWh/kWh | orta | dogrulanmis_url | guc_enerji |  | https://www.nature.com/articles/s41560-023-01355-z |
| bat_degen_dryroom_share | Degen degerinde kuru odanin payi | 0.4 | 0.25 – 0.6 | - | dusuk | tahmin | teknik |  | tahmin |
| bat_areal_capacity_Ah_m2 | Katot alan kapasitesi (tek yuz) | 25 | 18 – 35 | Ah/m2 | dusuk | hafizadan_dogrulanmadi | teknik |  | hafiza (2-3.5 mAh/cm2) |
| bat_material_cost_own_lo_usd_Wh | Kendi uretimde malzeme — LO/sert karbon, 26700 (kucuk lot) | 0.075 | 0.055 – 0.11 | USD/Wh | dusuk | hesap_turetilmis | guc_enerji |  | https://www-old.metal.com/price/New-Energy/Sodium-ion-Battery + tahmin |
| bat_material_cost_own_nfpp_usd_Wh | Kendi uretimde malzeme — NFPP/sert karbon, 50 Ah prizmatik | 0.06 | 0.047 – 0.09 | USD/Wh | dusuk | hesap_turetilmis | guc_enerji |  | hesap + SMM malzeme fiyatlari |
| bat_cathode_price_nfm_usd_kg | NFM111 katot fiyati | 6.64 | 6.51 – 6.77 | USD/kg | orta | dogrulanmis_url | guc_enerji |  | https://www-old.metal.com/price/New-Energy/Sodium-ion-Battery |
| bat_cathode_price_nfpp_usd_kg | NFPP katot fiyati | 3.65 | 3.42 – 3.88 | USD/kg | orta | dogrulanmis_url | guc_enerji |  | https://www-old.metal.com/price/New-Energy/Sodium-ion-Battery |
| bat_hard_carbon_price_usd_kg | Sert karbon fiyati | 4.08 | 3.14 – 6.25 | USD/kg | orta | dogrulanmis_url | guc_enerji |  | https://www-old.metal.com/price/New-Energy/Sodium-ion-Battery |
| bat_hard_carbon_ice | Sert karbon ilk cevrim kulombik verimi (ICE) | 0.85 | 0.8 – 0.92 | - | orta | dogrulanmis_url | teknik |  | https://pmc.ncbi.nlm.nih.gov/articles/PMC9910041/ |
| bat_defect_density_per_m2 | Olumcul kusur yogunlugu (kendi hat, ilk yillar) | 0.05 | 0.005 – 0.3 | 1/m2 | dusuk | tahmin | teknik |  | tahmin |
| bat_yield_other | Alandan bagimsiz verim (formasyon, kacak, olcu) | 0.92 | 0.8 – 0.97 | - | dusuk | tahmin | teknik |  | tahmin |
| bat_formation_grading_time_h | Formasyon + derecelendirme kanal suresi | 30 | 15 – 60 | saat | dusuk | hafizadan_dogrulanmadi | zaman |  | hafiza (Li-iyon pratigi) |
| bat_aging_days | Yaslandirma (K-degeri) bekleme suresi | 7 | 3 – 21 | gun | dusuk | hafizadan_dogrulanmadi | zaman |  | hafiza |
| bat_channel_utilization | Formasyon kanal doluluk orani | 0.8 | 0.6 – 0.9 | - | dusuk | tahmin | teknik |  | tahmin |
| bat_own_cell_dev_usd | Kendi hucre gelistirme ve kalifikasyonu (tasarim, protokol, hucre UN38.3, guvenlik) | 1.5e+06 | 500000 – 4e+06 | USD | dusuk | tahmin | urun_sabit |  | tahmin |
| bat_own_dev_amort_years | Gelistirme maliyeti itfa suresi | 5 | 3 – 7 | yil | dusuk | tahmin | urun_sabit | → `eco_life_machine_yr` | tahmin |
| bat_un383_cost_usd_per_design | UN 38.3 testi (pil tasarimi basina) | 10000 | 5000 – 25000 | USD/tasarim | dusuk | tahmin | urun_sabit |  | tahmin |
| bat_safety_cert_cost_usd | Guvenlik (IEC 62619 analogu / VDE-AR-E 2510-50 / UL 1973) + AB Md.12 Ek V dokumani | 40000 | 15000 – 100000 | USD/urun ailesi | dusuk | tahmin | urun_sabit |  | tahmin |
| bat_n_designs | Ayri test ve kalip gerektiren kutu tasarimi sayisi | 2 | 1 – 4 | adet | dusuk | tahmin | urun_sabit |  | tahmin |
| bat_eu_passport_threshold_Wh | AB 2 kWh esigi (pasaport Md.77, performans Md.10, karbon Md.7) | 2000 | 2000 – 2000 | Wh | yuksek | standart_metni_dogrulanmis | teknik |  | https://publications.europa.eu/resource/celex/32023R1542 (EUR-Lex 32023R1542) |
| bat_eu_portable_mass_limit_kg | AB tasinabilir pil kutle siniri | 5 | 5 – 5 | kg | yuksek | standart_metni_dogrulanmis | teknik |  | https://publications.europa.eu/resource/celex/32023R1542 |
| bat_eu_threshold_margin | 2 kWh esigi icin tasarim payi | 0.9 | 0.85 – 0.95 | - | dusuk | tahmin | teknik |  | tahmin |

## Saha altyapısı, İSG ve ekonomi (`altyapi`) — 149 parametre

| id | ad | değer | aralık | birim | güven | kaynak türü | sınıf | eşdeğer | kaynak |
|---|---|---|---|---|---|---|---|---|---|
| eco_fx_try_per_usd | TRY/USD kuru (model baz) | 49 | 45 – 60 | TRY/USD | yuksek | dogrulanmis_url | teknik |  | https://www.tcmb.gov.tr/kurlar/today.xml ; https://finans.mynet.com/haber/detay/doviz/26-eylul-2026-dolar-bugun-kac-tl-serbest-piyasa-dolar- |
| eco_try_cost_real_drift_frac_yr | TL bazli maliyetlerin USD cinsinden yillik reel kaymasi | 0.03 | -0.05 – 0.1 | 1/yil | dusuk | tahmin | teknik |  | tahmin (kaynak yok) |
| eco_rf_usd | Risksiz USD faizi (ABD 10 yillik hazine, kisa donem ortalamasi) | 0.05 | 0.045 – 0.055 | 1/yil | orta | hesap_turetilmis | teknik |  | https://tradingeconomics.com/united-states/government-bond-yield ; https://hibya.com/eurobond-getirilerinde-yukselis-goruldu-1027379 |
| eco_tr_erp | Turkiye hisse risk primi (Damodaran) | 0.0889 | 0.07 – 0.11 | 1/yil | yuksek | dogrulanmis_url | teknik |  | https://pages.stern.nyu.edu/~adamodar/New_Home_Page/datafile/ctryprem.html |
| eco_tr_eurobond_usd_10y | Turkiye USD Eurobond getirisi (2036 vade) | 0.071 | 0.065 – 0.08 | 1/yil | yuksek | dogrulanmis_url | teknik |  | https://hibya.com/eurobond-getirilerinde-yukselis-goruldu-1027379 |
| eco_kd_spread | Sirket borcunun Eurobond ustu marji | 0.02 | 0.015 – 0.04 | 1/yil | dusuk | tahmin | teknik |  | tahmin (kaynak yok) |
| eco_beta_equity | Oz kaynak betasi | 1.15 | 1 – 1.3 | - | dusuk | tahmin | teknik |  | tahmin (kaynak yok) |
| eco_equity_frac | Oz kaynak orani (E/(D+E)) | 0.6 | 0.5 – 0.7 | - | dusuk | tahmin | teknik |  | tahmin (kaynak yok) |
| eco_wacc_usd | USD bazli vergi sonrasi agirlikli sermaye maliyeti (iskonto orani) | 0.12 | 0.09 – 0.2 | 1/yil | orta | hesap_turetilmis | teknik |  | altyapi: eco_rf_usd, eco_tr_erp (Damodaran), eco_tr_eurobond_usd_10y, eco_kd_spread, eco_beta_equity, eco_equity_frac, eco_corporate_tax_rat |
| eco_corporate_tax_rate | Kurumlar vergisi orani (imalat kazanci, 2027 sonrasi) | 0.125 | 0.125 – 0.25 | - | orta | dogrulanmis_url | teknik |  | https://taxsummaries.pwc.com/turkey/corporate/taxes-on-corporate-income |
| eco_dep_life_tax_machine_yr | Vergisel amortisman suresi, makine | 8 | 5 – 10 | yil | dusuk | tahmin | teknik |  | tahmin (altyapi; VUK amortisman listesi dogrulanmadi) |
| eco_dep_life_tax_infra_yr | Vergisel amortisman suresi, tesisat/altyapi | 12 | 10 – 25 | yil | dusuk | tahmin | teknik |  | tahmin (altyapi) |
| eco_life_machine_yr | Makine ekonomik omru | 8 | 5 – 12 | yil | dusuk | tahmin | teknik |  | tahmin (altyapi) |
| eco_life_infra_yr | Saha altyapisi ekonomik omru | 12 | 8 – 20 | yil | dusuk | tahmin | teknik |  | tahmin (altyapi) |
| eco_maint_frac_capex_yr | Yillik bakim (capex orani) | 0.04 | 0.02 – 0.08 | 1/yil | dusuk | tahmin | teknik |  | tahmin (altyapi; kristal, hucre, modul, pil degerleri de tahmin) |
| eco_insurance_frac_capex_yr | Yillik sigorta (deprem teminati dahil) | 0.006 | 0.003 – 0.012 | 1/yil | dusuk | tahmin | teknik |  | tahmin (altyapi) |
| eco_hours_calendar_yr | Takvim saati | 8760 | 8760 – 8760 | h/yil | yuksek | hesap_turetilmis | teknik |  | 365 x 24 |
| eco_uptime_frac_default | Varsayilan zaman kullanilabilirligi | 0.9 | 0.8 – 0.95 | - | dusuk | tahmin | teknik |  | tahmin (altyapi) |
| eco_scale_exponent | Kapasite-maliyet olcek ussu (0.6 kurali) | 0.6 | 0.4 – 0.8 | - | orta | hafizadan_dogrulanmadi | teknik |  | Muhendislik maliyet tahmininde 0.6 kurali |
| eco_elec_energy_kr_kwh | Duzenlenmis sanayi tek zamanli aktif enerji bedeli (AG ve OG) | 290.969 | 285 – 330 | kurus/kWh | yuksek | dogrulanmis_url | teknik |  | https://www.aa.com.tr/tr/enerjiterminali/elektrik/epdk-2026-yekdem-maliyetlerini-revize-etti/56138 |
| eco_elec_dist_og_kr_kwh | Sanayi OG tek terimli dagitim bedeli | 118.246 | 108.27 – 125 | kurus/kWh | orta | dogrulanmis_url | teknik |  | https://www.hakedis.org/endeksler/epdk-elektrik-farturasi-vergi-ve-tarifeler |
| eco_elec_ptf_try_mwh | Piyasa takas fiyati (PTF), yillik ortalama vekili | 3634.98 | 2700 – 4500 | TL/MWh | dusuk | dogrulanmis_url | teknik |  | https://www.enerjigunlugu.net/spot-elektrik-fiyati-26-08-2026-icin-3634-98-tl-69541h.htm |
| eco_elec_yekdem_try_mwh | YEKDEM birim maliyeti (ortalama) | 372.4 | 189.15 – 602.51 | TL/MWh | orta | hesap_turetilmis | teknik |  | https://www.aa.com.tr/tr/enerjiterminali/elektrik/epdk-2026-yekdem-maliyetlerini-revize-etti/56138 |
| eco_elec_supplier_margin_frac | SKTT katsayisi veya ikili anlasma tedarikci marji | 0.05 | 0 – 0.1 | - | dusuk | hafizadan_dogrulanmadi | teknik |  | hafizadan (SKTT formulu (PTF+YEKDEM)*(1+K); K degeri dogrulanmadi) |
| eco_elec_tax_frac | Elektrik tuketim vergisi (BTV) ve fon orani, sanayi | 0.01 | 0.01 – 0.02 | - | orta | hafizadan_dogrulanmadi | teknik |  | hafizadan (sanayi BTV %1; enerji fonu durumu dogrulanmadi) |
| eco_elec_sktt_limit_kwh_yr | Son kaynak tedarik tarifesi (SKTT) tuketim limiti, mesken disi | 15000 | 15000 – 1.5e+07 | kWh/yil | dusuk | dogrulanmis_url | teknik |  | https://apollo.eco/tr/nisan-2026-guncellenen-elektrik-tarifesi-analizi/ |
| eco_elec_price_usd_kwh | Sanayi elektrik fiyati (OG, baz: piyasa bazli; vergiler dahil, KDV haric) | 0.105 | 0.084 – 0.14 | USD/kWh | orta | tahmin | teknik |  | altyapi: eco_elec_ptf_try_mwh (enerjigunlugu 26.08.2026), eco_elec_yekdem_try_mwh, eco_elec_dist_og_kr_kwh (hakedis.org), eco_elec_energy_kr |
| eco_water_isu_sanayi_usd_m3 | ISU sanayi su + atiksu bedeli (OSB disi) | 6.33 | 6.33 – 7 | USD/m3 | yuksek | dogrulanmis_url | teknik |  | https://www.isu.gov.tr/sufiyatlari |
| eco_water_isu_osb_usd_m3 | ISU su bedeli, ortak aritma tesisi olan OSB kategorisi | 4.22 | 4.22 – 4.6 | USD/m3 | yuksek | dogrulanmis_url | teknik |  | https://www.isu.gov.tr/sufiyatlari |
| eco_osb_wastewater_fee_usd_m3 | OSB ortak aritma (atiksu) bedeli | 1 | 0.3 – 3 | USD/m3 | dusuk | tahmin | teknik |  | tahmin (kaynak yok) |
| eco_water_price_usd_m3 | Sanayi su + atiksu toplam bedeli (baz: ortak aritmali OSB) | 5.22 | 3 – 6.33 | USD/m3 | orta | hesap_turetilmis | teknik |  | https://www.isu.gov.tr/sufiyatlari + eco_osb_wastewater_fee_usd_m3 (tahmin) |
| eco_rent_usd_m2_month | Gebze/Dilovasi OSB fabrika kira bedeli | 6.5 | 4 – 10 | USD/m2/ay | dusuk | hesap_turetilmis | teknik |  | https://www.century21.com.tr/gebze-kiralik/fabrika-imalathane |
| eco_rent_tax_factor | Kira vergi carpani (stopaj vb.) | 1 | 1 – 1.25 | - | dusuk | hafizadan_dogrulanmadi | teknik |  | hafizadan (sahis mulkunde %20 stopaj brut kirayi netin 1/0.8 katina cikarir; dogrulanmadi) |
| eco_min_wage_employer_cost_try_month | 2026 asgari ucret isveren maliyeti (imalat 5 puan tesvikli) | 39223.1 | 37953.1 – 40874.6 | TRY/ay | yuksek | dogrulanmis_url | teknik |  | https://www.alomaliye.com/2025/12/23/2026-yili-asgari-ucreti-2026-yili-asgari-ucret-bilgilendirme/ |
| eco_sgk_employer_factor | Isveren SGK + issizlik carpani (brut uzerine) | 1.1875 | 1.1875 – 1.2375 | - | yuksek | dogrulanmis_url | teknik |  | https://www.alomaliye.com/2025/12/23/2026-yili-asgari-ucreti-2026-yili-asgari-ucret-bilgilendirme/ |
| eco_labor_overhead_factor | Isveren maliyeti uzerine ek yuk carpani | 1.25 | 1.15 – 1.45 | - | dusuk | tahmin | teknik |  | tahmin (kaynak yok) |
| eco_productive_hours_fte_yr | Tam zamanli calisan basina yillik verimli saat | 2070 | 1950 – 2200 | h/yil | orta | hesap_turetilmis | teknik |  | https://www.mevzuat.gov.tr/MevzuatMetin/1.5.4857.pdf (md. 63, 53) |
| eco_fte_per_24x7_position | 24/7 pozisyon basina FTE maliyet esdegeri | 4.23 | 3.98 – 4.49 | FTE | orta | hesap_turetilmis | teknik |  | https://www.mevzuat.gov.tr/MevzuatMetin/1.5.4857.pdf (md. 63, 53, 41, 69) |
| eco_labor_operator_usd_h | Operator tam yuklu saat maliyeti (Kocaeli) | 8.4 | 5.8 – 11.5 | USD/h | orta | hesap_turetilmis | teknik |  | https://www.eleman.net/meslek/operator/maas ; https://www.alomaliye.com/2025/12/23/2026-yili-asgari-ucreti-2026-yili-asgari-ucret-bilgilendi |
| eco_labor_technician_usd_h | Teknisyen tam yuklu saat maliyeti (Kocaeli) | 13.4 | 10 – 18 | USD/h | orta | hesap_turetilmis | teknik |  | https://www.eleman.net/meslek/teknisyen/maas |
| eco_labor_engineer_usd_h | Muhendis tam yuklu saat maliyeti | 22 | 12 – 35 | USD/h | dusuk | tahmin | teknik |  | https://www.eleman.net/meslek/muhendis/maas + tahmin |
| eco_price_argon_bulk_usd_kg | Argon toptan/endeks fiyati | 0.68 | 0.55 – 0.9 | USD/kg | orta | hesap_turetilmis | teknik |  | https://www.imarcgroup.com/argon-pricing-report ; https://businessanalytiq.com/procurementanalytics/index/argon-price-index/ ; https://www.i |
| eco_argon_small_user_premium_frac | Kucuk kullanici teslim primi (argon) | 0.6 | 0.2 – 3 | - | dusuk | tahmin | teknik |  | tahmin (kaynak yok) |
| eco_price_argon_usd_kg | Sivi argon teslim fiyati (kucuk kullanici) | 1.1 | 0.66 – 3 | USD/kg | dusuk | hesap_turetilmis | teknik |  | eco_price_argon_bulk_usd_kg (https://www.imarcgroup.com/argon-pricing-report ; https://businessanalytiq.com/procurementanalytics/index/argon |
| eco_argon_tank_rent_usd_month | Sivi argon tanki + evaporator kirasi | 1200 | 400 – 3000 | USD/ay | dusuk | tahmin | teknik |  | tahmin (kaynak yok) |
| eco_price_ln2_usd_nm3 | Dokme sivi azot fiyati | 0.15 | 0.07 – 0.35 | USD/Nm3 | dusuk | tahmin | teknik |  | tahmin (altyapi) |
| eco_price_sih4_usd_kg | Monosilan fiyati (silindir, Turkiye'ye teslim) | 60 | 25 – 300 | USD/kg | dusuk | tahmin | teknik |  | tahmin (altyapi, hucre) |
| eco_price_nf3_usd_kg | NF3 fiyati | 40 | 20 – 100 | USD/kg | dusuk | tahmin | teknik |  | tahmin (altyapi) |
| eco_price_h2_usd_kg | Hidrojen fiyati (5.0, silindir/demet) | 25 | 4 – 60 | USD/kg | dusuk | tahmin | teknik |  | tahmin (altyapi, hucre) |
| eco_price_dopant_mix_usd_per_cyl | Katki gazi karisim silindiri (PH3 veya B2H6/TMB, %0.5-2, H2 icinde) | 3000 | 1000 – 8000 | USD/silindir | dusuk | tahmin | teknik |  | tahmin (altyapi) |
| eco_cyl_rent_usd_day | Gaz silindiri/demet kirasi | 2 | 0.5 – 5 | USD/gun/silindir | dusuk | tahmin | teknik |  | tahmin (kaynak yok) |
| eco_dopant_cyl_shelf_life_months | Katki gazi karisiminin raf omru | 12 | 6 – 24 | ay | dusuk | hafizadan_dogrulanmadi | teknik |  | hafizadan (B2H6 karisimlari zamanla bozunur; sure dogrulanmadi) |
| eco_price_lime_usd_kg | Sonmus kirec Ca(OH)2 fiyati | 0.2 | 0.1 – 0.4 | USD/kg | dusuk | tahmin | teknik |  | tahmin (kaynak yok) |
| eco_nre_machine_design_usd | Unite makinelerinin tasarim + prototip NRE'si | 5e+06 | 2e+06 – 1.5e+07 | USD | dusuk | tahmin | urun_sabit |  | tahmin (kaynak yok) |
| eco_learning_rate_unit_copy | Kopya unitede capex ogrenme orani (her iki katina cikista maliyet carpani) | 0.9 | 0.8 – 0.97 | - | dusuk | tahmin | teknik |  | tahmin (kaynak yok) |
| eco_foak_premium_frac | Ilk unite (FOAK) capex asimi | 0.3 | 0.1 – 1 | - | dusuk | tahmin | teknik |  | tahmin (kaynak yok) |
| eco_rampup_months | Unite rampa suresi | 12 | 6 – 24 | ay | dusuk | tahmin | teknik |  | tahmin (kaynak yok) |
| eco_rampup_avg_output_frac | Rampa suresince ortalama cikti orani | 0.5 | 0.3 – 0.7 | - | dusuk | tahmin | teknik |  | tahmin (kaynak yok) |
| eco_working_capital_days | Isletme sermayesi (stok + alacak - borc) gun sayisi | 90 | 45 – 180 | gun | dusuk | tahmin | teknik |  | tahmin (kaynak yok) |
| site_pga_dd2_g | Gebze tasarim depremi (DD-2, 475 yil) en buyuk yer ivmesi | 0.45 | 0.35 – 0.6 | g | orta | hesap_turetilmis | teknik |  | https://dergipark.org.tr/tr/download/article-file/208599 + arama ozeti (Kocaeli Gazetesi; sayfa 403, acilamadi) |
| site_seismic_capex_frac | Sismik onlemler ek capex orani | 0.03 | 0.01 – 0.08 | - | dusuk | tahmin | teknik |  | tahmin (kaynak yok) |
| site_area_per_unit_m2 | Unite basina kapali alan | 2500 | 1500 – 5000 | m2 | dusuk | tahmin | zaman |  | tahmin (kaynak yok) |
| site_area_shared_fixed_m2 | Saha paylasilan alani, sabit kisim (gaz odasi, kimyasal depo, lab, ofis) | 600 | 300 – 1500 | m2 | dusuk | tahmin | saha_sabit |  | tahmin (kaynak yok) |
| site_area_shared_per_unit_m2 | Saha paylasilan alani, unite basina artan kisim (UPW, AAT, sogutma) | 100 | 50 – 300 | m2/unite | dusuk | tahmin | saha_sabit |  | tahmin (kaynak yok) |
| site_clear_height_min_m | Gerekli net tavan yuksekligi (firin bolumu) | 9 | 7 – 14 | m | dusuk | tahmin | teknik |  | tahmin (kaynak yok) |
| site_floor_load_req_kN_m2 | Firin bolgesi gerekli doseme tasima kapasitesi | 30 | 15 – 60 | kN/m2 | dusuk | tahmin | teknik |  | tahmin (kaynak yok) |
| site_upw_resistivity_min_Mohm_cm | UPW ozdirenc gereksinimi (HJT temizlik/dokulama) | 17 | 15 – 18.18 | MOhm.cm | dusuk | tahmin | teknik |  | https://en.wikipedia.org/wiki/Ultrapure_water (fiziksel ust sinir) + tahmin |
| site_upw_l_per_m2 | Wafer alanina bagli degisken UPW tuketimi | 120 | 30 – 400 | L/m2 | dusuk | tahmin | teknik |  | tahmin (kaynak yok) |
| site_upw_fixed_lph_per_unit | Unite basina sabit UPW debisi (tank tasmasi/bekleme) | 500 | 150 – 2000 | L/h | dusuk | tahmin | teknik |  | tahmin (kaynak yok) |
| site_ro_recovery_frac | Ters ozmoz (RO) geri kazanim orani | 0.75 | 0.6 – 0.85 | - | dusuk | hafizadan_dogrulanmadi | teknik |  | hafizadan |
| site_upw_kwh_per_m3 | UPW uretim + dagitim ozgul enerjisi | 2 | 1 – 4 | kWh/m3 | dusuk | tahmin | teknik |  | tahmin (kaynak yok) |
| site_upw_module_cap_m3h | UPW referans modul kapasitesi | 3 | 1 – 6 | m3/h | dusuk | tahmin | teknik |  | tahmin (kaynak yok) |
| site_upw_module_capex_usd | UPW referans modul capex (RO+EDI+parlatma dongusu) | 250000 | 120000 – 450000 | USD/modul | dusuk | tahmin | teknik |  | tahmin (kaynak yok) |
| site_wwt_module_cap_m3h | AAT referans modul kapasitesi | 4 | 1 – 8 | m3/h | dusuk | tahmin | teknik |  | tahmin (kaynak yok) |
| site_wwt_module_capex_usd | HF/CaF2 + notralizasyon + filtre pres AAT modul capex | 200000 | 100000 – 450000 | USD/modul | dusuk | tahmin | teknik |  | tahmin (kaynak yok) |
| site_wwt_frac_of_upw | AAT'ye giden atiksu / UPW tuketimi | 0.95 | 0.8 – 1 | - | dusuk | tahmin | teknik |  | tahmin (kaynak yok) |
| site_kerf_ww_l_per_wafer | Tel testere ve kesim sonrasi temizlik atiksuyu | 1 | 0.3 – 5 | L/wafer | dusuk | tahmin | teknik |  | tahmin (kaynak yok) |
| site_si_sludge_disposal_usd_t | Si kerf camuru bertaraf/geri kazanim bedeli | 100 | 0 – 300 | USD/t yas | dusuk | tahmin | teknik |  | tahmin (kaynak yok) |
| site_trafo_module_kva | Trafo + OG hucre referans modul | 2000 | 1000 – 3150 | kVA | dusuk | tahmin | teknik |  | tahmin (kaynak yok) |
| site_trafo_module_capex_usd | Trafo + OG hucre modul capex | 120000 | 60000 – 200000 | USD/modul | dusuk | tahmin | teknik |  | tahmin (kaynak yok) |
| site_kva_per_kw_avg | Ortalama yuk basina kurulu trafo gucu | 1.6 | 1.3 – 2.2 | kVA/kW | dusuk | tahmin | teknik |  | tahmin (kaynak yok) |
| site_genset_module_kva | Jenerator referans modul | 1000 | 500 – 2000 | kVA | dusuk | tahmin | teknik |  | tahmin (kaynak yok) |
| site_genset_capex_usd_kva | Dizel jenerator + ATS kurulu maliyeti | 200 | 120 – 350 | USD/kVA | dusuk | tahmin | teknik |  | tahmin (kaynak yok) |
| site_cooling_module_mwth | Kuru sogutucu referans modul | 1 | 0.5 – 2 | MWth | dusuk | tahmin | teknik |  | tahmin (kaynak yok) |
| site_cooling_module_capex_usd | Kuru sogutucu + pompa + tampon tank modul capex | 120000 | 60000 – 250000 | USD/modul | dusuk | tahmin | teknik |  | tahmin (kaynak yok) |
| site_heat_to_water_frac | Unite isisinin sogutma suyuna giden orani | 0.6 | 0.4 – 0.8 | - | dusuk | tahmin | teknik |  | tahmin (kaynak yok) |
| site_heat_to_air_frac | Unite isisinin oda havasina giden orani (HVAC yuku) | 0.3 | 0.15 – 0.5 | - | dusuk | tahmin | teknik |  | tahmin (kaynak yok) |
| site_cda_nm3_min_per_unit | Unite basina basincli hava talebi | 4 | 2 – 8 | Nm3/dk | dusuk | tahmin | teknik |  | tahmin (kaynak yok) |
| site_cda_module_nm3_min | Kompresor + kurutucu referans modul | 10 | 5 – 20 | Nm3/dk | dusuk | tahmin | teknik |  | tahmin (kaynak yok) |
| site_cda_module_capex_usd | Kompresor + kurutucu modul capex | 60000 | 30000 – 120000 | USD/modul | dusuk | tahmin | teknik |  | tahmin (kaynak yok) |
| site_scrubber_module_m3h | Merkezi asit/alkali egzoz yikayici referans modul | 15000 | 5000 – 30000 | m3/h | dusuk | tahmin | teknik |  | tahmin (kaynak yok) |
| site_acid_scrubber_capex_usd_per_1000m3h | Merkezi yikayici birim capex | 8000 | 4000 – 15000 | USD/(1000 m3/h) | dusuk | tahmin | teknik |  | tahmin (kaynak yok) |
| site_gas_set_units_per_set | Bir gaz kabini setinin besleyebildigi unite sayisi | 4 | 2 – 8 | unite/set | dusuk | tahmin | teknik |  | tahmin (kaynak yok) |
| site_f_discharge_limit_mg_l | Florur desarj siniri (tasarim hedefi) | 15 | 5 – 20 | mg/L | orta | standart_metni_dogrulanmis | teknik |  | https://web.deu.edu.tr/atiksu/ana39/skkypdf.pdf (Su Kirliligi Kontrolu Yonetmeligi) |
| site_caf2_kg_per_kg_hf | HF basina CaF2 camuru (kuru) | 1.951 | 1.951 – 1.951 | kg/kg | yuksek | hesap_turetilmis | teknik |  | Stokiyometri: 2HF + Ca(OH)2 -> CaF2 + 2H2O |
| site_lime_kg_per_kg_hf | HF basina kirec tuketimi | 2.4 | 1.9 – 2.8 | kg/kg | orta | hesap_turetilmis | teknik |  | Stokiyometri + fazlalik (tahmin) |
| site_sludge_solids_frac | Filtre pres keki kuru madde orani | 0.4 | 0.25 – 0.6 | - | dusuk | tahmin | teknik |  | tahmin (kaynak yok) |
| site_sludge_disposal_usd_t | CaF2 camuru bertaraf/degerlendirme bedeli | 150 | 50 – 400 | USD/t yas | dusuk | tahmin | teknik |  | tahmin (kaynak yok) |
| site_h2_l_per_g_si_etched | Alkali ortamda asindirilan Si basina H2 | 1.596 | 1.596 – 1.596 | L(0 C, 1 atm)/g Si | yuksek | hesap_turetilmis | teknik |  | Stokiyometri: Si + 2OH- + H2O -> SiO3(2-) + 2H2 |
| site_sih4_lfl_frac | Silan alt yanicilik siniri (havada, tasarim degeri) | 0.01 | 0.01 – 0.014 | hacim orani | orta | dogrulanmis_url | teknik |  | https://sesha.org/wp-content/uploads/2019/11/Silane-Abatement-Considerations.pdf |
| site_h2_lfl_frac | Hidrojen alt yanicilik siniri (havada) | 0.04 | 0.04 – 0.04 | hacim orani | yuksek | dogrulanmis_url | teknik |  | https://sesha.org/wp-content/uploads/2019/11/Silane-Abatement-Considerations.pdf |
| site_dilution_lfl_target_frac | Egzozda hedef yanici konsantrasyon (LFL orani) | 0.25 | 0.1 – 0.25 | - | orta | hafizadan_dogrulanmadi | teknik |  | Yaygin endustri uygulamasi (hafizadan) |
| site_n_gas_cabinets | Saha gaz kabini sayisi (HJT) | 5 | 4 – 7 | adet | dusuk | tahmin | teknik |  | tahmin (kaynak yok) |
| site_gas_cabinet_capex_usd | Otomatik gaz kabini (2 silindirli, purge, asiri akis, alev dedektoru) | 45000 | 15000 – 120000 | USD/adet | dusuk | tahmin | teknik |  | tahmin (kaynak yok) |
| site_vmb_capex_usd | Valf manifold kutusu (VMB) + hat, gaz basina unite dagitimi | 15000 | 6000 – 30000 | USD/gaz/unite | dusuk | tahmin | teknik |  | tahmin (kaynak yok) |
| site_tgm_fixed_capex_usd | Merkezi gaz izleme, alarm, acil durdurma (EMO), guvenlik yukleri acil gucu | 120000 | 50000 – 250000 | USD | dusuk | tahmin | saha_sabit |  | tahmin (kaynak yok) |
| site_tgm_point_capex_usd | Gaz dedektor noktasi (unite ici) | 5000 | 2000 – 10000 | USD/nokta | dusuk | tahmin | teknik |  | tahmin (kaynak yok) |
| site_pou_abatement_capex_usd | Yakma-islak (burn-wet) POU abatement, tek girisli | 120000 | 40000 – 250000 | USD/cihaz | dusuk | tahmin | teknik |  | tahmin (fiyat); teknik gerekce: https://sesha.org/wp-content/uploads/2019/11/Silane-Abatement-Considerations.pdf |
| site_pou_inlets_per_unit | POU cihazi basina giris sayisi | 2 | 1 – 4 | giris/cihaz | dusuk | hafizadan_dogrulanmadi | teknik |  | hafizadan (cok girisli yakma-islak cihazlar ticari olarak mevcut; dogrulanmadi) |
| site_pou_capex_per_extra_inlet_frac | Ek giris basina POU capex artisi | 0.25 | 0.1 – 0.5 | - | dusuk | tahmin | teknik |  | tahmin (kaynak yok) |
| site_pou_abatement_opex_usd_yr | POU abatement isletme maliyeti | 20000 | 8000 – 50000 | USD/yil/cihaz | dusuk | tahmin | teknik |  | tahmin (kaynak yok) |
| site_exhaust_fan_kw_per_1000m3h | Egzoz fan gucu | 0.7 | 0.4 – 1.5 | kW/(1000 m3/h) | orta | hesap_turetilmis | teknik |  | P = Q*dp/eta |
| site_makeup_air_kwh_e_per_m3h_yr | Egzozla atilan havanin yerine taze hava sartlandirma enerjisi | 10 | 5 – 20 | kWh_e/((m3/h).yil) | dusuk | hesap_turetilmis | teknik |  | Isi dengesi + Gebze isitma derece-gun ~1900 (hafizadan) |
| site_minienv_iso_class | Wafer yolu mini-ortam ISO sinifi | 6 | 5 – 7 | ISO 14644-1 sinif | dusuk | tahmin | teknik |  | tahmin (kaynak yok) |
| site_ffu_w_per_m2 | FFU gucu, FFU yuzeyi basina (0.45 m/s) | 100 | 85 – 130 | W/m2 | orta | dogrulanmis_url | teknik |  | https://www.hepacleanroomfilter.com/product/en/equipment-fan-filter-unit.html |
| site_ffu_coverage_frac | Mini-ortam tavaninda FFU kaplama orani | 0.9 | 0.8 – 1 | - | orta | hafizadan_dogrulanmadi | teknik |  | hafizadan (mini-ortamlar tek yonlu akisla calisir); oda referansi https://terrapincg.com/news/cleanroom-construction-cost-per-square-foot-20 |
| site_minienv_capex_usd_m2 | Mini-ortam capex (FFU + kabin + kontrol), taban alani basina | 3000 | 1200 – 7000 | USD/m2 | dusuk | tahmin | teknik |  | tahmin; ust referans https://terrapincg.com/news/cleanroom-construction-cost-per-square-foot-2026 |
| site_cda_kwh_per_nm3 | Basincli hava ozgul enerjisi (7 bar, kurutulmus) | 0.12 | 0.1 – 0.16 | kWh/Nm3 | dusuk | hafizadan_dogrulanmadi | teknik |  | hafizadan |
| site_cooling_kwe_per_kwth | Suya atilan isi basina sogutma elektrigi (kuru sogutucu/kule) | 0.04 | 0.02 – 0.25 | kWe/kWth | dusuk | tahmin | teknik |  | tahmin (kaynak yok) |
| site_hvac_kwe_per_kwth | Oda havasina giden isi basina HVAC elektrigi | 0.25 | 0.17 – 0.35 | kWe/kWth | dusuk | hafizadan_dogrulanmadi | teknik |  | COP 3-6 (hafizadan) |
| site_hvac_capex_usd_per_kwth | HVAC (chiller + klima santrali) capex, oda isi yuku basina | 500 | 250 – 1000 | USD/kWth | dusuk | tahmin | teknik |  | tahmin (kaynak yok) |
| site_ups_capex_usd_kva | UPS (kontrol/PLC/vakum/cekme ve rotasyon suruculeri, 10-15 dk) | 400 | 250 – 700 | USD/kVA | dusuk | tahmin | teknik |  | tahmin (kaynak yok) |
| site_melt_t_onset_s | Isitici kesildiginde ergiyikte donmanin baslamasina kadar gecen sure | 60 | 30 – 120 | s | dusuk | hesap_turetilmis | teknik |  | https://en.wikipedia.org/wiki/Silicon + enerji dengesi |
| site_melt_frac_solid_crit | Geri donussuz kampanya kaybina yol acan katilasma orani | 0.2 | 0.05 – 0.5 | - | dusuk | tahmin | teknik |  | tahmin (kaynak yok) |
| site_grid_outage_events_yr | Kampanya kaybi esigini asan uzun sebeke kesintisi sayisi | 2 | 0.5 – 10 | 1/yil | dusuk | tahmin | teknik |  | tahmin (kaynak yok) |
| site_voltage_sag_events_yr | Gerilim cokmesi ve kisa kesinti sayisi | 15 | 3 – 50 | 1/yil | dusuk | hafizadan_dogrulanmadi | teknik |  | hafizadan (OG sanayi sebekelerinde yilda onlarca cokme tipik; dogrulanmadi) |
| site_p_structure_loss_per_sag | Govde buyumesi sirasinda bir cokmenin yapi kaybina yol acma olasiligi | 0.3 | 0.05 – 1 | - | dusuk | tahmin | teknik |  | tahmin (kaynak yok) |
| site_seveso_ph3_lower_t | BEKRA/Seveso III fosfin alt esigi | 0.2 | 0.2 – 0.2 | t | orta | dogrulanmis_url | teknik |  | https://www.legislation.gov.uk/uksi/2015/483/schedule/1 ; TR: https://www.resmigazete.gov.tr/eskiler/2019/03/20190302-1.htm |
| site_seveso_flam_gas_lower_t | BEKRA/Seveso III P2 yanici gaz alt esigi (silan, TMB) | 10 | 10 – 10 | t | orta | dogrulanmis_url | teknik |  | https://www.legislation.gov.uk/uksi/2015/483/schedule/1 |
| site_sprinkler_area_threshold_m2 | Parlayici madde bulunan yapida sprinkler zorunluluk esigi | 1000 | 1000 – 1000 | m2 | yuksek | standart_metni_dogrulanmis | teknik |  | https://www.mevzuat.gov.tr/MevzuatMetin/21.5.200712937.pdf (Binalarin Yangindan Korunmasi Hakkinda Yonetmelik, md. 96(2)e) |
| site_sprinkler_capex_usd_m2 | Sprinkler sistemi capex (unite alani basina) | 35 | 20 – 60 | USD/m2 | dusuk | tahmin | teknik |  | tahmin (kaynak yok) |
| site_flam_liquid_max_l_per_m2 | Fabrika binasinda tecritli yanici sivi depolama yogunlugu (en fazla 50 m2 alan) | 350 | 70 – 350 | L/m2 | yuksek | standart_metni_dogrulanmis | teknik |  | https://www.mevzuat.gov.tr/MevzuatMetin/21.5.200712937.pdf (md. 118(3), Ek-12/B) |
| site_batt_fire_capex_usd_per_unit | Pil formasyon/yaslandirma yangin bolmesi, algilama, sondurme; elektrolit dolum ATEX | 80000 | 30000 – 250000 | USD/unite | dusuk | tahmin | teknik |  | tahmin (kaynak yok) |
| site_batt_nmp_recovery_capex_usd | NMP geri kazanimi ve maruziyet kontrolu (yalniz PVDF/NMP secilirse) | 150000 | 60000 – 400000 | USD/unite | dusuk | tahmin | teknik |  | tahmin (kaynak yok) |
| site_chem_dist_capex_usd_per_unit | Unite ici kimyasal dagitim (HF, KOH, H2O2, HCl vb.) | 40000 | 15000 – 100000 | USD/unite | dusuk | tahmin | teknik |  | tahmin (kaynak yok) |
| site_fixed_capex_usd | Saha gercek sabit capex (N'den bagimsiz) | 860000 | 450000 – 1.9e+06 | USD | dusuk | tahmin | saha_sabit |  | tahmin (kalem toplami) |
| site_fixed_opex_usd_yr | Saha sabit isletme gideri (personel, OSGB, analiz, kalibrasyon, izin) | 180000 | 90000 – 350000 | USD/yil | dusuk | tahmin | saha_sabit |  | tahmin + eco_labor_* uzerinden kaba hesap |
| site_fixed_opex_step_usd_yr | Her 4 ek unite icin ek saha personeli | 29000 | 20000 – 45000 | USD/yil/adim | dusuk | tahmin | saha_sabit |  | tahmin (1 FTE teknisyen) |
| eco_usd_inflation_frac_yr | USD enflasyonu (reel/nominal donusum) | 0.0234 | 0.015 – 0.035 | 1/yil | orta | dogrulanmis_url | teknik |  | https://fred.stlouisfed.org/series/T10YIE (fredgraph.csv) ; https://fred.stlouisfed.org/series/T5YIFR |
| eco_maint_first_gen_extra_frac_yr | Ilk nesil kendi tasarim makinelerde ek bakim | 0.035 | 0 – 0.04 | 1/yil | dusuk | tahmin | teknik |  | tahmin; dayanak altyapi eco_maint_frac_capex_yr notu |
| eta_cell | Hucre verimi eta_cell (hucre / modul / wafer / altyapi / kristal) | 0.22 | 0.19 – 0.26 | - | dusuk | hesap_turetilmis | teknik |  | Hucre f_eta_cell ve Tablo 1: baslangic (eta_core 22.5, w_eq 0.75) a=50-210 mm'de %21.2-22.2; olgun B-arka %24.8-25.8, D %25.6-26.0; cell_eta |
| mod_ctm_power_calc | Hucreden module guc orani CTM | 0.974 | 0.956 – 0.992 | - | dusuk | hesap_turetilmis | teknik |  | Modul mod_f_ctm_calc / mod_f_design_loop: 60 V dalinda 50 W 0.992 ... 300 W 0.974 ... 500 W 0.964; 35 V dalinda 0.956-0.988; optik bilesen 1 |
| N_s_max | Seri hucre tavani N_s_max (60 V SELV) | 64 | 64 – 72 | adet | orta | hesap_turetilmis | teknik |  | IEC 60364-7-712:2017 712.414.101 ve Ek B.1; hesap: min(floor(60 / (1.2 x 0.745 x 1.03)) = 65, floor(60 / (1.2 x 0.77)) = 64) = 64 |
| wf_break_cell_ref | Kirilma orani (hucre hatti referansi) | 0.02 | 0.001 – 0.1 | - | dusuk | tahmin | teknik |  | wf_break_cell_blend: ilk nesil wf_break_cell_ref_firstgen 0.02 [0.005-0.1] (tahmin), olgun wf_break_cell_ref_mature 0.0025 (Risen, PRNewswir |
| wf_learn_weight | Ogrenme durumu (ilk nesil / olgun agirligi) | 1 | 0 – 1 | - | orta | tahmin | teknik |  | Wafer wf_learn_weight = 0.5^(Q_cum_m2 / wf_learn_half_m2); wf_learning_scenario onerisi |
| bat_E_cell_Wh | Pil hucre enerjisi E_cell | 58 | 57 – 62 | Wh | orta | hesap_turetilmis | teknik |  | Pil: 20 Ah x 2.9 V (bat_cell_pris_small_capacity_Ah, bat_cell_v_nom_nfpp_V 2.85-3.1); 26700 LO 3.10 V x 3.3 Ah = 10.23 Wh (Tycorun); 50 Ah N |
| bat_cell_v_max_V | Na hucre gerilim penceresi ust ucu | 3.8 | 3.7 – 3.95 | V | orta | dogrulanmis_url | teknik |  | Pil bat_cell_v_max_nfpp_V (OGSolar 160 Ah 3.8 V; 18650 3.7 V; EVLithium 210 Ah 3.95 V); LO bat_cell_v_max_lo_V 3.95 (Tycorun) |
| bat_ns_cells | Pil seri hucre sayisi (14S/15S) | 15 | 14 – 15 | adet | orta | hesap_turetilmis | teknik |  | bat_f08: min(bat_ns_design, floor(V_lim x 0.97 / V_cell_max)); NFPP 15 (57.0 V), LO 14 (55.3 V), LFP 15; 35 V rejiminde LO 8 |
| D_ingot_mm | Ingot capi D ve aralik | 250 | 80 – 300 | mm | dusuk | tahmin | teknik |  | Kristal model 80-260 mm (+290 kalibrasyon), oneri kucuk talepte 120, saha duzeyinde 160-210; wafer eta(a\|D) tablolari D=250/300 (D=250'de a= |

## Standartlar ve mevzuat (`standart`) — 84 parametre

| id | ad | değer | aralık | birim | güven | kaynak türü | sınıf | eşdeğer | kaynak |
|---|---|---|---|---|---|---|---|---|---|
| std_selv_pv_uocmax_limit_v | PV DC tarafi SELV/PELV icin azami acik devre gerilimi (U_OC_MAX, soguk hava dahil) | 60 | 60 – 60 | V DC | yuksek | standart_metni_dogrulanmis | teknik |  | IEC 60364-7-712:2017 madde 712.414.101 |
| std_austria_selv_pv_v | Avusturya ulusal sapmasi: PV DC SELV siniri (pazar bayragi) | 35 | 35 – 35 | V DC | yuksek | standart_metni_dogrulanmis | teknik |  | IEC 60364-7-712:2017 Ek F, AT 712.414.101 |
| std_selv_dry_no_basic_protection_dc_v | SELV/PELV: normal KURU kosulda temel korumanin gerekmedigi DC sinir | 60 | 60 – 60 | V DC | yuksek | standart_metni_dogrulanmis | teknik |  | IEC 60364-4-41:2005 madde 414.4.5 |
| std_selv_wet_no_basic_protection_dc_v | SELV/PELV: kuru olmayan (diger) kosullarda temel korumasiz DC sinir | 30 | 30 – 30 | V DC | yuksek | standart_metni_dogrulanmis | teknik |  | IEC 60364-4-41:2005 madde 414.4.5 |
| std_elv_band1_dc_max_v | ELV Band I ust siniri (SELV/PELV mutlak ust sinir) | 120 | 120 – 120 | V DC | yuksek | standart_metni_dogrulanmis | teknik |  | IEC 60364-4-41:2005 madde 414.1.1 |
| std_dvca_dc_wet_v | IEC 62109-1 DVC-A siniri, islak konum | 35 | 35 – 35 | V DC | yuksek | dogrulanmis_url | teknik |  | DEKRA test raporu 6067599.50A (TRF IEC62109_1B); IEC TS 62257-9-8:2020 onizlemesi |
| std_dvca_dc_dry_v | IEC 62109-1 DVC-A siniri, kuru konum | 60 | 60 – 60 | V DC | yuksek | dogrulanmis_url | teknik |  | DEKRA TRF IEC62109_1B |
| std_class3_voc_stc_max_v | IEC 61730-1:2016 Class III modul: azami Voc (STC) | 35 | 35 – 35 | V DC | yuksek | standart_metni_dogrulanmis | teknik |  | IEC 61730-1:2016 madde 4.4.1 (SIS resmi onizlemesi) |
| std_class3_pmax_w | Class III modul azami gucu (STC) | 240 | 240 – 240 | W | yuksek | standart_metni_dogrulanmis | teknik |  | IEC 61730-1:2016 madde 4.4.1 (SIS onizlemesi) |
| std_class3_isc_max_a | Class III modul azami kisa devre akimi (STC) | 8 | 8 – 8 | A | yuksek | standart_metni_dogrulanmis | teknik |  | IEC 61730-1:2016 madde 4.4.1 |
| std_uocmax_default_factor | U_OC_MAX / U_OC_STC geri dusus katsayisi (alfa veya T_min bilinmiyorsa) | 1.2 | 1.2 – 1.2 | - | yuksek | standart_metni_dogrulanmis | teknik |  | IEC 60364-7-712:2017 Ek B.1 |
| std_iscmax_factor | I_SC_MAX / I_SC_STC asgari katsayi | 1.25 | 1.25 – 1.4 | - | yuksek | standart_metni_dogrulanmis | teknik |  | IEC 60364-7-712:2017 Ek B.2 |
| std_tmin_site_c | U_OC_MAX hesabinda kullanilan en dusuk saha sicakligi | -40 | -40 – -9 | C | orta | tahmin | teknik |  | Tasarim secimi; dayanak MGM rekorlari (modul revizyonunda acildi): Istanbul -9.0, Ankara -24.9, Erzurum -37.2 C; modul kaynaginda Almanya Hu |
| std_ocpr_to_isc_ratio | Modul azami asiri akim koruma degeri / Isc | 2 | 1.5 – 3 | - | dusuk | tahmin | teknik |  | Tahmin (ticari veri sayfalarindaki 'max series fuse'/Isc oranlarina benzetme) |
| std_energy_hazard_va | IEC 62109-1 tehlikeli enerji esigi (60 s sonra kullanilabilir guc, U >= 2 V) | 240 | 240 – 240 | VA | yuksek | dogrulanmis_url | teknik |  | DEKRA TRF IEC62109_1B madde 7.4.1 (IEC 62109-1:2010 metni) |
| std_energy_hazard_cap_j | IEC 62109-1 kondansator depolanmis enerji tehlike esigi (U >= 2 V) | 20 | 20 – 20 | J | yuksek | dogrulanmis_url | teknik |  | DEKRA TRF IEC62109_1B madde 7.4.1 b) |
| std_connector_class2_above_v | PV DC konnektorlerinin Class II olma zorunlulugu esigi | 35 | 35 – 35 | V | yuksek | standart_metni_dogrulanmis | teknik |  | IEC 60364-7-712:2017 madde 712.526.1 |
| std_imd_mandatory_above_v | PV dizisi yalitim direnci olcumu/izleme zorunlulugunun acikca gecerli oldugu gerilim | 60 | 60 – 60 | V | orta | standart_metni_dogrulanmis | teknik |  | IEC 60364-7-712:2017 madde 712.531.3.101 basligi ve 712.421.101.2.2 |
| std_lvd_dc_lower_v | AB Alcak Gerilim Direktifi DC alt siniri | 75 | 75 – 75 | V DC | yuksek | dogrulanmis_url | teknik |  | Avrupa Komisyonu LVD sayfasi |
| std_lvd_ac_lower_v | AB Alcak Gerilim Direktifi AC alt siniri | 50 | 50 – 50 | V AC | yuksek | dogrulanmis_url | teknik |  | Avrupa Komisyonu LVD sayfasi |
| std_rohs_pb_max_frac | RoHS kursun azami konsantrasyonu (homojen malzemede, agirlikca) | 0.001 | 0.001 – 0.001 | - | yuksek | dogrulanmis_url | teknik |  | Direktif 2011/65/AB Ek II ve Madde 2(4)(i) (legislation.gov.uk AB kaynakli metin) |
| std_plugin_ac_max_va | Almanya fisli PV azami invertor besleme gucu | 800 | 800 – 800 | VA | yuksek | dogrulanmis_url | teknik |  | VDE basin bildirisi (DIN VDE V 0126-95:2025-12); pvplug (VDE-AR-N 4105:2026-03 F.1.2) |
| std_plugin_schuko_pv_max_wp | Almanya fisli PV: Schuko fisle azami toplam modul gucu | 960 | 960 – 960 | Wp | yuksek | dogrulanmis_url | teknik |  | VDE basin bildirisi (DIN VDE V 0126-95:2025-12) |
| std_plugin_special_plug_pv_max_wp | Almanya fisli PV: ozel enerji fisiyle azami modul gucu / basit kayit siniri | 2000 | 2000 – 2000 | Wp | yuksek | dogrulanmis_url | teknik |  | VDE basin bildirisi; pvplug |
| std_rfg_type_a_min_w | AB RfG 2016/631 Tip A uretim modulu alt esigi | 800 | 800 – 800 | W | orta | hafizadan_dogrulanmadi | teknik |  | Regulation (EU) 2016/631 Madde 5 |
| std_batt_portable_mass_max_kg | AB Pil Tuzugu 'tasinabilir pil' ust kutle siniri | 5 | 5 – 5 | kg | yuksek | dogrulanmis_url | teknik |  | Regulation (EU) 2023/1542 Madde 3(9) ve 3(13) (AB Yayin Ofisi XHTML, bu revizyonda indirildi) |
| std_batt_industrial_2kwh_threshold_kwh | AB Pil Tuzugu 2 kWh esigi (karbon ayak izi Md.7, performans Md.10, pasaport Md.77) - SBESS esigi DEGIL | 2 | 2 – 2 | kWh | yuksek | dogrulanmis_url | teknik |  | Regulation (EU) 2023/1542 Madde 7, 10, 77 ve Madde 3(15) (Yayin Ofisi XHTML) |
| std_batt_due_diligence_turnover_eur | AB Pil Tuzugu durusti inceleme ciro esigi (uygulama 18.08.2027) | 4e+07 | 4e+07 – 4e+07 | EUR/yil | yuksek | dogrulanmis_url | teknik |  | Regulation (EU) 2023/1542 Madde 47; Regulation (EU) 2025/1561 Madde 1 |
| std_air_batt_wh_threshold | Hava: ekipmanla/ekipman icinde Na-iyon pil Wh esigi (PI 977/978 Section I/II) | 100 | 100 – 100 | Wh | yuksek | dogrulanmis_url | teknik |  | IATA Battery Guidance Document 2026 akis semasi |
| std_air_cell_wh_threshold | Hava: ekipmanla/ekipman icinde Na-iyon hucre Wh esigi | 20 | 20 – 20 | Wh | yuksek | dogrulanmis_url | teknik |  | IATA Battery Guidance Document 2026 |
| std_air_soc_max_frac | Hava: Na-iyon pil azami sarj durumu | 0.3 | 0.3 – 0.3 | - | yuksek | dogrulanmis_url | teknik |  | IATA Battery Guidance Document 2026 |
| std_air_pax_pkg_batt_max_kg | Hava: yolcu ucaginda paket basina Na-iyon pil net kutlesi siniri (PI 977/978) | 5 | 5 – 5 | kg | yuksek | dogrulanmis_url | teknik |  | IATA Battery Guidance Document 2026 akis semasi |
| std_air_a88_low_prod_max_n | Hava: UN 38.3'ten gecmemis dusuk uretim serisi (SP A88) yillik azami adet | 100 | 100 – 100 | adet/yil | orta | dogrulanmis_url | teknik |  | IATA Battery Guidance Document 2026, B.04 |
| std_fx_eur_usd | Kur varsayimi EUR/USD | 1.15 | 1.05 – 1.25 | USD/EUR | dusuk | tahmin | teknik | → `el_fx_eur_usd` | Tahmin |
| std_tt_module_iec_usd | Modul tip testi + sertifika: IEC 61215 + IEC 61730 birlesik program, ilk aile | 60000 | 20000 – 150000 | USD/aile | dusuk | tahmin | urun_sabit |  | Tahmin; heavengreenenergy.com IEC 61215 sayfasi yalniz nitel |
| std_tt_module_duration_month | Modul tip testi suresi | 4 | 2 – 8 | ay | orta | dogrulanmis_url | teknik |  | heavengreenenergy.com IEC 61215 / 61730 sozluk |
| std_tt_module_samples_n | Modul tip testi numune sayisi (aile basina) | 12 | 8 – 30 | adet/aile | orta | dogrulanmis_url | teknik |  | heavengreenenergy.com IEC 61215; IEC 61215-1:2021 onizlemesi |
| std_tt_module_retest_usd | Modul ailesi degisikligi/ek boyut icin kismi tekrar test (IEC TS 62915) | 15000 | 3000 – 50000 | USD/degisiklik | dusuk | tahmin | urun_sabit |  | Tahmin; zorunluluk IEC 61215-1:2021 onizlemesi |
| std_tt_inverter_62109_usd | Kutu elektronigi guvenlik tip testi IEC/EN 62109-1/-2 (CB raporu) | 30000 | 10000 – 70000 | USD/model serisi | dusuk | tahmin | urun_sabit |  | Tahmin |
| std_tt_gridcode_per_country_usd | Sebeke baglanti uygunlugu, ulke basina (VDE-AR-N 4105, EN 50549-1, diger) | 25000 | 8000 – 60000 | USD/ulke | dusuk | tahmin | urun_sabit |  | Tahmin |
| std_tt_emc_usd | EMC tip testleri (EN IEC 61000-6-x, 61000-3-2/-3-3, CISPR 11 DC port) | 12000 | 5000 – 30000 | USD/model | dusuk | tahmin | urun_sabit |  | Tahmin (standart listesi hafizadan) |
| std_tt_radio_cyber_usd | Radyo (RED) + siber guvenlik (RED DA 2022/30; 11.12.2027'den CRA) | 15000 | 0 – 40000 | USD/model | dusuk | tahmin | urun_sabit |  | Tahmin; takvim Avrupa Komisyonu RED sayfasi |
| std_tt_plugin_system_incr_usd | DIN VDE V 0126-95 fisli sistem sertifikasi - ARTIMSAL (montaj, fis, kablo, sistem degerlendirmesi; 61730/62109/4105 raporlari yeniden kullanilir) | 10000 | 4000 – 30000 | USD/sistem varyanti | dusuk | tahmin | urun_sabit |  | Tahmin; kapsam VDE Institute duyurusu |
| std_tt_batt_un383_usd | UN 38.3 tasima testleri (hucre + paket tasarimi basina) | 12000 | 5000 – 30000 | USD/tasarim | dusuk | tahmin | urun_sabit |  | Tahmin; zorunluluk IATA 2026 |
| std_tt_batt_safety_usd | Na-iyon pil guvenlik temel degerlendirmesi (IEC 62619 benzeri / urun guvenligi) | 30000 | 10000 – 80000 | USD/tasarim | dusuk | tahmin | urun_sabit |  | Tahmin; IEC 62619 kapsami IEC webstore |
| std_tt_batt_annexv_extra_usd | SBESS icin AB Pil Tuzugu Ek V ek guvenlik testleri (isil yayilim, yangin, gaz emisyonu vb.) | 25000 | 8000 – 80000 | USD/tasarim | dusuk | tahmin | urun_sabit |  | Tahmin; parametre listesi Regulation (EU) 2023/1542 Ek V |
| std_tt_portable_62368_usd | Tasinabilir guc istasyonu guvenligi (EN IEC 62368-1 + PV girisi 62109) - B, AC cikisli | 20000 | 8000 – 50000 | USD/model | dusuk | tahmin | urun_sabit |  | Tahmin; standart secimi hafizadan |
| std_tt_ul2743_usd | ABD tasinabilir guc paketi UL 2743 listelemesi | 50000 | 25000 – 120000 | USD/model | dusuk | tahmin | urun_sabit |  | Tahmin |
| std_cfp_declaration_usd | Pil karbon ayak izi beyani + dogrulama (endustriyel > 2 kWh) | 30000 | 10000 – 80000 | USD/model | dusuk | tahmin | urun_sabit |  | Tahmin; kapsam 2023/1542 Madde 7 |
| std_batt_passport_setup_usd | Pil pasaportu altyapisi (veri modeli, QR, veri tasiyici, hizmet) - endustriyel > 2 kWh | 20000 | 5000 – 60000 | USD/model | dusuk | tahmin | urun_sabit |  | Tahmin; zorunluluk 2023/1542 Madde 77 ve Battery Pass |
| std_tt_comp_connector_usd | Kendi uretimi PV DC konnektor sertifikasi (IEC 62852) | 20000 | 8000 – 50000 | USD/konnektor ailesi | dusuk | tahmin | urun_sabit |  | Tahmin; gereklilik IEC 60364-7-712:2017 712.526.1 |
| std_tt_comp_jbox_usd | Kendi uretimi baglanti kutusu sertifikasi (IEC 62790) | 15000 | 5000 – 40000 | USD/aile | dusuk | tahmin | urun_sabit |  | Tahmin; standart numarasi hafizadan |
| std_tt_comp_enclosure_material_usd | Kasa/izolasyon polimeri malzeme testleri (UV, alev, RTI, kizdirma teli) - malzeme basina | 8000 | 3000 – 20000 | USD/malzeme | dusuk | tahmin | urun_sabit |  | Tahmin |
| std_rohs_verification_usd_per_bom | RoHS uygunluk dogrulamasi (XRF/ICP + teknik dosya) BOM basina | 3000 | 1000 – 8000 | USD/BOM | dusuk | tahmin | urun_sabit |  | Tahmin |
| std_tr_market_extra_usd | Turkiye piyasaya arz icin ek uygunluk/kayit maliyeti (AB belgelerinin taninmasi disinda) | 10000 | 0 – 50000 | USD/urun | dusuk | tahmin | urun_sabit |  | Tahmin - BILMIYORUZ |
| std_tr_plugin_pv_regime_known | Turkiye fisli/balkon PV yasal cercevesi biliniyor mu (0=dogrulanmadi, 1=var ve uygun) | 0 | 0 – 1 | bool | dusuk | hafizadan_dogrulanmadi | teknik |  | Resmi Gazete 12.05.2019 Lisanssiz Elektrik Uretim Yonetmeligi (fis/priz/balkon gecmiyor); 2020-2026 degisiklikleri dogrulanamadi |
| std_cert_maintenance_usd_per_cert_year | Sertifika/marka surdurme ucreti | 3000 | 1000 – 8000 | USD/sertifika/yil | dusuk | tahmin | urun_sabit |  | Tahmin |
| std_tt_total_lead_time_month | Pazara giris toplam sertifikasyon takvimi | 9 | 6 – 15 | ay | dusuk | tahmin | teknik |  | Tahmin |
| std_factory_inspection_usd_per_year | Sertifika kurulusu fabrika denetimi | 8000 | 3000 – 20000 | USD/saha/yil | dusuk | tahmin | saha_sabit |  | Tahmin |
| std_qms_62941_usd_per_year | Modul uretimi kalite sistemi (ISO 9001 + IEC 62941) | 15000 | 5000 – 40000 | USD/saha/yil | dusuk | tahmin | saha_sabit |  | Tahmin |
| std_qms_battery_usd_per_year | Hucre/pil ureticisi kalite yonetim programi (UN Model Regs tasima sarti) + pil hatti QMS | 10000 | 3000 – 30000 | USD/saha/yil | dusuk | tahmin | saha_sabit |  | Tahmin; gereklilik UN Model Regulations 2.9.4 (lityum icin, hafizadan; Na-iyon karsiligi dogrulanmadi) |
| std_atex_gascode_compliance_usd_per_site | Silan/H2 icin ATEX bolgeleme, patlamadan korunma dokumani, gaz kodu uyum/danismanlik (tek seferlik) | 60000 | 15000 – 200000 | USD/saha | dusuk | tahmin | saha_sabit |  | Tahmin; ATEX 2014/34/AB ve 1999/92/AT, gaz kodlari hafizadan |
| std_env_permit_usd_per_site | Cevre izinleri (CED gerekliligi degerlendirmesi, emisyon, desarj - HF/NOx/florur) tek seferlik | 40000 | 10000 – 150000 | USD/saha | dusuk | tahmin | saha_sabit |  | Tahmin |
| std_epr_admin_usd_per_country_year | Genisletilmis uretici sorumlulugu kayit + yetkili temsilci, ulke basina | 3000 | 500 – 10000 | USD/ulke/yil | dusuk | tahmin | urun_sabit |  | Tahmin |
| std_epr_fee_panel_usd_per_kg | WEEE geri alim ucreti - PV panel | 0.1 | 0.02 – 0.5 | USD/kg | dusuk | tahmin | alan |  | Tahmin |
| std_epr_fee_batt_usd_per_kg | Pil geri alim/EPR ucreti | 1 | 0.2 – 4 | USD/kg | dusuk | tahmin | guc_enerji |  | Tahmin |
| std_epr_fee_eee_usd_per_kg | WEEE ucreti - kutu elektronigi/kasa (pil haric) | 0.3 | 0.05 – 1.5 | USD/kg | dusuk | tahmin | adet |  | Tahmin |
| std_mach_techfile_usd_per_machine_type | Kendi tasarimi makine tipi basina risk degerlendirmesi + teknik dosya + uygunluk (2006/42/AT; 20.01.2027'den 2023/1230) | 25000 | 8000 – 80000 | USD/makine tipi | dusuk | tahmin | urun_sabit |  | Tahmin; yukumluluk 2006/42/AT Madde 2(i), tarih Avrupa Komisyonu makine sayfasi |
| std_mach_doc_usd_per_machine_copy | Kopyalanan her makine icin son kontrol, uygunluk beyani, CE/etiket | 2000 | 500 – 6000 | USD/makine | dusuk | tahmin | zaman |  | Tahmin |
| std_rf_ism_shield_usd_per_rf_machine | RF induksiyon (FZ vb.) ISM emisyon uyumu (CISPR 11 Grup 2) ve isci EMF maruziyeti icin ekranlama/olcum | 15000 | 3000 – 60000 | USD/makine | dusuk | tahmin | zaman |  | Tahmin; CISPR 11 Grup 2 ve 2013/35/AB hafizadan |
| std_rt_hipot_min_s | IEC 62109-1 rutin dielektrik testi asgari suresi | 1 | 1 – 1 | s | yuksek | dogrulanmis_url | teknik |  | DEKRA TRF IEC62109_1B madde 7.5.2.5 |
| std_rt_bonding_min_s | IEC 62109-1 koruyucu topraklama empedansi rutin testi asgari suresi (Sinif I, tek elemanli baglanti) | 2 | 2 – 2 | s | yuksek | dogrulanmis_url | teknik |  | DEKRA TRF IEC62109_1B madde 7.3.6.3.4 |
| std_rt_box_hipot_touch_s | Kutu rutin dielektrik testi - operator dokunma suresi | 10 | 3 – 30 | s/kutu | dusuk | tahmin | adet |  | Tahmin (test 1 s + kontak/fikstur) |
| std_rt_box_bonding_touch_s | Kutu koruyucu topraklama rutin testi - dokunma suresi (yalniz Sinif I) | 5 | 3 – 15 | s/kutu | dusuk | tahmin | adet |  | Tahmin; kosullar DEKRA TRF 7.3.6.3.4 |
| std_rt_module_iv_touch_s | Modul IV (flas) olcumu - dokunma suresi (etiket gucu, fiilen zorunlu) | 20 | 8 – 60 | s/panel | dusuk | tahmin | adet |  | Tahmin |
| std_rt_module_hipot_touch_s | Modul yalitim/dielektrik rutin testi - dokunma suresi | 10 | 3 – 30 | s/panel | dusuk | tahmin | adet |  | Tahmin; zorunluluk UL 61730 (hafizadan), IEC tarafinda fabrika denetimi (hafizadan) |
| std_rt_module_station_s | Modul zorunlu test istasyonu doluluk suresi (IV + hipot) | 30 | 10 – 90 | s/panel | dusuk | tahmin | zaman |  | Tahmin |
| std_rt_box_station_s | Kutu zorunlu test istasyonu doluluk suresi | 20 | 5 – 60 | s/kutu | dusuk | tahmin | zaman |  | Tahmin |
| std_rt_labor_usd_per_h | Test teknisyeni tam yuklu iscilik (Turkiye) - uretim alaninin ortak degeriyle degistirilmeli | 10 | 6 – 20 | USD/saat | dusuk | tahmin | zaman | → `eco_labor_technician_usd_h` | Tahmin |
| std_rt_module_test_capex_usd | Modul zorunlu test ekipmani (flas simulator + hipot; EL HARIC) | 80000 | 30000 – 250000 | USD/istasyon | dusuk | tahmin | zaman |  | Tahmin |
| std_rt_box_test_capex_usd | Kutu zorunlu guvenlik test ekipmani (hipot, topraklama, yalitim; sebeke simulatoru ve pil test cihazi HARIC) | 25000 | 8000 – 60000 | USD/istasyon | dusuk | tahmin | zaman |  | Tahmin |
| std_rt_module_el_s | Modul EL goruntuleme (kalite testi - standart zorunlulugu yok; uretim alanina referans) | 15 | 5 – 40 | s/panel | dusuk | tahmin | teknik |  | Tahmin |
| std_rt_box_functional_s | Kutu fonksiyon testi (NA koruma esikleri, MPPT, ulke ayari) - uretim/elektronik alanina referans | 120 | 30 – 600 | s/kutu | dusuk | tahmin | teknik |  | Tahmin |
| std_rt_batt_eol_s | Pil paketi hat sonu testi (OCV/IR, BMS, SoC ayari) - pil alanina referans | 300 | 60 – 1800 | s/paket | dusuk | tahmin | teknik |  | Tahmin |
