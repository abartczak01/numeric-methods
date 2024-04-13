class Matrix:
    def __init__(self):
        self.matrix = {}

    def set_value(self, r, c, value):
        self.matrix[(r, c)] = value

    def get_value(self, r, c):
        return self.matrix.get((r, c), 0)

    def display(self):
        rows = max(r for r, _ in self.matrix) + 1
        cols = max(c for _, c in self.matrix) + 1
        for i in range(rows):
            for j in range(cols):
                value = self.get_value(i, j)
                print(round(value, 3), end='\t')
            print()

    def create_simplified_version_matrix(self, n):
        for i in range(n):
            for j in range(n):
                if i == j:
                    self.set_value(i, j, 1)
                elif abs(i - j) == 1 and i != 0 and i != n - 1:
                    self.set_value(i, j, -0.5)

    def print_matrix(self):
        print(self.matrix)