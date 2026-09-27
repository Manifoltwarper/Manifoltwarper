"""Sermaye maliyetini zaman-ölçekli maliyete çeviren yardımcılar."""
from __future__ import annotations


def crf(oran: float, yil: float) -> float:
    """Sermaye geri kazanım faktörü (annüite): yıllık ödeme / capex."""
    if yil <= 0:
        raise ValueError("amortisman ömrü > 0 olmalı")
    if oran == 0:
        return 1.0 / yil
    q = (1.0 + oran) ** yil
    return oran * q / (q - 1.0)


def capex_saatlik(capex_usd: float, oran: float, yil: float, saat_yil: float,
                  bakim_orani: float = 0.0, sigorta_orani: float = 0.0) -> float:
    """Capex'in ekipman saati başına maliyeti (USD/saat).

    yıllık = capex × (CRF + bakım% + sigorta%);  saatlik = yıllık / çalışma saati
    """
    if saat_yil <= 0:
        raise ValueError("yıllık çalışma saati > 0 olmalı")
    return capex_usd * (crf(oran, yil) + bakim_orani + sigorta_orani) / saat_yil
