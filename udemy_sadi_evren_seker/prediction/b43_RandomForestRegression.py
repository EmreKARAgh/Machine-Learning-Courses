# -*- coding: utf-8 -*-
from sklearn.ensemble import RandomForestRegressor
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

data = pd.read_csv('sources/maaslar.csv')

x = data.iloc[:,1:2]
y = data.iloc[:,2:]

X = np.array(x, dtype=float) #X 2D array expected
K = X + 0.5
Z = X - 0.5

Y = np.array(y, dtype=float).ravel() #Y 1D column array expected

sample1= np.array([6.6], dtype=float).reshape(-1,1)
sample2= np.array([11], dtype=float).reshape(-1,1)

rf_reg = RandomForestRegressor(n_estimators=10,random_state=0)
rf_reg.fit(X,Y)
y_predict_RandomF_X = rf_reg.predict(X)
y_predict_RandomF_K = rf_reg.predict(K)
y_predict_RandomF_Z = rf_reg.predict(Z)

#print(rf_reg.predict(sample1))
#print(rf_reg.predict(sample2))

fig1 = plt.figure('Random Forest Regression')

fig1sub1 = fig1.add_subplot(111)
fig1sub1.scatter(X,Y,label='Original Data')
fig1sub1.plot(X,y_predict_RandomF_X, label='Random Forest Prediction for X')
fig1sub1.plot(X,y_predict_RandomF_K, label='Random Forest Prediction for K')
fig1sub1.plot(X,y_predict_RandomF_Z, label='Random Forest Prediction for Z')
fig1sub1.legend()

