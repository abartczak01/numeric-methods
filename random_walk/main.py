from Matrix import Matrix
from GaussianElimination import GaussianElimination
from GaussianEliminationPartialPivoting import GaussianEliminationPartialPivoting
from GaussSeidelSolver import GaussSeidelSolver
from ParkGraph import ParkGraph
import matplotlib.pyplot as plt
import networkx as nx

def draw_park(edges, osks, exits):
    G = nx.Graph()
    for edge in edges:
        node1, node2, weight = edge
        G.add_edge(node1, node2, weight=weight)

    pos = nx.spring_layout(G)
    node_colors = ["skyblue" if node not in osks and node not in exits else "pink" if node in osks else "lightgreen" for node in G.nodes()]
    nx.draw(G, pos, with_labels=True, node_size=700, node_color=node_colors, font_size=10, font_weight="bold")
    labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
    plt.savefig("graf.png", format="PNG")

# alleys = [[1, 2, 3], [1, 3, 2], [1, 6, 3], [3, 4, 2], [4, 5, 1], [5, 6, 4], [1, 4, 5], [1, 5, 4], [6,2, 2], [2, 3, 1]]
# osks = [3]
# exits = [2]
# intersections = 5
# draw_park(alleys, osks, exits)
# graph = ParkGraph(alleys, intersections=intersections, osks=osks, exits=exits)
# matrix, vector = graph.create_matrix_form()
# matrix.display()
# print(vector)
# solver = GaussianElimination(matrix, vector)
# solution = solver.solve()
# print("Solution gaussian elimination:")
# for i, val in enumerate(solution):
#     print(f"x{i + 1} =", val)
# solver.check_solution_accuracy(matrix, vector, solution)

# H1 rozmiar macierzy - długość alejek, liczba skryżowań; duża gęstość macierzy - skrzyżowania z wieloma alejkami
random_graph = ParkGraph.generate_random_graph(num_intersections=10, num_osks=1, 
                                               num_exits=3, max_alley_length=5, num_alleys=12)

# matrix, vector = random_graph.create_matrix_form()
# matrix.print_matrix()
# matrix.display()
# print(vector)
# draw_park(random_graph.alleys)