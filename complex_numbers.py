class Complex:
    def __init__(self, real=0, imaginary=1):
        """Initializes a complex number with the given real and imaginary parts. If no arguments are provided, it defaults to a complex number with real part 0 and imaginary part 1."""
        self.real = real
        self.imaginary = imaginary
 
    def __repr__(self):
        """Returns a string representation of the complex number in the form "a + bi" or "a - bi" depending on the sign of the imaginary part. If the real or imaginary part is 0, it is omitted from the string."""
        sign = '+' if self.imaginary>0 else '-'
        return (f'{self.real} ' if self.real!=0 else '') \
            + f'{sign}' + f'{abs(self.imaginary)}i'

    def __add__(self, other):
        """"Returns the sum of two complex numbers."""
        real_part = self.real + other.real
        imag_part = self.imaginary + other.imaginary
        return Complex(real_part, imag_part)

    def __sub__(self, other):
        """Returns the difference between two complex numbers."""
        real_part = self.real - other.real
        imag_part = self.imaginary - other.imaginary
        return Complex(real_part, imag_part)

    def __mul__(self, other):
        """Returns the product of two complex numbers."""
        real_part = (self.real * other.real) - (self.imaginary * other.imaginary)
        imag_part = (self.real * other.imaginary) + (self.imaginary * other.real) 
        return Complex(real_part, imag_part)

    def __truediv__(self, other):
        """Returns the quotient of two complex numbers in the form "a/b + ci/b"."""
        real_part = (self.real * other.real) + (self.imaginary * other.imaginary)
        imag_part = (self.imaginary * other.real) - (self.real * other.imaginary)
        upon = (other.real)**2 + (other.imaginary)**2
        return f'{real_part} + {imag_part}i / {upon}'
