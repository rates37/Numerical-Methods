# Author: Satya Jhaveri
#
# Simpson's 13 rule 
# 
# This file also contains a version of the trapezoids method that can be used on
#  discrete, non-uniform input data.
#

from typing import List, Callable

def trapezoidal(f: Callable, a: float, b: float, n: int) -> float:
    """
    Approximates the value of a definite integral using the trapezoidal rule and a specified number of points.

    Args:
        f (Callable): A continuous function to integrate over
        a (float): The lower integral interval
        b (float): The upper integral interval
        n (int): The number of trapezoids to use in the approximation

    Raises:
        ValueError: If lower integral is higher than upper integral
        ValueError: If the number of trapezoids is less than 1

    Returns:
        float: The approximated value of the integral
    """
    # Validating Inputs: