import numpy as np
import matplotlib.pyplot as plt
from funcs_to_test import exponential, integral_poly5, integral_sin20x, integral_sq_rt, poly5, sin20x, sq_rt
import os
from numeral_integration.algorithms import a1_riemann, a2_trapezoid, a3_simpson, a4_spline_interpolation

exact_values = {
    'exponential': np.exp(3) - np.exp(-3),  # -3 do 3
    'poly5': integral_poly5(6) - integral_poly5(0),  # 0 do 6
    'sin20x': integral_sin20x(3/2 * np.pi) - integral_sin20x(0),  # 0 do 3/2pi
    'sq_rt': integral_sq_rt(6) - integral_sq_rt(0)  # 0 do 6
}

functions = {
    'exponential': [exponential, -3, 3, exact_values['exponential']],
    'poly5': [poly5, 0, 6, exact_values['poly5']],
    'sin20x': [sin20x, 0, 3/2 * np.pi, exact_values['sin20x']],
    'sq_rt': [sq_rt, 0, 6, exact_values['sq_rt']]
}
os.makedirs('./functions', exist_ok=True)

i = 1
for name, (func, start, end, exact_value) in functions.items():
    x = np.linspace(start, end, 400)
    y = func(x)
    
    plt.figure()
    plt.plot(x, y, label=f"f{i}")
    plt.fill_between(x, y, alpha=0.3)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title(f"f{i}")
    i += 1
    plt.grid(True)
    plt.savefig(f'./functions/{name}.png')
    plt.close()

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
    plt.legend()
    plt.savefig(f'h1_h4/error_plot_{func_name}.png')