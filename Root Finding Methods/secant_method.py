# Author: Satya Jhaveri
#
# The secant method is an open method that approximates the root of a function.
# It can be used on any continuous function, f, given two values a and b for which f(a) and f(b) 
#  have differing signs. This root finding method works iteratively, by constructing a line
#  through the points (a, f(a)) and (b, f(b)), then using the root of that secant as the next
#  value in the series of 'x values'. We then set a = b and b = root, then repeat the process
#  with the new values for a and b until the precision is met.
#

from typing import Callable


def secant(f: Callable, x1: float, x2: float, precision: float) -> float:
    """
    Approximates the root to a function using the secant method.

    Args:
        f (Callable): A continuous function to approximate a root of
        x1 (float): The lower bound of the interval which contains the root
        x2 (float): The upper bound of the interval which contains the root
        precision (float): The maximum amount of error that is acceptable in method results

    Returns:
        float: Value which, when passed to f, returns a number of magnitude < precision.
        
    Raises:
        ValueError: If x1 and x2 are equal, if f(x1) and f(x2) have different signs, or if Precision is not greater than zero.
    """
    # Validating Inputs:
    if x1 == x2:
        raise ValueError("x1 and x2 cannot be the same value.")
    
    if f(x1) * f(x2) >= 0:
        raise ValueError("x1 and x2 must have different signs.")
    
    if precision <= 0:
        raise ValueError("Precision cannot be zero or negative.")
    
    # Actual Method:
    x_next = (x1 * f(x2) - x2 * f(x1)) / (f(x2) - f(x1))
    
    while abs(f(x_next)) > precision:
        # Updating the series of x values:
        x1 = x2
        x2 = x_next
        x_next = (x1 * f(x2) - x2 * f(x1)) / (f(x2) - f(x1))
    
    return x_next


if __name__ == "__main__":
    # Basic testing:
    precision = 0.0001
    
    def f(x: float) -> float: return (x-1) * (x+6)
    
    
    # Passing invalid values to the function:
    lower, upper = 0, 0
    try:
        secant(f, lower, upper, precision)
    except Exception as e:
        print(f"The exception '{e}' was raised successfully")
    
    lower, upper = 0, 10
    precision = -0.12345
    try:
        secant(f, lower, upper, precision)
    except Exception as e:
        print(f"The exception '{e}' was raised successfully")
