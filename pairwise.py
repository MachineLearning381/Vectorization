import datums as dat

resloop = []
xtrav = 0

print(dat.matrix)
print(len(dat.matrix))

for x in dat.matrix:
    resloop.append([])
    inc = 0
    while inc < len(dat.matrix):
        ytrav = 0
        val = 0
        for y in x:
            val += (dat.matrix[xtrav][ytrav] - dat.matrix[inc][ytrav]) ** 2
            ytrav+=1
        if (val<0):
            val*=-1
        resloop[xtrav].append(round(val ** .5,1))
        inc+=1
    xtrav+=1

print('\n\n')
print(resloop)