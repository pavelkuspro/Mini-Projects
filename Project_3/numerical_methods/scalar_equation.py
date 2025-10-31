"""
This module contains numerical methods for solving equations of one real variable.

Included methods:
    1. Bisection method
    2. Newton method
    3. Regula Falsi method
    4. Secant method
"""

from typing import Callable
import warnings

def bisection(
    f: Callable[[float], float],
    a: int|float, b:int|float,
    tol:float=1e-7,
    max_iter:int=100
) -> list[float]:
    """
    Solve f(x) = 0 using the bisection method.

    Parameters
    ----------
    f : Callable[[float], float]
        The function for which we want to find a root.
    a : int|float
        Left endpoint of the interval.
    b : int|float
        Right endpoint of the interval.
    tol : float, optional
        Desired tolerance (default is 1e-7).
    max_iter : int, optional
        Maximum number of iterations (default is 100).

    Returns
    -------
    list of float
        Estimates of the root at each iteration.

    Raises
    ------
    ValueError
        If f(a) and f(b) do not have opposite signs.
    UserWarning
        If maximum iterations are reached without achieving the desired tolerance.
    
    Example
    -------
    >>> f = lambda x: x**2 - 2
    >>> bisection(f, 0, 2)
    [1.0, 1.5, 1.25, ...]  # intermediate estimates
    """

    if f(a) * f(b) >= 0:
        raise ValueError("Endpoints must have different signs.")

    # list to store estimates of the root
    estimates = []

    for _ in range(max_iter):
        c = (a + b) / 2  # midpoint of current interval
        estimates.append(c)  # store estimate

        # check convergence
        if len(estimates) > 1 and abs(estimates[-1] - estimates[-2]) < tol:
            return estimates

        # decide which half interval contains the root
        if f(c) * f(a) < 0:
            b = c
        else:
            a = c

    # return all estimates if max iterations reached
    warnings.warn("The accuracy has not been reached.")
    return estimates

def newton(
    f: Callable[[float], float],
    f_prime: Callable[[float], float],
    x0: float,
    tol: float = 1e-7,
    max_iter: int = 100
) -> list[float]:
    """
    Solve f(x) = 0 using the Newton (tangent) method.

    Parameters
    ----------
    f : Callable[[float], float]
        The function for which we want to find a root.
    f_prime : Callable[[float], float]
        Derivative of the function f.
    x0 : int|float
        Initial guess for the root.
    tol : float, optional
        Desired tolerance for the function value (default is 1e-7).
    max_iter : int, optional
        Maximum number of iterations (default is 100).

    Returns
    -------
    list of float
        Estimates of the root at each iteration.

    Raises
    ------
    ValueError
        If derivative is zero at any iteration.
    UserWarning
        If maximum iterations are reached without achieving the desired tolerance.

    Example
    -------
    >>> f = lambda x: x**2 - 2
    >>> f_prime = lambda x: 2*x
    >>> newton_method(f, f_prime, x0=1.0)
    [1.0, 1.5, 1.416666..., ...]
    """

    estimates = [x0]
    x_current = x0

    for _ in range(max_iter):
        f_val = f(x_current)
        f_prime_val = f_prime(x_current)

        if f_prime_val == 0:
            raise ValueError("Derivative is zero. The Newton method failed.")

        x_new = x_current - f_val / f_prime_val
        estimates.append(x_new)

        if len(estimates) > 1 and abs(estimates[-1] - estimates[-2]) < tol:
            return estimates

        # if continuing, update x_current
        x_current = x_new

    # return all estimates if max iterations reached
    warnings.warn("The accuracy has not been reached.")
    return estimates

def regula_falsi(
    f: Callable[[float], float],
    a: int|float, b: int|float,
    tol: float = 1e-7,
    max_iter: int = 100,
) -> list[float]:
    """
    Solve f(x) = 0 using the regula falsi method.

    Parameters:
    ----------
        f (Callable[[float], float]):
            The function for which we want to find a root.    
        a : int|float
            Left endpoint of the interval.
        b : int|float
            Right endpoint of the interval.
        tol : float, optional
            Desired tolerance (default is 1e-7).
        max_iter : int, optional
            Maximum number of iterations (default is 100).

    Returns
    -------
    list of float
        Estimates of the root at each iteration.

    Raises
    ------
    ValueError
        If f(a) and f(b) do not have opposite signs.
    UserWarning
        If maximum iterations are reached without achieving the desired tolerance.
    
    Example
    -------
    >>> f = lambda x: x**2 - 2
    >>> regula_falsi(f, 0, 2)
    [1.0, 1.3333333333333333,  1.4, ...]  # intermediate estimates
    """

    if f(a) * f(b) >= 0:
        raise ValueError("Endpoints must have different signs.")

    # list to store estimates of the root
    estimates = []

    for _ in range(max_iter):

        # the crossection of the line connecting [a,f(a)] and [b,f(b)] with the x-axis
        c = f(b) * a / ( f(b)-f(a) ) - f(a) * b / ( f(b)-f(a) )

        estimates.append(c)  # store estimate

        # check convergence
        if len(estimates) > 1 and abs(estimates[-1] - estimates[-2]) < tol:
            return estimates

        # decide which half interval contains the root
        if f(c) * f(a) < 0:
            b = c
        else:
            a = c

    # return all estimates if max iterations reached
    warnings.warn("The accuracy has not been reached.")
    return estimates

def secant(
    f: Callable[[float], float],
    x0: int|float,
    x1: int|float,
    tol: float = 1e-7,
    max_iter: int = 100
) -> list[float]:
    """
    Solve f(x) = 0 using the secant method.

    Parameters
    ----------
    f : Callable[[float], float]
        The function for which we want to find a root.
    x0 : int|float
        The first starting point to find the root.
    x1 : int|float
        The second starting point to find the root.
    tol : float, optional
        Desired tolerance for the function value (default is 1e-7).
    max_iter : int, optional
        Maximum number of iterations (default is 100).

    Returns
    -------
    list of float
        Estimates of the root at each iteration.

    Raises
    ------
    ValueError
        If derivative approximation is zero at any iteration.
    UserWarning
        If maximum iterations are reached without achieving the desired tolerance.

    Example
    -------
    >>> f = lambda x: x**2 - 2
    >>> secant(f, 0, 2)
    [0, 2, 1.0, ...]
    """

    # list to store estimates of the root
    estimates = [x0, x1]

    for _ in range(max_iter):

        f0, f1 = f(x0), f(x1)  # function values at x0, x1

        if f1 - f0 == 0:
            raise ValueError("Derivative approximation is zero. The Secant method failed.")

        x_new = x1 - f1 * (x1 - x0) / (f1 - f0) # new estimated using x0, x1
        estimates.append(x_new)  # store estimate

        # check convergence
        if len(estimates) > 1 and abs(estimates[-1] - estimates[-2]) < tol:
            return estimates

        # if continuing, update x0, x1
        x0, x1 = x1, x_new

    # return all estimates if max iterations reached
    warnings.warn("The accuracy has not been reached.")
    return estimates
