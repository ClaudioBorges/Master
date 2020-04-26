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
```python
Perceptrons score (setosa and versicolor): 1.0
```

```python
Perceptrons score: 0.48
```

#### MLP
```python
MLP score: 0.98
```
### Exercise
- Use o Perceptron para classificar o dataset Iris, separando as classes “setosa” e “versicolor”.
- Faça o mesmo, separando as 3 classes.
- Teste o MLP Classifier para as 3 classes.
