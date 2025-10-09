def setZeroes(self, matrix: List[List[int]]) -> None:
    m = len(matrix)
    n = len(matrix[0])

    first_row_zero = any(matrix[0][j] == 0 for j in range(n))
    first_col_zero = any(matrix[i][0] == 0 for i in range(m))

    # 用第一行 / 第一列做標記
    for i in range(1, m):
        for j in range(1, n):
            if matrix[i][j] == 0:
                matrix[i][0] = 0
                matrix[0][j] = 0

    # 根據標記清零（跳過第一行/列先）
    for i in range(1, m):
        for j in range(1, n):
            if matrix[i][0] == 0 or matrix[0][j] == 0:
                matrix[i][j] = 0

    # 處理第一行
    if first_row_zero:
        for j in range(n):
            matrix[0][j] = 0

    # 處理第一列
    if first_col_zero:
        for i in range(m):
            matrix[i][0] = 0
