import numpy as np
from tools import calculate_area
import pytest


def test_calculate_area_negative():
    with pytest.raises(AssertionError):
        calculate_area(-1)


def test_calculate_area_pi():
    assert calculate_area(1) == np.pi, "For radius of 1, area should be pi"


def test_calculate_area_zero():
    assert calculate_area(0) == 0


def test_calculate_area_exp10():
    assert calculate_area(np.exp(10)) == 1524191413.6768537
