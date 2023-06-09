# -*- coding: utf-8 -*-
"""Intelligent Customer Retention

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1s01y1yLjNBbKhX1ZFITiwE_lvnab4dP_
"""

# Commented out IPython magic to ensure Python compatibility.
import pandas as pd
import numpy as np
import pickle
import matplotlib.pyplot as plt
# %matplotlib inline
import seaborn as sns
import sklearn
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.model_selection import RandomizedSearchCV 
import imblearn
from imblearn.over_sampling import SMOTE
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, classification_report,confusion_matrix,f1_score

data=pd.read_csv(r'/content/Telco_Cust_Churn.csv')
data

data.info()

data.TotalCharges = pd.to_numeric(data.TotalCharges,errors='coerce')
data.isnull().any()

data["TotalCharges"].fillna(data["TotalCharges"].median(),inplace=True)
data.isnull().sum()

from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()
data["gender"]=le.fit_transform(data["gender"])
data["Partner"] = le.fit_transform(data["Partner"])
data["Dependents"] = le.fit_transform(data["Dependents"])
data["PhoneService"] = le.fit_transform(data["PhoneService"])
data["MultipleLines"] = le.fit_transform(data["MultipleLines"])
data["InternetService"] = le.fit_transform(data["InternetService"])
data["OnlineSecurity"] = le.fit_transform(data["OnlineSecurity"])
data["OnlineBackup"] = le.fit_transform(data["OnlineBackup"])
data["DeviceProtection"] = le.fit_transform(data["DeviceProtection"])
data["TechSupport"] = le.fit_transform(data["TechSupport"])
data["StreamingTV"] = le.fit_transform(data["StreamingTV"])
data["StreamingMovies"] = le.fit_transform(data["StreamingMovies"])
data["Contract"] = le.fit_transform(data["Contract"])
data["PaperlessBilling"] = le.fit_transform(data["PaperlessBilling"])
data["PaymentMethod"] = le.fit_transform(data["PaymentMethod"])
data["Churn"] = le.fit_transform(data["Churn"])

data.head()

x=data.iloc[:,1:20].values
y=data.iloc[:,20:21].values
x

y

from sklearn.preprocessing import OneHotEncoder
one=OneHotEncoder()
a= one.fit_transform(x[:,6:7]).toarray()
b= one.fit_transform(x[:,7:8]).toarray()
c= one.fit_transform(x[:,8:9]).toarray()
d= one.fit_transform(x[:,9:10]).toarray()
e= one.fit_transform(x[:,10:11]).toarray()
f= one.fit_transform(x[:,11:12]).toarray()
g= one.fit_transform(x[:,12:13]).toarray()
h= one.fit_transform(x[:,13:14]).toarray()
i= one.fit_transform(x[:,14:15]).toarray()
j= one.fit_transform(x[:,16:17]).toarray()
x=np.delete(x,[6,7,8,9,10,11,12,13,14,16],axis=1)
x=np.concatenate((a,b,c,d,e,f,g,h,i,j,x),axis=1)

from imblearn.over_sampling import SMOTE

smt=SMOTE()
x_resample,y_resample = smt.fit_resample(x,y)

x_resample

y_resample

x.shape,x_resample.shape

y.shape,y_resample.shape

data.describe()

plt.figure(figsize=(12,5))
plt.subplot(1,2,1)
sns.distplot(data["tenure"])
plt.subplot(1,2,2)
sns.distplot(data["MonthlyCharges"])

import matplotlib.pyplot as plt  
import seaborn as sns  
import pandas as pd  
#loading the dataset'tips'  
df=pd.read_csv( r"/content/Telco_Cust_Churn.csv")
#plotting the graph  
plt.figure(figsize=(12,5))
plt.subplot(1,2,1)
sns.countplot(x='gender',data=df) 
plt.subplot(1,2,2)
sns.countplot(x='Dependents',data=df) 
plt.show()

sns.barplot(x="Churn",y="MonthlyCharges",data=data)

sns.heatmap(data.corr(),annot=True)

sns.pairplot(data=data, markers=["^","v"], palette="inferno")

from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x_resample,y_resample,test_size=0.2,random_state=0)

from sklearn.preprocessing import StandardScaler
sc=StandardScaler()
x_train=sc.fit_transform(x_train)
x_test=sc.fit_transform(x_test)

x_train.shape

def logreg(x_train,x_test,y_train,y_test):
  lr = LogisticRegression(random_state=0)
  lr.fit(x_train,y_train)
  y_lr_tr = lr.predict(x_train)
  print(accuracy_score(y_lr_tr,y_train))
  yPred_lr = lr.predict(x_test)
  print(accuracy_score(yPred_lr,y_test))
  print("***Logistic Regression***")
  print("Confusion_Matrix")
  print(confusion_matrix(y_test,yPred_lr))
  print("Classification Report")
  print(classification_report(y_test,yPred_lr))

logreg(x_train,x_test,y_train,y_test)

def decisionTree(x_train,x_test,y_train,y_test):
   dtc =DecisionTreeClassifier(criterion="entropy",random_state=0)
   dtc.fit(x_train,y_train)
   y_dt_tr = dtc.predict(x_train)
   print(accuracy_score(y_dt_tr,y_train))
   yPred_dt = dtc.predict(x_test)
   print(accuracy_score(yPred_dt,y_test))
   print("***Decision Tree***")
   print("confusion_Matrix")
   print(confusion_matrix(y_test,yPred_dt))
   print("Classification Report")
   print(classification_report(y_test,yPred_dt))

decisionTree(x_train,x_test,y_train,y_test)

def RandomForest(x_train,x_test,y_train,y_test):
   rf = RandomForestClassifier(criterion="entropy",n_estimators=10,random_state=0)
   rf.fit(x_train,y_train)
   y_rf_tr = rf.predict(x_train)
   print(accuracy_score(y_rf_tr,y_train))
   yPred_rf = rf.predict(x_test)
   print(accuracy_score(yPred_rf,y_test))
   print("***Random Forest")
   print("Confusion_Matrix")
   print(confusion_matrix(y_test,yPred_rf))
   print("Classification Report")
   print(classification_report(y_test,yPred_rf))

RandomForest(x_train,x_test,y_train,y_test)

def KNN(x_tarin,x_test,y_train,y_test):
   knn = KNeighborsClassifier()
   knn.fit(x_train,y_train)
   y_knn_tr = knn.predict(x_train)
   print(accuracy_score(y_knn_tr,y_train))
   yPred_knn = knn.predict(x_test)
   print(accuracy_score(yPred_knn,y_test))
   print("***KNN***")
   print("Confusion_Matrix")
   print(confusion_matrix(y_test,yPred_knn))
   print("Classification Report")
   print(classification_report(y_test,yPred_knn))

KNN(x_train,x_test,y_train,y_test)

def SVM(x_train,x_test,y_train,y_test):
  SVM = SVC(kernel = "linear")
  SVM.fit(x_train,y_train)
  y_svm_tr = SVM.predict(x_train)
  print(accuracy_score(y_svm_tr,y_train))
  yPred_svm = SVM.predict(x_test)
  print(accuracy_score(yPred_svm,y_test))
  print("***Support Vector Machine***")
  print("Confusion_Matrix")
  print(confusion_matrix(y_test,yPred_svm))
  print("Classification Report")
  print(classification_report(y_test,yPred_svm))

SVM(x_train,x_test,y_train,y_test)

import keras
from keras.models import Sequential
from keras.layers import Dense

classifier = Sequential()

classifier.add(Dense(units=30,activation='relu',input_dim=40))

classifier.add(Dense(units=30,activation='relu'))

classifier.add(Dense(units=1,activation='sigmoid'))

classifier.compile(optimizer='adam',loss='binary_crossentropy',metrics=['accuracy'])

model_history = classifier.fit(x_train,y_train, batch_size=10,validation_split=0.33, epochs=200)

ann_pred =classifier.predict(x_test)
ann_pred =(ann_pred>0.5)
ann_pred

print(accuracy_score(ann_pred,y_test))
print("***ANN Model***")
print("Confusion_Matrix")
print(confusion_matrix(y_test,ann_pred))
print("Classiification Report")
print(classification_report(y_test,ann_pred))

lr = LogisticRegression(random_state=0)
lr.fit(x_train,y_train)
print("Predicting on random input")
lr_pred_own = lr.predict(sc.transform([[0,0,1,1,0,0,0,0,1,0,0,1,0,0,1,0,0,1,0,0,1,0,0,1,0,0,1,0,1,0,0,1,1,0,0,456,1,0,3245,4567]]))
print("output is:", lr_pred_own)

dtc = DecisionTreeClassifier(criterion="entropy",random_state=0)
dtc.fit(x_train,y_train)
print("Predicting on random input")
dtc_pred_own = dtc.predict(sc.transform([[0,0,1,1,0,0,0,0,1,0,0,1,0,0,1,0,0,1,0,0,1,0,0,1,0,0,1,0,1,0,0,1,1,0,0,456,1,0,3425,4567]]))
print("output is: ",dtc_pred_own)

rf = RandomForestClassifier(criterion="entropy",n_estimators=10,random_state=0)
rf.fit(x_train,y_train)
print("Prediction on random input")
rf_pred_own = rf.predict(sc.transform([[0,0,1,1,0,0,0,0,1,0,0,1,0,0,1,0,0,1,0,0,1,0,0,1,0,0,1,0,1,0,0,1,1,0,0,456,1,0,3245,4567]]))
print("output is: ",rf_pred_own)

svc = SVC(kernel = "linear")
svc.fit(x_train,y_train)
print("Prediction on random input")
svm_pred_own = svc.predict(sc.transform([[0,0,1,1,0,0,0,0,1,0,0,1,0,0,1,0,0,1,0,0,1,0,0,1,0,0,1,0,1,0,0,1,1,0,0,456,1,0,3245,4567]]))
print("output is:",svm_pred_own)

knn = KNeighborsClassifier()
knn.fit(x_train,y_train)
print("Prediction on random input")
knn_pred_own = knn.predict(sc.transform([[0,0,1,1,0,0,0,0,1,0,0,1,0,0,1,0,0,1,0,0,1,0,0,1,0,0,1,0,1,0,0,1,1,0,0,456,1,0,3245,4567]]))
print("output is: ",knn_pred_own)

def compareModel(x_train,x_test,y_train,y_test):
  logreg(x_train,x_test,y_train,y_test)
  print('-'*100)
  decisionTree(x_train,x_test,y_train,y_test)
  print('-'*100)
  RandomForest(x_train,x_test,y_train,y_test)
  print('-'*100)
  SVM(x_train,x_test,y_train,y_test)
  print('-'*100)
  KNN(x_train,x_test,y_train,y_test)
  print('-'*100)

print(accuracy_score(ann_pred,y_test))
print("***ANN Model***")
print("Confusion_Matrix")
print(confusion_matrix(y_test,ann_pred))
print("Classification Report")
print(classification_report(y_test,ann_pred))

from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

# define the random forest classifier model
model = RandomForestClassifier()

# define the hyperparameters to tune
params = {
    'n_estimators': [50, 100, 200],
    'max_depth': [5, 10, 20],
    'min_samples_split': [2, 5, 10],
    'min_samples_leaf': [1, 2, 4]
}

# perform grid search cross-validation to find the best hyperparameters
grid_search = GridSearchCV(model, params, cv=5)
grid_search.fit(x_train, y_train)

# print the best hyperparameters found by grid search
print("Best hyperparameters:", grid_search.best_params_)

# get the best model from grid search
model = grid_search.best_estimator_

# evaluate the model on the training set
y_rf = model.predict(x_train)
print("Training set accuracy:", accuracy_score(y_rf, y_train))

# evaluate the model on the test set
yPred_rfcv = model.predict(x_test)
print("Test set accuracy:", accuracy_score(yPred_rfcv, y_test))

# print the confusion matrix and classification report for the test set
print("**Random Forest after Hyperparameter tuning**")
print("Confusion Matrix")
print(confusion_matrix(y_test, yPred_rfcv))
print("Classification Report")
print(classification_report(y_test, yPred_rfcv))

# use the model to predict on a new input
rfcv_pred_own = model.predict(sc.transform([[0,0,1,1,0,0,0,0,1,0,0,1,0,0,1,0,0,1,0,0,1,0,0,1,0,0,1,0,1,0,0,1,1,0,0,456,1,0,3245,4567]]))
print("Output is:", rfcv_pred_own)

classifier.save("telcom_churn.h5")

from flask import flask, render_template, request
import keras
from keras.models import load_model
app = flask(_name_)
model = load_model("telecom_churn.h5")

@app.rute('/') # rendering the html template
def home():
 return render_template('home.html')

@app.route('/')
def helloworld():
 return render_template("base.html")
@app.route('\assement')
def prediction():
 return render_template(/content/index.html.html")
@app.route('/predict', methods=['POST'])
def admin():
a=request.form["gender"]
if(a== 'f'):
    a=0
 if(a== 'm'):
     a=1
   b=request.form["srcitizen"]
 if(b== 'n'):	
      b=0
  if(a== 'y'):
     b=1
   c=request.form[" partner"]
   if(c== 'n'):
	c=0
    if(c== 'y'):
        c=1
    d=request.form[" dependents"]
      if(c== 'n'):
         d=0
     if(d== 'y'):
       d=1
     e=request.form[" tenure"]
     d=request.form["phservices"]
       if(f== 'n'):
          f=0
       if(f== 'y'):
          f=1
       e=request.form["multi"]
         if(g== 'n'):

import keras
from keras.models import sequential
from keras.layers import Dense

classifier=Sequential()
classifier.add(Dence(
q=request.form{“plb”]
if (q==’n’):
q=0
if(q==’y’):
q=1
r=request.form[‘mcharges”]
s=request.form[“tcharges’]
t=[[int(g1),int(g2),int(g3),int(h1),int(h2),int(h3),int(i),int(i2),int(i3),int(j1),int(j2),int(j3)
print(t)
x=model.predict(t)
print(x[0])
if(x[[0]]<=0.5):
y=’no’
return render_template(“predno.html”,z=y)
if(x[[0]]>=0.5)L
y=”Yes”
return render_template(“predyes.html”,z=y)
l1, 12, 13=1,0,0
if (1 == 'nis'):
l1, 12, 13=0,1,0
if (1 == 'y):
l1,12, 13=0,0,1
m= request.form[ "stv"]
if (m =='n'):
m1, m2, m3=1,0,0
if (m =='nis'):
m1, m2, m3=0,1,o
if (m == 'y'):
m1, m2, m3=0,0,1
request.form["smv"]
if (n == 'n'):
n1, n2, n3=1,0,0
if (n =='nis') :
n1, n2, n3-0,1,0
if (n =='y'):
n1,n2, n3=0,O,1
O= request.form["contract"]
if (o== 'mtm):
01,02,03=1,0,0
if (o == oyr'):
o1,02 , o3=0,1,0
if (o == 'tyrs):
01,02, 03=0,0,1
p= request.form["pmt"]
if (p == 'ec'):
p1,p2, p3, p4=1,0, 0, 0
if (p == 'mail'):
p1, p2, p3, p4-0,1,0,0
if (p == ‘bt'):
p1, p2, p3, p4-0,0, 1,0
if (p == 'cc'):
p1, p2, p3, p4=0,0,0, 1
q= request. form[ "plb"]
if (g == "n'):
gl,g2,g3=1,0,0
if (g == 'nps'):
g1,g2,g3=0,1,o
if (g == 'y"):
g1,g2,g3-0,0,1
h= request. form[ "is"]
if (h == 'dsl '):
hi,h2, h3=1,0,o
if (h == 'fo'):
hi, h2, h3-0,1,o
if (h == 'n'):
h1,h2, h3-0,0,1
i= request.form[ "os"]
if (i == 'n'):
i1, i2, i3-1,0,o
if (i == 'nis'):
i1, i2, i3-0,1,0
if (i == 'y):
i1,i2, i3=0, e,1
j= request.form["ob" ]
if (Ở == 'n'):
j1,j2, j3=1,0,e
if (j == 'nis'):
j1,j2,j3-0,1,
if (j == 'y"):
j1,j2,j3-0,0, 1
k= request. form[ "dp"]
if (k == 'n):
k1,k2, k3=1,0,e
if (k == 'nis '):
k1,k2, k3=0,1,0
if (k == 'y'):
k1, k2, k3=0,0,1
l= request.form[ "ts"]
if (1 == 'n'):
11,12,l3=1,0,0