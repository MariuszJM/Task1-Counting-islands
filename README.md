# Problem Statement

The task is to count the number of islands in a given matrix (MxN) that represents a map. The matrix contains 1s (islands) and 0s (ocean).

# Code Implementation

The provided code includes implementations for Depth-First Search (DFS) and Breadth-First Search (BFS).

Initially, a DFS implementation was created. To eliminate recursion, a BFS implementation was subsequently developed. The performance of both algorithms was compared out of curiosity. Although the problem statement does not explicitly state that the input matrix must remain unchanged, both algorithms transform the input matrix. If it were crucial to preserve the input matrix, a copy could be used instead.

# Performance Comparison

The experiments were conducted on a machine equipped with an Intel© Core™ i7-8550U CPU @ 1.80GHz × 4 processor and 15.5 GiB of memory, utilizing the CPU for computations.
The following performance comparison is based on test results:

| Test Case      | BFS Memory Usage (KB) | DFS Memory Usage (KB) | BFS Execution Time (100 runs) | DFS Execution Time (100 runs) |
|----------------|-----------------------|-----------------------|-------------------------------|-------------------------------|
| Small (3x3)    | 1.382812              | 0.351562              | 0.000002 sec/run              | 0.000002 sec/run              |
| Medium (10x10) | 0.437500              | 0.351562              | 0.000102 sec/run              | 0.000091 sec/run              |
| Large (100x100)| 6.980469              | 0.460938              | 0.059833 sec/run              | 0.052761 sec/run              |

The table shows that BFS consumes more memory than DFS. However, the execution times are similar for small and medium cases, with BFS performing slightly slower for the large test case.

# Conclusion

Both algorithms transform the input matrix, even though the problem statement does not explicitly require preserving it. If it were crucial to maintain the input matrix, a copy could be used instead. Based on the test results and the task requirements, the DFS implementation is chosen as the simpler solution and the final answer to the task.
