from Matrix import Matrix
from GaussianElimination import GaussianElimination
from GaussianEliminationPartialPivoting import GaussianEliminationPartialPivoting
from GaussSeidel import GaussSeidel
from ParkGraph import ParkGraph
from MonteCarlo import MonteCarlo
import matplotlib.pyplot as plt
import networkx as nx
import random
import math
import time
import statistics

def draw_park(edges, osks, exits, name="graf.png"):
    G = nx.MultiGraph()
    for edge in edges:
        node1, node2, weight = edge
        G.add_edge(node1, node2, weight=weight)
    print(G.size(), "rozmiar przy wizualizacji")
    pos = nx.spring_layout(G)
    node_colors = ["skyblue" if node not in osks and node not in exits else "pink" if node in osks else "lightgreen" for node in G.nodes()]
    nx.draw(G, pos, with_labels=True, node_size=700, node_color=node_colors, font_size=10, font_weight="bold")
    labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
    plt.savefig(name, format="PNG")

def H1_test1():
    for _ in range(2):
        for i in range(200):
            graph = ParkGraph.generate_random_graph(num_intersections=20, num_alleys=20+i, alley_length_range=(1,1), num_osks=2, num_exits=2)
            matrix, vector = graph.create_matrix_form()
            if i < 10:
                matrix.display()
            size = matrix.size()
            sparsity = matrix.sparsity()
            print(graph.graph)
            
            solver_a1 = GaussianElimination(matrix=matrix, vector=vector)
            solver_a2 = GaussianEliminationPartialPivoting(matrix=matrix, vector=vector)
            
            solution_a1 = solver_a1.solve()
            solution_a2 = solver_a2.solve()
            
            print(size, sparsity, '---------------------')
            print('a1', solution_a1)
            print('a2', solution_a2)


# test ze zmienionymi rzędami:
def H1_test2():
    random_graph = ParkGraph.generate_random_graph(num_intersections=5, num_osks=1, num_exits=1, alley_length_range=(1,2), num_alleys=20)
    # przed zamianą miejsc wierszy
    matrix, vector = random_graph.create_matrix_form()
    matrix.display()
    print(vector)
    solver = GaussianEliminationPartialPivoting(matrix, vector)
    solution = solver.solve()
    print('partial pivoting', solution)
    solver = GaussianElimination(new_matrix, new_vector)
    solution = solver.solve()
    print('no pivoting', solution)
    # po zamianie wierszy
    new_matrix, new_vector = random_graph.random_row_swaps(10)
    new_matrix.display()
    print(new_vector)
    print(new_matrix)
    solver = GaussianEliminationPartialPivoting(new_matrix, new_vector)
    solution = solver.solve()
    print('partial pivoting', solution)
    solver = GaussianElimination(new_matrix, new_vector)
    solution = solver.solve()
    print('no pivoting', solution)

def H2_test1():
    false_count = 0
    true_count = 0
    for i in range(1000):
        random_graph = ParkGraph.generate_random_graph(10, random.randint(1,3), random.randint(1,3), 
                                                    alley_length_range=(1, 4), num_alleys=random.randint(10,30))
        matrix, vector = random_graph.create_matrix_form()
        solver = GaussSeidel(matrix, vector)
        solution, _ = solver.solve()
        print(solution)
        if matrix.is_diagonally_dominant():
            true_count += 1
        else:
            false_count +=1
    print(false_count, true_count)

def H2_test2():
    alleys = [[1,2, 2], [2,4,4], [4,5,1], [5,6,4], [6,7,2], [3,7,3], [3,1,2], [3,6,4], [1,6,5], [1,5,4], [1,4,2], [3,2, 4]]
    osks = [4]
    exits = [6]
    graph = ParkGraph(alleys, 7, osks, exits)
    matrix, vector = graph.create_matrix_form()
    
    solver = GaussSeidel(matrix, vector, tol=1e-16)
    solution, differences = solver.solve_with_diff()
    # Tworzenie wykresu zbieżności
    plt.figure()  # Utwórz nowy wykres
    plt.plot(range(len(differences)), [math.log(diff) for diff in differences])
    plt.xlabel('Iteracja')
    plt.ylabel('Różnica między kolejnymi przybliżeniami')
    plt.title('Zbieżność metody Gaussa-Seidela')
    plt.grid(True)
    plt.savefig("h2_t2_zbieznosc.png")

    # Tworzenie wykresu planu parku
    plt.figure()  # Utwórz nowy wykres
    draw_park(alleys, osks, exits)


def H3_test1():
    times_gauss_seidel = []
    times_gaussian_elimination = []
    times_gaussian_elimination_partial_pivoting = []
    
    for j in range(1, 4):
        for i in range(500):
            random_graph = ParkGraph.generate_random_graph(5*j, random.randint(1,j), random.randint(1,j), 
                                                        alley_length_range=(1, 2), num_alleys=random.randint(5*j, 10*j))
            matrix, vector = random_graph.create_matrix_form()
            
            # Solver Gauss-Seidela
            start_time = time.time()
            solver = GaussSeidel(matrix, vector)
            solution = solver.solve()
            end_time = time.time()
            times_gauss_seidel.append(end_time - start_time)
            
            # Solver Eliminacji Gaussa
            start_time = time.time()
            solver = GaussianElimination(matrix, vector)
            solution = solver.solve()
            end_time = time.time()
            times_gaussian_elimination.append(end_time - start_time)
            
            # Solver Eliminacji Gaussa z częściowym wyborem
            start_time = time.time()
            solver = GaussianEliminationPartialPivoting(matrix, vector)
            solution = solver.solve()
            end_time = time.time()
            times_gaussian_elimination_partial_pivoting.append(end_time - start_time)
            
            print(f'{i}. tura')
    
    # Zapisywanie czasów do plików
    with open('times_gauss_seidel.txt', 'w') as file:
        for time1 in times_gauss_seidel:
            file.write(str(time1) + '\n')
    
    with open('times_gaussian_elimination.txt', 'w') as file:
        for time1 in times_gaussian_elimination:
            file.write(str(time1) + '\n')
    
    with open('times_gaussian_elimination_partial_pivoting.txt', 'w') as file:
        for time1 in times_gaussian_elimination_partial_pivoting:
            file.write(str(time1) + '\n')

    return times_gauss_seidel, times_gaussian_elimination, times_gaussian_elimination_partial_pivoting

def H3_test1_plot():
    # Wczytywanie czasów z plików
    with open('times_gauss_seidel.txt', 'r') as file:
        times_gauss_seidel = [float(line.strip()) for line in file.readlines()]
    
    with open('times_gaussian_elimination.txt', 'r') as file:
        times_gaussian_elimination = [float(line.strip()) for line in file.readlines()]
    
    with open('times_gaussian_elimination_partial_pivoting.txt', 'r') as file:
        times_gaussian_elimination_partial_pivoting = [float(line.strip()) for line in file.readlines()]

    # Obliczanie średniego czasu wykonania dla każdego algorytmu
    avg_time_gauss_seidel = sum(times_gauss_seidel)
    avg_time_gaussian_elimination = sum(times_gaussian_elimination)
    avg_time_gaussian_elimination_partial_pivoting = sum(times_gaussian_elimination_partial_pivoting)

    # Wydrukowanie średnich czasów
    print("Średni czas wykonania dla Gauss-Seidela:", avg_time_gauss_seidel, "sekundy")
    print("Średni czas wykonania dla Eliminacji Gaussa:", avg_time_gaussian_elimination, "sekundy")
    print("Średni czas wykonania dla Eliminacji Gaussa z częściowym wyborem:", avg_time_gaussian_elimination_partial_pivoting, "sekundy")

    # Tworzenie wykresu
    plt.figure(figsize=(10, 6))

    plt.plot(times_gauss_seidel, label='Gauss-Seidel', color='blue')
    plt.plot(times_gaussian_elimination, label='Gaussian Elimination', color='red')
    plt.plot(times_gaussian_elimination_partial_pivoting, label='Gaussian Elimination with Partial Pivoting', color='green')

    plt.xlabel('Iteration')
    plt.ylabel('Time (seconds)')
    plt.title('Time taken by different algorithms')
    plt.legend()
    plt.grid(True)
    plt.savefig("h3_plot.png")

def monte_carlo_matrix():
    alleys = [[1,2, 2], [2,4,4], [4,5,1], [5,6,4], [6,7,2], [3,7,3], [3,1,2], [3,6,4], 
              [1,6,5], [1,5,4], [1,4,2], [3,2, 4], [7,8,2], [3,8,1], [2,8,2]]
    osks = [4]
    exits = [6]
    n = 8
    graph = ParkGraph(alleys, n, osks, exits)
    matrix, vector = graph.create_matrix_form()
    solver = GaussianEliminationPartialPivoting(matrix, vector)
    solution = solver.solve()
    solver.check_solution_accuracy(matrix, vector, solution)
    print(graph.graph)
    # draw_park(alleys, osks, exits, "graf_monte_carlo.png")
    mean_diffs = []
    for i in range(100):
        approx_solutions = []
        for i in range(1, len(vector) + 1):
            if i in osks:
                approx_solutions.append(0)
            elif i in exits:
                approx_solutions.append(1)
            else:
                monte_carlo = MonteCarlo(graph.graph, osks, exits, i)
                result = monte_carlo.run_simulation()
                approx_solutions.append(result)

        diffs = []
        for i in range(len(solution)):
            diffs.append(abs(solution[i] - approx_solutions[i]))
        mean_diffs.append(statistics.mean(diffs))

    print(mean_diffs)
    plt.figure(figsize=(10, 6))
    plt.plot(range(1, 101), mean_diffs, marker='o', linestyle='-')
    plt.xlabel('Numer symulacji')
    plt.ylabel('Średnia różnica')
    plt.title('Średnie różnice między dokładnymi a przybliżonymi rozwiązaniami (100 symulacji)')
    plt.grid(True)

    # Oznaczenie największej i najmniejszej wartości
    max_diff = max(mean_diffs)
    min_diff = min(mean_diffs)
    print(max_diff)
    print(min_diff)
    plt.text(mean_diffs.index(max_diff) + 1, max_diff, f'Max', va='bottom', ha='center')
    plt.text(mean_diffs.index(min_diff) + 1, min_diff, f'Min', va='top', ha='center')
    plt.savefig("monte_carlo_diffs.png")

# H1_test1()
# H1_test2()
# H2_test1()
# H2_test2()
# H3_test1()
# H3_test1_plot()
# monte_carlo_matrix()
# wziąć pod uwagę strukture danych (nie mnożyć przez 0)
# zaimplementować metodę Gaussa-Seidela
# monte carlo na innych macierzach

graph = ParkGraph.generate_random_graph(5, 1, 1, (1,2), 10)
matrix, vector = graph.create_matrix_form()
matrix.display()
