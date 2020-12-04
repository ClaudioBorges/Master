# Prim is a greedy algorithm that finds minimum spanning tree for weighted
# undirected graph.
import random
import time
import heapq
import copy

def assert_square_matrix(matrix):
    n = len(matrix)
    for row in matrix:
        assert n == len(row), 'Matrix is not square'


def make_square_matrix(n, def_val=None):
    return [[def_val for j in range(n)] for i in range(n)]


def fill_half_square_matrix_with_random_weights(matrix, weights):
    assert_square_matrix(matrix)
    n = len(matrix)
    for i in range(n):
        for j in range(i + 1, n, 1):
            matrix[i][j] = random.choice(weights)


def mirror_half_square_matrix(matrix):
    assert_square_matrix(matrix)
    n = len(matrix)
    for i in range(n):
        for j in range(i + 1, n, 1):
            matrix[j][i] = matrix[i][j]


def make_undirected_adjacency_matrix(n, weights):
    adj = make_square_matrix(n)
    fill_half_square_matrix_with_random_weights(adj, weights)
    mirror_half_square_matrix(adj)
    return adj


def make_directed_adjacency_matrix(n, weights):
    adj = make_square_matrix(n)
    fill_half_square_matrix_with_random_weights(adj, weights)
    mirror_half_square_matrix(adj)
    fill_half_square_matrix_with_random_weights(adj, weights)
    return adj


def make_adjacency_list_from_matrix(adj_m):
    n = len(adj_m)
    adj_l = []
    for i in xrange(n):
        edges = []
        for j in xrange(n):
            if i != j and adj_m[i][j] != None:
                edges.append((j, adj_m[i][j]))
        adj_l.append(edges)
    return adj_l


INF = 999

def mst_prim(adj_l, root):
    n = len(adj_l)

    parents = [None for i in range(n)]
    not_visited = set(range(n))

    h_weights = [(INF, i) for i in range(n)]
    heapq.heapify(h_weights)

    heapq.heappush(h_weights, (0, root))
    while not_visited:
        w_min, v_min = heapq.heappop(h_weights)
        if v_min not in not_visited:
            continue

        for v, w in adj_l[v_min]:
            if v in not_visited and w < w_min:
                heapq.heappush(h_weights, (w, v))
                parents[v] = v_min
        not_visited.discard(v_min)

    return parents


def dijkstra(adj_l, src):
    n = len(adj_l)

    parents = [None for i in range(n)]
    weights = [INF for i in range(n)]
    not_visited = set(range(n))

    weights = [INF for i in range(n)]
    h_weights = [(INF, i) for i in range(n)]
    heapq.heapify(h_weights)

    weights[src] = 0
    heapq.heappush(h_weights, (0, src))
    while not_visited:
        w_min, v_min = heapq.heappop(h_weights)
        if v_min not in not_visited:
            continue

        for v, w in adj_l[v_min]:
            if v in not_visited and w + w_min < weights[v]:
                heapq.heappush(h_weights, (w + w_min, v))
                weights[v] = w + w_min
                parents[v] = v_min
        not_visited.discard(v_min)

    return parents


def pretty_print_adjacency_matrix(adj_m):
    for row in adj_m:
        print(row)


    for i in xrange(len(adj_l)):
        print str(i) + ': ' + str(adj_l[i])


def profile(f, *args):
    samples = []
    for n in xrange(120):
        t1 = time.time()
        _ = f(*args)
        t2 = time.time()
        samples.append(t2 - t1)
    return sum(samples)/len(samples)


def make_adjacency_list(n_vertex, weights, density):
    adj_l = [[] for i in xrange(n_vertex)]
    for j in xrange(1, density + 1, 1):
        for i in xrange(n_vertex):
            v = (i + j) % n_vertex
            w = random.choice(weights)
            adj_l[i].append((v, w))
    return adj_l


def main():
    n_vertex = 1000
    #s_p = []
    #s_d = []
    #weights = [1, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    #for i in xrange(10):
    #    g1 = make_adjacency_list_from_matrix(
    #        make_undirected_adjacency_matrix(n_vertex, weights))
    #    g2 = make_adjacency_list_from_matrix(
    #        make_directed_adjacency_matrix(n_vertex, weights))
    #    start = random.randint(0, n_vertex - 1)
    #    t_p = profile(mst_prim, g1, start)
    #    t_d = profile(dijkstra, g2, start)

    #    s_p.append(t_p)
    #    s_d.append(t_d)
    #m1 = sum(s_p)/len(s_p)
    #m2 = sum(s_d)/len(s_d)

    #print str(m1) + ',' + str(m2)
    #return

    for d in xrange(0, n_vertex + 1, n_vertex / 5):
        s_p = []
        s_d = []
        density = (d - 1) if d else 1

        weights = range(1, n_vertex / 10, 1)

        graph = make_adjacency_list(n_vertex, weights, density)
        start = random.randint(0, n_vertex - 1)

        t_d = profile(dijkstra, graph, start)
        t_p = profile(mst_prim, graph, start)

        s_p.append(t_p)
        s_d.append(t_d)

        m1 = sum(s_p)/len(s_p)
        m2 = sum(s_d)/len(s_d)

        print str(density) + ',' + str(m1) + ',' + str(m2)


if __name__ == "__main__":
    main()
