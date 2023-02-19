import numpy as np

x_0 = float(input())
n = int(input())
arr = np.arange(n)
teylor = lambda x: (-1)**(np.where(x)[0]+1)*x_0**(np.where(x)[0])/(np.where(x)[0])
arr = teylor (arr)
z = np.sum(arr)
print(z)
