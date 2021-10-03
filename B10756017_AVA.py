# -*- coding: utf-8 -*-
"""
Created on Sat Dec  5 19:39:54 2020

@author: DGE
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt 
#import matplotlib.lines as mlines
from sklearn.metrics import confusion_matrix

W=[]
W_AVA=[]
num=0
color=['red','blue','black']

def adline(w, intercept):
    global num
    """Plot a line from slope and intercept"""
    slope = -w[1]/(w[0])
    axes = plt.gca()
    x_vals = np.array(axes.get_xlim())
    y_vals = intercept + slope * x_vals
    #origin=[np.mean(x_vals), np.mean(y_vals)]
    #plt.text(0,0, 'W=' + str(w))
    plt.plot(x_vals, y_vals, '-',color=color[num])
    num+=1

def perceptron_sgd(X, Y):
    w = [1,-1]
    eta = 0.8
    epochs = 10
    for t in range(epochs):
        err=0.
        for i, x in enumerate(X):
            if (np.dot(X[i], w)*Y[i]) < 0:
                w = w + eta*X[i]*Y[i]
                err+=1
#         print("#err=%f"%(err/5)) 
    return w

# Data partition and training
def OVA():
    W=[]
    for i in range(3):  #OVA
        ind1 = Dy==(i+1)   #address
        ind2 = ind1==False #address
        #print(ind1)
        print("Preparing data with label=", (i+1))
        Y2 = np.copy(Dy)
        Y2[ind1]= 1     # Positive (T)
        Y2[ind2]=-1     # Negative (F)
        print(Y2)
        w = perceptron_sgd(DX,Y2)
        W.append(w)
        adline(w, 1)
    print('W=',W)
    return W

def AVA():
    W=[]
    num = 0
    for i in range(3):  #AVA
        for j in range(i+1,3):
            print(i+1,j+1)
            ind1 = Dy==(i+1)   #address
            ind2 = Dy==(j+1)   #address
            print("Preparing data with label=", (num+1))
            Y = np.copy(Dy)
            need = (Y==i+1) | (Y==j+1)  #class i and class j
            Y[ind1]= 1  # Positive (T)
            Y[ind2]=-1  # Negative (F)
            print(Y[need])
            Y=Y[need]
            w = perceptron_sgd(DX[need],Y)
            """cols = ['sepal','petal','variety']
            X = tr.loc[need,cols]  #符合Y條件的cols"""
            W.append(w)
            num+=1
    print('W=',W)
    return W

def clf(W):
    res = []
    for i in range(3):
        pred = (np.dot(TX, W[i])) #CLF[I].PREDICT(TEST)
        res.append(pred)
        #print(res)
    return res
    
#Input Data
tr = pd.read_csv("iris.data.multiclass.csv")
te = pd.read_csv("iris.test.multiclass.csv")
combine = [tr, te]
for dataset in combine:     #train test data
    dataset['sepal']=dataset['sepal.length']*dataset['sepal.width']
    dataset['petal']=dataset['petal.length']*dataset['petal.width']
    dataset['variety'] = dataset['variety'].map( {'Setosa': 1, 'Versicolor': 2, 'Virginica': 3} ).astype(int)   

DX = tr.drop(['variety'], axis=1)
Dy = tr['variety']
DX = pd.DataFrame(DX, columns= ['sepal', 'petal'])  #to 2D list
DX = DX.values.tolist()
DX = np.array(DX)   #np.dot Error
plt.scatter(DX[Dy==1,0], DX[Dy==1,1],color='red')
plt.scatter(DX[Dy==2,0], DX[Dy==2,1],color='blue')
plt.scatter(DX[Dy==3,0], DX[Dy==3,1],color='black')
#print(DX)
#print(Dy)
W=OVA()
W_AVA=AVA()

# Prediction(預測)
TX = te.drop(['variety'], axis=1)
Ty = te['variety']
Ty = np.array(Ty)
TX = pd.DataFrame(TX, columns= ['sepal', 'petal'])  #to 2D list
TX = TX.values.tolist()
TX = np.array(TX)   #np.dot Error

res = clf(W_AVA)

ans = np.array(res).argmax(0) +1    #np.argmax(res, axis=0)
print(np.array(res))
print("Predicted label=",ans)
print("label=",Ty)
print('Calculating the confusion matrix')
print(confusion_matrix(ans, Ty))
#print(classification_report(ans,Ty))

print('Calculating our own confusion matrix')
cm = np.zeros((3,3), np.int)
for ct, item in enumerate(Ty):
    cm[ans[ct]-1, item-1]+=1
print(cm)