# 🧩 LeetCode 73 — Set Matrix Zeroes
🔗 [題目連結](https://leetcode.com/problems/set-matrix-zeroes/)

---

## 📄 題目說明 | Problem Description

### 中文：

給定一個 𝑚 × 𝑛 的整數矩陣 matrix，如果某個元素為 0，則把該元素所在的整行與整列都設為 0。要在原地（in‑place）修改，不可以用額外的整個矩陣空間。

### English:
Given an 𝑚 × 𝑛 integer matrix matrix, if an element is 0, set its entire row and column to 0’s. Do this in-place, without allocating another matrix.

### Examples
- Example 1:

    ![](../images/73_mat1.jpg)

    Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
    
    Output: [[1,0,1],[0,0,0],[1,0,1]]

- Example 2:

    ![](../images/73_mat2.jpg)

    Input: matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
    
    Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]

---

## 🧠 解題思路 | Solution Idea

- 簡單版本是先標記哪些 row / col 要變 0，然後再做一次遍歷設置 0。但那會用額外 𝑂(𝑚 + 𝑛) 空間。
- 為了進一步優化到 常數空間 𝑂(1)，我們可以「借用」矩陣的第一行與第一列作為記號（marker）：

    1. 先單獨判斷原本第一行與第一列是否含 0（用兩個旗標記錄），因為之後會被用作記號不能破壞原始資訊。

    2. 對剩餘的 cell，如果 matrix[i][j] == 0，就把 matrix[i][0] 和 matrix[0][j] 設為 0，表示第 i 行與第 j 列要清零。

    3. 再遍歷除第一行與第一列之外的區域：如果 matrix[i][0] == 0 或 matrix[0][j] == 0，就把 matrix[i][j] = 0。

    4. 最後根據最初記錄的旗標，決定是否要把第一行或第一列整行／整列設為 0。

---

## 💻 程式碼實作 | Code (Python)
```python
from typing import List

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        m = len(matrix)
        n = len(matrix[0])

        # 判斷第一列與第一行是否需要清零
        first_row_zero = any(matrix[0][j] == 0 for j in range(n))
        first_col_zero = any(matrix[i][0] == 0 for i in range(m))

        # 用第一行與第一列做為標記
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0

        # 根據標記把中間區域清零
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

        # 處理第一列（如果原本有零）
        if first_row_zero:
            for j in range(n):
                matrix[0][j] = 0

        # 處理第一欄（如果原本有零）
        if first_col_zero:
            for i in range(m):
                matrix[i][0] = 0
```

| 區段             | 程式碼                                                                                 | 功能 / 解釋                             |
| -------------- | ----------------------------------------------------------------------------------- | ----------------------------------- |
| 判斷第一行、第一列是否需清零 | `first_row_zero = any(...)` / `first_col_zero = any(...)`                           | 因為第一行與第一列要被用作記號，如果原本本身應該被清零，我們要先記下來 |
| 標記階段           | 雙重迴圈從 `i=1, j=1` 開始：若 `matrix[i][j] == 0`，設 `matrix[i][0] = 0` 且 `matrix[0][j] = 0` | 用第一行／列儲存該行或列是否要清零                   |
| 清零中間區域         | 再雙重迴圈遍歷（跳過第一行與第一列）：若 `matrix[i][0] == 0 或 matrix[0][j] == 0` → 設 `matrix[i][j] = 0` | 根據標記把應該為 0 的地方設為 0                  |
| 清零第一行          | `if first_row_zero: for j in ... matrix[0][j] = 0`                                  | 如果原先第一行就應該清零，整列清零                   |
| 清零第一列          | `if first_col_zero: for i in ... matrix[i][0] = 0`                                  | 如果原先第一列就應該清零，整列清零                   |

- any() 是 Python 的一個內建函數，用來判斷：一個可迭代物裡面，只要有一個元素是 True，就回傳 True；否則回傳 False。
- all() 是 Python 的一個內建函數，用來判斷：全部滿足才 True

### 🎯 為什麼 Set Zeroes 這題需要 any()？

- 因為它用 matrix 第一列與第一欄 來存標記：
    ```python
    matrix[i][0] = 0  → 第 i 列應該全變 0
    matrix[0][j] = 0  → 第 j 欄應該全變 0
    ```
    - 但這會造成問題：

        - 如果第一列或第一欄本來就有 0 怎麼辦？
        - 你會不小心把第一列/第一欄重複清成 0

    - 所以我們提前用 any() 記錄：

        - 第一列原本有沒有 0

        - 第一欄原本有沒有 0

    - 最後再補上正確處理。

- 為什麼不能一開始看到 0 就直接把那一列、那一欄全部清成 0？為什麼一定要先記錄，再後面一起處理？
    - 因為 直接清零會破壞原始資訊，造成多清、不該清的地方、邏輯整個錯掉

---

## 🧪 範例流程 | Example Walkthrough

假設矩陣：
|       | 0 | 1 | 2 |
| ----- | - | - | - |
| **0** | 1 | 1 | 1 |
| **1** | 1 | 0 | 1 |
| **2** | 1 | 1 | 1 |

### 第 1 步：檢查是否需要清第一行或第一列

- 這裡第一行沒 0，第一列也沒 0 → first_row_zero = False、first_col_zero = False

### 第 2 步：從 (1,1) 開始標記

- 走過除了第一行與第一列以外的格子：

    - 在 (1,1) 發現 0 → 就標記 matrix[1][0] = 0（表示整行要清零），以及 matrix[0][1] = 0（表示整列要清零）

- 標記後矩陣變成：

|       | 0     | 1     | 2 |
| ----- | ----- | ----- | - |
| **0** | 1     | **0** | 1 |
| **1** | **0** | 0     | 1 |
| **2** | 1     | 1     | 1 |

（粗體表示已被用作標記）

### 第 3 步：跳過第一行和第一列，在中間區域清零

- 從 i = 1, j = 1 開始往右下：

    - 看格子 (1,1)：matrix[1][0] == 0 或 matrix[0][1] == 0 → 成真 → 設 matrix[1][1] = 0（它已經是 0）

    - (1,2)：matrix[1][0] == 0 為真 → matrix[1][2] = 0

    - (2,1)：matrix[0][1] == 0 為真 → matrix[2][1] = 0

    - (2,2)：matrix[2][0] != 0 且 matrix[0][2] != 0 → 不清零，保留原值

- 這樣清零後的中間區域變成：

|       | 0 | 1 | 2 |
| ----- | - | - | - |
| **0** | 1 | 0 | 1 |
| **1** | 0 | 0 | 0 |
| **2** | 1 | 0 | 1 |

### 第 4 步：處理第一行與第一列（若需要）

- 因為 first_row_zero = False 和 first_col_zero = False，所以我們不清第一行也不清第一列。在這例子中，第一列與第一行保留原標記 / 原值。

- 最終結果：

```lua
[[1, 0, 1],
 [0, 0, 0],
 [1, 0, 1]]
```

### ✅ 關鍵澄清

- 「清零階段跳過第一行/第一列」不是表示刪掉或縮小矩陣，而是 先不要動 這些格子，因為它們被用來存標記。

- 我們只在中間區域（從 row = 1, col = 1 開始的區塊）依據標記清零。

- 最後再依據 first_row_zero / first_col_zero 的旗標決定是否把最外層的第一行或第一列整行 / 整列設為 0。

---

## ⏱ 複雜度分析 | Complexity

- 時間複雜度：𝑂(𝑚 × 𝑛)，整個矩陣要遍歷幾次也是線性的。

- 空間複雜度：𝑂(1)（常數空間） — 我們只用了幾個額外變數，不依賴額外的矩陣或陣列。

---

## ✍️ 我學到的事情（What I Learned）

1. 空間最佳化技巧 : 利用矩陣第一行與第一列作為「旗標區」記錄要清零的行與列，節省額外空間。

2. 分階段處理的邏輯 : 先標記、再清零 → 要分清「不能馬上清零」，否則會影響其他格子的判斷。

3. 特例處理的重要性 : 第一行與第一列若有 0，需要額外記錄，不能直接當成其他標記用的行列處理。

4. 遍歷順序的控制 : 中間矩陣（跳過第一行和第一列）要先清，再處理最外圈，否則會提早破壞標記。