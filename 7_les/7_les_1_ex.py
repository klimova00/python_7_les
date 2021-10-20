class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        return '\n'.join([''.join(['%d\t' % i for i in row]) for row in self.matrix])

    def __len__(self):
        return len(self.matrix)  # количество строк

    def __add__(self, other):
        if not len(self.matrix) == len(other.matrix):
            raise ValueError(f'\033[1;31mFor addition, the sizes of the matrices must match\033[0m\n'
                             f'Size first matrix = {len(self.matrix)}\nSize second matrix = {len(other.matrix)}\n')
        else:
            return Matrix([[a + b for a, b in zip(*x)] for x in zip(self.matrix, other.matrix)])


matrix_1 = Matrix([[31, 22], [37, 43]])
matrix_2 = Matrix([[3, 5, 32], [2, 4, 6], [-1, 64, -8]])
matrix_3 = Matrix([[1, 1, 1], [1, 1, 1], [1, 1, 1]])

print(f'First matrix:\n{matrix_1}')
print(f'Second matrix:\n{matrix_2}')
print(f'Third matrix:\n{matrix_3}')
print("Second Matrix + Third Matrix =\n", matrix_2, '\n\t+\n', matrix_3, '\n\t=\n', matrix_2 + matrix_3)
print("First Matrix + Second Matrix =\n", matrix_1 + matrix_2)
# Смогла сделать проверку только на количество строк((
