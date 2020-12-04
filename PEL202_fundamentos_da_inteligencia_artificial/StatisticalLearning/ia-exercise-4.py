# This file uses scikit-learn package to classify the iris flower dataset.
# The algorithms used are:
# 1. Least Squares
# 2. PCA (Principal Component Analysis)
# 3. LDA (Linear Discriminant Analysis)
# 4. SVM (Support Vector Machine)

import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.linear_model import LinearRegression
from sklearn.decomposition import PCA
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn import svm

iris = datasets.load_iris()

X = iris.data
y = iris.target
dim = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
y_dim = [dim[i] for i in y]
target_names = iris.target_names
feature_names = iris.feature_names

colors = ['navy', 'turquoise', 'darkorange', 'purple']

# Plot the 4 features of Iris dataset: sepal length, sepal width, petal length,
# and petal width.
fig, g = plt.subplots(2, 2)
subplots = [g[0][0], g[0][1], g[1][0], g[1][1]]
for idx, feature in enumerate(feature_names):
    plot = subplots[idx]
    for color, i, target_name in zip(colors, [0, 1, 2], target_names):
        plot.scatter(X[y == i, idx], y[y == i], color=color, alpha=.8,
                     label=target_name)
    plot.legend(loc='best', shadow=False, scatterpoints=1)
    plot.title.set_text('Feature %s' % feature)

# Linear Regression used for classification
regr = LinearRegression()
regr.fit(X, y_dim)
y_pred = regr.predict(X)
print('\n')
print('Features: %s' % feature_names)
print('Targets: %s' % target_names)
print('Linear regression (classification) coef: %s' % regr.coef_)
print('Linear regression (classification) intercept: %s' % regr.intercept_)

fig, g = plt.subplots(2, 2)
subplots = [g[0][0], g[0][1], g[1][0], g[1][1]]
for idx, target in enumerate(target_names):
    plot = subplots[idx]
    for i in range(len(y_dim)):
        k = iris.target[i]
        plot.scatter(i, y_pred[i, idx], color=colors[k], alpha=0.8,
                        label=target_names[k])
    plot.plot([0, 150], [0.5, 0.5], color='black', alpha=0.8)
    plot.title.set_text(target)

# Linear Regression that tries to approximate from 0 until 2
regr = LinearRegression()
regr.fit(X, y)
y_pred = regr.predict(X)
print('\n')
print('Features: %s' % feature_names)
print('Linear regression coef: %s' % regr.coef_)
print('Linear regression intercept: %s' % regr.intercept_)

plt.figure()
for color, i, target_name in zip(colors, [0, 1, 2], target_names):
    plt.scatter(y[y == i], y_pred[y == i], color=color, alpha=.8, lw=.4,
                label=target_name)
plt.legend(loc='best', shadow=False, scatterpoints=1)
plt.title('Linear Regression')

# PCA
pca = PCA(n_components=2)
X_pca = pca.fit(X).transform(X)
print('\n')
print('PCA components: %s' % str(pca.components_))
print('PCA explained variance: %s' % str(pca.explained_variance_))
print('PCA mean: %s' % str(pca.mean_))
print('PCA explained variance ratio: %s' % str(pca.explained_variance_ratio_))

plt.figure()
for color, i, target_name in zip(colors, [0, 1, 2], target_names):
    plt.scatter(X_pca[y == i, 0], X_pca[y == i, 1], color=color, alpha=.8, lw=.4,
                label=target_name)
plt.legend(loc='best', shadow=False, scatterpoints=1)
plt.title('PCA of IRIS dataset')

# LDA
lda = LinearDiscriminantAnalysis(n_components=2)
X_lda = lda.fit(X, y).transform(X)
print('\n')
print('LDA coef: %s' % str(lda.coef_))
print('LDA intercept: %s' % str(lda.intercept_))
print('LDA explained variance ratio: %s' % str(lda.explained_variance_ratio_))

plt.figure()
for color, i, target_name in zip(colors, [0, 1, 2], target_names):
    plt.scatter(X_lda[y == i, 0], X_lda[y == i, 1], alpha=.8, color=color,
                label=target_name)
plt.legend(loc='best', shadow=False, scatterpoints=1)
plt.title('LDA of IRIS dataset')


# SVM
# Uses linear kernel to have an coefficient and intercept
#clf = svm.SVC(kernel= 'rbf', gamma = 'auto')
clf = svm.SVC(kernel= 'linear', gamma = 'auto')
clf.fit(X, y)
y_pred = clf.predict(X)
print('\n')
print('SVM coef: %s' % clf.coef_)
print('Linear regression intercept: %s' % clf.intercept_)

plt.figure()
for color, i, target_name in zip(colors, [0, 1, 2], target_names):
    plt.scatter(y_pred[y == i], y[y == i], alpha=.8, color=color,
                label=target_name)
plt.legend(loc='best', shadow=False, scatterpoints=1)
plt.title('SVM of IRIS dataset')

plt.xlabel(())
# Show all the plots
plt.show()
