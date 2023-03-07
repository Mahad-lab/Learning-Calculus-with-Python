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

    # TODO: fix
    def __mul__(self, other):
        real_part = self.real * other.real
        imag_part = self.imaginary * other.imaginary
        return complex(real_part, imag_part)

    # TODO: 
    def __div__(self, other):
        return complex()
