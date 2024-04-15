import random

class MonteCarlo:
    def __init__(self, graph, osks, exits, start_point):
        self.graph = graph  # Tutaj zakładam, że graph jest słownikiem, gdzie kluczami są wierzchołki, a wartościami są listy sąsiadów
        self.osks = osks
        self.exits = exits
        self.start_point = start_point

    def run_simulation(self, num_simulations=1000):
        print(self.start_point)
        successes = 0

        for _ in range(num_simulations):
            current_point = self.start_point
            while True:
                neighbors = self.graph[current_point]
                next_point = random.choice(neighbors)
                if next_point in self.exits:
                    successes += 1
                    break
                elif next_point in self.osks:
                    break
                else:
                    current_point = next_point

        success_rate = successes / num_simulations
        return success_rate


