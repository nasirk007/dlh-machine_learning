#!/usr/bin/env python3
"""Module calculates the derivative of polynomial"""


def poly_derivative(poly):
    """this is documentation to finding coefficient list of polynomial."""
    

    if not isinstance(poly, list):
        return None
    for element in poly:
        if not isinstance(element, int):
        return None
        if isinstance(element, float):
        return None
    # base case
    if len(poly) == 1:
        return [0]
    # if poly has more than one element
    new_poly = []
    for element in poly:
        


    
