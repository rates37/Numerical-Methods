# Author: Satya Jhaveri
#
# Simpson's Three Eighths Rule is the exact same as Simpson's 1/3 rule, however instead
#  of fitting a parabola to three points, a cubic polynomial is fitted to four 
#  consecutive points. This reduces the amount of error even more.
# 
#  The value of each small integration can be found individually, or all can be found
#  at once using the Composite Simpson's 3/8 Rule, which provides a formula for the
#  summation of all values at once, which is much more convenient.
# 
# This file also contains a version of this method that can be used on
#  discrete, non-uniform input data.
#

from typing import List, Callable


def simpsons_38(f: Callable, a: float, b: float, n: int) -> float:
    """
    Approximates the value of a definite integral using the Simpson's 3/8 rule and a specified number of points.

    Args:
        f (Callable): A continuous function to integrate over
        a (float): The lower integral interval
        b (float): The upper integral interval
        n (int): The number of points to use in the approximation

    Raises:
        ValueError: If lower integral is higher than upper integral
        ValueError: If the n is not congruent to four (mod 3)
        ValueError: If n is less than four

    Returns:
        float: The approximated value of the integral
    """
    # Validating Inputs:
    if n < 4:
        raise ValueError("Cannot use less than 3 points.")
    
    if (n - 1) % 3 != 0:
        raise ValueError("Cannot use a value of n that is not congruent to 4 (mod 3).")
    
    if a > b:
        raise ValueError("The lower bound of the integral cannot be more than the upper bound")
    
    # Actual Method:
    width = (b - a) / (n - 1)
    x = [a + i*width for i in range(n)]  # linearly spaced vector of x values between a and b
    
    # Evaluating the sums:
    sum1 = 3 * sum([f(i) for i in x[1:-3:3]])
    sum2 = 3 * sum([f(i) for i in x[2:-2:3]])
    sum3 = 2 * sum([f(i) for i in x[3:-4:3]])
    
    # Summing the overall integral:
    integral = (3 * width / 8) * (f(a) + sum1 + sum2 + sum3 + f(b))
    return integral


def simpsons_38_vec(x: List[float], y: List[float]) -> float:
    """
    Approximates the value of an integral using the Simpson's 3/8 method on discrete data.

    Args:
        x (List[float]): A list of the independent variable values
        y (List[float]): A list of the dependent variable values

    Raises:
        ValueError: If there is a different number of independent variable values than dependent variable values 
        ValueError: If there is less than three data points
        valueError: If there is an even number of data points

    Returns:
        float: The approximated value of the integral
    """
    # Validating inputs:
    if len(x) != len(y):
        raise ValueError("The number of points in each vector must be equal.")
    
    if len(x) < 4:
        raise ValueError("Cannot integrate on less than three data points.")
    
    if (len(x) - 1) % 3 != 0:
        raise ValueError("Cannot integrate on a number of data points that is not congruent to 4 (mod 3).")
    
    # Actual Method:
    n = len(x)
    # Sorting the input data based on independent variable values:
    tuple_list = [(x[i], y[i]) for i in range(n)]
    tuple_list.sort(key=lambda x: x[0], reverse=False)
    x = [tuple_list[i][0] for i in range(n)]
    y = [tuple_list[i][1] for i in range(n)]
    
    sum1, sum2, sum3 = 0, 0, 0
    # Evaluating the sums:
    for i in range(1, n - 2, 3):
        width = x[i] - x[i - 1]
        sum1 += (3 * width / 8) * 3 * y[i]
    
    for i in range(2, n - 1, 3):
        width = x[i] - x[i - 1]
        sum2 += (3 * width / 8) * 3 * y[i]
    
    for i in range(3, n - 3, 3):
        width = x[i] - x[i - 1]
        sum3 += (3 * width / 8) * 2 * y[i]
    
    
    # Summing overall integral:
    integral = ((x[1] - x[0]) * 3 / 8) * y[0] + sum1 + sum2 + sum3 + ((x[- 1] - x[- 2]) * 3 / 8) * y[-1]
    return integral
