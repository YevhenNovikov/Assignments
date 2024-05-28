import numpy as np

array_zeros = np.zeros((4, 3))
array_ones = np.ones((4, 3))
array_numbers = np.arange(12).reshape((4, 3))

x1 = np.arange(1, 101)
F1 = 2 * x1**2 + 5

x2 = np.arange(-10, 11)
F2 = np.exp(-x2)

array_zeros, array_ones, array_numbers, (x1, F1), (x2, F2)