from Matrix import Matrix
from GaussianElimination import GaussianElimination
from GaussianEliminationPartialPivoting import GaussianEliminationPartialPivoting
from GaussSeidelSolver import GaussSeidelSolver
from Graph import Graph


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


n = 4 # number of intersections
m = 5 # number of aisles

# alleys in the format [two intersections connected by an alley, length of alley]
alleys = [[1, 2, 2], [1, 4, 2], [2, 3, 3], [3, 4, 4], [2, 4, 3]]
osks = [1] # hole in intersection 1
exits = [2] # exit at intersection 2

graph = Graph(alleys, intersections=n, osks=osks, exits=exits)

graph.create_graph()
graph.display()

matrix, vector = graph.create_matrix_form()
matrix.display()

# solver = GaussSeidelSolver(matrix, vector)
# solver = GaussianElimination(matrix, vector)
solver = GaussianEliminationPartialPivoting(matrix, vector)
solution = solver.solve()
# print("\nSolution:")
# for i, val in enumerate(solution):
#     print(f"x{i + 1} =", val)

solver.check_solution_accuracy(matrix, vector, solution)

# num_alleys = 4
# num_intersections = 3
# num_osks = 1
# num_exits = 3
# max_alley_length = 5

# random_graph = Graph.generate_random_graph(num_alleys, num_intersections, num_osks, num_exits, max_alley_length)
# random_graph.display()
# matrix, vector = random_graph.create_matrix_form()

# solver = GaussianEliminationPartialPivoting(matrix, vector)
# solution = solver.solve()

# dopytać się o budowanie losowych macierzy - czy maja być budowane
# na podstawie danych wejściowych w podanym formacie, czy mogą być
# zupełnie losowe
# (tylko z określeniem "zagęszczenia macierzy" i jej rozmiaru)

# H1 rozmiar macierzy - długość alejek, liczba skryżowań; duża gęstość macierzy - skrzyżowania z wieloma alejkami
random_graph = Graph.generate_random_graph(5, 1, 1, 2)
random_graph.create_graph()
random_graph.display()

matrix, vector = random_graph.create_matrix_form()
matrix.display()
print(vector)