from SolutionChecker import SolutionChecker
class GaussSeidel(SolutionChecker):
    def __init__(self, matrix, vector, tol=1e-6, max_iter=1000):
        self.matrix = matrix
        self.vector = vector
        self.tol = tol
        self.max_iter = max_iter

    def solve(self):
        n = len(self.vector)
        x = [0] * n

        for k in range(self.max_iter):
            max_diff = 0.0
            for i in range(n):
                x_new = self.vector[i]
                row_sum = 0.0
                for j in range(n):
                    if j != i:
                        val = self.matrix.get_value(i, j)
                        if val != 0:
                            row_sum += val * x[j]
                x_new -= row_sum
                val = self.matrix.get_value(i, i)
                if val != 0:
                    x_new /= val

                diff = abs(x_new - x[i])
                if diff > max_diff:
                    
                    max_diff = diff

                x[i] = x_new

            if max_diff < self.tol:
                print(k)
                break

        return x

    def solve_with_diff(self):
        n = len(self.vector)
        x = [0] * n
        diffs = []

        for _ in range(self.max_iter):
            max_diff = 0.0
            for i in range(n):
                x_new = self.vector[i]
                row_sum = 0.0
                for j in range(n):
                    if j != i:
                        val = self.matrix.get_value(i, j)
                        if val != 0:
                            row_sum += val * x[j]
                x_new -= row_sum
                val = self.matrix.get_value(i, i)
                if val != 0:
                    x_new /= val

                diff = abs(x_new - x[i])
                if diff > max_diff:
                    max_diff = diff

                x[i] = x_new

            diffs.append(max_diff)

            if max_diff < self.tol:
                break

        return x, diffs