# 🪙 LeetCode 322. Coin Change
[LeetCode 題目連結](https://leetcode.com/problems/coin-change/)

---

## 📘 題目說明 | Problem Description

- **中文：**  
  給定一組不同面額的硬幣 `coins`（每種硬幣數量不限），以及目標金額 `amount`。請找出最少需要多少枚硬幣才能湊出這個金額，若無法湊出，請回傳 `-1`。

- **English:**  
  You are given coins of different denominations (`coins`) with unlimited supply and a target amount (`amount`). Return the **minimum number of coins** needed to make up that amount. If it’s impossible, return `-1`.

### Examples
- Example 1:

    - Input: coins = [1,2,5], amount = 11
    - Output: 3
    - Explanation: 11 = 5 + 5 + 1

- Example 2:

    - Input: coins = [2], amount = 3
    - Output: -1

- Example 3:

    - Input: coins = [1], amount = 0
    - Output: 0

---

## 🧠 解題思路 | Solution Ideas

### 💡 中文思路：
1. 建立一維陣列 `dp` 長度為 `amount + 1`，`dp[i]` 表示湊出金額 i 所需的最少硬幣數。
2. 初始化：
   - `dp[0] = 0`（湊 0 元需要 0 枚硬幣）
   - 其餘設為 `amount + 1`，表示無法達成
3. 遍歷每個硬幣 `coin`，再遍歷金額 `i`：
   - `dp[i] = min(dp[i], dp[i - coin] + 1)`
4. 若 `dp[amount]` 還是初始值，代表無法湊出 → 回傳 `-1`

### 🌐 English Explanation:
1. Create a 1D DP array `dp`, where `dp[i]` = min number of coins to make `i`
2. Init `dp[0] = 0`, others to `amount + 1`
3. For each coin and each amount `i`, update:
   `dp[i] = min(dp[i], dp[i - coin] + 1)`
4. Return `dp[amount]` if valid, else `-1`

### 🧩 Python 程式碼：
```python
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [0] + [amount + 1] * amount
        for coin in coins:
            for i in range(coin, amount + 1):
                dp[i] = min(dp[i], dp[i - coin] + 1)
        return dp[amount] if dp[amount] <= amount else -1
```
```python
dp = [0] + [amount + 1] * amount
```
- 建立一個 dp 陣列，長度為 amount + 1，用來記錄湊出金額 i 所需的最少硬幣數。

- dp[0] = 0：代表金額 0 不需要任何硬幣。

- 其餘初始化為 amount + 1，當作一個無限大的預設值（因為最大不可能超過 amount 枚硬幣）。

### 📘 小記法：

- 如果是「最小化」型 DP（像 Coin Change、Min Path Sum），
    - 初始化 = 很大值（amount + 1 或 float('inf')）

- 如果是「最大化」型 DP（像 House Robber、LCS），
    - 初始化 = 很小值（0 或 -inf）

```python
for coin in coins:
```
- 遍歷每一種硬幣面額。
```python
for i in range(coin, amount + 1):
```
- 嘗試用當前 coin 去更新每一個從 coin 到 amount 的金額 i。
```python 
dp[i] = min(dp[i], dp[i - coin] + 1)
```
- 對於金額 i，有兩個選擇：

    1. 不用這個硬幣 → dp[i]

    2. 用這個硬幣 → dp[i - coin] + 1（代表用掉一枚 coin 之後，剩下的部分已知最少硬幣數）

| 部分             | 意思                         |
| -------------- | -------------------------- |
| `dp[i - coin]` | 湊出金額 `(i - coin)` 需要的最少硬幣數 |
| `+ 1`          | 再加上「這次使用的這一枚硬幣」            |

- 取兩者的較小值來更新 dp[i]。
```python
return dp[amount] if dp[amount] <= amount else -1
```
- 最後，若 dp[amount] 仍然是初始的無限大（代表湊不到），回傳 -1；

- 否則回傳最少硬幣數 dp[amount]。

| 條件                     | 意義            | 動作              |
| ---------------------- | ------------- | --------------- |
| `dp[amount] <= amount` | 代表有被更新，真的湊得出  | 回傳最少硬幣數         |
| `dp[amount] > amount`  | 代表沒被更新（還是初始值） | 回傳 `-1` 表示不可能湊出 |


## 🧪 範例
```python
coins = [1, 2, 5]
amount = 11
```
### 🧮 初始 dp 陣列
```python
dp = [0, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12]
# dp[i] 表示湊出金額 i 所需的最少硬幣數
# 初始化為 amount + 1 = 12（不可能的預設值）
```
### 🪙 遍歷每一種硬幣
### 🔹 使用硬幣 1
```python
for i in range(1, 12):
    dp[i] = min(dp[i], dp[i - 1] + 1)
```
| i   | dp\[i] 更新                        |
| --- | -------------------------------- |
| 1   | dp\[1] = min(12, dp\[0] + 1) = 1 |
| 2   | dp\[2] = min(12, dp\[1] + 1) = 2 |
| 3   | dp\[3] = 3                       |
| ... | ...                              |
| 11  | dp\[11] = 11                     |

#### 🔧 dp 結果（用硬幣1後）：
```python
dp = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
```
### 🔹 使用硬幣 2
```python
for i in range(2, 12):
    dp[i] = min(dp[i], dp[i - 2] + 1)
```
| i   | dp\[i] 更新                         |
| --- | --------------------------------- |
| 2   | dp\[2] = min(2, dp\[0] + 1) = 1   |
| 3   | dp\[3] = min(3, dp\[1] + 1) = 2   |
| 4   | dp\[4] = min(4, dp\[2] + 1) = 2   |
| 5   | dp\[5] = min(5, dp\[3] + 1) = 3   |
| 6   | dp\[6] = min(6, dp\[4] + 1) = 3   |
| 7   | dp\[7] = min(7, dp\[5] + 1) = 4   |
| ... | ...                               |
| 11  | dp\[11] = min(11, dp\[9] + 1) = 6 |
#### 🔧 dp 結果（用硬幣2後）：
```python
dp = [0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6]
```
### 🔹 使用硬幣 5
```python
for i in range(5, 12):
    dp[i] = min(dp[i], dp[i - 5] + 1)
```
| i  | dp\[i] 更新                       |
| -- | ------------------------------- |
| 5  | dp\[5] = min(3, dp\[0] + 1) = 1 |
| 6  | dp\[6] = min(3, dp\[1] + 1) = 2 |
| 7  | dp\[7] = min(4, dp\[2] + 1) = 2 |
| 8  | dp\[8] = min(4, dp\[3] + 1) = 3 |
| 9  | dp\[9] = min(5, dp\[4] + 1) = 3 |
| 10 | dp\[10]= min(5, dp\[5] + 1)= 2  |
| 11 | dp\[11]= min(6, dp\[6] + 1)= 3  |

#### 🔧 最終 dp 結果：
```python
dp = [0, 1, 1, 2, 2, 1, 2, 2, 3, 3, 2, 3]
```
### 🎯 回傳結果
```python
return dp[11] = 3
```
✅ 因為可以用 5 + 5 + 1 湊成 11，共 3 枚硬幣。

---

## ⏱ 複雜度分析 | Time & Space Complexity
| 類型 | 複雜度           |
| -- | ------------- |
| 時間 | O(amount × N) |
| 空間 | O(amount)     |

### 🧠 時間複雜度 Time Complexity:

- O(n × amount)

    - n 是硬幣的種類數（len(coins)）

    - 外層跑所有 coin

    - 內層對每個 coin，從 coin 到 amount 更新 dp 陣列

### 🧠 空間複雜度 Space Complexity:

- O(amount)

    - 使用了一個大小為 amount + 1 的一維陣列 dp

---

## 📚 我學到了什麼 | What I Learned
### 中文：

- 這是一題典型的「完全背包問題」

- 善用 dp[i] = min(dp[i], dp[i - coin] + 1) 轉移公式

- 使用 amount + 1 作為不可能狀態的初始值是關鍵技巧

### English:

- Classic Unbounded Knapsack DP

- Use dp[i - coin] + 1 to build up the answer

- Using amount + 1 as a sentinel for unreachable states is an effective and widely used pattern.