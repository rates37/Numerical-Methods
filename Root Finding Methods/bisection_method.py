# Author: Satya Jhaveri
#
# The bisection method is a root finding method that utilizes a 'divide and conquer' strategy
#  to find the root of a function. 
# It can be used on any continuous function, f, given two values a and b for which f(a) and f(b) 
#  have differing signs. This root finding method works by halfing the interval between a and b, 
#  and checking which interval [a, (a+b)/2] or [(a+b)/2, b] contains the root. This is a consequence
#  of the Intermediate Value Theorem. The interval that contains the root is then 're-used' in the 
#  above process repeatedly until the method produces a value that meets the precision required.
# Test

from typing import Callable  # (For type hinting function)


def bisection(f: Callable, lower: float, upper: float, precision: float) -> float:
    """
    Approximates the root to a function using the bisection method.

    Args:
        f (Callable): A continuous function to approximate a root of
        lower (float): The lower bound of the interval which contains the root
        upper (float): The upper bound of the interval which contains the root
        precision (float): The maximum amount of error that is acceptable in method results

    Returns:
        (float): Value which, when passed to f, returns a number of magnitude < precision.
        
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
    
    # Actual method:
    mid = (lower + upper) / 2  # Split the interval into two smaller intervals
    
    while abs(f(mid)) > precision:  # Loop until the precision is met
        # Choosing the range for the new interval:
        if f(lower) * f(mid) < 0:
            upper = mid
        else:
            lower = mid
            
        # Set mid to the middle of the new interval:
        mid = (lower + upper) / 2
    
    return mid


