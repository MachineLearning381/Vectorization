from numpy import random
from sklearn import datasets

x = random.randint(25)
y = random.randint(25)

matrix = random.randint(25,size=(x,y))
iris = datasets.load_iris().target
breast_cancer = datasets.load_breast_cancer().target
digits = datasets.load_digits().target