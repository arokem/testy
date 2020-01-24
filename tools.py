import numpy as np


def calculate_area(r):
    """
    Calculates area of a circle

    Parameters
    ----------
    r : number

    Returns
    -------
    area : the area of circle with radius r

    Examples
    --------
    >>> calculate_area(1)
    3.141592653589793
    """
    assert r >= 0, "Radius can only be non-negative"
    area = np.pi * r **2
    return area


def calculate_circ(r):
    assert r >= 0, "Radius can only be non-negative"
    circ = 2 * np.pi * r
    return circ
