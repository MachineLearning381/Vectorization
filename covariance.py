import pairwise as dat

covar = []
mean = []
matrix = []

n = len(dat.matrix)
xtrav = 0

while xtrav < n:
    avg = 0
    ytrav = 0
    while ytrav < n:
        avg+=dat.matrix[xtrav][ytrav]
        ytrav+=1
    mean.append(round(avg/n,1))
    xtrav+=1

xtrav2 = 0

while xtrav2 < n:
    ytrav2 = 0
    covar.append([])
    while ytrav2 < n:
        val = 0
        z = 0
        while z < n:
            val+=(dat.matrix[xtrav2][z]-mean[xtrav])*(dat.matrix[ytrav][z]-mean[ytrav])
            z+=1
        covar[xtrav].append(round(val/(n-1),1))
        ytrav2+=1

print('Covariance:\n\n')
print(covar)

xtrav3 = 0

while xtrav3 < n:
    ytrav3 = 0
    matrix.append([])
    while ytrav < n:
        matrix[xtrav3].append(round(covar[xtrav3][ytrav3]/((covar[xtrav3][xtrav3]*covar[ytrav3][ytrav3])**.5),1))
        ytrav3+=1
    xtrav3+=1

print('Correlation:\n\n')
print(matrix)