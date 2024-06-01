import numpy as np

array_zeros = np.zeros((4, 3))
array_ones = np.ones((4, 3))
array_numbers = np.arange(12).reshape((4, 3))

x1 = np.arange(1, 101)
F1 = 2 * x1**2 + 5

x2 = np.arange(-10, 11)
F2 = np.exp(-x2)

print("Array of zeros:\n", array_zeros)
print("\nArray of ones:\n", array_ones)
print("\nArray of numbers from 0 to 11:\n", array_numbers)
print("\nValues of x1:\n", x1)
print("\nValues of F(x1) = 2x1^2 + 5:\n", F1)
print("\nValues of x2:\n", x2)
print("\nValues of F(x2) = e^-x2:\n", F2)