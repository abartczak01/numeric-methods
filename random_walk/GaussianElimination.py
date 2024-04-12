from SolutionChecker import SolutionChecker
class GaussianElimination(SolutionChecker):
    def __init__(self, matrix, vector):
        self.matrix = matrix
        self.vector = vector
        self.solution = []

    def forward_elimination(self):
        n = len(self.vector)

        for i in range(n):
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
