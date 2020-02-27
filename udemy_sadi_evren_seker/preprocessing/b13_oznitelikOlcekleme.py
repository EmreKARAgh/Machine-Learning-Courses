# -*- coding: utf-8 -*-
import b12_veriKumesindeTrainTest as b12
from sklearn.preprocessing import StandardScaler

myScript = b12.b12_veriOlcekleme()
x_train, x_test, y_train, y_test = myScript.getData()

sc = StandardScaler()
x_train = sc.fit_transform(x_train)
x_test = sc.fit_transform(x_test)
