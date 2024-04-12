from Matrix import Matrix
import random
import networkx as nx

class Graph:
    def __init__(self, alleys, intersections, osks, exits):
        self.alleys = alleys
        self.intersections = intersections
        self.osks = osks
        self.exits = exits
        self.graph = {}

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

    def create_matrix_form(self):
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
                    matrix_form.set_value(row_number, column_number, prob_next_location)

        return matrix_form, vector

    @staticmethod
    def generate_initial_intersection_connections(n):
        G = nx.Graph()
        G.add_nodes_from(range(1, n + 1))
        for i in range(1, n):
            random_node = random.randint(1, i)
            G.add_edge(i + 1, random_node)

        if nx.is_connected(G):
            return G
        else:
            components = list(nx.connected_components(G))
            while len(components) > 1:
                node1 = random.choice(components[0])
                node2 = random.choice(components[1])
                G.add_edge(node1, node2)
                components = list(nx.connected_components(G))
            return G

    @classmethod
    def generate_random_graph(cls, num_intersections, num_osks, num_exits, max_alley_length):
        intersections = num_intersections
        osks = random.sample(range(1, num_intersections + 1), num_osks)
        exits = random.sample(set(range(1, num_intersections + 1)) - set(osks), num_exits)
        connected_intersections = cls.generate_initial_intersection_connections(num_intersections)
        alleys = []
        for connection in connected_intersections.edges():
            alley_length = random.randint(1, max_alley_length)
            node1, node2 = connection
            alleys.append([node1, node2, alley_length])
        return cls(alleys, intersections, osks, exits)

    def display(self):
        print(self.graph)


# Example usage:
random_graph = Graph.generate_random_graph(5, 1, 1, 5)
random_graph.create_graph()
random_graph.display()
