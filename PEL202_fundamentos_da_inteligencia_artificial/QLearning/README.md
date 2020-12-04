The following program was developed for academic purpose, intended to be considered as the seventh task for the subject PEL202 "Fundamentos da Inteligência Artificial".

### Environemnt
I tested it using Python 3.7.7.

### How to execute
There are no external library
In bash:
```bash
python3 qlearning.py
```
### Introduction
The program uses Q-Learning to learn from rewards. Therefore a reward for each action in each state is needed. It keep building up the action-value table until it converges. Because it is a very small problems, the number of episodes to converge is small (although the program uses a very rudimentary method of convergency detection)

### Representation
It is a grid of 3x2 as of:

| 1 | 2 | 3 |
|---|---|---|
| 4 | 5 | 6 |

Actions:
A = <right, left, up, down>

States:
S = <1, 2, 3, 4, 5, 6>

Transitions:
* T(1, right) = 2; T(1, down) = 4
* T(2, right) = 3; T(2, left) = 1; T(2, down) = 5
* T(3, *) = 3
* T(4, right) = 5; T(4, up) = 1
* T(5, right) = 6; T(5, left) = 4; T(5, up) = 2
* T(6, left) = 5; T(6, up) = 3

Rewards:
* R(1, right) = 0; R(1, down) = 0
* R(2, right) = 100; R(2, left) = 0; R(2, down) = 0
* R(3, *) = 0
* R(4, right) = 0; R(4, up) = 0
* R(5, right) = 0; R(5, left) = 0; R(5, up) = 0
* R(6, left) = 0; R(6, up) = 100



### Results
The program produces the following output:
```
Optimal policy PI:  [2, 3, 0, 1, 2, 3]
V:  [90.0, 100.0, 0, 81.0, 90.0, 100.0]
Number of episodes:  1265
```
which is the optimal action policy and state-value

The Optimal policy PI is an array of length 6. Each position contains the next optimal position. The 0 represents that  there is no next position.

### Exercise
- Implemente o Q-learning para resolver o problema do mundo de grades.
- 3 x 2
- Taxa de aprendizado = 0,1; Gama = 0,9.
- Calcule a política ótima e o V para este problema.

Note: image not available

