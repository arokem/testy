import numpy as np


def calculate_area(r):
    assert r >= 0, "Radius can only be non-negative"
    area = np.pi * r **2
    return area


def calculate_circ(r):
    assert r >= 0, "Radius can only be non-negative"
    circ = 2 * np.pi * r
    return circ
