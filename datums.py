from numpy import random
from sklearn import datasets

x = random.randint(25)
y = random.randint(25)

matrix = random.randint(25,size=(x,y))
iris = datasets.load_iris()
breast_cancer = datasets.load_breast_cancer()
digits = datasets.load_digits()