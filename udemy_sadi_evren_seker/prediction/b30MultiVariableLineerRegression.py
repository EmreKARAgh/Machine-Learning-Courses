# -*- coding: utf-8 -*-
#Multi Dimensional LineerRegression
from sklearn.linear_model import LinearRegression
import b29PP
from sklearn.metrics import r2_score


obj = b29PP.b29PP()
x_train, x_test, y_train, y_test, data = obj.getData()

regressor = LinearRegression()
regressor.fit(x_train,y_train)

y_prediction = regressor.predict(x_test)
print(r2_score(y_test,y_prediction))

#r2_scores: BE- : 0.5269561623575656   BE+ :0.5130073269361772


