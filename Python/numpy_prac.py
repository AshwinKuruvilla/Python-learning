import numpy as np
print(np.__version__)

a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6], [7, 8]])


print(np.transpose(a))
print(np.transpose(b))
print(a @ b)
print(a*b)