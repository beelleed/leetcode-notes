# 🎨 LeetCode 733 - Flood Fill 油漆桶演算法

---

- 題目連結：[https://leetcode.com/problems/flood-fill](https://leetcode.com/problems/flood-fill)
- 題型：DFS / BFS
- 難度：Easy

---

## 📘 題目說明 | Problem Description

### ✅ 中文：
給定一張圖 `image`（二維整數陣列），表示圖片的像素顏色。給你起始像素位置 `(sr, sc)` 和新的顏色 `color`，請將從該起始像素出發，**所有與其相連且顏色相同的像素**（只能上下左右），統一改為新顏色。

### ✅ English:
Given a 2D array `image` representing a picture, a starting pixel `(sr, sc)` and a new color, perform a "flood fill" starting from that pixel. Replace all adjacent pixels (up/down/left/right) that have the same color as the starting pixel with the new color.

### Examples
- Example 1:

    - Input: image = [[1,1,1],[1,1,0],[1,0,1]], sr = 1, sc = 1, color = 2

    - Output: [[2,2,2],[2,2,0],[2,0,1]]

    - From the center of the image with position (sr, sc) = (1, 1) (i.e., the red pixel), all pixels connected by a path of the same color as the starting pixel (i.e., the blue pixels) are colored with the new color.

    - Note the bottom corner is not colored 2, because it is not horizontally or vertically connected to the starting pixel.

- Example 2:

    - Input: image = [[0,0,0],[0,0,0]], sr = 0, sc = 0, color = 0

    - Output: [[0,0,0],[0,0,0]]

    - Explanation: The starting pixel is already colored with 0, which is the same as the target color. Therefore, no changes are made to the image.

---

## 🧠 解題思路 | Solution Strategy
| 步驟     | 中文解釋                               | English Explanation                                  |
| ------ | ---------------------------------- | ---------------------------------------------------- |
| Step 1 | 取得起始像素的顏色 `original_color`         | Get the original color of the starting pixel         |
| Step 2 | 如果起始顏色與目標顏色相同，直接回傳                 | If the color is already the same, return early       |
| Step 3 | 用 DFS 從 `(sr, sc)` 出發，搜尋所有相連且同色的像素 | Use DFS to traverse connected pixels with same color |
| Step 4 | 把這些像素的顏色改成目標顏色                     | Change their color to the new target color           |

---

## 🔧 程式碼 | Python Code

```python
from typing import List

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        original_color = image[sr][sc]
        if original_color == color:
            return image  # 如果顏色一樣就不用改

        rows, cols = len(image), len(image[0])

        def dfs(r, c):
            if r < 0 or r >= rows or c < 0 or c >= cols:
                return
            if image[r][c] != original_color:
                return

            image[r][c] = color
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        dfs(sr, sc)
        return image
```

```python
from typing import List

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
```
- ✅ 定義一個方法 floodFill，參數包含：

    - image: 二維陣列，代表圖片（像素值）

    - sr、sc: 起始像素的行與列（start row, start column）

    - color: 要替換的新顏色

```python
original_color = image[sr][sc]
if original_color == color:
    return image
```
- ✅ 抓出起點顏色 original_color

- ✅ 若新顏色與原本顏色一樣，表示不需填色，直接回傳原圖

```python
rows, cols = len(image), len(image[0])
```
- ✅ 儲存圖片的行列數，方便之後做邊界檢查

```python
def dfs(r, c):
    if r < 0 or r >= rows or c < 0 or c >= cols:
        return
```
- ✅ DFS 遞迴函式，先檢查索引是否越界（不能超出圖片邊界）

```python
if image[r][c] != original_color:
    return
```
- ✅ 若當前像素顏色不是起始顏色，就不處理，直接返回

```python
image[r][c] = color
```
- ✅ 把符合條件的像素染上新顏色（表示已拜訪）

```python
dfs(r + 1, c)
dfs(r - 1, c)
dfs(r, c + 1)
dfs(r, c - 1)
```
- ✅ 往「下、上、右、左」四個方向繼續遞迴擴散染色

- ✅ 不考慮對角線，只處理上下左右相鄰格子

```python
dfs(sr, sc)
return image
```
- ✅ 從起點開始執行 DFS

- ✅ 回傳最終染色後的圖片

### 🧠 小結
- 這是一個經典的「連通區域遍歷」問題

- 使用 DFS 來搜尋整個區塊

- 需要熟悉邊界檢查與條件中止技巧

- 記得提前處理顏色相同的情況，避免無窮遞迴

---

## ⏱️ 複雜度分析 | Complexity
| 類型    | 中文說明                    | English Description                    |
| ----- | ----------------------- | -------------------------------------- |
| 時間複雜度 | O(M × N)，M 為列數，N 為欄數    | O(M × N), visit each cell at most once |
| 空間複雜度 | O(M × N)（最壞情況 DFS 遞迴堆疊） | O(M × N) due to DFS recursion stack    |

---

## 🧠 小知識補充 | Notes
- sr：starting row 起始行索引

- sc：starting column 起始列索引

- image[sr][sc]：起始像素顏色

- 四個方向：上、下、左、右（不含斜角）

---

## 🎯 我學到的東西 | What I Learned

### ✅ 中文：

- 理解了「Flood Fill」像是圖像處理裡的油漆桶工具。
- 熟悉如何用 DFS 遞迴來處理相連區塊問題。
- 學會判斷遞迴終止條件（越界、不同顏色）。
- 學會預處理：起始顏色與目標顏色若相同，可提前返回。
- 加強了對 2D 陣列座標操作的理解（行 row、列 column）。

### ✅ English:

- Learned how Flood Fill works like the Paint Bucket tool in image editing.
- Practiced using DFS to traverse connected components.
- Understood how to set base cases for recursion (out of bounds or color mismatch).
- Realized the importance of handling edge cases early.
- Strengthened understanding of 2D array navigation using row and column indexes.
