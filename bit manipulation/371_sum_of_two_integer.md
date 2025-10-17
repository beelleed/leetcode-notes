# 📘 LeetCode 371：Sum of Two Integers
🔗 [題目連結](https://leetcode.com/problems/sum-of-two-integers/)

---

## 🧮 題目 | Problem Statement

### 中文：
給你兩個整數 a 和 b，不能使用 + 或 - 運算子，請回傳它們的和。

### English：
Given two integers a and b, return the sum of the two integers without using the operators + or -. 

### Examples
- Example 1:

    - Input: a = 1, b = 2
    - Output: 3

- Example 2:

    - Input: a = 2, b = 3
    - Output: 5
 
---

## 🧠 解題思路 | Solution Idea

我們必須避開 + 和 -，所以只能用位元操作來模擬加法。在二進位加法中，有兩件事要處理：

1. 不考慮進位 的加法 — 可以用 XOR （^）來做：a ^ b

    - 因為 XOR 在位相同時給 0，不同時給 1，正好對應 bit 加法中相同 bit 不進位、不同 bit 結果為 1。

2. 進位 的部分 — 可以用 AND 並左移 1 位：(a & b) << 1

    - AND 找出哪一位兩者都是 1，那在加法中會產生進位，進位要加到下一個 bit，所以左移。

- 那麼整個加法過程就變成：

    - sum_without_carry = a ^ b

    - carry = (a & b) << 1

    - 然後我們要 把 carry 加到 sum_without_carry 上，但因為不能用 +，就重複這個流程：把 carry 當作新的 b，讓 a = sum_without_carry，繼續做 XOR + AND << 1。

    - 重複直到 carry 為 0 為止，此時 a 就是最終結果。

- 在 Python 中要注意的是：Python 的整數不是固定 32 位元，會有無限擴展問題；因此常見解法會用 & mask 限制在 32 位範圍內，並在最終處理正負號。

---

## ✅ 程式碼（Python 範例）
```python
class Solution:
    def getSum(self, a: int, b: int) -> int:
        # 為了模擬 32-bit 整數的行為，用 mask 限制
        mask = 0xFFFFFFFF
        # 最大的正數 32-bit
        MAX_INT = 0x7FFFFFFF
        
        a &= mask
        b &= mask
        
        while b != 0:
            # sum 不考慮進位
            sum_no_carry = (a ^ b) & mask
            # 進位部分
            carry = ((a & b) << 1) & mask
            
            a = sum_no_carry
            b = carry
        
        # 如果 a 在 32-bit 範圍內是正數，就直接回傳
        if a <= MAX_INT:
            return a
        else:
            # 否則是負數，轉回 Python 的負值表示
            return ~((a ^ mask))
```
### 🧠 背景邏輯簡述

- 在二進位加法中：

    - a ^ b 相當於「不考慮進位」的加法

    - (a & b) << 1 找出「進位」的部分

- 我們不斷地把「不含進位的總和」與「進位值」加起來，直到進位為 0，表示加法完成。

```python
mask = 0xFFFFFFFF
```

- 用來模擬 32-bit 的整數（全部都是 1，共 32 位）：

    - 0xFFFFFFFF → 11111111111111111111111111111111（二進位）

- 在 Python 中整數不是固定長度，這行是為了確保我們的數在 32-bit 範圍內運作。
```python
MAX_INT = 0x7FFFFFFF
```

- 代表 32-bit 有號整數最大值，也就是 2147483647（首位是 0 表示正號）
```python
a &= mask
b &= mask
```

- 把 a 和 b 限制在 32-bit 整數範圍內（做 & 運算，相當於只取低 32 位）
```python
while b != 0:
```

- 如果 b 還有進位值，就繼續模擬加法的「進位加上去」。
```python
sum_no_carry = (a ^ b) & mask
```

- 使用 XOR 模擬「不考慮進位」的加法（這部分是結果的基底）
```python
carry = ((a & b) << 1) & mask
```

- a & b：找出所有會進位的 bit（兩個都是 1 的位）

- << 1：進位要加到左邊的下一個 bit

- & mask：限制結果在 32 位元內
```python
a = sum_no_carry
b = carry
```

- 將加總結果重新當成新的 a

- 把進位值當成新的 b，繼續模擬「加上進位」
```python
if a <= MAX_INT:
    return a
```

- 如果結果 a 小於等於最大正整數，代表它是正數，可以直接回傳
```python
return ~((a ^ mask))
```

- 若 a 超過 MAX_INT，代表這是一個 負數

- a ^ mask 會把 a 的每個 bit 反轉（相當於 ~a 但控制在 32-bit 內）

- ~(...) 是 Python 的補數表示法，得到正確的負整數

---

## 🧪 範例演算 (a = 2, b = 3)
```ini
a = 2 (10₂), b = 3 (11₂)
```

- 第一次：

    - sum_no_carry = 2 ^ 3 = 1

    - carry = (2 & 3) << 1 = (10₂ & 11₂) << 1 = (10₂) << 1 = 100₂ = 4

    - 令 a = 1, b = 4

- 第二次：

    - sum_no_carry = 1 ^ 4 = 5

    - carry = (1 & 4) << 1 = 0 << 1 = 0

    - b = 0，停止

- 最終 a = 5，答案是 5。

---

## ⏱ 複雜度分析 | Complexity

- 時間複雜度：O(1)
    - 雖然用 while 迴圈，但在 32-bit 的情況下，最多做 32 次運算，所以可以視為常數時間。 

- 空間複雜度：O(1)
    - 只用到少數常數變數。

---

## 🧠 我學到什麼 / What I Learned

- 位元加法可以被拆解成 XOR（不含進位）與 AND（進位）兩部分。

- 重複計算直到沒有進位，就完成了整數相加。

- 在 Python 中要注意整數無限位的特性，因此要用 mask 來模擬固定 32-bit 行為。