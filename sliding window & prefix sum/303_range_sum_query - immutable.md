# 📊 LeetCode 303 - Range Sum Query: Immutable
🔗 [題目連結](https://leetcode.com/problems/permutation-in-string/)

---

## 📘 題目描述 | Problem Description

### 中文：
實作一個類別 `NumArray`，支援以下操作：
- 初始化時給定一個整數陣列 `nums`
- 支援查詢任意區間 `[left, right]` 的總和

> 陣列是**不可變的**，所以不會有更新操作。

### English:
Implement a class `NumArray` that supports:

- Initialize with an integer array `nums`
- Query the sum of any range `[left, right]`

> Array is **immutable**, so no update operations are needed.

### Examples
- Example 1:

    - Input: 
        - ["NumArray", "sumRange", "sumRange", "sumRange"]
        - [[[-2, 0, 3, -5, 2, -1]], [0, 2], [2, 5], [0, 5]]
    - Output: [null, 1, -1, -3]

    - Explanation:
        - NumArray numArray = new NumArray([-2, 0, 3, -5, 2, -1]);
        - numArray.sumRange(0, 2); // return (-2) + 0 + 3 = 1
        - numArray.sumRange(2, 5); // return 3 + (-5) + 2 + (-1) = -1
        - numArray.sumRange(0, 5); // return (-2) + 0 + 3 + (-5) + 2 + (-1) = -3

---

## 💡 解題思路 | Solution Idea

### 中文：
- 由於陣列不會改變，可以預先計算 **前綴和（Prefix Sum）**。
- 前綴和陣列 `prefix[i]` 表示 `nums[0]` 到 `nums[i-1]` 的總和。
- 查詢區間 `[left, right]` 的總和可以用：
  
    - sumRange=prefix[right+1]−prefix[left]

### English
- Since the array does not change, we can precompute the prefix sum.

- The prefix sum array prefix[i] represents the sum of elements from nums[0] to nums[i-1].

- The sum of a range [left, right] can be calculated as:

    - sumRange=prefix[right+1]−prefix[left]

---

## 🧾 Python 程式碼

```python
class NumArray:

    def __init__(self, nums: list[int]):
        self.prefix = [0]  # prefix[0] = 0
        for num in nums:
            self.prefix.append(self.prefix[-1] + num)

    def sumRange(self, left: int, right: int) -> int:
        return self.prefix[right + 1] - self.prefix[left]
```

### 🔹 Step 1：建構前綴和 (Constructor)
初始：
```python
self.prefix = [0]
```
| 步驟 | 當前 num | prefix 陣列更新                 |
| -- | ------ | --------------------------- |
| 0  | 無      | \[0]                        |
| 1  | -2     | \[0, -2]                    |
| 2  | 0      | \[0, -2, -2]                |
| 3  | 3      | \[0, -2, -2, 1]             |
| 4  | -5     | \[0, -2, -2, 1, -4]         |
| 5  | 2      | \[0, -2, -2, 1, -4, -2]     |
| 6  | -1     | \[0, -2, -2, 1, -4, -2, -3] |

最終：
```python
prefix = [0, -2, -2, 1, -4, -2, -3]
```
prefix[i] = nums[0] 到 nums[i-1] 的總和

### 🔹 Step 2：區間查詢 sumRange
公式：
```python
sumRange(left, right) = prefix[right+1] - prefix[left]
```
查詢逐步模擬

1️⃣ sumRange(0, 2)

- prefix[3] - prefix[0] = 1 - 0 = 1

2️⃣ sumRange(2, 5)

- prefix[6] - prefix[2] = -3 - (-2) = -1

3️⃣ sumRange(0, 5)

- prefix[6] - prefix[0] = -3 - 0 = -3

---

## ⏱ 複雜度分析 | Complexity
- 初始化時間複雜度: O(n)

- 查詢時間複雜度: O(1)

- 空間複雜度: O(n)

---

## 📚 我學到了什麼 | What I Learned
- 前綴和 prefix[i] 儲存從起點到 i-1 的總和。

- 查詢區間 [L, R] 可以用 右端和 - 左端和 來快速得到。

- 初始化 O(n)，每次查詢 O(1)，非常高效。
