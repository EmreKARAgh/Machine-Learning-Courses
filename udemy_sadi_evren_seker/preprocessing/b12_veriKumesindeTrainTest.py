# -*- coding: utf-8 -*-
import b11_veriBirlestirme as vb
from sklearn.model_selection import train_test_split
class b12_veriOlcekleme:
    def run(self):
        a = vb.VeriBirlestirme()
        veri = a.getData()
        
        source_columns = veri.iloc[:,0:-1]
        target_columns = veri.iloc[:,-1:]
        
        x_train, x_test, y_train, y_test = train_test_split(source_columns, target_columns, test_size=0.33, random_state=0)
        return x_train,x_test,y_train,y_test
    def getData(self):
        return self.run()
