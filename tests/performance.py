import timeit
from count_islands import count_islands_bfs, count_islands_dfs


def test_case_small(count_islands_func):
    matrix = [
        [0, 1, 0],
        [0, 0, 0],
        [0, 1, 1],
    ]
    return count_islands_func(matrix)

def test_case_medium(count_islands_func):
    matrix = [
        [0, 1, 0, 0, 0, 1],
        [0, 0, 0, 1, 1, 0],
        [0, 1, 1, 0, 1, 0],
        [0, 0, 0, 0, 0, 1],
        [1, 1, 0, 1, 1, 0],
        [0, 0, 0, 0, 0, 0],
    ]
    return count_islands_func(matrix)

def test_case_large(count_islands_func):
    matrix = [
        [0, 1, 0, 0, 0, 1, 0, 0, 1, 1],
        [0, 0, 0, 1, 1, 0, 0, 1, 1, 0],
        [0, 1, 1, 0, 1, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 1, 0, 1, 0, 1],
        [1, 1, 0, 1, 1, 0, 0, 0, 1, 0],
        [0, 0, 0, 0, 0, 0, 1, 1, 1, 0],
        [1, 0, 1, 0, 0, 0, 0, 1, 0, 1],
        [0, 1, 0, 1, 1, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 1, 1, 0, 1, 1],
        [1, 1, 1, 1, 0, 0, 0, 1, 0, 0],
    ]
    return count_islands_func(matrix)

algorithms = [("BFS", count_islands_bfs), ("DFS", count_islands_dfs)]

for algo_name, algo_func in algorithms:
    print(f"{algo_name} small test case:", timeit.timeit(lambda: test_case_small(algo_func), number=1000))
    print(f"{algo_name} medium test case:", timeit.timeit(lambda: test_case_medium(algo_func), number=1000))
    print(f"{algo_name} large test case:", timeit.timeit(lambda: test_case_large(algo_func), number=1000))
