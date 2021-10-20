class Cell:
    def __init__(self, number_of_cells):
        self.number_of_cells = int(number_of_cells)

    def __str__(self):
        return f' {self.number_of_cells * "*"}'

    def __add__(self, other):
        return Cell(self.number_of_cells + other.number_of_cells)

    def __sub__(self, other):
        if not (self.number_of_cells - other.number_of_cells) < 0:
            return Cell(self.number_of_cells - other.number_of_cells)
        else:
            return f'\033[1;31mThe number of cells in the first must be more than in the second\033[0m'

    def __mul__(self, other):
        return Cell(self.number_of_cells * other.number_of_cells)

    def __truediv__(self, other):
        return Cell(int(self.number_of_cells // other.number_of_cells))

    def make_order(self, cells_in_row):
        row = ''
        for i in range(int(self.number_of_cells // cells_in_row)):
            row += f'{"*" * cells_in_row}\n'
        row += f'{"*" * (self.number_of_cells % cells_in_row)}'
        return row


my_cell_1 = Cell(15)
my_cell_2 = Cell(10)
print(f"Cell_1 {my_cell_1}")
print(f"Cell_2 {my_cell_2}")
print(f'Cell_1/Cell_2 = {my_cell_1 / my_cell_2}')
print(f'Cell_1 + Cell_2 = {my_cell_1 + my_cell_2}')
print(f'Cell_1 - Cell_2 = {my_cell_1 - my_cell_2}')
print(f'Cell_2 + Cell_1 = {my_cell_2 - my_cell_1}')
print(f'Make_order_Cell_1:\n {my_cell_1.make_order(3)}')
print(f'Make order_Cell_2:\n {my_cell_2.make_order(5)}')
