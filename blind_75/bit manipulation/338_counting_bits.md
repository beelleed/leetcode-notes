# 📊 LeetCode 338 — Counting Bits / 二進位中 1 的個數
🔗 [題目連結](https://leetcode.com/problems/counting-bits/)


---

## 📄 題目說明 | Problem Description

**中文**：給定一個非負整數 `n`，請返回一個長度為 `n + 1` 的陣列 `ans`，其中 `ans[i]` 是整數 `i` 的二進位表示中 `1` 的個數。  

**English**: Given a non-negative integer `n`, return an array `ans` of length `n + 1` such that `ans[i]` is the number of `1` bits in the binary representation of `i`.

**Examples**
- Example 1:

    - Input: n = 2
    - Output: [0,1,1]
    - Explanation:
        0 --> 0
        1 --> 1
        2 --> 10

- Example 2:

    - Input: n = 5
    - Output: [0,1,1,2,1,2]
    - Explanation:
        0 --> 0
        1 --> 1
        2 --> 10
        3 --> 11
        4 --> 100
        5 --> 101
 

---

## 🧠 方法一：使用 “offset + DP” 優化法 | Optimized DP with Offset Trick

### 💡 思路 | Idea

- 我們可以利用已經算過的結果來構建新的結果，而不必對每個數字都重頭算。
- `offset` 表示當前最近的二的冪：「區段起始」  
- 若 `i == offset * 2`，則意味著我們進入下一個區段，`offset *= 2`  
- 對於任意 `i`，我們有：ans[i] = ans[i - offset] + 1
- 
這是因為 `i` 減去這個區段起始的 `offset` 後，剩下部分的 1 的數量已經計算過，只要加 1（因為最高那個 1）。

### 💻 程式碼

```python
class Solution:
  def countBits(self, n: int):
      ans = [0] * (n + 1)
      offset = 1
      for i in range(1, n + 1):
          if i == offset * 2:
              offset *= 2
          ans[i] = ans[i - offset] + 1
      return ans
```
- ans = [0] * (n + 1)：初始化答案陣列，大小為 n + 1，預設為 0

- offset = 1：起始的區段大小是 2^0 = 1

- 迴圈從 i = 1 到 n：

    - 若 i == offset * 2：代表到下一個區段起點 → offset *= 2

    - ans[i] = ans[i - offset] + 1：減掉區段起始後，再加 1

        - 假設我們目前正在處理數字 `i`。  
        我們知道 `offset` 代表「目前這個區段的起始二的冪次」，也就是說：

        - 當前的數字 `i` 位於這個區段範圍：  
        `[offset, offset * 2 - 1]`

        舉例來說：
        - 當 `offset = 4` 時，這個區段的範圍是 `[4, 7]`
        - 4 → `100`
        - 5 → `101`
        - 6 → `110`
        - 7 → `111`

        👉 可以觀察出這個規律：
        > 這一整個區段的二進位「都只是把前一個區段的位元結果加上最前面的一個 1」

        例如：
        | 數字 | 二進位 | 來自哪裡 | 舊的位元數量 | 新的 |
        |------|---------|-----------|---------------|-------|
        | 4    | 100     | 0 (`000`) + 1 | ans[0] = 0 | 0 + 1 = 1 |
        | 5    | 101     | 1 (`001`) + 1 | ans[1] = 1 | 1 + 1 = 2 |
        | 6    | 110     | 2 (`010`) + 1 | ans[2] = 1 | 1 + 1 = 2 |
        | 7    | 111     | 3 (`011`) + 1 | ans[3] = 2 | 2 + 1 = 3 |

        - 因此： 當我們在算 `i = 6` 時，我們知道「它只是把 `i - offset = 2` 的二進位加上一個最高位的 1」

        - 所以：ans[6] = ans[2] + 1 這樣就能快速得到新的數字的 1 的數量。

---

## 🧪 範例（n = 7）
| i | offset                      | i - offset | ans[i - offset] | ans[i] = +1 |
| - | --------------------------- | ---------- | --------------- | ----------- |
| 0 | 1                           | —          | —               | 0           |
| 1 | offset=1                    | 1 - 1 = 0  | ans[0] = 0      | 1           |
| 2 | 2 = offset * 2 → offset = 2 | —          | —               | —           |
| 2 | offset=2                    | 2 - 2 = 0  | ans[0] = 0      | 1           |
| 3 | offset=2                    | 3 - 2 = 1  | ans[1] = 1      | 2           |
| 4 | 4 = offset * 2 → offset = 4 | —          | —               | —           |
| 4 | offset=4                    | 4 - 4 = 0  | ans[0] = 0      | 1           |
| 5 | offset=4                    | 5 - 4 = 1  | ans[1] = 1      | 2           |
| 6 | offset=4                    | 6 - 4 = 2  | ans[2] = 1      | 2           |
| 7 | offset=4                    | 7 - 4 = 3  | ans[3] = 2      | 3           |

最後結果：[0,1,1,2,1,2,2,3]

## ### 🧪 範例：n = 8

| i | offset | i-offset | binary(i) | binary(i-offset) | ans[i-offset] | ans[i] = ans[i-offset] + 1 |
|---|---------|-----------|------------|------------------|----------------|----------------------------|
| 0 | 1 | — | 0 | — | — | 0 |
| 1 | 1 | 0 | 1 | 0 | 0 | 1 |
| 2 | 2 | 0 | 10 | 0 | 0 | 1 |
| 3 | 2 | 1 | 11 | 1 | 1 | 2 |
| 4 | 4 | 0 | 100 | 0 | 0 | 1 |
| 5 | 4 | 1 | 101 | 1 | 1 | 2 |
| 6 | 4 | 2 | 110 | 10 | 1 | 2 |
| 7 | 4 | 3 | 111 | 11 | 2 | 3 |
| 8 | 8 | 0 | 1000 | 0 | 0 | 1 |

最後得到結果：ans = [0,1,1,2,1,2,2,3,1]

---

## 🛠 方法二：暴力法 | Brute‑Force Method

### 🧠 思路 | Idea

對每個數字 `i`，把它轉成 **二進位字串**，然後用 Python 內建的 `.count('1')` 計算其中 `1` 的個數。

這是最直觀也最容易理解的方法，適合初學者。

---

## 💻 程式碼 | Python Code

```python
class Solution:
    def countBits(self, n: int):
        ans = []
        for i in range(n + 1):
            binary = bin(i)                  # 將數字轉換成二進位字串，如 5 → '0b101'
            ones_count = binary.count('1')  # 計算字串中出現 '1' 的次數
            ans.append(ones_count)
        return ans
```

### 🧪 範例（以 n = 5 為例）
| 數字 i | 二進位表示 | '1' 的個數 |
| ---- | ----- | ------- |
| 0    | 0b0   | 0       |
| 1    | 0b1   | 1       |
| 2    | 0b10  | 1       |
| 3    | 0b11  | 2       |
| 4    | 0b100 | 1       |
| 5    | 0b101 | 2       |

🔚 回傳結果：[0, 1, 1, 2, 1, 2]

```python
class Solution:
    def countBits(self, n: int):
        def count_ones(x: int) -> int:
            cnt = 0
            while x > 0:
                cnt += x & 1
                x >>= 1
            return cnt

        ans = []
        for i in range(n + 1):
            ans.append(count_ones(i))
        return ans
```
```python
while x > 0:
```
- 當 x 還不是 0，就繼續執行（直到所有 bit 都檢查完）

```python
    cnt += x & 1
```
- 檢查 x 的最後一位是 0 還是 1：

    - x & 1 只會是 0 或 1

    - 如果是 1，代表最後一位是 1，要加到計數器 cnt 裡

```python
    x >>= 1
```
- 把 x 的二進位右移 1 位，相當於「去掉最後一位」

    - 例如：x = 6，二進位是 110

        - 第一次 x & 1 是 0（最後一位是 0）

        - 然後變成 11 → x = 3

        - 第二次 x & 1 是 1（最後一位是 1）

        - 然後變成 1 → x = 1

        - 再來 x & 1 是 1

        - 再來變成 0 → 結束

```python
return cnt
```
- 回傳累積的 1 的數量

```python
        ans = []
        for i in range(n + 1):
            ans.append(count_ones(i))
        return ans
```

- 對每個 i（從 0 到 n）都呼叫 count_ones(i)

- 這樣每個數字都從頭計算其 1 的位元數

#### ✅ x & 1 的含義：

- 這會把 x 的二進位數字，和 000...0001 做 AND 運算。

    - 若結果是 1，代表 x 是奇數（最後一位是 1）

    - 若結果是 0，代表 x 是偶數（最後一位是 0）

### 💡 例子：
```python
x = 5  # 二進位為 101
print(x & 1)  # 輸出 1 → 是奇數

x = 8  # 二進位為 1000
print(x & 1)  # 輸出 0 → 是偶數
```

---

## ⏱ 複雜度分析 | Complexity
| 方法         | 時間複雜度      | 空間複雜度 |
| ---------- | ---------- | ----- |
| 偏移 + DP 方法 | O(n)       | O(n)  |
| 暴力法        | O(n log n) | O(n)  |

- 偏移 + DP 方法每個 i 只做常數操作 → O(n)

- 暴力法對每個數字做位元運算，最多 log(i) 步 → 總共 O(n log n)

---

## ✍ 我學到了什麼 / What I Learned

- 利用「二的冪區段」來重複利用已計算結果，是位元題常見技巧

- offset 方法能讓原本看似複雜的問題變得線性時間

- 暴力法雖然寫法直觀但在 n 大時會超時，是衡量優化前的 baseline
