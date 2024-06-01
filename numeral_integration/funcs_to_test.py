import numpy as np
from scipy import special
from algorithms import *
from scipy.special import ellipe

# s1-s4
def func_circle(x):
    return 2 * np.sqrt(1 - x**2)

def func_parabola(x):
    return x**2

def func_ellipse(a, b, x):
    return 2 * b * np.sqrt(1 - (x/a)**2)

def func_sine(x):
    return np.sin(x)

# https://en.wikipedia.org/wiki/Arc_length#Numerical_integration
# obliczam ćwiartkę długości i mnożę razy 4

# l1-l3
def len_circle(x):
    return 4/np.sqrt(1-x**2)

def ellipse_derivative_squared(a, b, x):
    return np.divide(b**2 * x ** 2, a**4 - a**2 * x ** 2, where=np.abs(x) != a)

def len_ellipse(a, b, x):
    return 2 * np.sqrt(1 + ellipse_derivative_squared(a, b, x))

def len_sine(x):
    return np.sqrt(1+(np.cos(x))**2)

def exact_area_ellipse(a,b):
    return np.pi * a * b

# 4aE(e^2)
def exact_len_ellipse(a, b):
    if a < b:
        a, b = b, a  # Ensure that a is the semi-major axis and b is the semi-minor axis
    e = np.sqrt(1 - (b / a)**2)
    circumference = 4 * a * ellipe(e**2)
    return circumference


def exponential(x):
    return np.exp(x)

def poly5(x):
    return x*(x-1)*(x-3)*(x-5)*(x-6)


def sin20x(x):
    return x * np.sin(20*x)

def sq_rt(x):
    return np.sqrt(x)

# całki dla powyzszych funkcji
# całka dla e^x = e^x
def integral_poly5(x):
    # return (540 * x**2 - 612 * x**3 + 231 * x**4 - 36*x**5 + 2*x**6)/12
    return x**6/6 -3 * x ** 5 + (77/4) * x**4 -51*x**3 + 45*x**2

def integral_cos10(x):
    return np.sin(10 * x)/10

def integral_sin20x(x):
    return 1/400 * (np.sin(20*x) - 20 * x * np.cos(20*x))

def integral_sq_rt(x):
    return 2/3 * x**(3/2)
