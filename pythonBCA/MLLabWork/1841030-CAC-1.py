import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.metrics import precision_recall_fscore_support
from sklearn.metrics import confusion_matrix , accuracy_score, classification_report
from sklearn import preprocessing
from sklearn import metrics

df=pd.read_csv("mushroom.csv")

df.head()

x=df.drop('class',axis = 1)
y=df['class']

cols=['cap-shape','cap-surface','cap-color','bruises','odor','gill-attachment','gill-spacing','gill-size','gill-color','stalk-shape', 'stalk-root', 
      'stalk-surface-above-ring','stalk-surface-below-ring', 'stalk-color-above-ring','stalk-color-below-ring', 'veil-type', 'veil-color',
      'ring-number','ring-type', 'spore-print-color', 'population', 'habitat']


# Convert the data into numeric form
from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()
for col in cols:
     x[col]=le.fit_transform(x[col])
y=le.fit_transform(y)
x.head()


# Question 2:  K=1 case for KNN classification leads to over fitting. Demonstrate it using a suitable dataset and sample program.


xk_train,xk_test,yk_train,yk_test= train_test_split(x,y,test_size=0.3, random_state=42)
k = KNeighborsClassifier(n_neighbors=1)
k.fit(xk_train, yk_train)

yk_pred = k.predict(xk_test)
yk_pred

print("Testing Accuracy:",k.score(xk_test, yk_test)*100)
print("Training Accuracy:",k.score(xk_train,yk_train)*100)

# As we can see that train accuracy is 100% so model is good at training dataset
# but on test data the accuracy drops to 68.8%. at it is leading towards overfitting.


# # Question 3:  Explain the suitability of F measure as accuracy metric for class imbalanced data with an example.

data=pd.read_csv("diabetes.csv")

data.head()

data['Outcome'].value_counts()

data.shape

x=data.drop('Outcome',axis = 1)
y=data['Outcome']

x_train_ib,x_test_ib,y_train_ib,y_test_ib=train_test_split(x,y,test_size=0.3, random_state=42)

knn_ib=KNeighborsClassifier()
knn_ib.fit(x_train_ib,y_train_ib)
y_predict_ib=knn_ib.predict(x_test_ib)
y_predict_ib

knn_ib.score(x_test_ib,y_test_ib)

print(classification_report(y_test_ib,knn_ib.predict(x_test_ib)))

# When we need to find FP and FN we use F measure over accuracy and above the F1 score is good.
