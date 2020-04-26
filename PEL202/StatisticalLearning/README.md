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

#### Least Squares
```python
Features: ['sepal length (cm)', 'sepal width (cm)', 'petal length (cm)', 'petal width (cm)']
Targets: ['setosa' 'versicolor' 'virginica']
Linear regression (classification) coef: [
 [ 0.06602977  0.24284787 -0.22465712 -0.05747273]
 [-0.02015368 -0.44561626  0.22066921 -0.4943066 ]
 [-0.04587608  0.20276839  0.00398791  0.55177932]]
Linear regression (classification) intercept: [ 0.11822289  1.57705897 -0.69528186]
```

```python
Features: ['sepal length (cm)', 'sepal width (cm)', 'petal length (cm)', 'petal width (cm)']
Linear regression coef: [-0.11190585 -0.04007949  0.22864503  0.60925205]
Linear regression intercept: 0.186495247206249
```

#### PCA
```python
PCA components: [[ 0.36138659 -0.08452251  0.85667061  0.3582892 ]
 [ 0.65658877  0.73016143 -0.17337266 -0.07548102]]
PCA explained variance: [4.22824171 0.24267075]
PCA mean: [5.84333333 3.05733333 3.758      1.19933333]
PCA explained variance ratio: [0.92461872 0.05306648]
```

#### LDA
```python
LDA coef: [[  6.31475846  12.13931718 -16.94642465 -20.77005459]
 [ -1.53119919  -4.37604348   4.69566531   3.06258539]
 [ -4.78355927  -7.7632737   12.25075935  17.7074692 ]]
LDA intercept: [-15.47783673  -2.02197415 -33.53768674]
LDA explained variance ratio: [0.9912126 0.0087874]
```

#### SVM
```python
SVM coef: [[-0.04625854  0.5211828  -1.00304462 -0.46412978]
 [-0.00722313  0.17894121 -0.53836459 -0.29239263]
 [ 0.59549776  0.9739003  -2.03099958 -2.00630267]]
Linear regression intercept: [1.4528445  1.50771313 6.78097119]
```

### Exercise
Use as funções do Scikit-learn para os Minimos Quadrados, PCA, LDA e SVM e use para a classificação dos dados de Iris de Fisher.

Compare as retas geradas pelos quatro métodos.

Em Python:
–from sklearn import datasets
–iris = datasets.load_iris()
