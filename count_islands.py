def count_islands_dfs(matrix):
    """Depth-First Search Approach"""
    #     todo check the imput
    def dfs(row, column):
        if (
            row < 0
            or column < 0
            or row >= len(matrix)
            or column >= len(matrix[0])
            or matrix[row][column] == 0
        ):
            return
        matrix[row][column] = 0
        dfs(row - 1, column)
        dfs(row + 1, column)
        dfs(row, column - 1)
        dfs(row, column + 1)

    count = 0
    for row in range(len(matrix)):
        for column in range(len(matrix[0])):
            if matrix[row][column] == 1:
                count += 1
                dfs(row, column)

    return count
