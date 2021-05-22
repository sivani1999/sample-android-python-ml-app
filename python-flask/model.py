# -*- coding: utf-8 -*-
"""
Created on Sat Feb 20 10:39:20 2021

@author: admin
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn import metrics
from sklearn import svm
import seaborn as sns
#from sklearn  import tree
from sklearn.naive_bayes import GaussianNB
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
#from imblearn.over_sampling import SMOTE
import pickle
import warnings 
warnings.simplefilter("ignore")


'''def smote_func(data):
    x=data.iloc[:,0:-1]
    y=data.iloc[:,-1]
    os= SMOTE(random_state=20)
    x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.20,random_state=10)
    columns=x_train.columns
    os_data_x,os_data_y=os.fit_sample(x_train,y_train)
    pd.DataFrame(data=os_data_x,columns=columns)
    pd.DataFrame(data=os_data_y,columns=['Output'])
    return   os_data_x,x_test, os_data_y,y_test'''


def ran(data): 
    random_forest_model=RandomForestClassifier()
    random_forest_model.fit(x_train,y_train)
    predict_train_data=random_forest_model.predict(x_test)
    ra=(metrics.accuracy_score(y_test,predict_train_data)*100)
    print("random",ra)
    return ra

def svc(data):
    obj=svm.SVC(kernel="linear",gamma='auto')
    obj.fit(x_train,y_train)
    y_predict_data=obj.predict(x_test)
    s=(metrics.accuracy_score(y_test,y_predict_data)*100)
    print("svm",s)
    return s


#naive_bayes
def nb(data):
    gaus=GaussianNB()
    gaus.fit(x_train,y_train)
    y_predicti=gaus.predict(x_test)
    g=(metrics.accuracy_score(y_test,y_predicti)*100)
    print("nb",g)
    return g
#'''Logistic Regression
def lr(data):
    obj1=LogisticRegression()
    obj1.fit(x_train,y_train)
    l=(obj1.score(x_test,y_test)*100)
    print("lr",l)
    return l
#KNN
def knn(data):
    obj2=KNeighborsClassifier()
    obj2.fit(x_train,y_train)
    y_pr=obj2.predict(x_test)
    k=(metrics.accuracy_score(y_test,y_pr)*100)
    print("knn",k)
    return k

data=pd.read_csv('./d.csv')

col=['n_pregnant','glucose_conc','bp','skin_thick','insulin','bmi','pedigree_fun','age','Output']
data.columns=col

#output count
diabetes_true_count= len(data.loc[data['Output'] == True])
diabetes_false_count = len(data.loc[data['Output'] == False])
print(diabetes_true_count,diabetes_false_count)


#replacing the null values with mean
col=['glucose_conc','bp','skin_thick','insulin','bmi']
for i in col:
    data[i].replace(0,np.mean(data[i]), inplace= True)


#outlier(data)

#plt.figure(figsize=(8,8))
#sns.heatmap(data.corr(),annot=True,cmap="coolwarm")


x=data.iloc[:,0:-1]
y=data.iloc[:,-1]
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=42)

a={}
a['RAN']=ran(data)
a['SVM']=svc(data)
a['NB']=nb(data)
a['LR']=lr(data)
a['KNN']=knn(data)
print(a)
'''fig=plt.figure()
ax=fig.add_axes([0,0,1,1])
algo=a.keys()
print(algo)
values=a.values()
ax.bar(algo,values,width=0.5,color=['blue'])
plt.show()'''

'''os=SMOTE(random_state=20)
os_data_x,os_data_y=os.fit_sample(x,y)
pd.DataFrame(data=os_data_x,columns=x.columns)
pd.DataFrame(data=os_data_y,columns=['num'])
x_train,x_test,y_train,y_test = train_test_split(x , y , test_size=0.20,random_state=10)'''

rf=RandomForestClassifier()

#Train the model
rf.fit(x_train,y_train)




# Saving model to disk
pickle.dump(rf, open('model.pkl','wb'))

# Loading model to compare the results
model = pickle.load(open('model.pkl','rb'))

