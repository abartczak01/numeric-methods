class SolutionChecker:
    def check_solution_accuracy(self, matrix, vector, solution, threshold=1e-6):
        n = len(vector)
        residual_errors = []

        for i in range(n):
            lhs = 0
            for j in range(n):
                lhs += matrix.get_value(i, j) * solution[j]
            rhs = vector[i]
            residual_errors.append(abs(lhs - rhs))

        # max_residual_error = max(residual_errors)
        print("residual errors:", residual_errors)

        # if max_residual_error <= threshold:
        #     print("Solutions are accurate within the specified threshold.")
        # else:
        #     print("Solutions are not accurate within the specified threshold. Maximum residual error:", max_residual_error)