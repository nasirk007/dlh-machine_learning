#!/usr/bin/env python3
"""This module creates a class binomial"""


class Binomial:
    """This class represents an binomial distribution"""
    def __init__(self, data=None, n=1, p=0.5):
        """constructor method."""
        # probility of k success in fixed no of trail (n),
        # where we have two possible outcome for each event
        # p is prob of success, fixed parameter in BD function
        # p is prob of success for single event, & bais is possible
        # flipping 2 coins = 2 event, results are outcome given x or k value
        # n is no bernoulli try/attempt/trails
        # four conditions for BD:
        # n no of trails must be fixed
        # p must remain constant for every trail
        # every trail will two possible outcome (succ. fail.)
        # Events (trails) and outcomes are indpendent from each other
        # mean of BD = np
        # variance = np(1-n)
        # Std Deviation = Squareroot of Np(1-n)
        # PDF = P(X=x)=(x/n)p^x (1−p)^n−x
        # CDF = summation of each PDF
        self.n = round(n)
        self.p = float(p)
        if data is None:
            if n <= 0:
                raise ValueError("n must be a positive value")
            if not (0 < p < 1):
                raise ValueError("p must be greater than 0 and less than 1")
        if data is not None:
            if not isinstance(data, list):
                raise TypeError("data must be a list")
            elif len(data) < 2:
                raise ValueError("data must contain multiple values")
            else:
                # mean → variance → p → n → recompute p
                value = 0
                for i in range(len(data)):
                    value += data[i]
                mean = value / len(data)

                # variance (v^2) = np(1-p) ==> as mean = np
                # rearrange formula to find P
                # so p = 1 - variance / mean
                # variance is till missing, calculate it first
                summation = 0
                for i in range(len(data)):
                    summation += (data[i] - mean) ** 2
                variance = summation / len(data)
                initial_P = 1 - (variance / mean)

                # compute n value, using mean = np
                no_of_attempts = round(mean / initial_P)
                # re-compute p value as required per task, using mean = np
                final_P = mean / no_of_attempts
            self.n = no_of_attempts
            self.p = final_P
