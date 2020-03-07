# -*- coding: utf-8 -*-
#Data Loading
import pandas as pd 
class b29PP:
    def run(self):
        data = pd.read_csv("sources/veriler.csv")
        #Categoric To Numeric
        from sklearn.preprocessing import OneHotEncoder 
        ulke = data.iloc[:,0:1]
        ohe = OneHotEncoder(categories='auto')
        ulke_ohe = ohe.fit_transform(ulke).toarray()
        
        cinsiyet = data.iloc[:,-1:]
        cinsiyet_ohe = ohe.fit_transform(cinsiyet).toarray()
        
        #numpy To DataFrame
        ulke = pd.DataFrame(data=ulke_ohe , index=data.index, columns=['fr','tr','us'])
        cinsiyet = pd.DataFrame(data=cinsiyet_ohe , index=data.index, columns=['cinsiyet','dummy'])
        cinsiyet = cinsiyet.drop(columns='dummy')
        
        
        #Data Integration
        data = pd.concat([ulke, data.iloc[:,1:4], cinsiyet], axis=1)
        
        source_columns = data.drop(columns='boy')
        target_columns = data[['boy']]
        
        
        #####################   Backward Elimination  ########################
        import statsmodels.api as sm
        import numpy as np
        temp_src = source_columns
        be_list = sm.add_constant(source_columns.to_numpy()) #fit_intercept.py
        while(True):
            results = sm.OLS(endog = target_columns, exog= be_list).fit()
#            print(results.summary())
            p_valuesArray = []
            for j in range(results.params.size):
                r_temp = np.zeros_like(results.params)
                r_temp[j] = 1
                T_test = results.t_test(r_temp)
                p_value = T_test.pvalue.item(0)
                p_valuesArray.append(float(p_value))
            maxPValue = max(p_valuesArray)
            if maxPValue > 0.05:
                source_columns = source_columns.drop(source_columns.columns[(p_valuesArray.index(max(p_valuesArray)))-1], axis='columns')#-1 :> numpy array ve Dataframe de const dan dolayı index farkı oluşur
                be_list = np.delete(arr=be_list,obj=p_valuesArray.index(max(p_valuesArray)) ,axis=1)
            else:
                break
        
        #Data split for Train and Test
        from sklearn.model_selection import train_test_split
        
        x_train, x_test, y_train, y_test = train_test_split(source_columns, target_columns, test_size=0.33, random_state=0)
        
       
        
        #Data Scaling
#        from sklearn.preprocessing import StandardScaler
#        sc= StandardScaler()
#        x_train_temp = sc.fit_transform(x_train)
#        x_test_temp = sc.fit_transform(x_test)
#        x_train = pd.DataFrame(data=x_train_temp, index=x_train.index, columns= x_train.columns)
#        x_test = pd.DataFrame(data=x_test_temp, index=x_test.index, columns= x_test.columns)
        
        return x_train, x_test, y_train, y_test, temp_src
    def getData(self):
        return self.run()
    
obj = b29PP()

x_train, x_test, y_train, y_test, source_columns = obj.getData()