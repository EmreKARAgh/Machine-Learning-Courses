# -*- coding: utf-8 -*-
import pandas as pd
import statsmodels.formula.api as sm
import numpy as np

from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.svm import SVR
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score

data = pd.read_csv('sources/maaslar_yeni.csv')

print(data.corr())

source_columns = data.drop(columns=['unvan','maas','Calisan ID'])
source_columns_BE = source_columns.copy()
target_columns = data[['maas']]

lin_reg = LinearRegression()
lin_reg.fit(source_columns,target_columns)
lin_reg_pred = lin_reg.predict(source_columns)

results=sm.OLS(lin_reg_pred, source_columns).fit()
print(results.rsquared)

results = sm.OLS(endog = target_columns, exog= source_columns_BE).fit()
print(results.rsquared)


print(r2_score(target_columns,lin_reg_pred))


#for i in range(len(source_columns_BE.columns)):
#    results = sm.OLS(endog = target_columns, exog= source_columns_BE).fit()
#    p_valuesArray = []
#    for j in range(results.params.size):
#        r_temp = np.zeros_like(results.params)
#        r_temp[j] = 1
#        T_test = results.t_test(r_temp)
#        p_value = T_test.pvalue.item(0)
#        p_valuesArray.append(float(p_value))
#    maxPValue = max(p_valuesArray)
#    if maxPValue > 0.05:
#        source_columns_BE = source_columns_BE.drop(source_columns_BE.columns[p_valuesArray.index(max(p_valuesArray))], axis='columns')