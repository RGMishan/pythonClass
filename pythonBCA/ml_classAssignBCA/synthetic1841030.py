import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d.axes3d as axes3d

from sklearn.datasets import make_classification
X,y = make_classification(n_samples = 3000,n_features=3,n_informative=3, 
                          n_redundant=0, n_repeated=0, n_classes=3, n_clusters_per_class=2,
                         class_sep=1.5,flip_y=0,weights=[0.5,0.5,0.5])

X=pd.DataFrame(X)
y =pd.DataFrame(y)


fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ax.scatter(X[0], X[1], X[2], c=y)

ax.set_xlabel('Parameter 1')
ax.set_ylabel('Parameter 2')
ax.set_zlabel('Parameter 3')

plt.show()

from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split

X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2,random_state=42)
model = KNeighborsClassifier(n_neighbors=5)
model.fit(X_train,y_train)

model.score(X_test,y_test)

X1,y1 = make_classification(n_samples=1000, n_features=3, n_informative=2, n_redundant=1, n_repeated=0, 
                          n_classes=2, n_clusters_per_class=2,class_sep=0.75,flip_y=0,weights=[0.5,0.5], random_state=17)

X1=pd.DataFrame(X1)
y1 =pd.DataFrame(y1)


fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ax.scatter(X1[0], X1[1], X1[2], c=y1)

ax.set_xlabel('Parameter 1')
ax.set_ylabel('Parameter 2')
ax.set_zlabel('Parameter 3')

from sklearn.datasets import make_multilabel_classification
X3, y3 = make_multilabel_classification(n_samples=5000, n_features=3,
                                      n_classes=2, random_state=0)

y3

X3=pd.DataFrame(X3)
y3 =pd.DataFrame(y3)


fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ax.scatter(X3[0], X3[1], X3[2], c=y3[0])

ax.set_xlabel('Parameter 1')
ax.set_ylabel('Parameter 2')
ax.set_zlabel('Parameter 3')

X3=pd.DataFrame(X3)
y3 =pd.DataFrame(y3)


fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ax.scatter(X3[0], X3[1], X3[2], c=y3[1])

ax.set_xlabel('Parameter 1')
ax.set_ylabel('Parameter 2')
ax.set_zlabel('Parameter 3')

X3_train,X3_test,y3_train,y3_test = train_test_split(X3,y3,test_size=0.2,random_state=42)
model = KNeighborsClassifier(n_neighbors=6)
model.fit(X3_train,y3_train)

model.score(X3_test,y3_test)

