# -*- coding: utf-8 -*-
from sklearn.naive_bayes import GaussianNB, MultinomialNB, ComplementNB, BernoulliNB, CategoricalNB
from sklearn.metrics import confusion_matrix
import preprocessing

pp = preprocessing.Preprocess('src/veriler.csv')
pp.dropCols(['ulke'])
#pp.encode()
data = pp.getData()

x_train, x_test, y_train, y_test = pp.trainTestSplitting(['cinsiyet'])
y_train = y_train.values.ravel()

gnb = GaussianNB() #continous dağılımlı veriler içeriyorsa
gnb.fit(x_train,y_train)
y_pred_gnb = gnb.predict(x_test)
cm_gnb = confusion_matrix(y_test,y_pred_gnb)
print('GaussianNB:\n',cm_gnb)

mnb = MultinomialNB() #nominal yani kesikli dağılım içeriyorsa
mnb.fit(x_train, y_train)
y_pred_mnb = mnb.predict(x_test)
cm_mnb= confusion_matrix(y_test,y_pred_mnb)
print('MultiominalNB:\n',cm_mnb)

compnb = ComplementNB() #Hedef sınıf nominal veriler içeriyorsa ve dengesizse (imbalanced) Özellikle text classificationda Complement > Multinominal
compnb.fit(x_train, y_train)
y_pred_compnb = compnb.predict(x_test)
cm_compnb= confusion_matrix(y_test,y_pred_compnb)
print('ComplementNB:\n',cm_compnb)

bernb = BernoulliNB() #Hedef sınıf binomial 0-1 veriler içeriyorsa 
bernb.fit(x_train, y_train)
y_pred_bernb = bernb.predict(x_test)
cm_bernb= confusion_matrix(y_test,y_pred_bernb)
print('BernoulliNB:\n',cm_bernb)

#catnb = CategoricalNB() #Eğitim Parametreleri categoric olan değerler için
#catnb.fit(x_train, y_train)
#y_pred_catnb = catnb.predict(x_test)
#cm_catnb= confusion_matrix(y_test,y_pred_catnb)
#print(' CategoricalNB:\n',cm_catnb)