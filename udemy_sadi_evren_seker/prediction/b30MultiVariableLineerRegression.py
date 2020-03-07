# -*- coding: utf-8 -*-
#Multi Dimensional LineerRegression
from sklearn.linear_model import LinearRegression
import b29PP




obj = b29PP.b29PP()
x_train, x_test, y_train, y_test, data = obj.getData()

regressor = LinearRegression()
regressor.fit(x_train,y_train)

y_prediction = regressor.predict(x_test)


print(regressor.score(x_train,y_train))

#r2_scores: BE- : 0.9145366334467461   BE+ :0.9131813596701345 #Yas kolonu silinir

