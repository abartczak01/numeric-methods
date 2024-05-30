import numpy as np
from funcs_to_test import *
from scipy.special import ellipeinc

n = 10000

# s1 koło
exact_circle = np.pi
b_circle = 1
a_circle = -1
I_mid_circle = a1_riemann(a_circle, b_circle, n, func_circle)
I_trap_circle = a2_trapezoid(a_circle, b_circle, n, func_circle)
I_simp_circle = a3_simpson(a_circle, b_circle, n, func_circle)
I_spline_circle = a4_spline_interpolation(a_circle, b_circle, n, func_circle)

print(f"Pole koła (π):")
print(f"Prostokąty: {I_mid_circle}, Błąd: {np.abs(exact_circle - I_mid_circle)}")
print(f"Trapezoid: {I_trap_circle}, Błąd: {np.abs(exact_circle - I_trap_circle)}")
print(f"Simpson: {I_simp_circle}, Błąd: {np.abs(exact_circle - I_simp_circle)}")
print(f"Interpolacja wielomianami trzeciego stopnia: {I_spline_circle}, Błąd: {np.abs(exact_circle - I_spline_circle)}")

# # s2 pole pod parabolą [0,1]
exact_parabola = 1/3
a_parabola = 0
b_parabola = 1
I_mid_parabola = a1_riemann(a_parabola, b_parabola, n, func_parabola)
I_trap_parabola = a2_trapezoid(a_parabola, b_parabola, n, func_parabola)
I_simp_parabola = a3_simpson(a_parabola, b_parabola, n, func_parabola)
I_spline_parabola = a4_spline_interpolation(a_parabola, b_parabola, n, func_parabola)

print(f"\nPole pod wykresem paraboli na [0,1]:")
print(f"Riemann: {I_mid_parabola}, Błąd: {np.abs(exact_parabola - I_mid_parabola)}")
print(f"Trapezoid: {I_trap_parabola}, Błąd: {np.abs(exact_parabola - I_trap_parabola)}")
print(f"Simpson: {I_simp_parabola}, Błąd: {np.abs(exact_parabola - I_simp_parabola)}")
print(f"Interpolacja wielomianami trzeciego stopnia: {I_spline_parabola}, Błąd: {np.abs(exact_parabola - I_spline_parabola)}")

# s3 pole dla elips
a_arr = [1.5, 5, 10, 15, 200]
b_arr = [1, 1, 1, 16, 100]
for i in range(len(a_arr)):
    a_ellipse = a_arr[i]
    b_ellipse = b_arr[i]
    exact_ellipse = exact_area_ellipse(a_ellipse, b_ellipse)
    I_mid_ellipse = a1_riemann(-a_ellipse, a_ellipse, n, lambda x: func_ellipse(a_ellipse, b_ellipse, x))
    I_trap_ellipse = a2_trapezoid(-a_ellipse, a_ellipse, n, lambda x: func_ellipse(a_ellipse, b_ellipse, x))
    I_simp_ellipse = a3_simpson(-a_ellipse, a_ellipse, n, lambda x: func_ellipse(a_ellipse, b_ellipse, x))
    I_spline_ellipse = a4_spline_interpolation(-a_ellipse, a_ellipse, n, lambda x: func_ellipse(a_ellipse, b_ellipse, x))

    print(f"\nPole elipsy (a={a_ellipse}, b={b_ellipse}):")
    print(f"Riemann: {I_mid_ellipse}, Błąd: {np.abs(exact_ellipse - I_mid_ellipse)}")
    print(f"Trapezoid: {I_trap_ellipse}, Błąd: {np.abs(exact_ellipse - I_trap_ellipse)}")
    print(f"Simpson: {I_simp_ellipse}, Błąd: {np.abs(exact_ellipse - I_simp_ellipse)}")
    print(f"Interpolacja wielomianami trzeciego stopnia: {I_spline_ellipse}, Błąd: {np.abs(exact_ellipse - I_spline_ellipse)}")


# s4 pole sinus
exact_sine = 2
a_sine = 0
b_sine = np.pi
I_mid_sine = a1_riemann(a_sine, b_sine, n, func_sine)
I_trap_sine = a2_trapezoid(a_sine, b_sine, n, func_sine)
I_simp_sine = a3_simpson(a_sine, b_sine, n, func_sine)
I_spline_sine = a4_spline_interpolation(a_sine, b_sine, n, func_sine)

print(f"\nPole pod wykresem sinus na [0, π]:")
print(f"Riemann: {I_mid_sine}, Błąd: {np.abs(exact_sine - I_mid_sine)}")
print(f"Trapezoid: {I_trap_sine}, Błąd: {np.abs(exact_sine - I_trap_sine)}")
print(f"Simpson: {I_simp_sine}, Błąd: {np.abs(exact_sine - I_simp_sine)}")
print(f"Interpolacja wielomianami trzeciego stopnia: {I_spline_sine}, Błąd: {np.abs(exact_sine - I_spline_sine)}")

# # l1
a_circle, b_circle = -np.sqrt(2)/2, np.sqrt(2)/2
exact_len_circle = 2 * np.pi
I_mid_len_circle = a1_riemann(a_circle, b_circle, n, len_circle)
I_trap_len_circle = a2_trapezoid(a_circle, b_circle, n, len_circle)
I_simp_len_circle = a3_simpson(a_circle, b_circle, n, len_circle)
I_spline_len_circle = a4_spline_interpolation(a_circle, b_circle, n, len_circle)
print(f"Pole koła (π):")
print(f"Prostokąty: {I_mid_len_circle}, Błąd: {np.abs(exact_len_circle - I_mid_circle)}")
print(f"Trapezoid: {I_trap_len_circle}, Błąd: {np.abs(exact_len_circle - I_trap_circle)}")
print(f"Simpson: {I_simp_len_circle}, Błąd: {np.abs(exact_len_circle - I_simp_circle)}")
print(f"Interpolacja wielomianami trzeciego stopnia: {I_spline_len_circle}, Błąd: {np.abs(exact_len_circle - I_spline_circle)}")


# # l2
a_arr = [1.5, 5, 10, 15, 200]
b_arr = [1, 1, 1, 16, 100]
for i in range(len(a_arr)):
    a_ellipse = a_arr[i]
    b_ellipse = b_arr[i]
    exact_ellipse = exact_len_ellipse(a_ellipse, b_ellipse)
    I_mid_ellipse = a1_riemann(-a_ellipse, a_ellipse, n, lambda x: len_ellipse(a_ellipse, b_ellipse, x))
    I_trap_ellipse = a2_trapezoid(-a_ellipse, a_ellipse, n, lambda x: len_ellipse(a_ellipse, b_ellipse, x))
    I_simp_ellipse = a3_simpson(-a_ellipse, a_ellipse, n, lambda x: len_ellipse(a_ellipse, b_ellipse, x))
    I_spline_ellipse = a4_spline_interpolation(-a_ellipse, a_ellipse, n, lambda x: len_ellipse(a_ellipse, b_ellipse, x))

    print(f"\nObwód elipsy (a={a_ellipse}, b={b_ellipse}):")
    print(f"Riemann: {I_mid_ellipse}, Błąd: {np.abs(exact_ellipse - I_mid_ellipse)}")
    print(f"Trapezoid: {I_trap_ellipse}, Błąd: {np.abs(exact_ellipse - I_trap_ellipse)}")
    print(f"Simpson: {I_simp_ellipse}, Błąd: {np.abs(exact_ellipse - I_simp_ellipse)}")
    print(f"Interpolacja wielomianami trzeciego stopnia: {I_spline_ellipse}, Błąd: {np.abs(exact_ellipse - I_spline_ellipse)}")

# l3
# porównujemy do przyblizenia z biblioteki zcipy
a_sine, b_sine = 0, 2 * np.pi
exact_sine = np.sqrt(2) * (ellipeinc(b_sine, 1/2) - ellipeinc(a_sine, 1/2))
print(np.sqrt(1+(np.cos(2 * np.pi))**2))
I_mid_len_sine = a1_riemann(a_sine, b_sine, n, len_sine)
I_trap_len_sine = a2_trapezoid(a_sine, b_sine, n, len_sine)
I_simp_len_sine = a3_simpson(a_sine, b_sine, n, len_sine)
I_spline_len_sine = a4_spline_interpolation(a_sine, b_sine, n, len_sine)
print(f"\nDługość sin na [0, 2π]:")
print(f"Riemann: {I_mid_len_sine}, Błąd: {np.abs(exact_sine - I_mid_len_sine)}")
print(f"Trapezoid: {I_trap_len_sine}, Błąd: {np.abs(exact_sine - I_trap_len_sine)}")
print(f"Simpson: {I_simp_len_sine}, Błąd: {np.abs(exact_sine - I_simp_len_sine)}")
print(f"Interpolacja wielomianami trzeciego stopnia: {I_spline_len_sine}, Błąd: {np.abs(exact_sine - I_spline_len_sine)}")
