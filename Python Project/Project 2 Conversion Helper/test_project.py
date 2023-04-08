from project import time_hour_clock, time_pass_by, weight_convert, length_convert, fahrenheit_to_celsius, celsius_to_fahrenheit
from datetime import timedelta
from pytest import raises


def test_time_hour_clock():
    assert time_hour_clock("9amto5pm") == "09:00 to 17:00"
    assert time_hour_clock("7pm to 8pm") == "19:00 to 20:00"
    assert time_hour_clock("6 AM to 8 AM") == "06:00 to 08:00"
    with raises(ValueError):
        assert time_hour_clock("6 to 8 AM")
        assert time_hour_clock("5 pm 9 AM")
        assert time_hour_clock("7 to 10 ")


def test_time_pass_by():
    assert time_pass_by("2023-02-27", "2023-03-28") == timedelta(days=29)
    assert time_pass_by("2023-01-01", "2023-02-27") == timedelta(days=57)
    assert time_pass_by("2022-12-01", "2023-03-28") == timedelta(days=117)
    with raises(ValueError):
        assert time_pass_by("20221201", "20230328")
        assert time_pass_by("20221208")
        assert time_pass_by("2022 12 08", "2023 03 28")


def test_fahrenheit_to_celsius():
    assert fahrenheit_to_celsius("12") == "12.00 degrees in Fahrenheit is -11.11 degrees in Celsius"
    assert fahrenheit_to_celsius("60") == "60.00 degrees in Fahrenheit is 15.56 degrees in Celsius"
    with raises(ValueError):
        assert fahrenheit_to_celsius("dog")
        assert fahrenheit_to_celsius("cat")


def test_celsius_to_fahrenheit():
    assert celsius_to_fahrenheit("20") == "20.00 degrees in Celsius is 68.00 degrees in Fahrenheit"
    assert celsius_to_fahrenheit("0") == "0.00 degrees in Celsius is 32.00 degrees in Fahrenheit"
    with raises(ValueError):
        assert celsius_to_fahrenheit("cat")
        assert celsius_to_fahrenheit("dog")


def test_length_convert():
    assert length_convert(1, 1.5) == "1.50 feet is 18.00 inches"
    assert length_convert(2, 24) == "24.00 inches is 2.00 feet"
    assert length_convert(3, 2) == "2.00 miles is 3218.69 meters"
    assert length_convert(4, 2000) == "2000.00 meters is 1.24 miles"
    assert length_convert(5, 20) == "20.00 centimeters is 7.87 inches"
    assert length_convert(6, 1) == "1.00 inches is 2.54 centimeters"
    with raises(ValueError):
        assert length_convert(1, "dog")
        assert length_convert(8, "cat")


def test_weight_convert():
    assert weight_convert(1, 12.5) == "12.50 pounds is 200.00 ounces"
    assert weight_convert(2, 32) == "32.00 ounces is 2.00 pounds"
    assert weight_convert(3, 12) == "12.00 ounces is 340.19 grams"
    assert weight_convert(4, 400) == "400.00 grams is 14.11 ounces"
    assert weight_convert(5, 1000) == "1000.00 grams is 2.20 pounds"
    assert weight_convert(6, 1) == "1.00 pounds is 453.59 grams"
    with raises(ValueError):
        assert weight_convert(2, "dog")
        assert weight_convert(7, "cat")
