# 🔍 LeetCode 268 — Missing Number / 缺失的數字
🔗 [題目連結](https://leetcode.com/problems/missing-number/)

---

## 📄 題目說明 | Problem Description

**中文**  
給定一個包含 n 個 **不重複** 整數的陣列 `nums`，其值範圍是在 `[0, n]`。也就是說，在這個範圍內有 `n+1` 個整數，但陣列裡只出現了 n 個，缺少一個。請找出哪個數字缺失。

**English**  
Given an array `nums` containing `n` distinct numbers from the range `[0, n]`, return the one number in the range that is missing from the array.

**Examples**
- Example 1:

    - Input: nums = [3,0,1]

    - Output: 2

    - Explanation:

        - n = 3 since there are 3 numbers, so all numbers are in the range [0,3]. 2 is the missing number in the range since it does not appear in nums.

- Example 2:

    - Input: nums = [0,1]

    - Output: 2

    - Explanation:

        - n = 2 since there are 2 numbers, so all numbers are in the range [0,2]. 2 is the missing number in the range since it does not appear in nums.

- Example 3:

    - Input: nums = [9,6,4,2,3,5,7,0,1]

    - Output: 8

    - Explanation:

        - n = 9 since there are 9 numbers, so all numbers are in the range [0,9]. 8 is the missing number in the range since it does not appear in nums.

---

## 🧠 解法思路 | Solution Ideas

### 方法 A：利用算術公式（高斯求和法）

- 因為 0 到 n 的和是 \(\frac{n(n+1)}{2}\)  
- 我們把這個總和減去 `nums` 中所有數字的和，剩下的差值就是缺失的數字  

- 公式：  
    - expected_sum = n * (n + 1) // 2
    - actual_sum = sum(nums)
    - missing = expected_sum - actual_sum

### 方法 B：位元操作 XOR（最常被考）

- 特性：a ^ a = 0, a ^ 0 = a  
- 構造：把 0 到 n 全部 XOR 一遍，再 XOR 所有 nums 中的數字  
- 這樣剩下的就是「那個只出現一次的數字」，也就是缺失值  

---

## 💻 方法 A - 數學總和法（Gauss' Formula）
```python
from typing import List

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        expected = n * (n + 1) // 2  # 完整 0~n 的總和
        actual = sum(nums)          # 現有數字總和
        return expected - actual    # 缺失的那個就是差值
```

### 📘 解釋說明

- 使用高斯公式：0 + 1 + 2 + ... + n = n(n+1) / 2	​
- 然後用「應有總和 - 實際總和」來找出缺失的數字

- 時間複雜度是 O(n)，空間複雜度是 O(1)

### 🧪 範例

假設 nums = [3, 0, 1]

- n = 3

- 應有總和 = 0 + 1 + 2 + 3 = 6

- 實際總和 = 3 + 0 + 1 = 4

- 缺失 = 6 - 4 = 2

---

## 💻 方法 B - XOR

```python
from typing import List

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        missing = 0
        # XOR 所有從 0 到 n 的整數
        for i in range(n + 1):
            missing ^= i
        # 再 XOR nums 中的每個數字
        for num in nums:
            missing ^= num
        return missing
```
```python
n = len(nums)
missing = 0
```
- n 是陣列長度，其實是 “缺少一個數字” 前後總共應該有 n+1 個數字

- missing 初始化為 0，作為累積 XOR 的變數

```python
for i in range(n + 1):
    missing ^= i
```

- 把從 0 到 n 的每個整數都 XOR 進 missing

- 理論上這一步後 missing = 0 ^ 1 ^ 2 ^ … ^ n

```python
for num in nums:
    missing ^= num
```
- 再把陣列中的每個數字 XOR 進來

- 因為陣列中有 n 個數字，原本從 0~n 的 XOR 已經包含完整範圍

- 所有出現在 nums 的數字都會被 XOR 抵消（a ^ a = 0），剩下的就是那個缺失的數字

```python
return missing
```
- 返回 XOR 運算後的結果，就是缺少的數字

### 🎯 XOR（^）是什麼？

- ^：兩個位元不同 → 結果為 1；相同 → 結果為 0

    - 0 ^ 0 = 0

    - 1 ^ 1 = 0

    - 0 ^ 1 = 1

    - 1 ^ 0 = 1
        ```python
        a = 5       # 二進位: 0101
        b = 3       # 二進位: 0011

        a ^= b      # a = a ^ b → 0101 ^ 0011 = 0110（即 6）

        print(a)    # ➝ 6
        ```

### 🧪 範例演算
- 假設 nums = [3, 0, 1]，長度 n = 3。那麼應該包含的數字是 0, 1, 2, 3，缺少的是 2。

- 初始狀態

    - n = 3

    - missing = 0

### 步驟 1：XOR 所有從 0 到 n（0 ~ 3）
```plaintext
missing = 0

missing ^= 0   → 000 ^ 000 = 000
missing ^= 1   → 000 ^ 001 = 001
missing ^= 2   → 001 ^ 010 = 011
missing ^= 3   → 011 ^ 011 = 000
```

- 所以目前 missing = 000（十進位是 0）

- 為什麼？因為我們 XOR 了 0^1^2^3，後來自己 XOR 抵消的情況會讓重複部分抵消。

### 步驟 2：再 XOR nums 中的每個數字

-  我們接著把陣列裡的每個值都 XOR 一次：
```plaintext
missing ^= 3   → 000 ^ 011 = 011
missing ^= 0   → 011 ^ 000 = 011
missing ^= 1   → 011 ^ 001 = 010
```

- 最終 missing = 010（二進位），也就是十進位的 2

### ✅ 為什麼這樣能得到缺失值？

- XOR 的特性：

    - a⊕a=0

    - a⊕0=a

    - XOR 是可交換與可結合的

- 當先對 0 到 n 全做 XOR，接著再對 nums 裡的元素做 XOR，等於你把在 nums 裡出現的數字「抵消」掉，最後剩下的就是唯一沒有在 nums 出現的那一個數字。

- 這樣方法的優點是時間複雜度 O(n)，空間複雜度 O(1)，而且沒有溢出的風險（相較於加總法在某些語言可能發生整數溢出）。

---

## ⏱ 複雜度分析 | Complexity
| 方法     | 時間複雜度  | 空間複雜度  |
| ------ | ------ | ------ |
| XOR 方法 | (O(n)) | (O(1)) |
| 算術公式方法 | (O(n)) | (O(1)) |

---

## ✍ 我學到了什麼 / What I Learned

- 利用 XOR 的特性可以在常數空間中解出缺失值，非常巧妙

- XOR 方法比求和方法更安全，因為求和可能有整數溢出（在一些語言中）

- 這類題常考 bit manipulation 思維，是面試中值得掌握的技巧
