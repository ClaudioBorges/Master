from __future__ import print_function
from collections import deque
import random


class ImmutableJar:
    """ Jar contains units limited to the capacity and can carry liquids.
    """

    def __init__(self, capacity, units=0):
        """ Jar contains liquid units limited to a capacity.
        :param capacity: Maximum capacity in units (inclusive).
        :param units: Initial units this Jar is carrying.
        """
        self.capacity = capacity
        self.units = units

    def fill(self):
        # type: () -> ImmutableJar
        """ Return a new instance of Jar with the same capacity but full.
        :return: A new Jar instance.
        """
        return ImmutableJar(capacity=self.capacity, units=self.capacity)

    def empty(self):
        # type: () -> ImmutableJar
        """ Return a new instance of Jar with the same capacity but empty.
        :return: A new Jar instance.
        """
        return ImmutableJar(capacity=self.capacity, units=0)

    def transfer_to(self, other):
        # type: (ImmutableJar) -> tuple
        """ Transfer the units from Jar A to B, respecting the Jar capacity.
        :param other: The other Jar.
        :return: A tuple of 2 new instances Jar.
        """
        if isinstance(other, ImmutableJar):
            other_potential = other.capacity - other.units
            transfer = min(other_potential, self.units)
            return (ImmutableJar(capacity=self.capacity,
                                 units=(self.units - transfer)),
                    ImmutableJar(capacity=other.capacity,
                                 units=(other.units + transfer)),)
        return NotImplemented

    def transfer_from(self, other):
        # type: (ImmutableJar) -> tuple
        """ Transfer the units from Jar B to A, respecting the Jar capacity.
        :param other: The other Jar.
        :return: A tuple of 2 new instances Jar.
        """
        (jar2, jar1,) = self.transfer_to(other)
        return jar1, jar2,

    def __str__(self):
        return str(self.units)

    def __eq__(self, other):
        if isinstance(other, ImmutableJar):
            return (self.units == other.units
                    and self.capacity == other.capacity)
        return NotImplemented

    def __hash__(self):
        return hash((self.capacity, self.units,))


class Node:
    """" Represent a Tree node.
    The node is composed of 2 Jars and can have n children.
    """

    def __init__(self, jar1, jar2):
        self.jar1 = jar1
        self.jar2 = jar2

    def get_all_children(self, shuffle=False):
        # type: () -> list(Node)
        """ Return a collection of valid nodes that are children of this Node.
        A valid Jar Node is any node that is different than the parent and
        some action was done under it. For example: a full Jar can't filled
        with more units, or an empty Jar can't be emptied again.
        :return: A list of children Nodes.
        """
        states = [
            Node(self.jar1.fill(), self.jar2),
            Node(self.jar1.empty(), self.jar2),
            Node(*self.jar1.transfer_to(self.jar2)),
            Node(self.jar1, self.jar2.fill()),
            Node(self.jar1, self.jar2.empty()),
            Node(*self.jar2.transfer_from(self.jar1)),
        ]

        if shuffle:
            random.shuffle(states)

        # Seen is used to remove duplications while keeping the list ordering.
        seen = set()
        # Add the self so that we guarantee there is no child equals to the
        # parent.
        seen.add(self)
        return [x for x in states if not (x in seen or seen.add(x))]

    def contains(self, jar):
        # type: (ImmutableJar) -> Boolean
        """ Does this node contains a Jar?
        :param jar: Jar to be verified.
        :return: True if node contains the Jar, otherwise False.
        """
        return self.jar1 == jar or self.jar2 == jar

    def __str__(self):
        return "(" + str(self.jar1) + ", " + str(self.jar2) + ")"

    def __eq__(self, other):
        if isinstance(other, Node):
            return (self.jar1 == other.jar1
                    and self.jar2 == other.jar2)
        return NotImplemented

    def __hash__(self):
        return hash((self.jar1, self.jar2,))


def find_solution_bfs(root, expected_jar):
    """ Find the path traveled until it gets to the expected_jar.
    It uses the BFS (breadth first search) to travel along the Nodes.

    Starting from the root, a collection of children is retrieved and inserted
    into a FIFO (First-in First-Out); the next element from the FIFO is
    popped and the cycle continues until the expected_jar is found.

    :param root: Root node
    :param expected_jar: The expected Jar
    :return: The list of Nodes traveled until find the expected_jar.
    """
    solution = []

    dq = deque()
    # Add root to the collection, hence there is no need for any special
    # handling.
    dq.append(root)
    while dq:
        node = dq.popleft()
        # Whenever we visit a node, add it to the solution 'cause it's been
        # visited.
        solution.append(node)
        if node.contains(expected_jar):
            break
        children = node.get_all_children()
        for child in children:
            dq.append(child)
    return solution


def find_solution_dfs(root, expected_jar):
    """ Find the path traveled until it gets to the expected_jar.
    It uses the DFS (deep first search) to travel along the Nodes.

    Starting from the root, a collection of children is retrieved and inserted
    into a FILO (First-in Last-Out); the next element from the FILO is
    popped and the cycle continues until the expected_jar is found. An
    additional, measure is necessary; if a node has already been visited, we
    just ignore it; hence there is no cycle.

    :param root: Root node
    :param expected_jar: The expected Jar
    :return: The list of Nodes traveled until find the expected_jar.
    """
    solution = []
    dq = deque()
    # Add root to the collection, hence there is no need for any special
    # handling.
    dq.append(root)
    # Instead of using the solution collection to determine if it's already
    # visited a node, use the visited collection, which is a set and have
    # O(1) access time, while solution has O(n) but keep order of insertion.
    visited = set()
    while dq:
        node = dq.pop()
        if node in visited:
            # If we have already seen this node, we just ignore it
            continue
        visited.add(node)
        solution.append(node)
        if node.contains(expected_jar):
            break
        children = node.get_all_children()
        for child in children:
            dq.append(child)
    return solution


def print_path(preamble, path):
    print(preamble)
    print("Path (len=" + str(len(path)) + "): " + ", ".join(map(str, path)))


def main():
    # The root Node contains 2 jars, one of capacity 3 an another one of
    # capacity 4.
    root = Node(ImmutableJar(capacity=3), ImmutableJar(capacity=4))

    # The expected jar is the one with capacity 4 and with 2 units
    expected_jar = ImmutableJar(capacity=4, units=2)

    # Find solution using both BFS and DFS
    print_path("BFS", find_solution_bfs(root, expected_jar))
    print_path("DFS", find_solution_dfs(root, expected_jar))


if __name__ == "__main__":
    main()