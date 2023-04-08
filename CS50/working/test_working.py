from working import convert
import pytest


def test_convert():
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"
    assert convert("10:30 PM to 8:50 AM") == "22:30 to 08:50"
    with pytest.raises(ValueError):
        convert("9 AM - 5 PM")
        convert("9:00 AM 17:00 PM")


def test_convert2():
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert convert("10 PM to 8 AM") == "22:00 to 08:00"


def test_convert_time_valid():
    with pytest.raises(ValueError):
        convert("8:60 AM to 4:60 PM")
        convert("6:65 AM to 21:80 PM")



