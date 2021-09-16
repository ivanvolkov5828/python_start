class ComplexNumber:
    def __init__(self, number):
        self.number = number

    def __add__(self, other):
        return self.number + other.number

    def __mul__(self, other):
        return self.number * other.number


first_number = ComplexNumber(complex(1, 2))
second_number = ComplexNumber(complex(3, 4))

print(first_number + second_number)
print(first_number * second_number)