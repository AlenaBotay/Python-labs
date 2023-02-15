import numpy as np
x = np.array([1, 0, 1, 1, 0, 1, 1, 0])
y = np.array([0, 2, 0, 2, 0, 2, 0, 0])
nulx = np.where(x == 0)

nuly = np.where(y == 0)
print(nulx[0])
print(nuly[0])

z = nulx[0][np.in1d(nulx[0],nuly[0])]
both0 = len(z)
not0 = len(x) - len(z)

print(z)
print(both0)
print(not0)
