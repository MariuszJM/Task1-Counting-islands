import pytest
import random
import timeit
import tracemalloc
from count_islands import count_islands_bfs, count_islands_dfs


def generate_random_matrix(rows, cols):
    random.seed(42)
    return [[random.choice([0, 1]) for _ in range(cols)] for _ in range(rows)]


test_data = [
    ("small", generate_random_matrix(3, 3)),
    ("medium", generate_random_matrix(40, 40)),
    ("large", generate_random_matrix(1000, 1000)),
]


@pytest.mark.parametrize("algo_name, algo_func", [("BFS", count_islands_bfs), ("DFS", count_islands_dfs)])
@pytest.mark.parametrize("size, matrix", test_data)
def test_time_execution(algo_name, algo_func, size, matrix, num_runs=1000):
    start_time = timeit.default_timer()
    for _ in range(num_runs):
        algo_func(matrix)
    elapsed_time = timeit.default_timer() - start_time
    avg_time = elapsed_time / num_runs
    print(f"{algo_name} {size} test case ({num_runs} runs): {avg_time:.6f} seconds per run")


def measure_memory(func, matrix):
    tracemalloc.start()
    func(matrix)
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    return peak / 1024


@pytest.mark.parametrize("algo_name, algo_func", [("BFS", count_islands_bfs), ("DFS", count_islands_dfs)])
@pytest.mark.parametrize("size, matrix", test_data)
def test_memory_consumption(algo_name, algo_func, size, matrix):
    memory = measure_memory(algo_func, matrix)
    print(f"Memory usage {algo_name} {size} test case: {memory:.6f} KB")
