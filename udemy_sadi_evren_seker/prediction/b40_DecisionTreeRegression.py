import pandas as pd
from sklearn.tree import DecisionTreeRegressor
import numpy as np
from matplotlib import pyplot as plt

data = pd.read_csv('sources/maaslar.csv')
x = data.iloc[:,1:2]
y = data.iloc[:,2:]

X = np.array(x, dtype=float)
Y = np.array(y, dtype=float)
K = X + 0.5
Z = X - 0.4

reg_decT = DecisionTreeRegressor(random_state=0)
reg_decT.fit(X, Y)
y_predict_X = reg_decT.predict(X)
y_predict_K = reg_decT.predict(K)
y_predict_Z = reg_decT.predict(Z)

sample1 = np.array([6.6], dtype=float).reshape(-1,1)
sample2 = np.array([11], dtype=float).reshape(-1,1)

fig1 = plt.figure('Decision Tree Regression')
fig1sub1 = fig1.add_subplot(111)

fig1sub1.scatter(X, Y, label='Scaled Original Data')
fig1sub1.plot(X, y_predict_X, color='orange', label='Decision Tree Prediction X')
fig1sub1.plot(X, y_predict_K, color='c', label='Decision Tree Prediction K')
fig1sub1.plot(X, y_predict_Z, color='m', label='Decision Tree Prediction Z')

fig1sub1.scatter(6.6, reg_decT.predict(sample1),color='green', label=('sample1(6.6): '+ str(reg_decT.predict(sample1).item(0))))
fig1sub1.scatter(11, reg_decT.predict(sample2),color='red', label=('sample2(11): '+ str(reg_decT.predict(sample2).item(0))))

fig1sub1.legend()

plt.show()