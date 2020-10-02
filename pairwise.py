import time

def pairwise(dat):

    start_time = time.time()

    print('Dataset:\n')
    print(dat)

    matrix = []
    n = len(dat)
    d = len(dat[0])
    xtrav = 0

    while xtrav < n:
        matrix.append([])
        inc = 0
        while inc < n:
            ytrav = 0
            val = 0
            while ytrav < d:
                val += (dat[xtrav][ytrav] - dat[inc][ytrav])**2
                ytrav+=1
            if (val<0):
                val*=-1
            matrix[xtrav].append(round(val**.5,1))
            inc+=1
        xtrav+=1

    print('\n\n')
    print('Distance:\n')
    print(matrix)

    print("PAIRWISE--- %s seconds ---" % (time.time() - start_time))