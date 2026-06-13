# 🔍 LeetCode 74 - Search a 2D Matrix

## 📖 Problem Description | 題目描述

You are given an `m × n` matrix with the following properties:

給定一個 `m × n` 的矩陣，滿足：

### ✅ Property 1

Each row is sorted in ascending order.

每一列都是遞增排序。

```text
1  3  5  7
10 11 16 20
23 30 34 60
```

---

### ✅ Property 2

The first element of each row is greater than the last element of the previous row.

每列的第一個元素都大於前一列最後一個元素。

```text
7 < 10
20 < 23
```

---

### 🎯 Goal

Determine whether `target` exists in the matrix.

判斷 `target` 是否存在於矩陣中。

---

# 💡 Key Observation | 核心觀察

The matrix can be viewed as a single sorted array.

整個矩陣其實可以看成一個排序好的一維陣列。

```text
1  3  5  7
10 11 16 20
23 30 34 60
```

⬇️

```text
[1,3,5,7,10,11,16,20,23,30,34,60]
```

---

# 🧠 Solution Idea | 解題思路

Since the entire matrix is globally sorted:

由於整個矩陣是全域排序：

✅ Binary Search

---

# 🔄 Index Mapping | 一維與二維轉換

Assume:

```python
rows = len(matrix)
cols = len(matrix[0])
```

If Binary Search gives:

```python
mid
```

Convert it into matrix coordinates:

```python
row = mid // cols
col = mid % cols
```

---

## 📌 Example

Suppose:

```python
cols = 4
mid = 5
```

Then:

```python
row = 5 // 4 = 1
col = 5 % 4 = 1
```

So:

```python
matrix[1][1]
```

equals:

```python
11
```

---

# ⭐ Most Important Formula

```python
row = mid // cols
col = mid % cols
```

### Memory Trick

```text
// → row
%  → col
```

---

# 💻 Code

```python
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        rows = len(matrix)
        cols = len(matrix[0])

        left = 0
        right = rows * cols - 1

        while left <= right:

            mid = (left + right) // 2

            row = mid // cols
            col = mid % cols

            value = matrix[row][col]

            if value == target:
                return True

            elif value < target:
                left = mid + 1

            else:
                right = mid - 1

        return False
```

---

# 📝 Step-by-Step Explanation | 詳細步驟

## ① Get Matrix Size

取得矩陣大小

```python
rows = len(matrix)
cols = len(matrix[0])
```

Example:

```python
[
 [1,3,5,7],
 [10,11,16,20],
 [23,30,34,60]
]
```

```python
rows = 3
cols = 4
```

---

## ② Create Search Range

建立搜尋範圍

```python
left = 0
right = rows * cols - 1
```

Total elements:

```python
3 × 4 = 12
```

Index range:

```text
0 ~ 11
```

---

## ③ Calculate Mid

取得中間位置

```python
mid = (left + right) // 2
```

---

## ④ Convert Mid to (row, col)

將一維索引轉成二維座標

```python
row = mid // cols
col = mid % cols
```

---

## ⑤ Compare Value

取得元素：

```python
value = matrix[row][col]
```

---

### 🎯 Found Target

```python
if value == target:
    return True
```

找到直接回傳。

---

### ➡️ Search Right Half

```python
elif value < target:
    left = mid + 1
```

代表：

```text
target 在右半邊
```

---

### ⬅️ Search Left Half

```python
else:
    right = mid - 1
```

代表：

```text
target 在左半邊
```

---

# 🔬 Example Walkthrough | 範例追蹤

Input:

```python
matrix = [
 [1,3,5,7],
 [10,11,16,20],
 [23,30,34,60]
]

target = 16
```

---

## Round 1️⃣

```python
left = 0
right = 11

mid = 5
```

Convert:

```python
row = 1
col = 1
```

Value:

```python
11
```

```python
11 < 16
```

Move right:

```python
left = 6
```

---

## Round 2️⃣

```python
left = 6
right = 11

mid = 8
```

Convert:

```python
row = 2
col = 0
```

Value:

```python
23
```

```python
23 > 16
```

Move left:

```python
right = 7
```

---

## Round 3️⃣

```python
left = 6
right = 7

mid = 6
```

Convert:

```python
row = 1
col = 2
```

Value:

```python
16
```

🎉 Found Target

```python
return True
```

---

# ⏱️ Complexity Analysis | 複雜度分析

## 🚀 Time Complexity

```text
O(log(m × n))
```

Binary Search on all matrix elements.

---

## 💾 Space Complexity

```text
O(1)
```

Only a few variables are used.

---

# 🎯 Interview Takeaways | 面試重點

### 🔑 Signal 1

Matrix is globally sorted.

矩陣整體有序。

⬇️

Think:

```text
Binary Search
```

---

### 🔑 Signal 2

Need to convert 1D index into 2D coordinates.

需要將一維索引轉換成二維座標。

```python
row = mid // cols
col = mid % cols
```

---

# 🏆 Memory Cheat Sheet

```text
LeetCode 74

Matrix
↓
Sorted Array
↓
Binary Search

mid
↓
row = mid // cols
col = mid % cols

Time: O(log(m*n))
Space: O(1)
```

### 🌟 One-Sentence Summary

> Treat the matrix as one sorted array and use Binary Search with index mapping.

> 將矩陣視為一個排序陣列，再利用 Binary Search 搭配座標轉換搜尋目標值。
