from collections import deque
from typing import List


def count_islands_dfs(matrix: List[List[int]]) -> int:
    """Depth-First Search Approach"""

    def dfs(row, column):
        if not (0 <= row < len(matrix)) or not (0 <= column < len(matrix[0])) or matrix[row][column] == 0:
            return
        matrix[row][column] = 0
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        for dr, dc in directions:
            dfs(row + dr, column + dc)

    count = 0
    for row, row_values in enumerate(matrix):
        for column, value in enumerate(row_values):
            if value == 1:
                count += 1
                dfs(row, column)

    return count


def count_islands_bfs(matrix: List[List[int]]) -> int:
    """Breadth-First Search Approach"""

    def bfs(row, column):
        queue = deque([(row, column)])
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        while queue:
            r, c = queue.popleft()
            if not (0 <= r < len(matrix)) or not (0 <= c < len(matrix[0])) or matrix[r][c] == 0:
                continue
            matrix[r][c] = 0
            queue.extend((r + dr, c + dc) for dr, dc in directions)

    count = 0
    for row, row_values in enumerate(matrix):
        for column, value in enumerate(row_values):
            if value == 1:
                count += 1
                bfs(row, column)

    return count
