import pytest

from fuel import convert, gauge

def test_convert_values():
    assert convert("1/100") == 1
    assert convert("99/100") == 99
    assert convert("3/4") == 75

def test_convert_exception():
    with pytest.raises(ValueError):
        convert("1-2")
    with pytest.raises(ValueError):
        convert("2/1")
    with pytest.raises(ValueError):
        convert("1.0/2")
    with pytest.raises(ValueError):
        convert("1/2.0")

    with pytest.raises(ZeroDivisionError):
        convert("1/0")

def test_gauge():
    assert gauge(0) == "E"
    assert gauge(1) == "E"
    assert gauge(32) == "32%"
    assert gauge(99) == "F"
    assert gauge(100) == "F"