import numpy as np



cov = np.array([ [1,2,3,],[4,5,6,],[7,8,9,] ]);



q = np.sqrt( np.std(cov) )
w = np.sqrt( np.std(np.transpose(cov)) )

e = np.multiply(q,w)


cov = np.divide( cov, e )