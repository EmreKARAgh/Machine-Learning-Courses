# -*- coding: utf-8 -*-
from sklearn.linear_model import LinearRegression
import b32PP
from sklearn.metrics import r2_score

obj = b32PP.b32PP()
x_train, x_test, y_train, y_test, source_columns,data_e = obj.getData()

regressor = LinearRegression()
regressor.fit(x_train,y_train)

y_prediction = regressor.predict(x_test)
print(r2_score(y_test,y_prediction))

#r2_scores: BE- : -1.3108047443640687   BE+ :-0.30228134925220784
