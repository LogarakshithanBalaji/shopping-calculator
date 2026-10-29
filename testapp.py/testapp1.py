import pytest
from app.py import calculate_total

def test_calculate_total():
    assert calculate_total(10.5, 3) == 31.5
    assert calculate_total(0, 5) == 0

def test_negative_values():
    with pytest.raises(ValueError):
        calculate_total(-10, 2)