import numpy as np
import matplotlib.pyplot as plt
from funcs_to_test import *

from zad1 import oblicz_obwod, oblicz_wektory_nkata


def test_z1h1():
    roznice = []
    ns = list(range(70000, 500000, 5000))
    for n in ns:
        print(n)
        wektory = oblicz_wektory_nkata(n)
        obwod = oblicz_obwod(wektory)
        roznica = np.abs(np.pi - obwod/2)
        roznice.append(roznica)

    print(roznice)
    print(min(roznice))
    plt.plot(ns, roznice, marker='.', linestyle='None')
    plt.xlabel(r'Liczba boków wielokąta $n$')
    plt.ylabel(r'Błąd w skali logarytmicznej')
    plt.grid(True)
    plt.yscale('log')
    plt.savefig('h5_zad1.png')


test_z1h1()

def test_z3h5_pole():
    n_values = list(range(100000, 300000, 10000))

    exact_circle = np.pi
    b_circle = 1
    a_circle = -1

    errors_mid = []
    errors_trap = []
    errors_simp = []
    errors_spline = []

    for n in n_values:
        print(n)
        I_mid_circle = a1_riemann(a_circle, b_circle, n, func_circle)
        I_trap_circle = a2_trapezoid(a_circle, b_circle, n, func_circle)
        I_simp_circle = a3_simpson(a_circle, b_circle, n, func_circle)
        I_spline_circle = a4_spline_interpolation(a_circle, b_circle, n, func_circle)

        errors_mid.append(np.abs(exact_circle - I_mid_circle))
        errors_trap.append(np.abs(exact_circle - I_trap_circle))
        errors_simp.append(np.abs(exact_circle - I_simp_circle))
        errors_spline.append(np.abs(exact_circle - I_spline_circle))

    print(min(errors_mid))
    print(min(errors_trap))
    print(min(errors_simp))
    print(min(errors_spline))
    plt.plot(n_values, errors_mid, marker='.', label='Prostokąty', linestyle='None')
    plt.plot(n_values, errors_trap, marker='.',label='Trapezy', linestyle='None')
    plt.plot(n_values, errors_simp, marker='.',label='Simpson', linestyle='None')
    plt.plot(n_values, errors_spline, marker='.',label='CSI', linestyle='None')

    plt.yscale('log')
    plt.grid(True)
    plt.xlabel('Liczba podziałów (n)')
    plt.ylabel('Błąd')
    # plt.title('Błąd w wyznaczaniu libcz')
    plt.legend()
    plt.grid(True)
    plt.savefig("h5_zad3_pole.png")

test_z3h5_pole()

def test_z3h5_len():
    n_values = list(range(100000, 300000, 10000))
    # n_values = [500000, 1000000, 1500000, 2000000]

    exact_circle = np.pi
    a_circle, b_circle = -np.sqrt(2)/2, np.sqrt(2)/2

    errors_mid = []
    errors_trap = []
    errors_simp = []
    errors_spline = []

    for n in n_values:
        print(n)
        I_mid_circle = a1_riemann(a_circle, b_circle, n, len_circle)
        I_trap_circle = a2_trapezoid(a_circle, b_circle, n, len_circle)
        I_simp_circle = a3_simpson(a_circle, b_circle, n, len_circle)
        I_spline_circle = a4_spline_interpolation(a_circle, b_circle, n, len_circle)

        errors_mid.append(np.abs(exact_circle - I_mid_circle/2))
        errors_trap.append(np.abs(exact_circle - I_trap_circle/2))
        errors_simp.append(np.abs(exact_circle - I_simp_circle/2))
        errors_spline.append(np.abs(exact_circle - I_spline_circle/2))

    print(min(errors_mid))
    print(min(errors_trap))
    print(min(errors_simp))
    print(min(errors_spline))
    plt.plot(n_values, errors_mid, marker='.', label='Prostokąty', linestyle='None')
    plt.plot(n_values, errors_trap, marker='.',label='Trapezy', linestyle='None')
    plt.plot(n_values, errors_simp, marker='.',label='Simpson', linestyle='None')
    plt.plot(n_values, errors_spline, marker='.',label='CSI', linestyle='None')

    plt.yscale('log')
    plt.grid(True)
    plt.xlabel('Liczba podziałów (n)')
    plt.ylabel('Błąd')
    plt.legend()
    plt.grid(True)
    plt.savefig("h5_zad3_len2.png")

test_z3h5_len()
