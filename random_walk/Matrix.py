import math
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

    def is_diagonally_dominant(self):
        rows, cols = self.size()
        for i in range(rows):
            diagonal_value = float(self.get_value(i, i))
            sum_of_abs_non_diagonal = sum(abs(self.get_value(i, j)) for j in range(cols) if j != i)
            if diagonal_value < sum_of_abs_non_diagonal:
                print(diagonal_value, '<', sum_of_abs_non_diagonal)
                return False
        return True
    
    def check_convergence_f(self):
        suma = math.sqrt(sum(value**2 for value in self.matrix.values()))
        return suma < 1
    
    def check_convergence_w(self):
        max_row_sum = 0
        for i in range(self.size()[0]):
            row_sum = sum(abs(self.get_value(i, j)) for j in range(self.size()[1]))
            if row_sum > max_row_sum:
                max_row_sum = row_sum
        return max_row_sum < 1
    
    def check_convergence_k(self):
        max_col_sum = 0
        for j in range(self.size()[1]): 
            col_sum = sum(abs(self.get_value(i, j)) for i in range(self.size()[0]))
            if col_sum > max_col_sum:
                max_col_sum = col_sum
                
        return max_col_sum < 1

