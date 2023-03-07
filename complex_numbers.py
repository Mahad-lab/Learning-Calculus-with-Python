class complex:
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
        return complex(real_part, imag_part)

    def __sub__(self, other):
        real_part = self.real - other.real
        imag_part = self.imaginary - other.imaginary
        return complex(real_part, imag_part)

    def __mul__(self, other):
        real_part = (self.real * other.real) - (self.imag * other.imag)
        imag_part = (self.real * other.imag) + (self.imag * other.real) 
        return complex(real_part, imag_part)

    def __div__(self, other):
        real_part1 = (self.real * other.real) + (self.imag * other.imag)
        imag_part1 = (self.imag * other.real) - (self.real * other.imag)
        upon = (other.real)**2 + (other.imag)**2 
        return f'{real_part1}/{upon} + {imag_part1}i/{upon} '
    
