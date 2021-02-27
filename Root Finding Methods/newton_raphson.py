# Author: Satya Jhaveri
#
# The Newton Raphson method is a root finding method that uses the derivative of the
#  function to make each guess.
# It can be used on any continuous function, f, given a point (a, f(a)). This method
#  works iteratively by using the root of the tangent to the function at the current
#  estimate point as the estimate point in the next iteration, until a value that
#  satisfies the required precision.
# 

from typing import Callable  # (For type hinting function)


def newton_raphson(f: Callable, df: Callable, xi: float, precision: float) -> float:
    """
    Approximates the root to a function using the false position method.

    Args:
        f (Callable): A continuous function to approximate a root of
        df (Callable): The derivative of the function f, with respect to the independent variable
        xi (float): The initial guess of the root of the function
        precision (float): The maximum amount of error that is acceptable in method results

    Raises:
        ValueError: If Precision is not greater than zero.

    Returns:
        float: Value which, when passed to f, returns a number of magnitude < precision.
    """
    # Validating Inputs:
    if precision <= 0:
        raise ValueError("Precision cannot be zero or negative.")

    # Actual Method:
    x_next = xi - f(xi) / df(xi)
    
    while abs(f(x_next)) > precision:
        xi = x_next
        x_next = xi - f(xi) / df(xi)
    
    return x_next

