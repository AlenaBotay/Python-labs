import numpy as np

x = np.array([8, 0, 0, 1, 0, 0, 0, -17.5, 0])
y = np.arange(len(x))
y[x == 0] = 0
y = np.maximum.accumulate(y) #повторяем максимальный элемент
z = x[y] 
print(z)
