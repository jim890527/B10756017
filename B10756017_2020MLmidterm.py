# -*- coding: utf-8 -*-
"""
Created on Wed Nov 11 15:08:34 2020

@author: DGE
"""
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix

# KNN Classifier
def knn_classifier(train_x, train_y):
    from sklearn.neighbors import KNeighborsClassifier
    model = KNeighborsClassifier(algorithm='auto', leaf_size=30, metric='minkowski',
           metric_params=None, n_jobs=1, n_neighbors=5, p=2,
           weights='uniform')
    model.fit(train_x, train_y)     # 訓練模型
    return model

# Decision Tree Classifier
def decision_tree_classifier(train_x, train_y):
    from sklearn import tree
    model = tree.DecisionTreeClassifier(criterion='entropy', max_depth=None, 
    min_samples_split=2, min_samples_leaf=1, min_weight_fraction_leaf=0.0, 
    max_features=None, random_state=None, max_leaf_nodes=None, 
    min_impurity_decrease=0.0, min_impurity_split=None,
     class_weight=None, presort=False)
    model.fit(train_x, train_y)     # 訓練模型
    return model

# SVM Classifier
def svm_classifier(train_x, train_y):
    from sklearn import svm
    model = svm.SVC(gamma=0.00001, C=10000, kernel='rbf', probability=True)
    model.fit(train_x, train_y)     # 訓練模型
    return model

# SVM Classifier using cross validation
def svm_cross_validation(train_x, train_y):
    from sklearn.model_selection import GridSearchCV
    from sklearn import svm
    model = svm.SVC(gamma=0.001, C=1000, kernel='rbf', probability=True)
    param_grid = {'C': [1e+4, 1e+5, 1e+6], 'gamma': [0.001, 0.0001]}
    grid_search = GridSearchCV(model, param_grid, n_jobs = 1, verbose=1)
    grid_search.fit(train_x, train_y)
    best_parameters = grid_search.best_estimator_.get_params()
    for para, val in list(best_parameters.items()):
        print(para, val)
    model = svm.SVC(kernel='rbf', C=best_parameters['C'], gamma=best_parameters['gamma'], probability=True)
    model.fit(train_x, train_y)
    return model

#Main         
tr = pd.read_csv("train.csv")     #nrows=1000讀取X行
te = pd.read_csv("test.csv")
tr = tr.fillna(0)
te = te.fillna(0)
te = te.drop(['PerStatus'], axis=1)
X = tr.drop(['PerStatus'], axis=1)   #axis1刪除縱col
y = tr['PerStatus']
#yy = tr[tr['PerStatus'] == 1]   #離職資料
print(X)
X_train, X_test, y_train, y_test = train_test_split(X.values, y.values, test_size = 0.2)   #8成Train 2成Test
#print(X_train.size)

#model.fit(X_train,y_train)  # 訓練模型
model = decision_tree_classifier(X_train, y_train)
train = model.predict(X_test)    # 訓練所預測出的結果
#print(y_test)   # train的真實結果

print(confusion_matrix(y_test,train))       #計算模組的準確率
print(classification_report(y_test,train))      #計算模組的準確率

ans = model.predict(te)     # 丟進模組預測結果
print(ans)

No = te['PerNo']
#print(No)

data={'PerNo':No,'PerStatus':ans}
#print(data)

df = pd.DataFrame(data)
#print(df)

df.to_csv('ans.csv',index=0)

#https://www.itread01.com/content/1546068790.html
#DT 0.18