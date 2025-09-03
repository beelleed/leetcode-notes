# 🧮 238. Product of Array Except Self | 陣列中除自身以外的乘積

## 📘 題目說明 | Problem Description

### **中文：**  
  給定一個整數陣列 `nums`，請輸出陣列 `answer`，使得 `answer[i]` 等於 `nums` 陣列中除 `nums[i]` 外所有元素的乘積。

### **English:**  
  Given an integer array `nums`, return an array `answer` such that `answer[i]` is equal to the product of all the elements of `nums` except `nums[i]`.

### Examples
- Example 1:

    - Input: nums = [1,2,3,4]
    - Output: [24,12,8,6]

- Example 2:

    - Input: nums = [-1,1,0,-3,3]
    - Output: [0,0,9,0,0]

---

## 💡 前綴 × 後綴法（Prefix & Suffix，O(n) 時間，常數額外空間）

### 🧠 中文思路：
1. 建立長度為 `n` 的結果陣列 `result`，初始化為 1。
2. **第一次遍歷（從左到右）**：維護 `left_product`（初值為 1）並更新每個位置的左側乘積。
3. **第二次遍歷（從右到左）**：維護 `right_product`，將其與 `result[i]` 相乘，即為最終答案。

### 🧠 English Explanation:
1. Initialize a result array with `1`s.
2. **Left pass:** keep track of `left_product`, update `result[i] = left_product`.
3. **Right pass:** track `right_product`, update `result[i] *= right_product`.

---

## 🧑‍💻 Python 程式碼 | Code

```python
from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [0] * n

        # First pass: left products
        left_product = 1
        for i in range(n):
            result[i] = left_product
            left_product *= nums[i]

        # Second pass: right products
        right_product = 1
        for i in range(n - 1, -1, -1):
            result[i] *= right_product
            right_product *= nums[i]

        return result
```
```python
n = len(nums)
result = [0] * n
```
- n 是輸入長度。

- 建立一個結果陣列 result，初始全部為 0。

❗實際上這一行預設為 0 只是佔位，下面會馬上改值，所以也可寫成 [1] * n 效果一樣。

### 🔁 第一次遍歷：從左往右，計算每個位置左側乘積
```python
left_product = 1
for i in range(n):
    result[i] = left_product
    left_product *= nums[i]
```
| 變數             | 意義              |
| -------------- | --------------- |
| `left_product` | 到目前為止的左邊所有元素的乘積 |
| `result[i]`    | 等於左邊所有元素的乘積     |

舉例（nums = [1, 2, 3, 4]）：
| i | nums\[i] | result\[i] | left\_product 更新後 |
| - | -------- | ---------- | ----------------- |
| 0 | 1        | 1          | 1×1 = 1           |
| 1 | 2        | 1          | 1×2 = 2           |
| 2 | 3        | 2          | 2×3 = 6           |
| 3 | 4        | 6          | 6×4 = 24          |

### 🔁 第二次遍歷：從右往左，乘上右側乘積
```python
right_product = 1
for i in range(n - 1, -1, -1):
    result[i] *= right_product
    right_product *= nums[i]
```
這段意思是：

- 用一個變數 right_product，記錄「右邊所有元素的乘積」。

- 再乘進 result[i] 中（前面已經是左邊乘積）。

舉例：
| i | nums\[i] | result\[i]（乘前） | result\[i]（乘後） | right\_product 更新後 |
| - | -------- | -------------- | -------------- | ------------------ |
| 3 | 4        | 6              | 6×1 = 6        | 1×4 = 4            |
| 2 | 3        | 2              | 2×4 = 8        | 4×3 = 12           |
| 1 | 2        | 1              | 1×12 = 12      | 12×2 = 24          |
| 0 | 1        | 1              | 1×24 = 24      | 24×1 = 24          |

### ✅ 最終結果
```python
return result
```
- 結果為：[24, 12, 8, 6]，就是除了自己以外的乘積。

---

## ⏱ 複雜度分析 | Time & Space Complexity
| 項目    | 複雜度          |
| ----- | ------------ |
| 時間複雜度 | `O(n)`       |
| 空間複雜度 | `O(1)`（不含輸出） |

---

## 📚 我學到了什麼 | What I Learned
### 中文：

- 本題可利用「前綴與後綴乘積」的技巧在不使用除法的情況下解決問題。

- 不需要額外空間，只用兩個變數（左乘積與右乘積）即可完成，符合空間最佳化。

### English:

- By using the prefix and suffix product method, we can compute the result without division.

- The solution is time-efficient and space-optimized, only using a constant number of variables.