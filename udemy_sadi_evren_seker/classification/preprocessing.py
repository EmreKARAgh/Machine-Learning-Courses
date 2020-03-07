# -*- coding: utf-8 -*-
import pandas as pd

class Preprocess:
    def __init__(self, data_name_c,autoImpute=True):
        try:
            self.data_name = data_name_c
            self.data = pd.read_csv(('src/'+self.data_name))
            if autoImpute:
                self.impute()
        except:
            print('Can not initialize')
    def print(self,cols=None):
        try:
            if cols == None:
                cols = self.data
            print(self.data)
        except:
            print('Can not print')
    def impute(self,cols=None,strategy_n='mean',strategy_s='most_frequent',fill_value_c = None):
        try:
            if(cols == None):
                cols=self.data
            else:
                cols = self.getCols(cols)
            from sklearn.impute import SimpleImputer
            import numpy as np
            imputer = SimpleImputer(missing_values=np.NaN , strategy=strategy_n)
            imputer_s = SimpleImputer(missing_values=np.NaN , strategy= strategy_s, fill_value=fill_value_c)
            for column_name in cols:
                column = self.data[[column_name]]
                try:
                    column_temp = imputer.fit_transform(column)
                except AttributeError as error:
                    if str(error) == '\'DataFrame\' object has no attribute \'dtype\'':
                        column_temp = imputer_s.fit_transform(column)
                self.__updateColumn(column_temp,column_name)
        except:
            print('Can not impute')
    def dropCols(self,cols):
        try:
            cols = self.getCols(cols)
            self.data.drop(columns=cols,  inplace=True)
            return self.data
        except:
            print('Can not Drop Columns')
    def encode(self,cols,encoder = 'LabelEncoder'):
        try:
            cols = self.getCols(cols)
            if encoder == 'LabelEncoder':
                from sklearn.preprocessing import LabelEncoder
                le = LabelEncoder()
                for column_name in cols:
                    column = self.data[column_name].values.ravel()
                    column_temp = le.fit_transform(column)
                    self.__updateColumn(column_temp, column_name)
            elif encoder == 'OneHotEncoder':
                print('Not implemented')
        except:
            print('Can not encode')
    def __updateColumn(self,arr,arr_name):
        new_column = pd.Series(arr.ravel(), name=arr_name)
        self.data.update(new_column)
    def trainTestSplitting(self,target_columns,source_columns=None, test_size_c=0.33, random_state_c=0):
        try:
            from sklearn.model_selection import train_test_split
            if source_columns == None:
                target_columns = self.getCols(target_columns)
                source_columns = self.data
                for i in target_columns:
                    source_columns = source_columns.drop(columns = i)
            else:
                source_columns = self.getCols(source_columns)
                target_columns = self.getCols(target_columns)
            x_train, x_test, y_train, y_test = train_test_split(source_columns, target_columns, test_size = test_size_c, random_state = random_state_c)
            return x_train, x_test, y_train, y_test
        except:
            print('Can not Split for Train-Test')
            return [],[],[],[]
    def scale(self,cols=None):
        try:
            if(cols == None):
                cols=self.data
            else:
                cols = self.getCols(cols)
            from sklearn.preprocessing import StandardScaler
            sc = StandardScaler()
            for column_name in cols:
                column = self.data[[column_name]].astype(float)
                column = sc.fit_transform(column)
                self.__updateColumn(column, column_name)
        except:
            print('Can not Scale')
    def bWElimination(self,target_columns,source_columns=None,pValue=0.05):
        import statsmodels.api as sm
        import numpy as np
        if source_columns == None:
            if source_columns == None:
                target_columns = self.getCols(target_columns)
                source_columns = self.data
                for i in target_columns:
                    source_columns = source_columns.drop(columns = i)
        else:
            source_columns = self.getCols(source_columns)
            target_columns = self.getCols(target_columns)
        be_list = sm.add_constant(source_columns.to_numpy()) #fit_intercept.py
        while(True):
            results = sm.OLS(endog = target_columns.astype(float), exog= be_list.astype(float)).fit()
            p_valuesArray = []
            for j in range(results.params.size):
                r_temp = np.zeros_like(results.params)
                r_temp[j] = 1
                T_test = results.t_test(r_temp)
                p_value = T_test.pvalue.item(0)
                p_valuesArray.append(float(p_value))
            maxPValue = max(p_valuesArray)
            if maxPValue > pValue:
                source_columns = source_columns.drop(source_columns.columns[(p_valuesArray.index(max(p_valuesArray)))-1], axis='columns')#-1 :> numpy array ve Dataframe de const dan dolayı index farkı oluşur
                be_list = np.delete(arr=be_list,obj=p_valuesArray.index(max(p_valuesArray)) ,axis=1)
            else:
                self.data = pd.concat([source_columns,target_columns], axis=1)
                break
    def getCols(self, cols):
        if all(isinstance(n, int) for n in cols):
            cols_temp=[]
            for i in cols:
                cols_temp.append(self.data.columns[i])     
            cols = self.data[cols_temp]
            return cols
        if all(isinstance(n, str) for n in cols):
            return self.data[cols]
obj = Preprocess('veriler.csv', autoImpute=True) #AutoImpute : True
#obj.impute([3,4], strategy_s='const', fill_value_c='e')
#cols = obj.dropCols([0,2])
#Impute first!
#obj.encode(['ulke','cinsiyet'])
obj.encode([0,4])
obj.scale()
obj.bWElimination([1])
x_train, x_test, y_train, y_test = obj.trainTestSplitting([1])
obj.print()