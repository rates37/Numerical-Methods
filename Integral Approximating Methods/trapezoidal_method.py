# Author: Satya Jhaveri
#
# The trapezoidal method uses trapezoids to approximate the value of
#  an integral. It creates trapezoids that roughly fit the shape of the function
#  and finds the sum of the trapezoids between the intervals in order to
#  approximate the integral.
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
    if n < 1:
        raise ValueError("n must be greater than or equal to 1.")
    if a > b:
        raise ValueError("The lower bound of the integral cannot be more than the upper bound")
    
    # Actual Method:
    width = (b - a) / (n - 1)  # This is the width of each trapezoidal segment
    x = [a + i*width for i in range(n)]  # A vector of n linearly spaced x values between a and b
    
    return (width / 2) * (f(a) + 2 * sum([f(point) for point in x[2:-2]]) + f(x[-1]))
    

def trapezoidal_vec(x: List[float], y: List[float]) -> float:
    """
    Approximates the value of an integral using the trapezoidal method on discrete data.

    Args:
        x (List[float]): A list of the independent variable values
        y (List[float]): A list of the dependent variable values

    Raises:
        ValueError: If there is a different number of independent variable values than dependent variable values 
        ValueError: If there is only one point

    Returns:
        float: The approximated value of the integral
    """
    # Validating inputs:
    if len(x) != len(y):
        raise ValueError("The number of points in each vector must be equal.")
    
    if len(x) < 2:
        raise ValueError("Cannot integrate on less than two data points.")
    
    # Actual Method:
    n = len(x)
    acc = 0
    
    # Sorting the input data based on independent variable values:
    tuple_list = [(x[i], y[i]) for i in range(n)]
    tuple_list.sort(key=lambda x: x[0], reverse=False)
    x = [tuple_list[i][0] for i in range(n)]
    y = [tuple_list[i][1] for i in range(n)]
    
    for i in range(1, n):
        width = x[i] - x[i - 1]
        acc += (width / 2) * (y[i-1]+y[i])
    return acc


if __name__ == "__main__":
    def f(x): return x*x
    a,b = -5, 5
    n = 1000000
    print(trapezoidal(f,a,b,n))
    x = [5,4,3,2,1]
    y = [25, 16, 9, 4, 1]
    print(trapezoidal_vec(x,y))
    