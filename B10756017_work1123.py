# -*- coding: utf-8 -*-
"""
Created on Mon Oct 19 20:56:16 2020

@author: DGE
"""
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix
#from sklearn import preprocessing

class Perceptron(object):

    def __init__(self, no_of_inputs, iterations=100, learning_rate=0.1):   #在class中直接執行
        self.iterations = iterations
        self.lr = learning_rate
        self.weights = np.zeros(no_of_inputs + 1)   #np.zero(shape)  
      
    def normalization(self,X):
        _, Feat_din = X.shape
        for i in range(Feat_din):
            # m1 = np.mean(X[:,i])
            # v1 = np.std(X[:,i]) 
            X[:,i] = (X[:,i])/np.max(X[:,i])
        return X    
    
    def randomize(self, X, y):
        len1 = len(X)
        idx = np.array(range(len1))
        #rn.shuffle(idx)
        X = X[idx]
        y = y[idx]
        return X, y
    
    def predict(self, inputs):
        results = []
        for item in inputs:
            pred = np.dot(item, self.weights[1:]) + self.weights[0]  ## x1*w1+x2*w2+...xn*wn + b(bias)
            results.append(np.sign(pred))
        return results
    
    def train(self, training_inputs, labels,nm = False):
        if nm :
            training_inputs = self.normalization(training_inputs)
        for _ in range(self.iterations):
 #             training_inputs, labels = self.randomize(training_inputs, labels)
            for inputs, label in zip(training_inputs,labels):
                prediction = self.predict([inputs])
#                 self.weights[1:] += lr (label - prediction) * inputs
#                 self.weights[0] +=  (label - prediction)
                if prediction[0]*label<=0:
                    self.weights[1:] += self.lr*np.dot(inputs, label)
                    self.weights[0] +=  label

#data1
d1 = pd.read_csv("iris.data1.csv")
X1 = d1.drop(['variety'], axis=1)   #axis1刪除縱列
y1 = d1['variety']      #y為label欄
y1 = y1.apply(lambda x:1 if x==0 else -1)
t1 = pd.read_csv("iris.test1.csv",delimiter='\t',header=None)
t1.columns = ['a','b','c','d','label']  #test
Xt1 = t1.drop(['label'], axis=1)
yt1 = t1['label']
yt1 = yt1.apply(lambda x:1 if x==0 else -1)
X_train, X_test, y_train, y_test = train_test_split(X1.values, y1.values, test_size = 0.20)   #import  8成給X 2成給Y
model = Perceptron(X_train.shape[1])   #X_train.shape[1]=4
model.train(X_train, y_train)   #訓練模型
y_pred = model.predict(X_test)  #測試結果
print(confusion_matrix(y_test,y_pred))
print(classification_report(y_test,y_pred))
ans1 = model.predict(Xt1.values)
print(ans1)
print(confusion_matrix(yt1,ans1))
print(classification_report(yt1,ans1))

#data2
d2 = pd.read_csv("iris.data2.csv")
y2 = d2['variety']      #y為label欄
y2 = y2.apply(lambda x:1 if x==0 else -1)
t2 = pd.read_csv("iris.test2.csv",delimiter=',',header=None)
t2.columns = ['a','sepal.width','c','d','label']  #test
Xt2 = t2.drop(['label'], axis=1)
yt2 = t2['label']
yt2 = yt2.apply(lambda x:1 if x==0 else -1)
#data normalization
combine = [d2, t2]
"""for dd in combine:
    #dd.loc[dd['sepal.width'] >= 10,'sepal.width']/=10
    dd['sepal.width'] /=10"""
X2 = d2.drop(['variety'], axis=1)   #刪除答案列
#print(X2)
X2_train, X2_test, y2_train, y2_test = train_test_split(X2.values, y2.values, test_size = 0.20)   #import  8成給X 2成給Y
model = Perceptron(X2_train.shape[1])   #X_train.shape[1]=4
model.train(X2_train, y2_train)   #訓練模型
y2_pred = model.predict(X2_test)  #測試結果
print(confusion_matrix(y2_test,y2_pred))
print(classification_report(y2_test,y2_pred))
ans2 = model.predict(Xt2.values)
print(ans2)
print(confusion_matrix(yt2,ans2))
print(classification_report(yt2,ans2))