# -*- coding: utf-8 -*-
import preprocessing
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix

pp = preprocessing.Preprocess('veriler.csv')
pp.dropCols(['ulke'])
pp.dropRows([0,1,2,3,4])
#pp.scale([0,1,2])

x_train, x_test, y_train, y_test = pp.trainTestSplitting(['cinsiyet'])

knn = KNeighborsClassifier(n_neighbors=1, metric='minkowski')
knn.fit(x_train,y_train.values.ravel())

y_pred = knn.predict(x_test)

cm=confusion_matrix(y_test,y_pred)
print('y_pred:', y_pred)
print('y_test:', y_test)
print(cm)
