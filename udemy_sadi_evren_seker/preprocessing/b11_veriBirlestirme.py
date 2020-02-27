from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder
import pandas as pd
import numpy as np

class VeriBirlestirme:
    def run(self):
        veriler = pd.read_csv('sources/eksikveriler.csv')
        imputer = SimpleImputer(missing_values=np.nan , strategy='mean')
        yas = veriler.iloc[:,1:4].values
        yas = imputer.fit_transform(yas)
        
        ohe = OneHotEncoder(categories='auto')
        ulke = veriler.iloc[:,0:1]
        ulke = ohe.fit_transform(ulke).toarray()
        
        sonuc = pd.DataFrame(data = ulke, index = range(22) , columns=['fr','tr','us'])
        #print(sonuc)
        
        sonuc2 = pd.DataFrame(data = yas, index = range(22), columns=['boy','kilo','yas'])
        #print(sonuc2)
        
        cinsiyet = veriler.iloc[:,-1:]
        #print(cinsiyet)
        
        sonuc3 = cinsiyet
        
        final_frame = pd.concat([sonuc,sonuc2,sonuc3],axis=1)
        return final_frame
        #print(final_frame)
    def getData(self):
        return self.run()
        
