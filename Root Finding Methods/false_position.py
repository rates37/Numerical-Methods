# Author: Satya Jhaveri
#
# The false position method is a root finding method that utilizes a 'divide and conquer' strategy
#  to find the root of a function. 
# It can be used on any continuous function, f, given two values a and b for which f(a) and f(b) 
#  have differing signs. This root finding method works by splitting the interval [a, b] into
#  two smaller intervals, where the point used to split the interval in two is the root of the 
#  secant line of the function between the two points (a, f(a)), and (b, f(b)). Using the 
#  Intermediate Value Theorem, the interval that contains the root is then 'reused' the method 
#  produces a value that meets the precision required.
#

from typing import Callable


def false_position(f: Callable, lower: float, upper: float, precision: float) -> float:
    """
    Approximates the root to a function using the false position method.

    Args:
        f (Callable): A continuous function to approximate a root of
        lower (float): The lower bound of the interval which contains the root
        upper (float): The upper bound of the interval which contains the root
        precision (float): The maximum amount of error that is acceptable in method results

    Returns:
        float: Value which, when passed to f, returns a number of magnitude < precision.
        
    Raises:
        ValueError: If precision is not greater than 0, if f(lower) and f(upper) are of the same sign, or if lower == upper.
    """
    # Validating inputs:
    if lower >= upper:
        raise ValueError("Lower cannot be greater than or equal to upper.")
    
    if f(lower) * f(upper) > 0:
        raise ValueError("f(lower) and f(upper) must have different signs.")
    
    if precision <= 0:
        raise ValueError("Precision cannot be zero or negative.")
    
    # Actual Method:
    root_guess = lower - (upper - lower) * f(lower) / (f(upper) - f(lower))
    
    while abs(f(root_guess)) > precision:
        # Choosing the range for the new interval:
        if f(lower) * f(root_guess) < 0:
            upper = root_guess
        else:
            lower = root_guess
        
        # Resetting the root guess:
        root_guess = lower - (upper - lower) * f(lower) / (f(upper) - f(lower))
    
    return root_guess
