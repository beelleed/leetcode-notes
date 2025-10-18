# 📘 LeetCode 191：Number of 1 Bits
🔗 [題目連結](https://leetcode.com/problems/number-of-1-bits/)


---

## 🧮 題目 | Problem (“Number of 1 Bits”)

### 中文：
給你一個 32 位元的無號整數 n，請回傳它的二進位表示中有多少個 1 位元。也稱為漢明權重（Hamming Weight）。

### English：
Given a 32-bit unsigned integer n, return the number of 1 bits it has (also known as the Hamming weight). 

### Examples
| 輸入                                 | 輸出 | 說明                         |
| ---------------------------------- | -- | -------------------------- |
| `00000000000000000000000000001011` | 3  | 有三個 `1` 位元    |
| `00000000000000000000000010000000` | 1  | 只有一個 `1`      |
| `11111111111111111111111111111101` | 31 | 除一位之外，全是 `1`  |

---

## 🧠 解題思路 | Solution Idea

- 這題是位元操作（bit manipulation）題目。你可以有兩種常見做法：

### 方法 A：逐位檢查 + 右移法

- 初始化 count = 0，用來記錄 1 的數量。

- 重複 32 次（對於 32 位元）：

    - count += (n & 1)：檢查最右邊那一位是否為 1。

    - n >>= 1：把 n 右移一位，讓下一位變成新的最右位。

- 最後回傳 count。

這樣你會檢查每個位元是否為 1。

### 方法 B：Brian Kernighan’s 演算法（清除最低位的 1）

- 這是一個優化技巧：

    - 每次做 n = n & (n - 1)，可以把 n 最右邊的那個 1 直接清除。

    - 每做一次清除，就代表找到一個 1。

    - 重複執行直到 n 變成 0 為止，其執行次數就等同於原有的 1 的數量。

這樣如果 n 有很少的 1，做的次數就少。

---

## ✅ 程式碼 | Python 實作

### Method A

```python
class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        for _ in range(32):
            count += (n & 1)
            n >>= 1
        return count
```
```python
count = 0
```
- 用來累加 1 的數量。

```python
for _ in range(32):
```
- 因為是 32 位元整數，所以檢查 32 次。

```python
count += (n & 1)
```
- n & 1：檢查最右邊那一位是 0 或 1。

- 如果最右邊是 1，那這行會加 1；若是 0，則加 0。

```python
n >>= 1
```
- 把現在的 n 右移一位。也就是把已經檢查過的最低位拿掉，下一位成為最低位，準備下一輪檢查。

```python
return count
```
- 回傳最終的 1 的總數。

---

## 🧪 範例演算流程（以 n = 11 為例）
- n = 11 的二進位是 1011（補到 32 位元看為 000...01011）：

    - 第一次：n & 1 = 1，count = 1，n >>= 1 → n = 5（0101）

    - 第二次：n & 1 = 1，count = 2，n >>= 1 → n = 2（0010）

    - 第三次：n & 1 = 0，count = 2，n >>= 1 → n = 1（0001）

    - 第四次：n & 1 = 1，count = 3，n >>= 1 → n = 0

    - 之後 n = 0 時，n & 1 = 0 持續加 0

- 最終 count = 3，正確。

---

### Method B: Kernighan 方法：
```python
class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n:
            n &= (n - 1)
            count += 1
        return count
```
```python
class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
```
- count 是我們用來累加「1 的數量」的變數。
```python
        while n:
```
- 這個 while 迴圈會持續執行，直到 n 變成 0。

- 每次會處理掉 n 的 最右邊的 1。

```python
            n &= (n - 1)
```
### 🧩 基本概念：& 是 bitwise AND

- a & b 代表：a 與 b 每一位相同時才是 1，其餘是 0。

### 🔧 這是關鍵技巧！
- 這一行可以 刪除 n 的最右邊的一個 1 bit。

- 例子：
    - 假設 n = 12，二進位是 1100

```text
n      = 1100
n - 1  = 1011
n & n-1 = 1000
```
- n & (n - 1) 會把 最右邊的 1 清掉。
- 每次執行這行，代表「找到一個 1」，所以我們可以 count += 1。

```python
            count += 1
```
- 每次刪掉一個 1，就把 count 加一。

```python
        return count
```
- 回傳總共刪了幾次（也就是原本有幾個 1）。

---

## 🧪 範例流程（n = 13）
- n = 13 二進位是 1101

```text
初始 n = 1101

1. n = 1101
   n - 1 = 1100
   n &= n - 1 → n = 1100
   count = 1

2. n = 1100
   n - 1 = 1011
   n &= n - 1 → n = 1000
   count = 2

3. n = 1000
   n - 1 = 0111
   n &= n - 1 → n = 0000
   count = 3

結束，答案 = 3（共有三個 1）
```

---

## ⏱ 複雜度分析 | Complexity
| 方法                 | 時間複雜度                          | 空間複雜度  |
| ------------------ | ------------------------------ | ------ |
| 逐位檢查 + 右移法         | (O(1))（固定 32 次）                | (O(1)) |
| Brian Kernighan 方法 | (O(k))，(k) = `1` 的數量（最壞也 ≤ 32） | (O(1)) |

因為輸入總是固定 32 位，兩方法在實務上都可視為常數時間 O(1)

---

## 🧠 我學到什麼 | What I Learned

- 位元操作基本技巧（& 1、>>= 1、&= n–1）很實用。

- Kernighan 方法能有效跳過大量的 0 位，而不用逐位遍歷。