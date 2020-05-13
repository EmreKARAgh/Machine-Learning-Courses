# -*- coding: utf-8 -*-
from sklearn.ensemble import RandomForestClassifier
from preprocessing import Preprocess
from sklearn.metrics import confusion_matrix

pp = Preprocess('src/veriler.csv')
pp.dropCols(['ulke'])
data = pp.getData()

x_train, x_test, y_train, y_test = pp.trainTestSplitting(['cinsiyet'])
y_train = y_train.values.ravel()


for i in range(5,20):
    rfc = RandomForestClassifier(n_estimators = i)
    rfc.fit(x_train,y_train)
    y_pred = rfc.predict(x_test)
    cm = confusion_matrix(y_test,y_pred)
    print(str(cm[0][0] + cm[1][1]) +'/'+ str(8))

