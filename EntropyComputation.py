import numpy as np
import time
import datums as dat
import pairwise as dis
import pairwiseVectorization as ndis
import covariance as cov
import CorrelationVectorized as ncov

def entrop(X):
    print('starting running .....')
    np.random.seed(100)
    params = range(10,141,10)   # different param setting
    nparams = len(params)       # number of different parameters

    perf_loop = np.zeros([10,nparams])  # 10 trials = 10 rows, each parameter is a column
    perf_cool = np.zeros([10,nparams])

    counter = 0

    for ncols in X:
        nrows = len(X[0])

        print("matrix dimensions: ", nrows, ncols)

        for i in range(10):
            #X = np.random.randint(0,20,[nrows,ncols])   # random matrix
                                                        # you need to use random.rand(...) for float matrix

            st = time.time()
            entropy_dist = dis.pairwise(X)
            et = time.time()
            perf_loop[i,counter] = et - st              # time difference

            st = time.time()
            entropy_npdist = ndis.vecpair(X)
            et = time.time()
            perf_cool[i,counter] = et - st



            assert np.isclose(entropy_loop, entropy_cool, atol=1e-06)

        counter = counter + 1

    mean_loop = np.mean(perf_loop, axis = 0)    # mean time for each parameter setting (over 10 trials)
    mean_cool = np.mean(perf_cool, axis = 0)

    std_loop = np.std(perf_loop, axis = 0)      # standard deviation
    std_cool = np.std(perf_cool, axis = 0)

    import matplotlib.pyplot as plt
    plt.errorbar(params, mean_loop[0:nparams], yerr=std_loop[0:nparams], color='red',label = 'Loop Solution')
    plt.errorbar(params, mean_cool[0:nparams], yerr=std_cool[0:nparams], color='blue', label = 'Matrix Solution')
    plt.xlabel('Number of Cols of the Matrix')
    plt.ylabel('Running Time (Seconds)')
    plt.legend()
    plt.savefig('CompareEntropyFig.pdf')
    # plt.show()    # uncomment this if you want to see it right way

    print("result is written to CompareEntropyFig.pdf")

def do_run():
    print('Random\n')
    dis.pairwise(dat.matrix)
    ndis.vecpair(dat.matrix)
    cov.correl(dat.matrix)
    ncov.veccor(dat.matrix)
    entrop(dat.matrix)

    ''' print('\nIris\n')
    dis.pairwise(dat.iris)
    ndis.vecpair(dat.iris)
    cov.correl(dat.iris)
    ncov.veccor(dat.iris)


    print('\nBreast Cancer\n')
    dis.pairwise(dat.breast_cancer)
    ndis.vecpair(dat.breast_cancer)
    cov.correl(dat.breast_cancer)
    ncov.veccor(dat.breast_cancer)


    print('\nDigits\n')
    dis.pairwise(dat.digits)
    ndis.vecpair(dat.digits)
    cov.correl(dat.digits)
    ncov.veccor(dat.digits) '''