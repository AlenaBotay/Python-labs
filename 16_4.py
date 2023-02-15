import numpy as np
x = np.array([0, 11, 0, 0, -7, 2, 0, 4, 0])

a = np.where(x ==0)[0]
print(a)

x1 = np.array(list(x)+[0])
print(x1)

y = x1[a+1]
print(y)

m = max(y)
print(m)
