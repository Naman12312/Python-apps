from __future__ import annotations

class Complex:
    real: float
    imaginary: float

    def __init__(self: Complex, real: float, imaginary: float) -> None: 
        self.real = real
        self.imaginary = imaginary

    def __add__(self: Complex, self2: Complex) -> Complex:
        newreal = self.real + self2.real
        newimaginary = self.imaginary + self2.imaginary
        return Complex(newreal, newimaginary)

    def __sub__(self: Complex, self2: Complex) -> Complex:
        newreal = self.real - self2.real
        newimaginary = self.imaginary - self2.imaginary
        return Complex(newreal, newimaginary)

    def __mul__(self: Complex, self2: Complex) -> Complex:
        newreal = self.real * self2.real - self.imaginary * self2.imaginary
        newimaginary = self.real * self2.imaginary + self.imaginary * self2.real
        return Complex(newreal, newimaginary)

    def __truediv__(self: Complex, self2: Complex) -> Complex:
        denom = self2.real ** 2 + self2.imaginary ** 2
        newreal = (self.real * self2.real + self.imaginary * self2.imaginary) / denom
        newimaginary = (self.imaginary * self2.real - self.real * self2.imaginary) / denom
        return Complex(newreal, newimaginary)

    def __floordiv__(self: Complex, self2: Complex) -> Complex:
        newreal = self.real / self2.real
        newimaginary = self.imaginary / self2.imaginary
        return Complex(newreal, newimaginary)

    def __str__(self) -> str:
        return f"{self.real} + {self.imaginary}i"

if __name__ == "__main__":
    mycomplex: Complex = Complex(1, 2)
    print(mycomplex)
    mycomplex += Complex(1, 2)
    print(mycomplex)
    mycomplex *= Complex(4, 5)
    print(mycomplex)
    mycomplex -= Complex(4, 5)
    print(mycomplex)
    mycomplex /= Complex(4, 5)
    print(mycomplex)
    mycomplex += Complex(1, 1)
    mycomplex //= Complex(2, 4)
    print(mycomplex)
