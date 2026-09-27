import math

import pytest

from pvbat.costs import CostItem, Ledger
from pvbat.econ import capex_saatlik, crf
from pvbat.params import Param, ParamSet


def _p(**kw):
    base = dict(id="x", ad="x", birim="-", deger=1.0, alt=0.5, ust=2.0, alan="test",
                kaynak="tahmin", kaynak_turu="tahmin", guven="dusuk", aciklama="kaba hesap")
    base.update(kw)
    return Param(**base)


def test_param_gecerli():
    assert _p().hatalar() == []


def test_param_aralik_disi():
    assert any("aralık dışı" in h for h in _p(deger=3.0).hatalar())


def test_guven_tavani():
    assert any("tavan" in h for h in _p(guven="yuksek").hatalar())


def test_tahmin_dayanaksiz():
    assert any("dayanak" in h for h in _p(aciklama="").hatalar())


def test_paramset_override_degismez():
    ps = ParamSet({"x": _p()})
    ps2 = ps.override(x=1.5)
    assert ps.x == 1.0 and ps2.x == 1.5
    with pytest.raises(KeyError):
        ps.override(y=1)
    with pytest.raises(AttributeError):
        ps.y


def test_ledger_gruplama():
    L = Ledger(P_panel_W=100)
    L.ekle(CostItem("a", "a", "hucre", "alan", 10.0, "m2", 0.5, "10*0.5"),
           CostItem("b", "b", "elektronik", "guc_enerji", 0.1, "W", 100, "0.1*100", kapsam="kutu"))
    assert L.toplam_panel() == pytest.approx(15.0)
    assert L.usd_per_W("kutu") == pytest.approx(0.10)
    assert L.grupla("sinif") == pytest.approx({"alan": 0.05, "guc_enerji": 0.10})
    with pytest.raises(ValueError):
        L.ekle(CostItem("a", "a", "hucre", "alan", 1, "m2", 1, ""))


def test_crf():
    assert crf(0.0, 10) == pytest.approx(0.1)
    assert crf(0.10, 10) == pytest.approx(0.16275, rel=1e-4)
    assert capex_saatlik(1e6, 0.0, 10, 8000) == pytest.approx(12.5)


def test_esdeger_tek_sahip():
    sahip = _p(id="eco_x", deger=2.0, alt=1.0, ust=3.0)
    takma = _p(id="mod_x", deger=9.0, alt=0.0, ust=10.0, esdeger="eco_x", esdeger_carpan=1.5)
    ps = ParamSet({"eco_x": sahip, "mod_x": takma})
    assert ps.mod_x == pytest.approx(3.0)
    assert ps.override(eco_x=3.0).mod_x == pytest.approx(4.5)
    with pytest.raises(KeyError):
        ps.override(mod_x=1.0)
    assert ps.sahipler() == ["eco_x"]
    assert ps.dogrula() == []
    assert "mod_x" in ps and "yok" not in ps


def test_esdeger_zinciri_hata():
    a = _p(id="a"); b = _p(id="b", esdeger="a"); c = _p(id="c", esdeger="b")
    assert any("zinciri" in h for h in ParamSet({"a": a, "b": b, "c": c}).dogrula())


def test_gercek_varsayimlar_gecerli():
    """data/varsayimlar/*.yaml: her kayıt tutarlı, eşdeğerler tek sahipli."""
    ps = ParamSet.load()
    assert len(ps) > 900
    assert ps.dogrula() == []
