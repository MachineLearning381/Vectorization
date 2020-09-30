import numpy as np

X = np.array([ [1,2,3],[4,5,6],[7,8,9] ]);


Z = np.dot(X,np.transpose(X))

v = np.diagonal(Z)
Z = np.multiply(Z,2)

Z = np.transpose(Z)-v
Z = abs(np.transpose(Z)-v)

Z = Z**0.5

print(Z)