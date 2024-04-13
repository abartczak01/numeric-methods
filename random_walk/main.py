from Matrix import Matrix
from GaussianElimination import GaussianElimination
from GaussianEliminationPartialPivoting import GaussianEliminationPartialPivoting
from GaussSeidelSolver import GaussSeidelSolver
from Graph import Graph
import matplotlib.pyplot as plt
import networkx as nx

def draw_park(edges, osks, exits):
    # Utworzenie grafu z listy krawędzi
    G = nx.Graph()
    for edge in edges:
        node1, node2, weight = edge
        G.add_edge(node1, node2, weight=weight)

    # Wizualizacja grafu
    pos = nx.spring_layout(G)  # Pozycje wierzchołków

    # Ustalenie kolorów wierzchołków
    node_colors = ["skyblue" if node not in osks and node not in exits else "pink" if node in osks else "lightgreen" for node in G.nodes()]

    nx.draw(G, pos, with_labels=True, node_size=700, node_color=node_colors, font_size=10, font_weight="bold")

    # Dodanie etykiet krawędzi
    labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)

    # Zapis do pliku
    plt.savefig("graf.png", format="PNG")

alleys = [[1, 2, 3], [1, 3, 2], [1, 6, 3], [3, 4, 2], [4, 5, 1], [5, 6, 4], [1, 4, 5], [1, 5, 4], [6,2, 2], [2, 3, 1]]
osks = [3]
exits = [2]
intersections = 5
draw_park(alleys, osks, exits)
graph = Graph(alleys, intersections=intersections, osks=osks, exits=exits)
matrix, vector = graph.create_matrix_form()
matrix.display()
print(vector)
solver = GaussianElimination(matrix, vector)
solution = solver.solve()
print("Solution gaussian elimination:")
for i, val in enumerate(solution):
    print(f"x{i + 1} =", val)

# # mat = Matrix()
# # mat.create_simplified_version_matrix(6)
# # mat.display()
# # vector = [1, 0, 0, 0, 0, 0]


# # solver = GaussianElimination(mat, vector)
# # solution = solver.solve()
# # print("Solution gaussian elimination:")
# # for i, val in enumerate(solution):
# #     print(f"x{i} =", val)


# # solver = GaussianEliminationPartialPivoting(mat, vector)
# # solution = solver.solve()
# # print("\nSolution elimination partial pivot:")
# # for i, val in enumerate(solution):
# #     print(f"x{i} =", val)


# # solver = GaussSeidelSolver(mat, vector)
# # solution = solver.solve()
# # print("\nSolution gauss-seidel:")
# # for i, val in enumerate(solution):
# #     print(f"x{i} =", val)


# n = 4 # number of intersections
# m = 5 # number of aisles

# # alleys in the format [two intersections connected by an alley, length of alley]
# alleys = [[1, 2, 2], [1, 4, 2], [2, 3, 3], [3, 4, 4], [2, 4, 3]]
# osks = [1] # hole in intersection 1
# exits = [2] # exit at intersection 2

# graph = Graph(alleys, intersections=n, osks=osks, exits=exits)

# graph.display()

# matrix, vector = graph.create_matrix_form()
# matrix.display()

# # solver = GaussSeidelSolver(matrix, vector)
# # solver = GaussianElimination(matrix, vector)
# solver = GaussianEliminationPartialPivoting(matrix, vector)
# solution = solver.solve()
# # print("\nSolution:")
# # for i, val in enumerate(solution):
# #     print(f"x{i + 1} =", val)

# solver.check_solution_accuracy(matrix, vector, solution)


# H1 rozmiar macierzy - długość alejek, liczba skryżowań; duża gęstość macierzy - skrzyżowania z wieloma alejkami
# random_graph = Graph.generate_random_graph(10, 1, 1, 3, 15)
# print(random_graph.alleys)

# matrix, vector = random_graph.create_matrix_form()
# # matrix.print_matrix()
# # matrix.display()
# # print(vector)
# draw_park(random_graph.alleys)