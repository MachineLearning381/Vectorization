import datums as dat
import pairwise as dis
import covariance as cov

print('Random\n')
dis.pairwise(dat.matrix)
cov.correl(dat.matrix)

print('\nIris\n')
dis.pairwise(dat.iris)
cov.correl(dat.iris)

print('\nBreast Cancer\n')
dis.pairwise(dat.breast_cancer)
cov.correl(dat.breast_cancer)

print('\nDigits\n')
dis.pairwise(dat.digits)
cov.correl(dat.digits)