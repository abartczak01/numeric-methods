import math
import random
import numpy as np
import matplotlib.pyplot as plt
import time

# H1
def oblicz_wektory_nkata(n):
    theta = 2 * math.pi / n
    w0 = [math.cos(theta) - 1, math.sin(theta)]
    wektory = [w0]
    for i in range(1, n):
        w0 = [w0[0]*math.cos(theta) - w0[1]*math.sin(theta), w0[0]*math.sin(theta) + w0[1]*math.cos(theta)]
        wektory.append(w0)
    return wektory

def oblicz_obwod(wektory):
    obwod = sum(math.sqrt(w[0]**2 + w[1]**2) for w in wektory)
    return obwod


# H1
def plot_log_roznice(ns):
    log_roznice = []
    for n in ns:
        wektory = oblicz_wektory_nkata(n)
        obwod = oblicz_obwod(wektory)
        roznica = np.abs(np.pi*2 - obwod)
        log_roznice.append(math.log(roznica))

    plt.plot(ns, log_roznice, marker='.', linestyle='None')
    plt.xlabel(r'Liczba boków wielokąta $n$')
    plt.ylabel(r'Logarytm z różnicy między $2\pi$ a obwodem')
    plt.title(r'Wartość logarytmu z różnicy między $2\pi$ a obwodem dla różnych $n$')
    plt.grid(True)
    plt.savefig('h1_plot.png')

# H2
def suma_wektorow_h2(wektory):
    x_suma = 0
    y_suma = 0
    for wektor in wektory:
        x_suma += wektor[0]
        y_suma += wektor[1]
    return x_suma, y_suma

def test_h2(ns):
    blisko_0 = 0
    for n in ns:
        wektory = oblicz_wektory_nkata(n)
        suma_wektorów = suma_wektorow_h2(wektory)
        if np.allclose(suma_wektorów, [0, 0], atol=1e-10):
            print(suma_wektorów)
            blisko_0 += 1
    print(blisko_0, blisko_0/len(ns))

# H3
def suma_wektorow_h3(wektory):
    x_dodatnie = [wektor[0] for wektor in wektory if wektor[0] > 0]
    x_ujemne = [wektor[0] for wektor in wektory if wektor[0] < 0]
    y_dodatnie = [wektor[1] for wektor in wektory if wektor[1] > 0]
    y_ujemne = [wektor[1] for wektor in wektory if wektor[1] < 0]
    
    Sx_dodatnie = sum(sorted(x_dodatnie))
    Sx_ujemne = sum(sorted(x_ujemne, reverse=True))
    Sy_dodatnie = sum(sorted(y_dodatnie))
    Sy_ujemne = sum(sorted(y_ujemne, reverse=True))

    suma_wektorów = (Sx_dodatnie + Sx_ujemne, Sy_dodatnie + Sy_ujemne)
    return suma_wektorów

def monte_carlo_pi(n):
    punkty_wewnatrz_okregu = 0

    for _ in range(n):
        x = random.uniform(0, 1)
        y = random.uniform(0, 1)
        odleglosc = x**2 + y**2

        if odleglosc <= 1:
            punkty_wewnatrz_okregu += 1

    return 4 * punkty_wewnatrz_okregu / n


def calculate_distance(a, b):
    length = math.sqrt((a[0]-b[0])**2 + (a[1]-b[1])**2)
    return length


# H1
ns = list(range(3, 1003, 10))
plot_log_roznice(ns)

# H2 
test_h2(ns)

# H3
def h_3(test_n):
    od_zerowego_h2 = []
    od_zerowego_h3 = []
    for n in test_n:
        test_wektory = oblicz_wektory_nkata(n)
        suma_h2 = suma_wektorow_h2(test_wektory)
        suma_h3 = suma_wektorow_h3(test_wektory)
        od_zerowego_h2.append(np.linalg.norm(suma_h2))
        od_zerowego_h3.append(np.linalg.norm(suma_h3))

    srednia_h2 = np.mean(od_zerowego_h2)
    srednia_h3 = np.mean(od_zerowego_h3)

    plt.plot(test_n, od_zerowego_h2, label='metoda z hipotezy 2', marker='o')
    plt.plot(test_n, od_zerowego_h3, label='metoda z hipotezy 3', marker='o')
    plt.xlabel('Wartość n')
    plt.ylabel('odległość od wektora zerowego')
    plt.title('Porównanie średnich odległości')
    plt.legend()
    plt.grid(True)
    plt.savefig('h3_plot.png')
    return srednia_h2, srednia_h3

test_n = list(range(3, 1003, 25))
srednia_h2, srednia_h3 = h_3(test_n)
print(srednia_h2, srednia_h3)
if srednia_h3 > srednia_h2:
    print('h3 wieksze')
else:
    print("h3 mniejsze")

roznica_srednich = abs(srednia_h2 - srednia_h3)
print(roznica_srednich)

# H4
def znajdz_n_dla_dokladnosci(dokladnosc, metoda):
    print("nowy test")
    n = 3
    while True:
        if abs(metoda(n) - math.pi) < dokladnosc:
            return n
        n += 1


def czas_mc(ns):
    times = []
    for n in ns:
        start = time.time()
        monte_carlo_pi(n)
        end = time.time()
        times.append(end - start)

    return np.mean(times)

def czas_wektory(n, liczba_probek=100):
    times = []
    for _ in range(liczba_probek):
        start = time.time()
        oblicz_obwod(oblicz_wektory_nkata(n))/2
        end = time.time()
        times.append(end - start)
    return np.mean(times)

dokladnosc_pi = 1e-4

n_wektory = znajdz_n_dla_dokladnosci(dokladnosc_pi, lambda n: oblicz_obwod(oblicz_wektory_nkata(n))/2)
print("wektory", czas_wektory(n_wektory))

ns_mc = [znajdz_n_dla_dokladnosci(dokladnosc_pi, monte_carlo_pi) for _ in range(100)]
print(ns_mc)
print("mc", czas_mc(ns_mc))
