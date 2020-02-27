# -*- coding: utf-8 -*-
import pandas as pd
from sklearn.model_selection import train_test_split
class preprocessing:
    def run(self):
        data = pd.read_csv('sources/satislar.csv')
        
        aylar = data.iloc[:,0:1]
        satislar = data.iloc[:,1:2]
        
        x_train,x_test, y_train, y_test = train_test_split(aylar, satislar, test_size=0.33, random_state=0)
        return x_train,x_test, y_train, y_test
    def getData(self):
        return self.run()
    
    
obj = preprocessing()
x_train,x_test, y_train, y_test = obj.getData()


