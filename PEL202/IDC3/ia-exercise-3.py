# IDC3 implementation for the Iris flower data set implementation
# https://en.wikipedia.org/wiki/ID3_algorithm
#
# The iris flower data set was introduced by Ronald Fisher in his 1936 paper,
# as an example of linear discriminant analysis using multiple measurements
# in taxonomic problem.
# The data set can be retrieved at http://archive.ics.uci.edu/ml/datasets/Iris
# and contains 150 instances and 4 attributes: sepal length, sepal width,
# petal length and petal width all of them in centimeter. The last column
# is the class: Setosa, Vericolour, and Virginica. The class distribution is
# 33.3% for each of 3 classes.
#
# THE ALGORITHM:
# The algorithm uses the information gain as a metric.
# On each interaction, the algorithm tries to find the best attribute that
# maximized the information gain of the data sets. Therefore, it is a greedy
# algorithm.
# Because the attributes values are continues, i.e. the values can range from
# 0 until infinite, I've chosen to make binary partitions by classifying the
# classes are less or equals than a given value or greater than a given value.
# The binary partitions are parents with exactly 2 children, the left when
# the attribute is lower or equals, and the right when the attribute is greater.
# The algorithm finds the threshold, i.e the limit value for classifying an
# instance, by collecting metrics from the lowest value of an attribute until
# the maximum value 0.1 by 0.1. The value 0.1 was carefully chosen based on the
# observation that the iris flower dataset has 2 decimals of precision, hence
# 0.1 is the minimum possible step value. Doing so, cause an explosion of
# tries before finding the best value, and could have been naive if the values
# range were too large, but they are not too large and the number of tries
# are computationally possible (it takes less than 1 second to compute
# everything on a Core i5). A more predictable approch  would be to divide the
# value range in a linear space

import csv
from collections import defaultdict
from math import log
from math import floor


def read_dataset(path, delimiter=','):
    # type: (str, str) -> list(list(str))
    # The dataset should not contain any header
    with open(path) as csv_file:
        content = csv.reader(csv_file, delimiter=delimiter)
        examples = [example for example in content if len(example)]
        return examples


def get_entropy(n_instances_per_class, n_instances):
    # type: (list(int), int) -> float
    e = 0
    for instance in n_instances_per_class:
        p = float(instance) / n_instances
        e += - p * log(p, 2) if p else 0
    return e


def get_examples_per_class(examples):
    # Giving list of examples, return a dictionary where the key is the class
    # and the value is the frequency
    examples_per_class = defaultdict(int)
    for example in examples:
        # The last element of as example is its class (or target)
        example_class = example[-1]
        examples_per_class[example_class] += 1
    return examples_per_class


def get_examples_entropy(partition):
    # Giving a partition, i.e a list of examples, return the entropy.
    examples_per_class = get_examples_per_class(partition)
    n_examples = len(partition)
    return get_entropy(examples_per_class.values(), n_examples)


def get_information_gain(partitions):
    # Giving a set of partitions, return the information gain by having then
    # partitioned instead of one single bunch.
    normalized_entropies = []
    total_n_examples = sum([len(examples) for examples in partitions])
    for partition in partitions:
        n_examples = len(partition)
        entropy = get_examples_entropy(partition)
        normalized_entropies.append(
            float(n_examples) / total_n_examples * entropy)
    # Calculate the entropy if the partitions were a single one
    examples = [example
                for partition in partitions
                for example in partition]
    current_entropy = get_examples_entropy(examples)  # type: float
    # The information Gain is how much the entropy has decreased from the
    # current entropy
    return current_entropy - sum(normalized_entropies)


def partition_by_attribute(examples, attribute_idx, threshold):
    # type: (list(str), int, float) -> list(str)
    # There are 2 types of partition,  when the value of the attribute_idx is
    # less or equals than threshold, and when the value is greater to threshold.
    # The reason is because the attributes are continuous, i.e. they can
    # represent any value in the spectrum of real number greater than 0.
    partitions = {'left': [], 'right': []}
    for example in examples:
        value = example[attribute_idx]
        partition_name = 'left' if value <= threshold else 'right'
        partitions[partition_name].append(example)
    return partitions


def choose_best_attribute(examples,
                          remaining_attributes_idx,
                          threshold_step=0.1):
    # Choose the best attribute and threshold to partition the examples
    max_ig = -1
    chosen = None
    # Find the attribute that has a higher information gain
    for attr_idx in remaining_attributes_idx:
        min_val = min([example[attr_idx] for example in examples])
        max_val = max([example[attr_idx] for example in examples])
        range_val = max_val - min_val
        n_steps = int(floor(range_val / threshold_step) + 1)
        threasholds = [min_val + i * threshold_step
                       for i in xrange(0, n_steps + 1)]
        # Find the threshold for a giving attribute that has a higher
        # information gain
        for threshold in threasholds:
            partitions = partition_by_attribute(examples, attr_idx, threshold)
            partitions_list = [partitions['left'], partitions['right'], ]
            ig = get_information_gain(partitions_list)
            if ig > max_ig:
                max_ig = ig
                chosen = {
                    'partitions': partitions,
                    'attr_idx': attr_idx,
                    'threshold': threshold
                }
    return chosen


def get_classes(examples):
    # Giving a list of examples, return a list of unique classes
    examples_per_class = get_examples_per_class(examples)
    return [c for c in examples_per_class]


def get_most_frequent_class(examples):
    # Givin a list of examples, return the most frequent class
    examples_per_class = get_examples_per_class(examples)
    max_val = -1
    most_frequent_class = None
    for c in examples_per_class:
        if examples_per_class[c] > max_val:
            max_val = examples_per_class[c]
            most_frequent_class = c
    return most_frequent_class


def id3(examples, remaining_attributes_idx):
    # Execute the ID3 algorithm
    classes = get_classes(examples)
    node = {}

    if len(classes) == 1:
        node['class'] = classes[0]
        return node

    if len(remaining_attributes_idx) == 0:
        node['class'] = get_most_frequent_class(examples)
        return node

    chosen = choose_best_attribute(examples, remaining_attributes_idx)
    partitions = chosen['partitions']
    left = partitions['left']
    right = partitions['right']

    if len(left) == 0 or len(right) == 0:
        # If it was unable to partition the data, that means we have reached
        # a leaf
        node['class'] = get_most_frequent_class(examples)
        return node

    # Remove the attribute from the set of available attributes
    remaining_attributes_idx.discard(chosen['attr_idx'])

    # Create a node that is not a leaf
    node['attr_idx'] = chosen['attr_idx']
    node['threshold'] = chosen['threshold']
    node['left'] = id3(left, remaining_attributes_idx)
    node['right'] = id3(right, remaining_attributes_idx)
    return node


def get_iris_flower_dataset():
    # Prepare the iris flower dataset
    # Read it from the iris.data file and convert the numeric fields into float.
    rows = read_dataset('iris.data')
    examples = []
    for row in rows:
        example = []
        for elm in row:
            # Convert to float what can be converted
            try:
                example.append(float(elm))
            except ValueError:
                example.append(elm)
        examples.append(example)
    return examples


def print_decision_tree(node, level=0):
    # Print the decision tree a sequence of IF, THEN, ELSE
    attribute_idx_to_name = {
        0: 'sepal_length',
        1: 'sepal_width',
        2: 'petal_length',
        3: 'petal_width',
    }
    ident = '  '

    if 'class' in node:
        # This is a leaf
        msg = 'THEN ' + node['class']
    else:
        attribute = attribute_idx_to_name[node['attr_idx']]
        threshold = str(node['threshold'])
        msg = 'IF ' + attribute + ' <= ' + threshold + ':'

    print (ident * level + msg)

    if 'class' not in node:
        print_decision_tree(node['left'], level + 1)
        print (ident * level + 'ELSE:')
        print_decision_tree(node['right'], level + 1)


def main():
    iris_flower_dataset = get_iris_flower_dataset()
    # The valid attributes are coluns 0, 1, 2 and 3.
    attributes_idx = set([0, 1, 2, 3, ])
    root = id3(iris_flower_dataset, attributes_idx)

    print ('IRIS FLOWER DECISION TREE')
    print_decision_tree(root, level=1)


if __name__ == "__main__":
    main()
