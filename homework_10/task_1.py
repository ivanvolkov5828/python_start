class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        return f"Наша искомая матрица {self.matrix}"

    def __add__(self, other):
        return Matrix([[self.matrix[i][j] + other.matrix[i][j] for j in range(len(self.matrix[0]))] for i in
                       range(len(other.matrix))])


matrix_1 = [[1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]]

matrix_2 = [[10, 11, 12],
            [13, 14, 15],
            [16, 17, 18]]

matrix_sum_1 = Matrix(matrix_1)
matrix_sum_2 = Matrix(matrix_2)

print(matrix_sum_1 + matrix_sum_2)
