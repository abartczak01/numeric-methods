import numpy as np
from integrals import *

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
def len_circle(x):
    return 4/np.sqrt(1-x**2)

def ellipse_derivative_squared(a, b, x):
    return np.divide(b**2 * x ** 2, a**4 - a**2 * x ** 2, where=np.abs(x) != a)

# def len_ellipse(a, b, x):
#     return 2 * np.sqrt(1 + b**2 * x**2/(a**4 - a**2 * x**2))

def ellipse_circumference(a, b):
    # Ramanujan's approximation for the circumference of an ellipse
    h = ((a - b)**2) / ((a + b)**2)
    circumference = np.pi * (a + b) * (1 + (3*h) / (10 + np.sqrt(4 - 3*h)))
    return circumference


def len_ellipse2(a, b, x):
    return 2 * np.sqrt(1 + ellipse_derivative_squared(a, b, x))

# https://math.stackexchange.com/questions/45089/what-is-the-length-of-a-sine-wave-from-0-to-2-pi
def len_sine(x):
    return np.sqrt(1+(np.cos(x))**2)


a = 2
b = 1
n = 100000
x = 2

I_mid_len_ellipse = a4_spline_interpolation2(-a, a, n, lambda x: len_ellipse2(a, b, x))
print(I_mid_len_ellipse, "spline")
# I_mid_len_ellipse = a1_riemann(-a, a, n, lambda x: len_ellipse2(a, b, x))
# print(I_mid_len_ellipse, "riemann")


a_circle, b_circle = -1, 1
a_parabola, b_parabola = 0, 1
a_sine, b_sine = 0, np.pi
a_ellipse, b_ellipse = 2, 1 
n = 100

exact_circle = np.pi
exact_ellipse = np.pi * a_ellipse * b_ellipse
exact_sine = - np.cos(b_sine) + np.cos(a_sine)
exact_parabola = b_parabola**3/3

# print(f"długość koła (π):")
# print(f"Riemann: {I_mid_len_circle}, Błąd: {np.abs(2*np.pi - I_mid_len_circle)}")
# print(f"Trapezoid: {I_trap_len_circle}, Błąd: {np.abs(2*np.pi - I_trap_len_circle)}")
# print(f"Simpson: {I_simp_len_circle}, Błąd: {np.abs(2*np.pi - I_simp_len_circle)}")
# print(f"Interpolacja wielomianami trzeciego stopnia: {I_spline_len_circle}, Błąd: {np.abs(2*np.pi - I_spline_len_circle)}")


# exact_parabola = b_parabola**3/3 - a_parabola**3/3
# x**3/3
# print(exact_circle, exact_ellipse, exact_sine, exact_parabola)

# Pole koła (wyznaczanie pi) s1
# I_mid_circle = a1_riemann(a_circle, b_circle, n, func_circle)
# I_trap_circle = a2_trapezoid(a_circle, b_circle, n, func_circle)
# I_simp_circle = a3_simpson(a_circle, b_circle, n, func_circle)
# I_spline_circle = a4_spline_interpolation(a_circle, b_circle, n, func_circle)

# # Pole pod wykresem paraboli s2
# I_mid_parabola = a1_riemann(a_parabola, b_parabola, n, func_parabola)
# I_trap_parabola = a2_trapezoid(a_parabola, b_parabola, n, func_parabola)
# I_simp_parabola = a3_simpson(a_parabola, b_parabola, n, func_parabola)
# I_spline_parabola = a4_spline_interpolation(a_parabola, b_parabola, n, func_parabola)

# Pole elipsy dla kilku półosi s3 

# I_mid_ellipse = a1_riemann(-a_ellipse, a_ellipse, n, lambda x: func_ellipse(a_ellipse, b_ellipse, x))
# I_trap_ellipse = a2_trapezoid(-a_ellipse, a_ellipse, n, lambda x: func_ellipse(a_ellipse, b_ellipse, x))
# I_simp_ellipse = a3_simpson(-a_ellipse, a_ellipse, n, lambda x: func_ellipse(a_ellipse, b_ellipse, x))
# I_spline_ellipse = a4_spline_interpolation(-a_ellipse, a_ellipse, n, lambda x: func_ellipse(a_ellipse, b_ellipse, x))

# # Pole pod wykresem sinus s4
# I_mid_sine = a1_riemann(a_sine, b_sine, n, func_sine)
# I_trap_sine = a2_trapezoid(a_sine, b_sine, n, func_sine)
# I_simp_sine = a3_simpson(a_sine, b_sine, n, func_sine)
# I_spline_sine = a4_spline_interpolation(a_sine, b_sine, n, func_sine)

# print(f"Pole koła (π):")
# print(f"Riemann: {I_mid_circle}, Błąd: {np.abs(np.pi - I_mid_circle)}")
# print(f"Trapezoid: {I_trap_circle}, Błąd: {np.abs(np.pi - I_trap_circle)}")
# print(f"Simpson: {I_simp_circle}, Błąd: {np.abs(np.pi - I_simp_circle)}")
# print(f"Interpolacja wielomianami trzeciego stopnia: {I_spline_circle}, Błąd: {np.abs(np.pi - I_spline_circle)}")

# print(f"\nPole pod wykresem paraboli na [0,1]:")
# print(f"Riemann: {I_mid_parabola}, Błąd: {np.abs(exact_parabola - I_mid_parabola)}")
# print(f"Trapezoid: {I_trap_parabola}, Błąd: {np.abs(exact_parabola - I_trap_parabola)}")
# print(f"Simpson: {I_simp_parabola}, Błąd: {np.abs(exact_parabola - I_simp_parabola)}")
# print(f"Interpolacja wielomianami trzeciego stopnia: {I_spline_parabola}, Błąd: {np.abs(exact_parabola - I_spline_parabola)}")

# print(f"\nPole elipsy (a={a_ellipse}, b={b_ellipse}):")
# print(f"Riemann: {I_mid_ellipse}, Błąd: {np.abs(exact_ellipse - I_mid_ellipse)}")
# print(f"Trapezoid: {I_trap_ellipse}, Błąd: {np.abs(exact_ellipse - I_trap_ellipse)}")
# print(f"Simpson: {I_simp_ellipse}, Błąd: {np.abs(exact_ellipse - I_simp_ellipse)}")
# print(f"Interpolacja wielomianami trzeciego stopnia: {I_spline_ellipse}, Błąd: {np.abs(exact_ellipse - I_spline_ellipse)}")

# print(f"\nPole pod wykresem sinus na [0, π]:")
# print(f"Riemann: {I_mid_sine}, Błąd: {np.abs(exact_sine - I_mid_sine)}")
# print(f"Trapezoid: {I_trap_sine}, Błąd: {np.abs(exact_sine - I_trap_sine)}")
# print(f"Simpson: {I_simp_sine}, Błąd: {np.abs(exact_sine - I_simp_sine)}")
# print(f"Interpolacja wielomianami trzeciego stopnia: {I_spline_sine}, Błąd: {np.abs(exact_sine - I_spline_sine)}")


# l1 - l3

# a_circle, b_circle = -np.sqrt(2)/2, np.sqrt(2)/2
# a_sine, b_sine = 0, 2 * np.pi
# I_mid_len_circle = a1_riemann(a_circle, b_circle, n, len_circle)
# I_trap_len_circle = a2_trapezoid(a_circle, b_circle, n, len_circle)
# I_simp_len_circle = a3_simpson(a_circle, b_circle, n, len_circle)
# I_spline_len_circle = a4_spline_interpolation(a_circle, b_circle, n, len_circle)

# I_mid_len_ellipse = a1_riemann(-a_ellipse, a_ellipse, n, lambda x: len_ellipse(a_ellipse, b_ellipse, x))
# I_trap_len_ellipse = a2_trapezoid(-a_ellipse, a_ellipse, n, lambda x: len_ellipse(a_ellipse, b_ellipse, x))
# I_simp_len_ellipse = a3_simpson(-a_ellipse, a_ellipse, n, lambda x: len_ellipse(a_ellipse, b_ellipse, x))
# I_spline_len_ellipse = a4_spline_interpolation(-a_ellipse, a_ellipse, n, lambda x: len_ellipse(a_ellipse, b_ellipse, x))

# I_mid_len_sine = a1_riemann(a_sine, b_sine, n, len_sine)
# I_trap_len_sine = a2_trapezoid(a_sine, b_sine, n, len_sine)
# I_simp_len_sine = a3_simpson(a_sine, b_sine, n, len_sine)
# I_spline_len_sine = a4_spline_interpolation(a_sine, b_sine, n, len_sine)

# print(I_mid_len_sine)
# print(I_trap_len_sine)
# print(I_simp_len_sine)
# print(I_spline_len_sine)
