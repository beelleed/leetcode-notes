# 🔄 LeetCode 48 — Rotate Image / 旋轉圖像
🔗 [題目連結](https://leetcode.com/problems/rotate-image/)

---

## 📄 題目說明 | Problem Description

### 中文  
給你一個 n × n 的二維矩陣 `matrix`，代表一張圖像。請你**原地**將這張圖像順時針旋轉 90 度。注意：不能額外開新矩陣，你必須在原本的 `matrix` 上修改。

### English 
You are given an n × n 2D matrix representing an image. Rotate the image by 90 degrees **clockwise**, doing so **in-place**—you must modify the input matrix directly without allocating another matrix.

### Examples
- Example 1:

    ![](../images/048_mat1.jpg)
    - Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
    - Output: [[7,4,1],[8,5,2],[9,6,3]]

- Example 2:

    ![](../images/048_mat2.jpg)

    - Input: matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
    - Output: [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]

---

## 🧠 解法思路 | Solution Idea

兩種常見方法：

1. **在輔助矩陣上做映射再覆寫**（簡單但用額外空間）  
   - 每個元素 `(i, j)` 在旋轉後的新座標是 `(j, n - 1 - i)`  
   - 建一個新的矩陣把所有映射好，再複製回原矩陣  

2. **原地法：先轉置，再反轉每一行**  
   - 先做矩陣的 **轉置**（Transpose），即 `matrix[i][j]` ↔ `matrix[j][i]`  
   - 再 **反轉每一行**，使每一行的元素左右對調  
   - 這樣兩步合起來就等同於順時針旋轉 90 度。  

---

## 💻 程式碼（Python，原地法）

```python
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        # Step 1: 轉置（沿主對角線交換）
        for i in range(n):
            for j in range(i+1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        # Step 2: 反轉每一行（左右對調）
        for i in range(n):
            matrix[i].reverse()
```

### 🔍 程式碼詳解（分段）

- n = len(matrix)：取得矩陣邊長

- 轉置階段
    ```python
    for i in range(n):
        for j in range(i+1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    ```

    - 只做 j > i 的交換，避免重複交換

    - 把上三角的元素與下三角對調

    - 為什麼轉置矩陣時，是 for j in range(i + 1, n) 而不是 range(n)?
        - 原因：避免重複交換 ＋ 避免自己跟自己交換
            ```ini
            i=0 → j=0 → swap (0,0) <-> (0,0)     ❌ 自己換自己（沒意義）
            i=0 → j=1 → swap (0,1) <-> (1,0)     ✔ 正確
            i=0 → j=2 → swap (0,2) <-> (2,0)     ✔ 正確

            i=1 → j=0 → swap (1,0) <-> (0,1)     ❌ 重複交換（又換回來）
            i=1 → j=1 → swap (1,1) <-> (1,1)     ❌ 自己換自己
            i=1 → j=2 → swap (1,2) <-> (2,1)     ✔ 正確

            i=2 → j=0 → swap (2,0) <-> (0,2)     ❌ 重複交換
            i=2 → j=1 → swap (2,1) <-> (1,2)     ❌ 重複交換
            i=2 → j=2 → swap (2,2) <-> (2,2)     ❌ 自己換自己
            ```
        - 所以我們只需要交換右上角的三角形（不含對角線）
    - 只寫 matrix[i][j] = matrix[j][i] 會：

        - 把右下角的值複製到左上

        - 原本左上的值直接消失

        - 假設：
        ```text
        1 2
        3 4
        ```
        當 i=0, j=1：
        ```text
        matrix[0][1] = matrix[1][0]
        ```
        變成：
        ```text
        1 3
        3 4
        ```
        但正確轉置應該是：
        ```text
        1 3
        2 4
        ```
        你把 2 覆蓋掉了。

- 反轉每一行
    ```python
    for i in range(n):
        matrix[i].reverse()
    ```

    - 把每一行的元素左右位置調換

- 合起來就完成順時針 90 度旋轉。

---

## 🧪 範例演算（3×3 矩陣）

假設初始矩陣：
```python
1 2 3
4 5 6
7 8 9
```
- Step 1：轉置

    - 對角線為基準交換，上三角與下三角交換：

得到：
```python
1 4 7
2 5 8
3 6 9
```
- Step 2：反轉每一行

    - 把每一行左右對調：
```python
7 4 1
8 5 2
9 6 3
```
- 這正是把原圖順時針轉 90 度後的結果。

---

## ⏱ 複雜度分析 | Complexity
| 方法            | 時間複雜度 | 空間複雜度 |
| ------------- | ----- | ----- |
| 原地法（轉置 + 反轉行） | O(n²) | O(1)  |
| 輔助矩陣法         | O(n²) | O(n²) |

---

## 🧠 我學到了什麼 | What I Learned

- 矩陣旋轉這類題常見 trick：轉置 + 反轉行

- 要注意交換邊界（i < j）與反轉的方法

- 面試時若先寫輔助矩陣法說明座標映射，再提出原地優化法，這樣思路清楚且全面

- 在原地修改時要留意不覆蓋還沒交換的值