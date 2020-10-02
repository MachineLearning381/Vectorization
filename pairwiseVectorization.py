import numpy as np
import time


X = np.array([ [1,2,3],[4,5,6],[7,8,9] ]);

def vecpair(dat):

    start_time = time.time()

    Z = np.dot(dat,np.transpose(dat))

    v = np.diagonal(Z)
    Z = np.multiply(Z,2)

    Z = np.transpose(Z)-v
    Z = abs(np.transpose(Z)-v)

    Z = Z**0.5

    print('\nNumpy Distance\n')
    print(Z)

    print("PAIRWISEVECTOR--- %s seconds ---" % (time.time() - start_time))