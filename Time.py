import pairwise as pw
from sklearn import datasets
import time 

iris = datasets.load_iris().data

start_time = time.time()


pw(iris);



print("--- %s seconds ---" % (time.time() - start_time))
