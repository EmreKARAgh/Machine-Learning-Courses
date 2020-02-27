from sklearn.impute import SimpleImputer
import pandas as pd
import numpy as np

veriler = pd.read_csv('sources/eksikveriler.csv')
print(veriler)
 
imputer = SimpleImputer(missing_values=np.NaN , strategy='mean')
"""
strategystring, default=’mean’
The imputation strategy.

If “mean”, then replace missing values using the mean along each column. Can only be used with NUMERIC data.

If “median”, then replace missing values using the median along each column. Can only be used with CUMERIC data.

If “most_frequent”, then replace missing using the most frequent value along each column. Can be used with STRİNGS OR NUMERİC data.

If “constant”, then replace missing values with fill_value. Can be used with STRİNGS OR NUMERIC data.

"""

yas = veriler.iloc[:,1:4].values
print(yas)

print("-----------------------------------")
imputer = imputer.fit(yas)
yas = imputer.transform(yas)
print(yas)

