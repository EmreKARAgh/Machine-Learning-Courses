# -*- coding: utf-8 -*-
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
import numpy as np
import statsmodels.api as sm

y = np.array([1,3,4,5,2,3,4])
X = np.array(range(1,8)).reshape(-1,1) # reshape to column

lr = LinearRegression()
lr.fit(X,y)
print('lr.score 1:    ', lr.score(X,y))

y_pred=lr.predict(X)
print('r2_score 1:    ',r2_score(y, y_pred))

X_const = sm.add_constant(X)
model = sm.OLS(y,X_const) # X_const here
results = model.fit()
print('re.rsquared 1: ', results.rsquared)


######################################################


lr2 = LinearRegression(fit_intercept=False)
lr2.fit(X,y)
print('lr2.score: 2  ', lr2.score(X,y))

y_pred2=lr2.predict(X)
print('r2_score 2:   ',r2_score(y, y_pred2))

model2 = sm.OLS(y,X) # X_const here
results2 = model2.fit()
print('re.rsquared 2: ', results2.rsquared)

#https://stackoverflow.com/questions/54614157/scikit-learn-statsmodels-which-r-squared-is-correct