import numpy as np
from funcs_to_test import *

exact_values = {
    'exponential': np.exp(3) - np.exp(-3),  # -3 do 3
    'poly5': integral_poly5(6) - integral_poly5(0),  # 0 do 6
    'cos10': integral_cos10(3/2 * np.pi) - integral_cos10(0),  # 0 do 3/2pi
    'sin20x': integral_sin20x(3/2 * np.pi) - integral_sin20x(0),  # 0 do 3/2pi
    'sq_rt': integral_sq_rt(6) - integral_sq_rt(0)  # 0 do 6
}

# Słownik z funkcjami, przedziałami i dokładnymi wartościami
functions = {
    'exponential': [exponential, -3, 3, exact_values['exponential']],
    'poly5': [poly5, 0, 6, exact_values['poly5']],
    'cos10': [cos10, 0, 3/2 * np.pi, 0],
    'sin20x': [sin20x, 0, 3/2 * np.pi, exact_values['sin20x']],
    'sq_rt': [sq_rt, 0, 6, exact_values['sq_rt']]
}

# dokładne wartości sprawdzone z wolfram alfa

n_values = list(range(100, 10101, 500))
print(n_values)

# Testowanie metod
results = {}
for name, (func, a, b, exact) in functions.items():
    results[name] = {}
    for n in n_values:
        riemann = a1_riemann(a, b, n, func)
        trapezoid = a2_trapezoid(a, b, n, func)
        simpson = a3_simpson(a, b, n, func)
        spline = a4_spline_interpolation(a, b, n, func)
        results[name][n] = {
            'Error Rectangle': abs(riemann - exact),
            'Error Trapezoid': abs(trapezoid - exact),
            'Error Simpson': abs(simpson - exact),
            'Error Spline': abs(spline - exact)
        }

# Wyświetlanie wyników
for func_name, res in results.items():
    print(f"Results for {func_name}:")
    for n, methods in res.items():
        print(f"  n = {n}:")
        for method, value in methods.items():
            print(f"    {method}: {value}")


for func_name, res in results.items():
    plt.figure(figsize=(10, 6))
    
    n_values_plot = list(res.keys())
    errors_riemann = [methods['Error Rectangle'] for methods in res.values()]
    errors_trapezoid = [methods['Error Trapezoid'] for methods in res.values()]
    errors_simpson = [methods['Error Simpson'] for methods in res.values()]
    errors_spline = [methods['Error Spline'] for methods in res.values()]
    
    plt.plot(n_values_plot, errors_riemann, marker='o', label='Rectangle')
    plt.plot(n_values_plot, errors_trapezoid, marker='s', label='Trapezoid')
    plt.plot(n_values_plot, errors_simpson, marker='^', label='Simpson')
    plt.plot(n_values_plot, errors_spline, marker='d', label='CSI')

    plt.yscale('log')
    plt.xlabel('Liczba przedziałów (n)')
    plt.ylabel('Błąd')
    # plt.title(f'Błąd metod numerycznych dla funkcji {func_name}')
    plt.legend()
    plt.savefig(f'h1_h4/error_plot_{func_name}.png')
    # plt.show()