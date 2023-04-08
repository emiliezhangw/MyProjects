import pytest
from fuel import convert, gauge


def test_convert():
    assert convert("3/4") == 75
    assert convert("1/4") == 25
    with pytest.raises(ValueError):
        convert("cat/dog")
        convert("2/1")
    with pytest.raises(ZeroDivisionError):
        convert("2/0")


def test_gauge():
    assert gauge(75) == "75%"
    assert gauge(25) == "25%"


def test_empty():
    assert gauge(99) == "F"


def test_full():
    assert gauge(1) == "E"
