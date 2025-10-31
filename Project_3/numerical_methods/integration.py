"""
This module provides numerical methods for solving ordinary differential equations
of the form dy/dx = f(x, y).

Included methods
----------------
    1. Explicit Euler method
    2. Fourth-order Runge–Kutta method (RK4)
"""

from typing import Callable

def explicit_euler(
    f: Callable[[float, float], float],
    x0: int|float, y0:int|float,
    h: float, n: int,
) -> tuple[list[float], list[float]]:

    """
    Solve the initial value problem dy/dx = f(x, y) using the explicit Euler method.

    Parameters
    ----------
    f : Callable[[float, float], float]
        Function defining the derivative dy/dx = f(x, y).
    x0 : float
        Initial x value.
    y0 : float
        Initial y value at x0, i.e., y(x0) = y0.
    h : float
        Step size.
    n : int
        Number of y-points to compute, including the initial value.

    Returns
    -------
    tuple[list[float], list[float]]
        Lists of x and y values approximating the solution at x0 + j*h
        for j = 0, 1, ..., n-1.

    Example
    -------
    >>> f = lambda x: x**2 - 2
    >>> x_list_ee, y_list_ee = explicit_euler(f = f, x0 = 0, y0 = 0, h = 0.001, n = 10000)
    [0, 0.001, 0.002, 0.003, ...]  # e.g. time points
    [0, 0.0, 9.999998333333418e-10, 4.999997166667209e-09, ...]  # intermediate estimates
    """

    x_list, y_list = [x0], [y0]

    for _ in range(1,n):
        x_i, y_i = x_list[-1], y_list[-1]
        y_i = y_i + h * f(x_i, y_i)
        x_i = x_i + h
        x_list.append(x_i)
        y_list.append(float(y_i))

    return x_list, y_list

def explicit_runge_kutta4(
    f: Callable[[float, float], float],
    x0: float,
    y0: float,
    h: float,
    n: int
) -> tuple[list[float], list[float]]:
    """
    Solve the initial value problem dy/dx = f(x, y)
    using the classical 4th-order explicit Runge-Kutta method (RK4).

    Parameters
    ----------
    f : Callable[[float, float], float]
        Function defining the derivative dy/dx = f(x, y).
    x0 : float
        Initial x value.
    y0 : float
        Initial y value at x0, i.e., y(x0) = y0.
    h : float
        Step size.
    n : int
        Number of y-points to compute, including the initial value.

    Returns
    -------
    tuple[list[float], list[float]]
        Lists of x and y values approximating the solution at
        x0 + j*h for j = 0, 1, ..., n-1.
    
    Example
    -------
    >>> f = lambda x: x**2 - 2
    >>> x_list_erk, y_list_erk = explicit_runge_kutta4(f = f, x0 = 0, y0 = 0, h = 0.001, n = 10000)
    [0, 0.001, 0.002, 0.003, ...]  # e.g. time points 
    [0, 3.33-10, 2.67e-09, 9.00-09, ...]  # intermediate estimates
    """

    x_list, y_list = [x0], [y0]

    for _ in range(1, n):
        x_i, y_i = x_list[-1], y_list[-1]

        k1 = f(x_i, y_i)
        k2 = f(x_i + 0.5 * h, y_i + 0.5 * h * k1)
        k3 = f(x_i + 0.5 * h, y_i + 0.5 * h * k2)
        k4 = f(x_i + h, y_i + h * k3)

        y_new = y_i + (h / 6.0) * (k1 + 2*k2 + 2*k3 + k4)
        x_new = x_i + h

        x_list.append(x_new)
        y_list.append(float(y_new))

    return x_list, y_list
