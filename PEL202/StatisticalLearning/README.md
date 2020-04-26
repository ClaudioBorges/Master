The following program was developed for academic purpose, intended to be
considered as the fourth task for the subject PEL202 "Fundamentos da Inteligência
Artificial".

### Environemnt
I tested it using Python 3.7.7.

### How to execute
This project uses 2 external libraries, the scikit-learn (0.22.2) and matplotlib (3.2.1). You may want to enable the virtual environment to have the libraries available without importing them:
In bash:
```bash
source venv/bin/activate
python3 ia-exercise-4.py
```
### Analysis
The program uses the iris dataset provided by the scikit-learn. It uses 4 differents methods:
1. Least Squares
1. PCA (Principal Component Analysis)
1. LDA (Linear Discriminant Analysis)
1. SVM (Support Vector Machine)

The Iris flower has 3 dimensions, setosa, versicolor, and virginica, and the dataset has 4 features, sepal length (cm), sepal width (cm), petal length (cm), and petal width (cm) as plot below:

![Image of Iris Dataset](https://github.com/ClaudioBorges/Master/blob/master/PEL202/StatisticalLearning/img/Figure_1.png)

Intuitively, some features seem to influence more the distinguish between the dimension. The petal (either length and width) seems to be a good feature when classifying the setosa dimension. Other features and dimension are harder to distinguish.

#### Least Squares
The first comparion used the least squares method to classify the dimensions, through a vector of n dimension (i.e. `[1,0,0], [0,1,0], [0,0,1]`). In such case, there are 3 intercepts and a matrix of 3x4 representing the coeeficients.

```python
Features: ['sepal length (cm)', 'sepal width (cm)', 'petal length (cm)', 'petal width (cm)']
Targets: ['setosa' 'versicolor' 'virginica']
Linear regression (classification) coef: [
 [ 0.06602977  0.24284787 -0.22465712 -0.05747273]
 [-0.02015368 -0.44561626  0.22066921 -0.4943066 ]
 [-0.04587608  0.20276839  0.00398791  0.55177932]]
Linear regression (classification) intercept: [ 0.11822289  1.57705897 -0.69528186]
```
Looking at the produced coefficient, there is an indicative that a setosa is likely to have a higher sepal width and a lower petal length, while a virginica has the largest petal width, and a versicolor has the lowest sepal width.
A feature's coefficient that is near 0 has a lower or no influence in the dimension regression.

The result of such classification can is plot below:
![Image of Least Square Classification](https://github.com/ClaudioBorges/Master/blob/master/PEL202/StatisticalLearning/img/Figure_2.png)

The second comparison uses the dimension as 0, 1 and 2 instead of classes, producing a single row of coefficient. 
```python
Features: ['sepal length (cm)', 'sepal width (cm)', 'petal length (cm)', 'petal width (cm)']
Linear regression coef: [-0.11190585 -0.04007949  0.22864503  0.60925205]
Linear regression intercept: 0.186495247206249
```

The plot below shows real dimension (x axys) against the inferred dimension (y axys).
![Image of Least Square](https://github.com/ClaudioBorges/Master/blob/master/PEL202/StatisticalLearning/img/Figure_3.png)

#### PCA
The PCA (principal component analysis) was configured to reduce the number of dimension to 2, transforming the coordinating seeking to have the maximum variance.
```python
PCA components: [[ 0.36138659 -0.08452251  0.85667061  0.3582892 ]
 [ 0.65658877  0.73016143 -0.17337266 -0.07548102]]
PCA explained variance: [4.22824171 0.24267075]
PCA mean: [5.84333333 3.05733333 3.758      1.19933333]
PCA explained variance ratio: [0.92461872 0.05306648]
```
The PCA components indicate the petal length is the feature that has the largest variance and sepal length the second one. That way, the petal length and sepal length are the 2 most important component. The same is indicated in the variance. It is insteresting to notice the coordinates are centeres in the PCA means, for that reason we have negative values.

The plot below is the PCA fitted and transformed:
![Image of PCA](https://github.com/ClaudioBorges/Master/blob/master/PEL202/StatisticalLearning/img/Figure_4.png)

#### LDA
The LDA (Linear discriminant analysis) is similar to PCA in the way that it reduces the number of dimensions (in this case to 2), but it tries to maximize the distinction between the classes (instead of the variances).
```python
LDA coef: [[  6.31475846  12.13931718 -16.94642465 -20.77005459]
 [ -1.53119919  -4.37604348   4.69566531   3.06258539]
 [ -4.78355927  -7.7632737   12.25075935  17.7074692 ]]
LDA intercept: [-15.47783673  -2.02197415 -33.53768674]
LDA explained variance ratio: [0.9912126 0.0087874]
```
The coefficients indicate the petal are the 2 most important features to distinguish the setosa and virginica. The 2 most important components of versicolor are the sepal width, and petal length, but not so good as the before.

The plot below is the PCA fitted and transformed:
![Image of LDA](https://github.com/ClaudioBorges/Master/blob/master/PEL202/StatisticalLearning/img/Figure_5.png)


#### SVM
In this SVM version I used the linear kernel, which produced 4 coefficients for each dimension.

```python
SVM coef: [[-0.04625854  0.5211828  -1.00304462 -0.46412978]
 [-0.00722313  0.17894121 -0.53836459 -0.29239263]
 [ 0.59549776  0.9739003  -2.03099958 -2.00630267]]
Linear regression intercept: [1.4528445  1.50771313 6.78097119]
```
The plot below shows real dimension (x axys) against the inferred dimension (y axys).
![Image of SVM](https://github.com/ClaudioBorges/Master/blob/master/PEL202/StatisticalLearning/img/Figure_6.png)


### Exercise
Use as funções do Scikit-learn para os Minimos Quadrados, PCA, LDA e SVM e use para a classificação dos dados de Iris de Fisher.

Compare as retas geradas pelos quatro métodos.

Em Python:
–from sklearn import datasets
–iris = datasets.load_iris()
