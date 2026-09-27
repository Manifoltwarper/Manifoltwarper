"""Panel gücü taraması (ana değişken P_panel = 50–500 W)."""
from __future__ import annotations

from typing import Iterable

import pandas as pd

from .model import Sonuc, degerlendir
from .params import ParamSet
from .secimler import Secimler

VARSAYILAN_GUCLER = tuple(range(50, 501, 25))


def tara(p: ParamSet, s: Secimler, gucler: Iterable[float] = VARSAYILAN_GUCLER) -> tuple[pd.DataFrame, pd.DataFrame, list[Sonuc]]:
    """Döner: (özet tablo — güç başına bir satır, uzun maliyet dökümü, ham sonuçlar)."""
    sonuclar = [degerlendir(p, s, P) for P in gucler]
    ozet = pd.DataFrame([r.ozet_satiri() for r in sonuclar])
    dokum = pd.DataFrame([row for r in sonuclar for row in r.defter.satirlar()])
    return ozet, dokum, sonuclar
