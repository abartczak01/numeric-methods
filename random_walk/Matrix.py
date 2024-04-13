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

    def size(self):
        rows = max(r for r, _ in self.matrix) + 1
        cols = max(c for _, c in self.matrix) + 1
        return rows, cols

    def sparsity(self):
        r, c = self.size()
        total_elements = r * c
        non_zero_elements = 0
        for value in self.matrix.values():
            if value != 0:
                non_zero_elements += 1
        return non_zero_elements / total_elements if total_elements != 0 else 0

    def create_simplified_version_matrix(self, n):
        for i in range(n):
            for j in range(n):
                if i == j:
                    self.set_value(i, j, 1)
                elif abs(i - j) == 1 and i != 0 and i != n - 1:
                    self.set_value(i, j, -0.5)

    
    