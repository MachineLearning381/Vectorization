import numpy as np
import time

cov = np.array([ [1,2,3,],[4,5,6,],[7,8,9,] ]);


def veccor(dat):

    start_time = time.time()

    N = np.sum(dat)       # use np.sum rather than sum, check the difference
    if N == 0:          # if N is zero, quit right way
        return 0
    q = np.std(dat)
    w = np.std(np.transpose(dat))

    e = np.multiply(q,w)

    cov = np.divide( dat, e )
    print('\nNumpy Correlation\n')
    print(cov)

    #print("CORRELATIONVECTORIZED--- %s seconds ---" % (time.time() - start_time))