from copy import deepcopy
from random import randint
import time

def partition(A, p, r):
    med = p
    pivot = A[r]
    for j in xrange(p, r):
        if A[j] < pivot:
            A[med], A[j] = A[j], A[med]
            med = med + 1
    A[med], A[r] = A[r], A[med]
    return med

def random_partition(A, p, r):
    k = randint(p, r)
    A[k], A[r] = A[r], A[k]
    return partition(A, p, r)

def regular_partition(A, p, r):
    k = randint(p, r)
    A[k], A[r] = A[k], A[r]
    return partition(A, p, r)

def _quicksort(A, p, r, fpartition):
    if p < r:
        med = fpartition(A, p, r)
        _quicksort(A, p, med - 1, fpartition)
        _quicksort(A, med + 1, r, fpartition)
    return A


def quicksort(A):
    return _quicksort(A, 0, len(A) - 1, fpartition=partition)

def quicksort_random_partition(A):
    return _quicksort(A, 0, len(A) - 1, fpartition=random_partition)

def bubblesort(A):
    for i in xrange(len(A) - 1, 0, -1):
        for j in xrange(i - 1, -1, -1):
            if (A[j] > A[i]):
                A[i], A[j] = A[j], A[i]
    return A


def assert_ordered(array):
    for i in xrange(len(array) - 1):
        assert array[i] <= array[i+1]


def rand_list(size):
    return [randint(0, size*size) for i in range(size)]

def sort(A, sorting_function):
    A_copy = deepcopy(A)
    t1 = time.time()
    A_sort = sorting_function(A_copy)
    t2 = time.time()
    return t2 - t1

import os
import sys
def main():
    os.nice(0)
    sys.setrecursionlimit(30000)
    for k in range(150):
        A = rand_list(2**(k/10))
        list.sort(A, reverse=True)
        t_bubble = sort(A, bubblesort)
        t_quick = sort(A, quicksort)
        t_rquick = sort(A, quicksort_random_partition)

        print str(len(A)) + "," + str(t_bubble) + "," + str(t_quick) + "," + str(t_rquick)
        #print "n=" + str(len(A)) + ", t_bubble=" + str(t_bubble) + ", t_quick=" + str(t_quick) + ", t_rquick=" + str(t_rquick)

if __name__ == "__main__":
    main()
