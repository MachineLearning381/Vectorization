import time

def correl(dat):

    start_time = time.time()

    covar = []
    mean = []
    matrix = []

    n = len(dat)
    d = len(dat[0])
    ytrav = 0

    while ytrav < d:
        avg = 0
        xtrav = 0
        while xtrav < n:
            avg+=dat[xtrav][ytrav]
            xtrav+=1
        mean.append(round(avg/n,1))
        ytrav+=1

    print('\n\n')
    print('Mean:\n')
    print(mean)

    xtrav2 = 0

    while xtrav2 < d:
        ytrav2 = 0
        covar.append([])
        while ytrav2 < d:
            val = 0
            z = 0
            while z < n:
                val+=(dat[z][xtrav2]-mean[xtrav2])*(dat[z][ytrav2]-mean[ytrav2])
                z+=1
            covar[xtrav2].append(round(val/(d-1),1))
            ytrav2+=1
        xtrav2+=1

    print('\n\n')
    print('Covariance:\n')
    print(covar)

    xtrav3 = 0

    while xtrav3 < d:
        ytrav3 = 0
        matrix.append([])
        while ytrav3 < d:
            matrix[xtrav3].append(round(covar[xtrav3][ytrav3]/((covar[xtrav3][xtrav3]*covar[ytrav3][ytrav3])**.5),1))
            ytrav3+=1
        xtrav3+=1

    print('\n\n')
    print('Correlation:\n')
    print(matrix)

    print("CORRELATION--- %s seconds ---" % (time.time() - start_time))