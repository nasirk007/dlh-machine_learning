#!/usr/bin/env python3
def summation_i(n):
    if not isinstance(n, (int, float)):
        return None
    else:
        total = int(n*(n + 1)(2*n + 1)/6)
    return total
