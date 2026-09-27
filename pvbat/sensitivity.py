"""Duyarlılık analizi.

Tornado (tek-seferde-bir parametre): her parametre alt ve üst değerine
çekilir, diğerleri taban değerde kalır; sonuçtaki değişim sıralanır.
Sınırlama: etkileşimleri görmez. Faz 2'de Morris / Monte Carlo eklenecek.
"""
from __future__ import annotations

from typing import Callable, Iterable

import pandas as pd

from .model import Sonuc, degerlendir
from .params import ParamSet
from .secimler import Secimler

Metrik = Callable[[Sonuc], float]


def sistem_usd_per_W(r: Sonuc) -> float:
    return r.defter.usd_per_W()


def tornado(p: ParamSet, s: Secimler, P_panel_W: float, metrik: Metrik = sistem_usd_per_W,
            parametreler: Iterable[str] | None = None) -> pd.DataFrame:
    taban = metrik(degerlendir(p, s, P_panel_W))
    satirlar = []
    for pid in (parametreler or list(p)):
        m = p.meta(pid)
        if m.alt == m.ust:
            continue
        sonuc = {}
        for uc, deger in (("alt", m.alt), ("ust", m.ust)):
            try:
                sonuc[uc] = metrik(degerlendir(p.override(**{pid: deger}), s, P_panel_W))
            except (ValueError, ZeroDivisionError) as e:  # fiziksel olarak geçersiz uç
                sonuc[uc] = float("nan")
                sonuc[f"{uc}_hata"] = str(e)
        satirlar.append({
            "parametre": pid, "ad": m.ad, "alan": m.alan, "birim": m.birim,
            "taban_deger": p[pid], "alt": m.alt, "ust": m.ust, "guven": m.guven,
            "metrik_taban": taban, "metrik_alt": sonuc["alt"], "metrik_ust": sonuc["ust"],
            "etki_araligi": abs(sonuc["ust"] - sonuc["alt"]),
            "hata": "; ".join(v for k, v in sonuc.items() if k.endswith("_hata")),
        })
    df = pd.DataFrame(satirlar)
    if not df.empty:
        df = df.sort_values("etki_araligi", ascending=False, na_position="last").reset_index(drop=True)
    return df
