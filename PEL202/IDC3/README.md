The following program was developed for academic purpose, intended to be
considered as the third task for the subject PEL202 "Fundamentos da Inteligência
Artificial".

### Environemnt
I tested it using Python 3.6.10 and Python 2.6.9.

### How to execute
In bash: `python ia-exercise-3.py`

The program will automatically read the `iris.data` dataset.
Each line of the dataset is expected to have 5 columns, sepal length in cm, sepal width in cm, petal length in cm, petal width in cm, and instance class (Iris Setosa, Iris Versicolour, and Iris Virginica).

The output of the program is a colection of IF, THEN, ELSE statements.
Givin the [UCI iris flower dataset](http://archive.ics.uci.edu/ml/datasets/Iris), the program generate the following output:
Example:
```
IRIS FLOWER DECISION TREE

  IF petal_length <= 1.9:
    THEN Iris-setosa
  ELSE:
    IF petal_width <= 1.7:
      IF sepal_length <= 7.0:
        IF sepal_width <= 2.8:
          THEN Iris-versicolor
        ELSE:
          THEN Iris-versicolor
      ELSE:
        THEN Iris-virginica
    ELSE:
      THEN Iris-virginica
```

### Algorithm
The algorithm uses the information gain (IG) as the solely metric.
On each interaction, the algorithm tries to find the best attribute that maximized the information gain of the data sets. Therefore, it is a greedy algorithm.

Because the attributes' values are continues, i.e. the values can range from 0 until infinite, I've chosen to make binary partitions by classifying the classes that are less or equals than a given value or greater than the value.
The binary partitions are parents with exactly 2 children, the left when the attribute is lower or equals, and the right when the attribute is greater.

The algorithm finds the threshold, i.e the limit value used to classify an instance, by collecting metrics from the lowest value of an attribute until the maximum value, walking 0.1 by 0.1. The value 0.1 was carefully chosen based on the observation that the iris flower dataset has 2 decimals of precision, hence 0.1 is the minimum possible step value. Doing so may cause an explosion of tries before finding the best value, and could have been naive if the values range were too large, but they are not too large and the number of tries are computationally possible (it takes less than 1 second to compute everything on a Core i5). A more predictable approch would be to divide the value range in a linear space.

### Exercise
Implementem o algoritmo ID3:
https://en.wikipedia.org/wiki/ID3_algorithm

É muito similar ao explicado em aula.
Use o programa para criar uma árvore de decisão para o problema de classificação dos dados de Iris de Fisher.
http://en.wikipedia.org/wiki/Iris_flower_data_set
