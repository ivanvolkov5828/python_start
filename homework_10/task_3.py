class Cell:
    def __str__(self):
        return f"{self.n}"

    def __init__(self, n):
        self.n = n

    def __add__(self, other):
        return Cell(self.n + other.n)

    def __sub__(self, other):
        if (self.n - other.n) > 0:
            return Cell(self.n - other.n)
        print("Меньше нуля")

    def __mul__(self, other):
        return Cell(self.n * other.n)

    def __floordiv____truediv__(self, other):
        return Cell(self.n / other.n)

    def make_order(self, k):
        while k >= 5:
            print(f"{'*' * 5}/n", end="")
            k -= 5
        print(f"{'*' * k}", end="")


cell_1 = Cell(15)
cell_2 = Cell(14)
print(cell_1 - cell_2)
cell_1.make_order(17)
