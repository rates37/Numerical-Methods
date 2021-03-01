# Author: Satya Jhaveri
#
# Simpson's One Third Rule works similarly to how the trapezoidal method works, in that
#  it fits shapes to points on the function, however instead of fitting a trapezoid to
#  two consecutive points, this method fits a parabola to three consecutive points.
#  The parabola is then integrated over the domain of the points used to construct it
#  and the total area from all parabolas are summed to obtain the approximation for the
#  integral. 
#  The value of each small integration can be found individually, or all can be found
#  at once using the Composite Simpson's 1/3 Rule, which provides a formula for the
#  summation of all values at once, which is much more convenient.
# 
# This file also contains a version of this method that can be used on
#  discrete, non-uniform input data.
#

from typing import List, Callable


def simpsons_13(f: Callable, a: float, b: float, n: int) -> float:
    """
    Approximates the value of a definite integral using the Simpson's 1/3 rule and a specified number of points.

    Args:
        f (Callable): A continuous function to integrate over
        a (float): The lower integral interval
        b (float): The upper integral interval
        n (int): The number of points to use in the approximation

    Raises:
        ValueError: If lower integral is higher than upper integral
        ValueError: If the n is even 
        ValueError: If n is less than three

    Returns:
        float: The approximated value of the integral
    """
    # Validating Inputs:
    if n < 3:
        raise ValueError("Cannot use less than 3 points.")
    
    if n % 2 == 0:
        raise ValueError("Cannot use an even number of points.")
    
    if a > b:
        raise ValueError("The lower bound of the integral cannot be more than the upper bound")
    
    
    # Actual method:
    width = (b - a) / (n - 1)
    x = [a + i*width for i in range(n)]  # linearly spaced vector of x values between a and b
    
    odd_sum = 2* sum([f(i) for i in x[3:-3:2]])
    even_sum = 4 * sum([f(i) for i in x[2:-2:2]])
    integral = (width / 3) * (f(a) + odd_sum + even_sum + f(b))
    return integral


def simpsons_13_vec(x: List[float], y: List[float]) -> float:
    """
    Approximates the value of an integral using the Simpson's 1/3 method on discrete data.

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
    
    if len(x) < 3:
        raise ValueError("Cannot integrate on less than three data points.")
    
    if len(x) % 2 == 0:
        raise ValueError("Cannot integrate on an even number of points.")
    
    # Actual Method:
    n = len(x)
    # Sorting the input data based on independent variable values:
    tuple_list = [(x[i], y[i]) for i in range(n)]
    tuple_list.sort(key=lambda x: x[0], reverse=False)
    x = [tuple_list[i][0] for i in range(n)]
    y = [tuple_list[i][1] for i in range(n)]
    
    
    odd_sum, even_sum = 0, 0
    # Evaluating the even sums:
    for i in range(1, n, 2):
        width = abs(x[i] - x[i - 1])
        even_sum += (width / 3) * 4 * y[i]
    
    # Evaluating the odd sums:
    for i in range(2, n - 1, 2):
        width = abs(x[i] - x[i - 1])
        odd_sum += (width / 3) * 2 * y[i]
    
    # Evaluating the final integral:
    integral = ((x[1] - x[0]) / 3) * y[0] + even_sum + odd_sum + ((x[-1] - x[-2]) / 3) * y[-1]
    return integral


if __name__ == "__main__":
    def f(x): return x*x
    a,b = -5, 5
    n = 10001
    print(simpsons_13(f,a,b,n))

    x = [5,4,3,2,1, 0, -1]
    y = [f(i) for i in x]
    print(simpsons_13_vec(x,y))