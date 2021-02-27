# Author: Satya Jhaveri
#
# The rectangle method is the most basic method for integral approximation.
#
# As the name suggests, this method uses rectangles to approximate the value of
#  an integral. It creates rectangles that roughly fit the shape of the function
#  and finds the sum of the rectangles between the intervals.
# 
# This file also contains a version of the rectangle method that can be used on
#  discrete, non-uniform input data.
#

from typing import Callable, List

def rectangle(f: Callable, a: float, b: float, n: int) -> int:
    """
    Calculates the value of a definite integral using the rectangle method using a specified number of rectangles.

    Args:
        f (Callable): A continuous function to integrate over
        a (float): The lower integral interval
        b (float): The upper integral interval
        n (int): The number of rectangles to use in the approximation

    Raises:
        ValueError: If lower integral is higher than upper integral
        ValueError: If the number of rectangles is less than 1

    Returns:
        int: The approximated value of the integral
    """
    # Checking Inputs:
    if a > b:
        raise ValueError("Lower integral interval must be lower than upper interval.")
    if n < 1:
        raise ValueError("The number of rectangles to use cannot be less than one")
    
    # Actual method:
    step = (b - a) / n
    acc = 0
    for i in range(n):
        acc += step * f(a + i * step)
    return acc


def rectangle_vec(x: List[float], y: List[float]) -> float:
    """
    Approximates the value of an integral using the rectangle method on discrete data.
    Note: This method does not include the first data point and thus is very useless. However it establishes concepts 
            of how to handle discrete data, which prove useful in more complex integral-approximating methods.

    Args:
        x (List[float]): A list of the independent variable values
        y (List[float]): A list of the dependent variable values

    Raises:
        ValueError: If there is a different number of independent variable values than dependent variable values

    Returns:
        float: The approximated value of the integral
    """
    # Validating inputs:
    if len(x) != len(y):
        raise ValueError("The number of points in each vector must be equal.")
    
    # Actual Method:
    n = len(x)
    
    # Sorting the input data based on independent variable values:
    tuple_list = [(x[i], y[i]) for i in range(n)]
    tuple_list.sort(key=lambda x: x[0], reverse=False)
    x = [tuple_list[i][0] for i in range(n)]
    y = [tuple_list[i][1] for i in range(n)]
    
    acc = 0
    for i in range(1, n):
        acc += (x[i] - x[i-1]) * y[i]
    
    return acc
