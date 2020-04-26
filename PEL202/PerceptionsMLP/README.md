The following program was developed for academic purpose, intended to be considered as the fifth task for the subject PEL202 "Fundamentos da Inteligência Artificial".

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
The program uses the iris dataset provided by the scikit-learn. It uses perceptrons and MLP to classify the data

#### Perceptrons 
It isn't possible to predict high degree of accuracy the 3 dimensions (i.e. setosa, versicolor, and virginica) using 1 layer of perceptron. The reason is that a perceptron is not able to distinguish dimensions that are non-linear or have complex linear relationship.

The first test used 2 dimensions, the setosa and versicolor. The score was 1.0, i.e. the perceptron was able to classify them.
```python
Perceptrons score (setosa and versicolor): 1.0
```
The plot below shows real dimension (x axys) against the inferred dimension (y axys). 
![Image of Perceptron 2D](https://github.com/ClaudioBorges/Master/blob/master/PEL202/PerceptionsMLP/img/Figure_1.png)

The second test used all dimensions (3), and the score was below 0.48.
```python
Perceptrons score: 0.48
```
The plot below shows real dimension (x axys) against the inferred dimension (y axys). 
![Image of Perceptron 3D](https://github.com/ClaudioBorges/Master/blob/master/PEL202/PerceptionsMLP/img/Figure_2.png)

#### MLP
The proposed MLP used 1 hidder layer with 100 neurons. The number of neurons were choosen empirically to maximize the score. The score was 0.98, meaning that it was able to classify most of the samples correctly.
```python
MLP score: 0.98
```
The plot below shows real dimension (x axys) against the inferred dimension (y axys). 
![Image of MLP](https://github.com/ClaudioBorges/Master/blob/master/PEL202/PerceptionsMLP/img/Figure_3.png)

### Exercise
- Use o Perceptron para classificar o dataset Iris, separando as classes “setosa” e “versicolor”.
- Faça o mesmo, separando as 3 classes.
- Teste o MLP Classifier para as 3 classes.
