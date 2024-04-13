from SolutionChecker import SolutionChecker
class GaussSeidelSolver(SolutionChecker):
    def __init__(self, matrix, vector, tol=1e-6, max_iter=1000):
        self.matrix = matrix
        self.vector = vector
        self.tol = tol
        self.max_iter = max_iter

    def solve(self):
        n = len(self.vector)
        x = [0] * n
        x_new = [0] * n

        for _ in range(self.max_iter):
            max_diff = 0.0
            for i in range(n):
                x_new[i] = self.vector[i]
                row_sum = 0.0
                for j in range(n):
                    if j != i:
                        val = self.matrix.get_value(i, j)
                        if val != 0:
                            row_sum += val * x_new[j]
                x_new[i] -= row_sum
                val = self.matrix.get_value(i, i)
                if val != 0:
                    x_new[i] /= val

                diff = abs(x_new[i] - x[i])
                if diff > max_diff:
                    max_diff = diff

            if max_diff < self.tol:
                break

            x = x_new.copy()

        return x_new