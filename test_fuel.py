import pytest
from fuel import convert, gauge

# Pruebas para convert
def test_convert_valid():
    assert convert("3/4") == 75
    assert convert("1/2") == 50
    assert convert("1/100") == 1
    assert convert("99/100") == 99

def test_convert_zero_division():
    with pytest.raises(ZeroDivisionError):
        convert("1/0")

def test_convert_value_error_non_integer():
    with pytest.raises(ValueError):
        convert("a/b")
    with pytest.raises(ValueError):
        convert("1.5/2")

def test_convert_value_error_x_greater_than_y():
    with pytest.raises(ValueError):
        convert("5/4")

# Pruebas para gauge
def test_gauge_empty_and_full():
    assert gauge(0) == "E"
    assert gauge(1) == "E"
    assert gauge(99) == "F"
    assert gauge(100) == "F"

def test_gauge_middle_values():
    assert gauge(50) == "50%"
    assert gauge(75) == "75%"
    assert gauge(2) == "2%"
