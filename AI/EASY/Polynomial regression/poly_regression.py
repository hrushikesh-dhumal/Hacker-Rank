# Enter your code here. Read input from STDIN. Print output to STDOUT
#import sys

from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures

# Read first line for getting train data dimensions
(F, N) = [int(val) for val in raw_input().split()]

# Read next N lines to get train data
data_train_X = []
data_train_y = []
for i in range(N):
    new_feature = []
    j = 0
    for val in raw_input().split():
        if j < F:
            new_feature.append(float(val))
        else:
            data_train_y.append(float(val))
        j = j+1
    data_train_X.append(new_feature)
        
# Read next line to get test data dimension
N = int(raw_input())

# Read next N lines to get test data
data_test = [[float(val) for val in raw_input().split()] for i in range(N)]

#generate a model of polynomial features
poly = PolynomialFeatures(degree=3)

#transform the x data for proper fitting (for single variable type it returns,[1,x,x**2])
data_train_X_ = poly.fit_transform(data_train_X)

#generate the regression object
clf = LinearRegression()

#preform the actual regression
clf.fit(data_train_X_, data_train_y)

for each_result in clf.predict(poly.fit_transform(data_test)):
    print each_result
    