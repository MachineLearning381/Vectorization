import datums as dat

resloop = []
xtrav = 0

print(dat.matrix)

for x in dat.matrix:
    resloop.append([])
    inc = 0
    while inc < len(dat.matrix):
        ytrav = 0
        val = 0
        for y in x:
            val += (dat.matrix[xtrav][ytrav] - dat.matrix[inc][ytrav]) ** 2
            ytrav++
        if (val<0)
            val*=-1
        resloop[inc].append(val ** .5)
        inc++

print('\n\n')
print(resloop)