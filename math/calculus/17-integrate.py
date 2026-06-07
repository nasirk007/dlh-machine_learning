#!/usr/bin/env python3
"""Module calculates the integral of polynomial"""


def poly_integral(poly, C=0):
    """integral coefficient = value divided by new power (i + 1)."""

    if not isinstance(poly, list) or len(poly) == 0:
        return None
    if not isinstance(C, int):
        return None
    for element in poly:
        if not isinstance(element, (int, float)):
            return None

    # integration of function above constant
    new_poly = [C]
    for i in range(len(poly)):
        new_poly.append(poly[i] / (i + 1))
    return new_poly
