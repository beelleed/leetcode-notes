# 📘 LeetCode 190：Reverse Bits（反轉位元）
🔗 [題目連結](https://leetcode.com/problems/reverse-bits/)

---

## 🧩 題目說明 | Problem Description
### 中文
給你一個 32 位元的無號整數 n，把它的二進位表示反轉後，回傳反轉後的新整數。

### English
You are given a 32‑bit unsigned integer n. Reverse all bits in its binary representation and return the resulting integer.

### Examples
- Example 1:

    - Input: n = 43261596

    - Output: 964176192

    - Explanation:

    - Integer	Binary
    43261596	00000010100101000001111010011100
    964176192	00111001011110000010100101000000

- Example 2:

    - Input: n = 2147483644

    - Output: 1073741822

    - Explanation:

    - Integer	Binary
    2147483644	01111111111111111111111111111100
    1073741822	00111111111111111111111111111110

---

## 🧠 解題思路 | Solution Idea 
- 整數在記憶體中其二進位是固定 32 位元（從 bit0 到 bit31）。

- 要反轉，就是把第 0 位（最右邊）放到第 31 位、把第 1 位放到第 30 位，以此類推。

- 方法：逐個 bit 處理
    - 用 n & 1 擷取最右邊那一位（0 或 1）
    - 這一個 bit 左移到反轉位置：<< (31 - i)
    - 用 OR 或加法把它加到答案 ans 上
    - 把 n 右移一位（n >>= 1），繼續處理下一位

- 做 32 次就把所有位元反轉了。

---

## 💻 程式碼（Python）
```python
class Solution:
    def reverseBits(self, n: int) -> int:
        ans = 0
        for i in range(32):
            # 擷取最右邊那一位
            bit = n & 1
            # 把這位放到反轉位置
            ans |= (bit << (31 - i))
            # 準備處理下一位
            n >>= 1
        return ans
```
```python
class Solution:
    def reverseBits(self, n: int) -> int:
        ans = 0
```
- 我們建立一個變數 ans 來儲存反轉後的結果，初始為 0。

```python
        for i in range(32):
```
- 因為 n 是 32 位元整數，我們要處理它的 每一位 bit，共 32 次。

```python
            bit = n & 1
```
- 這行是 取出 n 最右邊的 1 位。

- n & 1 的意思是與 000...0001 做 bitwise AND，只留下最後一位。例如：

    - 如果 n = 1011（2進位）→ n & 1 = 1

    - 如果 n = 1010（2進位）→ n & 1 = 0

```python
            ans |= (bit << (31 - i))
```
- bit << (31 - i) 是把剛剛擷取的 bit 放到正確的反轉位置：

    - 第 0 位（最低位）要放到第 31 位（最高位）

    - 第 1 位要放到第 30 位...

- |= 是「或等於」（bitwise OR）：把結果加入到 ans 中。

    - 如果 ans 那位是 0，而你 shift 出來的是 1，那這位就變 1。

    - 如果那位是 1，就不變。

```python
            n >>= 1
```
- 把原本的數字 n 右移一位，準備擷取下一位。

- 例如：n = 1010 → n >>= 1 → 0101

```python
        return ans
```
- 結束迴圈，回傳反轉後的新整數 ans

---

## 🔍 範例：n = 5
### 🎲 初始狀態

- n = 5，轉成 32 位的二進位是：
```markdown
00000000000000000000000000000101
                             ↑
                         ←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←
```
### 🔁 運作過程（前 3 次迴圈）
```python
ans = 0
```
- 第一次迴圈 (i = 0)：

    - bit = n & 1 → 5 & 1 = 1

    - ans |= (1 << 31) → ans = 10000000000000000000000000000000 (2^31)

    - n >>= 1 → n = 2

- 第二次迴圈 (i = 1)：

    - bit = 2 & 1 = 0

    - ans |= (0 << 30) → ans 不變

    - n >>= 1 → n = 1

- 第三次迴圈 (i = 2)：

    - bit = 1 & 1 = 1

    - ans |= (1 << 29) → ans = 10100000000000000000000000000000
（第 31 位和第 29 位為 1）

    - n >>= 1 → n = 0

### 🧮 最終結果
```python
return ans  # 2684354560
```

對應二進位：

10100000000000000000000000000000

---

## 📊 複雜度分析 | Complexity

- 時間複雜度：O(1)
    - 因為總是固定做 32 次操作，不論 n 多大或小。有人也會寫成 O(32)，但因為 32 是常數，所以是 O(1)。 


- 空間複雜度：O(1)
    - 只用了少數變數，沒有額外依輸入大小成長的資料結構。

---

## ✅ 我學到什麼 / What I Learned

- 處理位元題目要熟悉 AND、OR、左移、右移操作

- 要反轉整個 32 位元，就按位（bit by bit）做是最直觀又可靠的方法

- 雖然看起來像迴圈，用 32 次也不算長，對位元題來說是常數操作

- 在面試中，如果這題問得快，可以順口說出這種「擷取 + 左移 + OR + 右移」的位元操作方法