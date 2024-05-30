import numpy as np
from scipy.interpolate import interp1d, CubicSpline
import matplotlib.pyplot as plt
from scipy.sparse import csr_array, csr_matrix
from scipy.sparse.linalg import spsolve

def plot_riemann(x, func):
    plt.plot(x, func(x), 'ro')
    plt.bar(x, func(x), width=x[1] - x[0], align='center', alpha=0.5)
    plt.title('Metoda prostokątów (Riemann)')
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.grid(True)
    plt.savefig("./visuals/protokaty.png")
    plt.close()

def plot_trapezoid(x, func):
    plt.plot(x, func(x), 'ro-')
    plt.fill_between(x, func(x), alpha=0.5)
    plt.title('Metoda trapezów')
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.grid(True)
    plt.savefig("./visuals/trapezy.png")
    plt.close()

def plot_simpson(x, func):
    plt.plot(x, func(x), 'ro-')
    plt.fill_between(x, func(x), alpha=0.5)
    plt.title('Metoda Simpsona')
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.grid(True)
    plt.savefig("./visuals/simpson.png")
    plt.close()

def plot_cubic_spline(x, func):
    cs = CubicSpline(x, func(x))
    x_new = np.linspace(x[0], x[-1], 1000)
    y_new = cs(x_new)
    plt.plot(x, func(x), 'o', label='Original data')
    plt.plot(x_new, y_new, '-', label='Cubic spline interpolation')
    plt.legend()
    plt.title('Cubic Spline Interpolation')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.grid(True)
    plt.savefig("./visuals/interpolacja.png")
    plt.close()

# n - liczba przedziałów, n + 1 - liczba punktów
def a1_riemann(a, b, n, func, toPlot=False):
    h = (b - a) / (n)
    x = np.linspace(a, b, n + 1)
    midpoints = (x[:n] + x[1:]) / 2
    I_mid = h * sum(func(midpoints))
    
    if toPlot:
        plot_riemann(midpoints, func)
    
    return I_mid

def a2_trapezoid(a, b, n, func, toPlot=False):
    h = (b - a) / n
    x = np.linspace(a, b, n + 1)
    f = func(x)
    I_trap = (h / 2) * (f[0] + 2 * sum(f[1:n]) + f[n])
    
    if toPlot:
        plot_trapezoid(x, func)
    
    return I_trap

# Simpson's 1/3
def a3_simpson(a, b, n, func, toPlot=False):
    if n % 2 == 1:
        raise ValueError("Liczba przedziałów n musi być parzysta.")
    
    h = (b - a) / n
    x = np.linspace(a, b, n + 1)
    f = func(x)

    I_simp = (h / 3) * (f[0] + 2 * sum(f[2:n-1:2]) + 4 * sum(f[1:n:2]) + f[n])
    # print("========= nowe", I_simp)

    if toPlot:
        plot_simpson(x, func)
    
    return I_simp


def a4_spline_interpolation(a_beg, b_fin, n, func, toPlot=False):
    x = np.linspace(a_beg, b_fin, n + 1)
    y = func(x)
    h = (b_fin - a_beg) / n

    B = np.zeros(n+1)
    # Wypełniamy macierz A i wektor B zgodnie z warunkami brzegowymi
    row = [0, n]
    col = [0, n]
    data = [1, 1]

    for i in range(1, n):
        row.append(i)
        col.append(i)
        data.append(4 * h)

        row.append(i)
        col.append(i - 1)
        data.append(h)

        row.append(i)
        col.append(i + 1)
        data.append(h)
        B[i] = 3 * ((y[i+1] - y[i]) / h - (y[i] - y[i-1]) / h)
    
    A = csr_array((data, (row, col)))
    # Rozwiązujemy układ równań
    c = spsolve(A, B)
    
    # Obliczamy współczynniki b i d
    b = np.zeros(n)
    d = np.zeros(n)
    for i in range(n):
        b[i] = (y[i+1] - y[i]) / h - h * (2 * c[i] + c[i+1]) / 3
        d[i] = (c[i+1] - c[i]) / (3 * h)

    total_area = 0
    for i in range(n):
        a_i = y[i]
        b_i = b[i]
        c_i = c[i]
        d_i = d[i]
        h_i = h
        
        integral = (
            a_i * h_i +
            b_i * h_i**2 / 2 +
            c_i * h_i**3 / 3 +
            d_i * h_i**4 / 4
        )
        # print("++++++", integral)
        total_area += integral
    
    # print(f"Całkowite pole pod wykresem: {total_area}")
    
    # for i in range(n):
    #     print(f"Przedział [{x[i]}, {x[i+1]}]:")
    #     print(f"S(x) = {y[i]} + {b[i]}*(x - {x[i]}) + {c[i]}*(x - {x[i]})^2 + {d[i]}*(x - {x[i]})^3")
    
    def spline(x_val):
        for i in range(n):
            if x[i] <= x_val <= x[i+1]:
                dx = x_val - x[i]
                return y[i] + b[i]*dx + c[i]*dx**2 + d[i]*dx**3
        return None  # Wartość x_val jest poza przedziałem [a, b]

    if toPlot:
        x_vals = np.linspace(a_beg, b_fin, 100) 
        y_vals = func(x_vals) # wartości dla og funkcji
        y_spline = [spline(x) for x in x_vals] # wartości dla poszczególnych wielomianów
        
        plt.plot(x_vals, y_vals, label='Oryginalna funkcja')
        plt.plot(x_vals, y_spline, label='Interpolacja spline', linestyle='--')
        plt.scatter(np.linspace(a_beg, b_fin, n+1), func(np.linspace(a_beg, b_fin, n+1)), color='red')
        plt.legend()
        plt.savefig("cubic_interpolation.png")
    
    return total_area


def a4(a, b, n, func, toPlot=False):
    x = np.linspace(a, b, n + 1)
    y = func(x)
    
    cs = CubicSpline(x, y)
    coefs = cs.c  # współczynniki mają postać (4, n-1), gdzie 4 oznacza [a_i, b_i, c_i, d_i]
    
    integral_val = 0
    for i in range(n):
        a_i = coefs[0, i]
        b_i = coefs[1, i]
        c_i = coefs[2, i]
        d_i = coefs[3, i]
        x_i = x[i]
        x_ip1 = x[i+1]
        
        integral = (
            (a_i / 4) * (x_ip1 - x_i)**4 + 
            (b_i / 3) * (x_ip1 - x_i)**3 + 
            (c_i / 2) * (x_ip1 - x_i)**2 + 
            d_i * (x_ip1 - x_i)
        )
        integral_val += integral

    if toPlot:
        plot_cubic_spline(x, func)
    
    return integral_val

