# -*- coding: utf-8 -*-
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVR
from matplotlib import pyplot as plt
import b37_PolyRegres
import numpy as np


data = pd.read_csv('sources/maaslar.csv')
x = data.iloc[:,1:2]
y = data.iloc[:,2:]

X = np.array(x, dtype=float)
Y = np.array(y, dtype=float)


sc1 = StandardScaler()
x_scaled = sc1.fit_transform(X)
sc2 = StandardScaler()
y_scaled = sc2.fit_transform(Y)

svr_reg = SVR(kernel='rbf') #default kernel = rbf, default degree=3
svr_reg.fit(x_scaled, y_scaled)
y_predict_SVR_rbf = svr_reg.predict(x_scaled)

svr_reg = SVR(kernel='poly') #default kernel = rbf, default degree=3
svr_reg.fit(x_scaled, y_scaled)
y_predict_SVR_poly = svr_reg.predict(x_scaled)

svr_reg = SVR(kernel='sigmoid') #default kernel = rbf, default degree=3
svr_reg.fit(x_scaled, y_scaled)
y_predict_SVR_sigmoid = svr_reg.predict(x_scaled)

svr_reg = SVR(kernel='linear') #default kernel = rbf, default degree=3
svr_reg.fit(x_scaled, y_scaled)
y_predict_SVR_linear = svr_reg.predict(x_scaled)

#svr_reg = SVR(kernel='precomputed') #default kernel = rbf, default degree=3
#svr_reg.fit(x_scaled, y_scaled)
#y_predict_SVR_precomputed = svr_reg.predict(x_scaled)




fig1 = plt.figure('SVR Regression')
fig1.suptitle('Eğitim Seviyesi Maaş İlişkisi Analizi', fontsize=12)
fig1sub1 = fig1.add_subplot(1,1,1)
fig1sub1.scatter(x_scaled, y_scaled, color='gray', label='Scaled Original Data')
fig1sub1.plot(x_scaled, y_predict_SVR_rbf, label = 'SVR RBF')
fig1sub1.plot(x_scaled, y_predict_SVR_linear, label = 'SVR Linear')
fig1sub1.plot(x_scaled, y_predict_SVR_poly, label = 'SVR Poly')
fig1sub1.plot(x_scaled, y_predict_SVR_sigmoid, label = 'SVR Sigmoid')
fig1sub1.legend()

other_reg = b37_PolyRegres.b37_PolyReg()
fig2 = other_reg.getData()