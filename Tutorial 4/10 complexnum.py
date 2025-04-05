class Complex:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def __add__(self, other):
        return Complex(self.real + other.real, self.imag + other.imag)

    def __str__(self):
        return f"{self.real} + {self.imag}i"

complex1 = Complex(3, 2)
complex2 = Complex(1, 7)

result = complex1 + complex2
print("Sum of complex numbers:", result)
