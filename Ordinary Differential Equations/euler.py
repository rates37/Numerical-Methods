# Author: Satya Jhaveri
#
# The Forward Euler method is a numerical method for approximating the solutions
#  to ordinary differential equations (ODEs), when given an initial value. It is the
#  most basic method of solving ODEs. The method works by choosing a step size (the 
#  smaller the step size, the more accurate the solution). Call this step size Δt.
#  Let t_k be a sequence of t values between the initial and final value. We can say
#  that t_(k+1) = t_k + Δt. The solution values can then be approximated in steps as:
#  y_(k+1) = y_k + Δt * dy/dt(t_k, y_k).
#
# The forward euler method is an explicit method for approximating the solutions
# to ODEs. Explicit methods calculate the value of the solution without solving
#  algebraic equations.
#
# 
#
from typing import Callable, Tuple, List
from math import floor
def forward_euler(df: Callable, initial_x: float, final_x: float, initial_y: float, step: float) -> Tuple[List[float]]:
    """
    Approximates the solution to an ordinary differential equation using Euler's method on the derivative of the original function

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
        Tuple[x_vector, y_vector:   A tuple of vectors, containing the x values, and corresponding approximated y values for each index
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
        y[i + 1] = y[i] + df(x[i], y[i]) * h
    
    return x, y
    
    
if __name__ == "__main__":
    def f(x,y):
        return y
    
    x, y = forward_euler(f, 0, 4, 1, 0.005)
    from matplotlib import pyplot as plt
    from math import exp
    plt.plot(x,y)
    def sol(x):
        return exp(x)
    actual_y = [exp(i) for i in x]
    plt.plot(x,actual_y)
    plt.show()
