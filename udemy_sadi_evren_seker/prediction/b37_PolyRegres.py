# -*- coding: utf-8 -*-
import pandas as pd
from matplotlib import pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures

class b37_PolyReg:
    def run(self):
        data = pd.read_csv('sources/maaslar.csv')
        x = data.iloc[:,1:2]
        y = data.iloc[:,2:]
        
        #lineer Regression
        lin_reg = LinearRegression()
        lin_reg.fit(x,y)
        y_predicy_lineer = lin_reg.predict(x)
        #Polynomial Regression
        poly_reg_2 = PolynomialFeatures(degree=2)
        x_poly = poly_reg_2.fit_transform(x) #Changes the X and create new X
        lin_reg2 = LinearRegression()
        lin_reg2.fit(x_poly,y)
        y_predict_poly = lin_reg2.predict(poly_reg_2.fit_transform(x))
        
        poly_reg_4 = PolynomialFeatures(degree=4)
        x_poly_4 = poly_reg_4.fit_transform(x) #Changes the X and create new X
        lin_reg2_4 = LinearRegression()
        lin_reg2_4.fit(x_poly_4,y)
        y_predict_poly_4 = lin_reg2_4.predict(poly_reg_4.fit_transform(x))
        
        
        
        x = x.sort_index()
        y = y.sort_index()
        fig = plt.figure('Data and Regressions')
        
        fig.suptitle('Eğitim Seviyesi Maaş İlişkisi Analizi', fontsize=12)
        fig1sub1 = fig.add_subplot(2,1,1)
        fig1sub1.scatter(x, y, color='gray', label='Original Data')
        fig1sub1.plot(x, y_predicy_lineer, color='r', label='Lineer Regression')
        fig1sub1.plot(x, y_predict_poly, color='b', label='Polynomial Regression 2. degree')
        fig1sub1.legend()
        
        fig1sub2 = fig.add_subplot(2,1,2)
        fig1sub2.scatter(x, y, color='gray', label='Original Data')
        fig1sub2.plot(x, y_predicy_lineer, color='r', label='Lineer Regression')
        fig1sub2.plot(x, y_predict_poly_4, color='g', label='Polynomial Regression 4. degree')
        fig1sub2.legend()
        
        return fig
    def getData(self):
        return self.run()

#obj = b37_PolyReg()
#fig = obj.getData()