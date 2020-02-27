# -*- coding: utf-8 -*-
import pandas as pd
from sklearn.preprocessing import OneHotEncoder, LabelEncoder
import statsmodels.formula.api as sm
import numpy as np
from sklearn.model_selection import train_test_split


class b32PP:
    def run(self):
        #Data Loading
        data = pd.read_csv('sources/odev_tenis.csv')
        outlook_column = data[['outlook']]
        windy_column = data[['windy']]
        play_column = data[['play']]
        
        
        
        #Data Transforming
        ohe = OneHotEncoder(categories='auto') #Contains 3 variable
        outlook_column_e = ohe.fit_transform(outlook_column).toarray()
        outlook_column_e = pd.DataFrame(data=outlook_column_e, index=outlook_column.index, columns=['overcast','rainy','sunny'])  
        
        le = LabelEncoder() #Contains Binary:2 variable
        windy_column_e = le.fit_transform(windy_column.values.ravel())
        windy_column_e = pd.DataFrame(data=windy_column_e, index=windy_column.index, columns=windy_column.columns)
        play_column_e = le.fit_transform(play_column.values.ravel())
        play_column_e = pd.DataFrame(data=play_column_e, index=play_column.index, columns=play_column.columns)
        
        #Data Integration
        data_e = pd.concat([outlook_column_e, data.iloc[:,1:3],windy_column_e,play_column_e], axis=1)
        source_columns = data_e.drop(columns='humidity')
        target_columns = data_e[['humidity']]
        
        #Backward Elimination  
        for i in range(len(source_columns.columns)):
            results = sm.OLS(endog=target_columns, exog=source_columns).fit()
            p_valuesArray = []
            for j in range(results.params.size):
                r_temp = np.zeros_like(results.params)
                r_temp[j] = 1
                T_test = results.t_test(r_temp)
                p_value = T_test.pvalue.item(0)
                p_valuesArray.append(p_value)
            maxPValue = max(p_valuesArray)
            if maxPValue > 0.05:
                source_columns = source_columns.drop(source_columns.columns[p_valuesArray.index(maxPValue)], axis='columns')
            
            
        #Data split
        x_train, x_test, y_train, y_test = train_test_split(source_columns, target_columns, test_size=0.33, random_state=0)
        
        return x_train, x_test, y_train, y_test, source_columns,data_e
    def getData(self):
        return self.run()
        

#obj = b32PP()
#x_train, x_test, y_train, y_test, source_columns, data_e = obj.getData()

