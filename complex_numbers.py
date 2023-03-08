class Complex:
    def __init__(self, real=0, imaginary=1):
        self.real = real
        self.imaginary = imaginary
 
    def __repr__(self):
        sign = '+' if self.imaginary>0 else '-'
        return (f'{self.real} ' if self.real!=0 else '') \
            + f'{sign}' + f'{abs(self.imaginary)}i'

    def __add__(self, other):
        real_part = self.real + other.real
        imag_part = self.imaginary + other.imaginary
        return Complex(real_part, imag_part)

    def __sub__(self, other):
        real_part = self.real - other.real
        imag_part = self.imaginary - other.imaginary
        return Complex(real_part, imag_part)

    def __mul__(self, other):
        real_part = (self.real * other.real) - (self.imaginary * other.imaginary)
        imag_part = (self.real * other.imaginary) + (self.imaginary * other.real) 
        return Complex(real_part, imag_part)

    def __truediv__(self, other):
        real_part = (self.real * other.real) + (self.imaginary * other.imaginary)
        imag_part = (self.imaginary * other.real) - (self.real * other.imaginary)
        upon = (other.real)**2 + (other.imaginary)**2
        return f'{real_part}/{upon} + {imag_part}i/{upon} '
