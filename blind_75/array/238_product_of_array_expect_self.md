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

🔹 初始：
```python
right_product = 1
```
（表示「目前還沒乘任何數」）
- i = 3：

    - nums[3] = 4

    - 執行 result[3] *= right_product ➜ 6 × 1 = 6

    - 更新：right_product *= nums[3] ➜ 1 × 4 = 4

- i = 2：

    - nums[2] = 3

    - 執行 result[2] *= right_product ➜ 2 × 4 = 8

    - 更新：right_product *= nums[2] ➜ 4 × 3 = 12

- i = 1：

    - nums[1] = 2

    - 執行 result[1] *= right_product ➜ 1 × 12 = 12

    - 更新：right_product *= nums[1] ➜ 12 × 2 = 24

- i = 0：

    - nums[0] = 1

    - 執行 result[0] *= right_product ➜ 1 × 24 = 24

    - 更新：right_product *= nums[0] ➜ 24 × 1 = 24（最後也沒用了）

#### 📘 語法格式：
```python
range(start, stop, step)
```
| 參數    | 意義           |
| ----- | ------------ |
| start | 起始值（**包含**）  |
| stop  | 結束值（**不包含**） |
| step  | 每次增加或減少多少    |

- 假設 n = 4，這段會變成：
```python
range(3, -1, -1)
```
👉 從 3 開始

👉 每次 減 1

👉 到 大於 -1 為止（也就是 0 為止）

🔁 會產生的數字是：3, 2, 1, 0

### ✅ 最終結果
```python
return result
```
- 結果為：[24, 12, 8, 6]，就是除了自己以外的乘積。

---

## 🎯 題目本質

- 題目在問：對每個 i 要算「除了自己以外的全部乘積」

- 寫成數學：

    - 𝑟𝑒𝑠𝑢𝑙𝑡[𝑖] = 𝑛𝑢𝑚𝑠[0] × 𝑛𝑢𝑚𝑠[1] × ... × 𝑛𝑢𝑚𝑠[𝑖 - 1] × 𝑛𝑢𝑚𝑠[𝑖 + 1] × ... × 𝑛𝑢𝑚𝑠[𝑛 - 1]

### 🧠 第一步：拆開來看

- 你會發現：「除了自己」

    - 其實就是：

        - 👉 左邊全部
        
        - 👉 右邊全部

    - 也就是： =(左邊乘積)×(右邊乘積)

- 這一步是關鍵觀察。

### 🔥 第二步：問自己

- 如果我要一直重算左邊乘積會怎樣？

    - 例如：nums = [1,2,3,4]

        - i=3 時：

        - 左邊是 1×2×3

        - 你每次都重新算嗎？

        - 那會變 O(n²)

### 🎯 第三步：動態規劃思考

- 左邊乘積其實有重複計算。

- 例如：
```text
i=2 的左邊 = 1×2
i=3 的左邊 = (1×2)×3
```

- 你發現什麼？ 👉 可以累積

- 這就是：
```text
prefix[i] = prefix[i-1] × nums[i-1]
```
- 這是一個「累積型 DP」。

### 🚀 第四步：右邊也是一樣

- 右邊：
```text
suffix[i] = suffix[i+1] × nums[i+1]
```
- 只是方向反過來。

### 🔎 為什麼這樣是自然的思考？

- 因為這題是：全部乘積 - 自己

- 當你不能用除法時，自然會想：「那我把自己排除掉」

- 排除自己的方式只有兩種：

    - 切開

    - 或倒著算

### 🧩 這其實是「切一刀」的思想

- 想像數線：[  左邊  |  自己  |  右邊  ]

- 看到：要排除一個元素

- 就會想到：👉 左右分離

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