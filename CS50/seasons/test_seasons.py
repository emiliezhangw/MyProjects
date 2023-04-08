from seasons import get_birth, get_minute
from pytest import raises
from datetime import date


def test_minute():
    assert get_minute(date(2003, 1, 1), date(2001, 1, 1)) == "One million, fifty-one thousand, two hundred minutes"
    assert get_minute(date(2032, 1, 1), date(2020, 6, 1)) == "Six million, ninety-two thousand, six hundred forty minutes"
    assert get_minute(date(2000, 1, 1), date(1998, 6, 20)) == "Eight hundred six thousand, four hundred minutes"


def test_get_birth():
    with raises(ValueError):
        get_birth("February 6th, 1998")
        get_birth("199-1-1")


