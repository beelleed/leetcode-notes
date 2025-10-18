# 121. Best Time to Buy and Sell Stock | 最佳買賣股票時機

[Leetcode 121](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/)

---

## 📘 題目說明 | Problem Description

### **中文：**  
  給定一個整數陣列 `prices`，其中 `prices[i]` 表示第 i 天的股票價格。你只能進行 **一次買入和一次賣出**，且必須在買入之後才賣出（不能同一天操作）。請計算可獲得的最大利潤，若無法獲利則回傳 `0`。

### **English:**  
  Given an integer array `prices`, where `prices[i]` is the stock price on day `i`, you are allowed to complete at most **one** transaction (buy one and sell one share of stock). Return the maximum profit you can achieve. If no profit is possible, return `0`.

### Examples

- Example 1:

    - Input: prices = [7,1,5,3,6,4]
    - Output: 5
    - Explanation: 
        - Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
        - Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
- Example 2:

    - Input: prices = [7,6,4,3,1]
    - Output: 0
    - Explanation: In this case, no transactions are done and the max profit = 0.

---

##  💡 解題思路 | Solution Idea

### 中文思路：
1. 使用兩個變數：
   - `min_price`：把當前見過的最低價格記下來（代表理想的買入成本）
   - `max_profit`：當前能獲得的最大利潤
2. 遍歷 `prices` 陣列：
   - 更新 `min_price = min(min_price, price)`
   - 更新 `max_profit = max(max_profit, price - min_price)`
3. 最終 `max_profit` 即為最大可得利潤，若始終無正利，則為 `0`。

### English Explanation:
1. Track two values:
   - `min_price`: the lowest price seen so far (best day to buy)
   - `max_profit`: maximum profit achievable up to current day
2. Iterate over `prices`:
   - Update `min_price` using the lowest seen so far
   - Compute current profit `price - min_price` and update `max_profit` if larger
3. The result is `max_profit` (0 if no profit possible)

---

##  Python 程式碼 | Code

```python
from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float('inf')
        max_profit = 0

        for price in prices:
            min_price = min(min_price, price)           # 更新最低買入價
            max_profit = max(max_profit, price - min_price)  # 計算賣出 profit

        return max_profit
```
```python
min_price = float('inf')
```
- 初始化：
    - min_price 設為「無限大」：代表目前還沒買股票，要找到最低的買入價。
```python
max_profit = 0
```
🔹 初始化最大利潤為 0（因為可能無法賺錢，只能賺 0）。
```python
for price in prices:
```
🔁 遍歷每天的股票價格。
```python
min_price = min(min_price, price)
```
- 更新目前為止看過的「最低價格」。

    - 這代表「如果今天之前就買了股票，最低成本是多少？」
```python
max_profit = max(max_profit, price - min_price)
```
- 嘗試在今天賣出：

    - price - min_price 就是「今天賣出」能得到的利潤。

    - 看看這筆利潤是不是目前為止最大。
```python
return max_profit
```
✅ 回傳整個過程中找到的最大利潤。

---

## 🧪 範例模擬

假設 prices = [7, 1, 5, 3, 6, 4]
| Day | price | min\_price | price - min\_price | max\_profit |
| --- | ----- | ---------- | ------------------ | ----------- |
| 0   | 7     | 7          | 0                  | 0           |
| 1   | 1     | 1 ✅        | 0                  | 0           |
| 2   | 5     | 1          | 4 ✅                | 4           |
| 3   | 3     | 1          | 2                  | 4           |
| 4   | 6     | 1          | 5 ✅                | 5           |
| 5   | 4     | 1          | 3                  | 5           |

🟢 回傳結果：5

### ✅ 核心觀念

- 保留目前為止的「最低價格」

- 每天試著當作賣出日，計算利潤

- 每次更新最大利潤

---

## ⏱ 時間與空間複雜度 | Complexity
| 項目    | 複雜度             |
| ----- | --------------- |
| 時間複雜度 | `O(n)` — 單次遍歷   |
| 空間複雜度 | `O(1)` — 只用兩個變數 |

---

## ✅ 我學到了什麼 | What I Learned
### 中文：

- 解這題的核心是用 在遍歷中保持「最低買入價」，同時更新最大利潤，不需要使用兩層迴圈。

- 這是一個典型的 greedy + 一次掃描 問題，是許多類似題目的入門模板。

- 一旦你懂用「最低價 + 實時計算利潤」的方式，面對更多 variant 的股票題型（例如可多次交易、加 cooldown 等）都能延伸思考。

### English:

- The key insight is maintaining a running minimum buy price and updating profit in real-time—no need for nested loops.

- This is a classical example of a greedy + one-pass solution, and a pattern frequent in many related problems.

- Once comfortable with this "min price + instant profit calculation" idea, you can generalize to variants like multiple transactions, cooldowns, or transaction fees.