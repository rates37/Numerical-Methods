# Author: Satya Jhaveri
#
# Heun's method aims to improve on Euler's method by finding the average slope, by taking the
#  mean of the value of the slope at the beginning of the step and the value of the slope at
#  the end of the step. This is called a predictor-corrector method, as we first predict the value
#  at the end of the slope, and then make a corretion step to (hopefully) produce a more accurate 
#  result.
# 
# Predictor Step: y_g = y_i + f(t_i, y_i)
#
# Corrector Step: y_(i+1) = y_i + 0.5 * h * (f(t_i, y_i) + f(t_(i+1), y_g))
#
from typing import Callable, Tuple, List
from math import floor

def heun(df: Callable, initial_x: float, final_x: float, initial_y: float, step: float) -> Tuple[List[float]]:
    """
    Approximates the solution to an ordinary differential equation using Heun's method on the derivative of the original function

    Args:
        df (Callable):              A function of two variables (independent, dependent) that is the 'dy/dx'
        initial_x (float):          The value of x at the initial point
        final_x (float):            The value of x at the final point
        initial_y (float):          The value of y at the initial point
        step(float):                The step size to use when approximating each solution point

    Raises:
        ValueError:                 If the final x value is less than the initial x value
        ValueError:                 If the step size is less than or equal to zero

    Returns:
        Tuple[x_vector, y_vector]:  A tuple of vectors, containing the x values, and corresponding approximated y values for each index
    """
    # Validating Inputs:
    if initial_x >= final_x:
        raise ValueError("Initial value of x cannot be greater than the final value of x")
    
    if step <= 0:
        raise ValueError("Euler method step size cannot be less than or equal to zero")
    
    # Actual Method:
    # Creating vector of x values:
    n = floor((final_x - initial_x) / step)
    width = (final_x - initial_x) / (n - 1)
    x = [initial_x + i*width for i in range(n)]  # linearly spaced vector of x values between initial and final x

    # Ensuring final_x is in the vector of x values:
    if final_x > x[n-1]:
        x.append(final_x)
        n += 1
    y = [initial_y for _ in range(n)]
    
    # Applying method:
    for i in range(n - 1):
        h = x[i + 1] - x[i]
        yg = y[i] + h * df(x[i], y[i])
        avg_grad = 0.5 * (df(x[i],y[i]) + df(x[i + 1], yg))
        y[i + 1] = y[i] + h * avg_grad
    
    return x, y

if __name__ == "__main__":
    # Plotting real vs approximated solution:
    
    def f(x,y):
        return y
    
    x, y = heun(f, 0, 4, 1, 0.125)
    from matplotlib import pyplot as plt
    from math import exp
    plt.plot(x,y)
    def sol(x):
        return exp(x)
    actual_y = [exp(i) for i in x]
    plt.plot(x,actual_y)
    plt.show()
    