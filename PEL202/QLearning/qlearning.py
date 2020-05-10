# Problem:
# |-----------|
# | 1 | 2 | 3 |
# |-----------|
# | 4 | 5 | 6 |
# |---|---|---|
# Actions:
# A = <right, left, up, down>
#
# States:
# S = <1, 2, 3, 4, 5, 6>
#
# Transitions:
# T(1, right) = 2; T(1, down) = 4
# T(2, right) = 3; T(2, left) = 1; T(2, down) = 5
# T(3, *) = 3
# T(4, right) = 5; T(4, up) = 1
# T(5, right) = 6; T(5, left) = 4; T(5, up) = 2
# T(6, left) = 5; T(6, up) = 3
#
# Rewards:
# R(1, right) = 0; R(1, down) = 0
# R(2, right) = 100; R(2, left) = 0; R(2, down) = 0
# R(3, *) = 0
# R(4, right) = 0; R(4, up) = 0
# R(5, right) = 0; R(5, left) = 0; R(5, up) = 0
# R(6, left) = 0; R(6, up) = 100

import copy
import random

# Number of states (i.e 6 grids)
STATES = 6
# Invalid representation
INV = -1
# Use INV in the Reward table to inform which transition is not possible
# The possible transitions have valid rewards (as described in the problem)
R = [
    #   1,    2,    3,    4,    5,    6
    [INV, 000, INV, 000, INV, INV],  # 1
    [000, INV, 100, INV, 000, INV],  # 2
    [INV, INV, 000, INV, INV, INV],  # 3
    [000, INV, INV, INV, 000, INV],  # 4
    [INV, 000, INV, 000, INV, 000],  # 5
    [INV, INV, 100, INV, 000, INV],  # 6
]

alpha = 0.9  # learning rate
gamma = 0.9  # gamma


def qlearning(Q, s):
    # Pick a random action
    s_t1 = s
    while R[s][s_t1] is INV:
        s_t1 = random.randrange(STATES)
    # Compute the new Action-Value
    Q[s][s_t1] = (1 - alpha) * Q[s][s_t1] + \
                 alpha * (R[s][s_t1] + gamma * max(Q[s_t1]))
    return s_t1


def main():
    # Action-Value
    Q = [[0 for i in range(STATES)] for k in range(STATES)]
    # State-Value
    V = [0] * STATES
    # Action-Policy
    PI = [0] * STATES

    # Count up the number of episodes needed to find the converged action-value
    # table
    episodes = 0
    # Number of equals episode; if this number is much higher than the dimension
    # of the action-value table, it is considered converged
    n_convergence = 0
    s = random.randrange(STATES)
    while True:
        episodes += 1
        Q_ = copy.deepcopy(Q)
        s_t1 = qlearning(Q, s)
        if Q == Q_:
            n_convergence += 1
            if n_convergence == 1000:
                # Rudimentary convergence detection; if it does not
                # changes for 100 episodes, then consider it converged
                break
        # Avoid infinite loops, i.e. keep working on the sequence as long as
        # the new value is not the same as the old one
        s = s_t1 if s != s_t1 else random.randrange(STATES)

    # Build V and Pi (optimal) using Q
    for i in range(STATES):
        for j in range(STATES):
            if V[i] < Q[i][j]:
                V[i] = Q[i][j]
                PI[i] = j + 1

    print('Optimal policy PI: ', str(PI))
    print('V: ', str(V))
    print('Number of episodes: ', str(episodes))


if __name__ == '__main__':
    main()
