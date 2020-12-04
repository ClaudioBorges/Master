import matplotlib.pyplot as plt
from sklearn.linear_model import Perceptron
from sklearn import datasets
from sklearn.neural_network import MLPClassifier
import numpy as np

iris = datasets.load_iris()
X = iris.data
y = iris.target
target_names = iris.target_names

colors = ['navy', 'turquoise', 'darkorange', 'purple']

# Perceptrons

# Iris dataset s classes
clf = Perceptron(tol=1e-6, random_state=0)
X1 = np.concatenate((X[y == 0], X[y == 1]), axis=0)
y1 = np.concatenate((y[y == 0], y[y == 1]), axis=0)
clf.fit(X1, y1)
y_pred = clf.predict(X1)
score = clf.score(X1, y1)
print('Perceptrons score (setosa and versicolor): {}'.format(score))

for color, i, target_name in zip(colors, [0, 1], target_names):
    plt.scatter(y1[y1 == i], y_pred[y1 == i], color=color, alpha=.8, lw=.4,
                label=target_name)
plt.legend(loc='best', shadow=False, scatterpoints=1)
plt.title('Perceptrons for setosa and versicolor')


# Iris dataset 3 classes
clf = Perceptron(tol=1e-6, random_state=0)
clf.fit(X, y)
y_pred = clf.predict(X)
score = clf.score(X, y)
print('Perceptrons score: {}'.format(score))

plt.figure()
for color, i, target_name in zip(colors, [0, 1, 2], target_names):
    plt.scatter(y[y == i], y_pred[y == i], color=color, alpha=.8, lw=.4,
                label=target_name)
plt.legend(loc='best', shadow=False, scatterpoints=1)
plt.title('Perceptrons')


# MLP
clf = MLPClassifier(hidden_layer_sizes=(100),
                    max_iter=5000,
                    solver='sgd',
                    tol=1e-6)
clf.fit(X, y)
y_pred = clf.predict(X)
score = clf.score(X, y)
print('MLP score: {}'.format(score))

plt.figure()
for color, i, target_name in zip(colors, [0, 1, 2], target_names):
    plt.scatter(y[y == i], y_pred[y == i], color=color, alpha=.8, lw=.4,
                label=target_name)
plt.legend(loc='best', shadow=False, scatterpoints=1)
plt.title('MLP')

# Show all the plots
plt.show()

