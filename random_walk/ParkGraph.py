from Matrix import Matrix
import random
import networkx as nx

class ParkGraph:
    def __init__(self, alleys, intersections, osks, exits):
        self.alleys = alleys
        self.intersections = intersections
        self.osks = osks
        self.exits = exits
        self.graph = {}
        self.create_graph()

    def create_graph(self):
        self.set_main_intersections()
        self.add_edges()

    def set_main_intersections(self):
        for i in range(1, self.intersections + 1):
            self.graph[i] = []

    def add_edges(self):
        for alley in self.alleys:
            u, v, length = alley
            self.add_edge(u, v, length)

    def add_edge(self, u, v, length):
        if u not in self.graph:
            self.graph[u] = []
        if v not in self.graph:
            self.graph[v] = []
        if length == 1:
            self.graph[u].append(v)
            self.graph[v].append(u)
        else:
            for i in range(1, length):
                new_intersection = len(self.graph) + 1
                self.graph[new_intersection] = []
                if i == 1:
                    self.graph[new_intersection].append(u)
                    self.graph[u].append(new_intersection)
                else:
                    self.graph[new_intersection].append(new_intersection - 1)
                    self.graph[new_intersection - 1].append(new_intersection)
                if i == length - 1:
                    self.graph[new_intersection].append(v)
                    self.graph[v].append(new_intersection)

    def random_row_swaps(self, n):
        matrix_form, vector = self.create_matrix_form()
        rows = matrix_form.size()[0]

        for _ in range(n):
            row1, row2 = random.sample(range(rows), 2)
            for j in range(matrix_form.size()[1]):
                temp = matrix_form.get_value(row1, j)
                matrix_form.set_value(row1, j, matrix_form.get_value(row2, j))
                matrix_form.set_value(row2, j, temp)

            # Swap elements in the vector
            vector[row1], vector[row2] = vector[row2], vector[row1]

        return matrix_form, vector

    def create_matrix_form(self):
        # print(self.graph)
        matrix_form = Matrix()
        vector = []
        for node, neighbours in self.graph.items():
            row_number = node - 1
            column_number = row_number
            if node in self.osks:
                vector.append(0)
                matrix_form.set_value(row_number, column_number, 1)
            elif node in self.exits:
                vector.append(1)
                matrix_form.set_value(row_number, column_number, 1)
            else:
                vector.append(0)
                matrix_form.set_value(row_number, column_number, 1)
                prob_next_location = -1 / len(neighbours)
                for neighbour in neighbours:
                    column_number = neighbour - 1
                    curr_value = matrix_form.get_value(row_number, column_number)
                    if curr_value == 0:
                        matrix_form.set_value(row_number, column_number, prob_next_location)
                    else:
                        matrix_form.set_value(row_number, column_number, curr_value + prob_next_location)
        return matrix_form, vector

    @staticmethod
    def generate_initial_intersection_connections(intersections_num, edges_num=None, multi_edges=True):
        G = nx.MultiGraph()
        G.add_nodes_from(range(1, intersections_num + 1))

        for _ in range(edges_num):
            node1 = random.randint(1, intersections_num)
            node2 = random.randint(1, intersections_num)
            # avoiding loops
            while node1 == node2:
                node2 = random.randint(1, intersections_num)
            G.add_edge(node1, node2)

        # Checking graph connectivity
        if nx.is_connected(G):
            return G
        else:
            components = list(nx.connected_components(G))
            while len(components) > 1:
                node1 = random.choice(list(components[0]))
                node2 = random.choice(list(components[1]))
                G.add_edge(node1, node2)
                components = list(nx.connected_components(G))
            return G

    @classmethod
    def generate_random_graph(cls, num_intersections, num_osks, num_exits, alley_length_range=[1,5], num_alleys=None):
        osks = random.sample(range(1, num_intersections + 1), num_osks)
        exits = random.sample(set(range(1, num_intersections + 1)) - set(osks), num_exits)
        connected_intersections = cls.generate_initial_intersection_connections(num_intersections, edges_num=num_alleys)
        alleys = []
        for connection in connected_intersections.edges():
            alley_length = random.randint(alley_length_range[0], alley_length_range[1])
            node1, node2 = connection
            alleys.append([node1, node2, alley_length])
        return cls(alleys, num_intersections, osks, exits)

    def display(self):
        print(self.graph)


