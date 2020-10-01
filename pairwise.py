def pairwise(dat):
    print('Dataset:\n')
    print(dat)

    matrix = []
    xtrav = 0

    for x in dat:
        matrix.append([])
        inc = 0
        while inc < len(dat):
            ytrav = 0
            val = 0
            for y in x:
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