# Learning-Calculus-with-Python
Practicing Calculus concepts and implementing it in Python

## Complex Number Operations

In `complex_numbers.py` a class 'Complex' represents complex numbers and allows basic arithmetic operations to be performed on them, including addition, subtraction, multiplication, and division.

### Usage
To use this module, import the 'Complex' class and create objects of the class with the desired real and imaginary parts. The arithmetic operations can then be performed on these objects using the '+' (addition), '-' (subtraction), '*' (multiplication), and '/' (division) operators. The resulting object will also be a 'Complex' object.

Example:
```python
from complex_number_operations import Complex

# create two complex numbers
c1 = Complex(3, 4)  # 3 + 4i
c2 = Complex(1, -2) # 1 - 2i

# perform arithmetic operations
summation = c1 + c2
difference = c1 - c2
product = c1 * c2
quotient = c1 / c2

# print results
print(summation)        # 4 + 2i
print(difference)       # 2 + 6i
print(product)          # 11 - 2i
print(quotient)         # -5 + 10i / 5 (currently in string)
```
