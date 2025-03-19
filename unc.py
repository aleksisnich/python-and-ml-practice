from sklearn import metrics
from sklearn.datasets import load_breast_cancer
from sklearn.linear_model import Perceptron
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
from sklearn.metrics import ConfusionMatrixDisplay

import matplotlib.pyplot as plt
import numpy as np
from sklearn.neural_network import MLPClassifier

data = load_breast_cancer()
X = data.data
Y = data.target

print(X.shape)
print(Y.shape)

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42)
print(X_train.shape)
print(Y_train.shape)
print(X_test.shape)
print(Y_test.shape)

clf = Perceptron(max_iter=1000, eta0=0.01, random_state=0)
clf.fit(X_train, Y_train)
Y_pred = clf.predict(X_test)
print("Accuracy: ", accuracy_score(Y_test, Y_pred))

# cm = confusion_matrix(Y_test, Y_pred)
# disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=[False, True])
# disp.plot()
# plt.show()


# Далее строим модель многослойного перцептрона

mlp = MLPClassifier(hidden_layer_sizes=(30, 30, 30, 30), max_iter=1000, alpha=0.0001, random_state=3)
mlp.fit(X_train, Y_train)
prediction = mlp.predict(X_test)
score = np.round(metrics.accuracy_score(Y_test, prediction), 2)
print("AccuCY: ", accuracy_score(Y_test, prediction))

mp = confusion_matrix(Y_test, prediction)
dis = ConfusionMatrixDisplay(confusion_matrix=mp, display_labels=[False, True])
dis.plot()
plt.show()