from SolutionChecker import SolutionChecker
class GaussianEliminationPartialPivoting(SolutionChecker):
    def __init__(self, matrix, vector):
        self.matrix = matrix
        self.vector = vector
        self.solution = []

    def forward_elimination(self):
        n = len(self.vector)

        for i in range(n):
            max_row = i
            max_val = self.matrix.get_value(i, i)
            for k in range(i + 1, n):
                val = self.matrix.get_value(k, i)
                if abs(val) > abs(max_val):
                    max_row = k
                    max_val = val
            if max_row != i:
                print("Zmiana pivota: Wiersz", i, "zamieniony z wierszem", max_row)
                for j in range(i, n):
                    temp = self.matrix.get_value(i, j)
                    self.matrix.set_value(i, j, self.matrix.get_value(max_row, j))
                    self.matrix.set_value(max_row, j, temp)
                temp = self.vector[i]
                self.vector[i] = self.vector[max_row]
                self.vector[max_row] = temp

            for j in range(i + 1, n):
                factor = self.matrix.get_value(j, i) / self.matrix.get_value(i, i)
                for k in range(i, n):
                    self.matrix.set_value(j, k, self.matrix.get_value(j, k) - factor * self.matrix.get_value(i, k))
                self.vector[j] -= factor * self.vector[i]

    def backward_substitution(self):
        n = len(self.vector)
        self.solution = [0] * n

        for i in range(n - 1, -1, -1):
            self.solution[i] = self.vector[i]
            for j in range(i + 1, n):
                self.solution[i] -= self.matrix.get_value(i, j) * self.solution[j]
            self.solution[i] /= self.matrix.get_value(i, i)

    def solve(self):
        self.forward_elimination()
        self.backward_substitution()
        return self.solution
    