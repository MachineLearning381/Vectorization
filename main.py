import EntropyComputation as entr
import datums as dat
import pairwise as dis
import pairwiseVectorization as ndis
import covariance as cov
import CorrelationVectorized as ncov

print('Random\n')
dis.pairwise(dat.matrix)
ndis.vecpair(dat.matrix)
cov.correl(dat.matrix)
ncov.veccor(dat.matrix)

# print('\nIris\n')
# dis.pairwise(dat.iris)
# ndis.vecpair(dat.iris)
# cov.correl(dat.iris)
# ncov.veccor(dat.iris)


# print('\nBreast Cancer\n')
# dis.pairwise(dat.breast_cancer)
# ndis.vecpair(dat.breast_cancer)
# cov.correl(dat.breast_cancer)
# ncov.veccor(dat.breast_cancer)


# print('\nDigits\n')
# dis.pairwise(dat.digits)
# ndis.vecpair(dat.digits)
# cov.correl(dat.digits)
# ncov.veccor(dat.digits)