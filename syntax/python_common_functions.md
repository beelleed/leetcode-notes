# 🧠 Python 演算法常見 10 個內建函式 + 實戰應用表
## 1️⃣ abs(x) — 取絕對值（去掉負號）

📘 用途： 比較差距、距離、誤差，不管方向。
📍 你會看到它在： 幾何題、移動距離題。
```python
# LeetCode 1266. Minimum Time Visiting All Points
time = max(abs(x2 - x1), abs(y2 - y1))
```

---

## 2️⃣ max(a, b, ...) — 取最大值
## 3️⃣ min(a, b, ...) — 取最小值

📘 用途： 兩值比較時最直覺的選擇。
📍 你會看到它在： 動態規劃、雙指標、子陣列問題。
```python
# LeetCode 53. Maximum Subarray
max_sum = max(nums[i], max_sum + nums[i])

# LeetCode 121. Best Time to Buy and Sell Stock
profit = max(profit, price - min_price)
```

## 4️⃣ sum(iterable) — 求和

📘 用途： 計算總和、前綴和、滑動視窗。
📍 常見在： 陣列總和、統計題。
```python
# LeetCode 724. Find Pivot Index
if sum(nums[:i]) == sum(nums[i+1:]):
    return i
```

---

## 5️⃣ sorted(iterable, key=..., reverse=...) — 排序

📘 用途： 按某個規則排序。
📍 你會看到它在： 排序 + 雙指標 / 貪婪題。
```python
# LeetCode 56. Merge Intervals
intervals = sorted(intervals, key=lambda x: x[0])
```

- 🎯 key=...：定義「排序依據」
    🔹 範例 1：根據字串長度排序

        ```python
        words = ["apple", "pie", "banana"]
        sorted(words, key=len)
        # → ['pie', 'apple', 'banana']
        ```

    🔹 範例 2：根據 tuple 的第二個值排序

        ```python
        pairs = [(1, 3), (2, 2), (3, 1)]
        sorted(pairs, key=lambda x: x[1])
        # → [(3, 1), (2, 2), (1, 3)]

        # 這裡的 lambda x: x[1] 意思是：「用每個 tuple 的第二個值（索引 1）來排序。」
        ```
    
    🔹 範例 3：根據出現次數排序（搭配 Counter）
        
        ```python
        from collections import Counter
        nums = [1,1,2,3,3,3]
        count = Counter(nums)
        sorted(count.items(), key=lambda x: x[1], reverse=True)
        # → [(3, 3), (1, 2), (2, 1)]
        ```
    
- 🎯 reverse=：是否反轉（由大到小）

預設是 False（由小到大）。
設成 True 則是由大到小排序。

    🔹 範例 1：

        ```python
        nums = [5, 2, 9]
        sorted(nums, reverse=True)
        # → [9, 5, 2]
        ```

    🔹 範例 2：結合 key

        ```python
        words = ["apple", "pie", "banana"]
        sorted(words, key=len, reverse=True)
        # → ['banana', 'apple', 'pie']
        ```


---

## 6️⃣ enumerate(iterable) — 同時取出索引和元素

📘 用途： 你需要同時知道「第幾個」與「它是什麼」。
📍 你會看到它在： 字串 / 陣列滑動題。
```python
for i, ch in enumerate(s):
    print(i, ch)  # 索引 + 值
```

---

## 7️⃣ zip(a, b, ...) — 把多個列表「綁」在一起

📘 用途： 同時走訪兩個序列。
📍 你會看到它在： 配對題、矩陣操作。
```python
# 例子：把兩個 list 合併成一組組 tuple
for name, score in zip(names, scores):
    print(name, score)
```

---

## 8️⃣ all(iterable) / any(iterable)

📘 用途：

- all-()：全部都 True → 回傳 True

- any()：有一個 True → 回傳 True
📍 你會看到它在： 判斷條件題。
```python
nums = [2, 4, 6]
print(all(n % 2 == 0 for n in nums))  # True (全部偶數)
```

---

## 9️⃣ len(obj) — 取長度

📘 用途： 幾乎所有題的基本函式。
📍 你會看到它在： 陣列、字串、滑動視窗、動態規劃。
```python
while right < len(s):
    ...
```

## 🔟 range(start, stop, step) — 建立迴圈範圍

📘 用途： 控制 for 迴圈的索引。
📍 你會看到它在： 幾乎每個演算法的 for-loop。
```python
for i in range(len(nums) - 1, -1, -1):
    ...
```

---

## 🌟 額外推薦：常用搭配組合
| 組合                          | 作用         | 範例                         |
| --------------------------- | ---------- | -------------------------- |
| `max(a, b, c)`              | 找最大三值      | `max(dp[i-1], dp[i-2], 0)` |
| `sorted(arr, reverse=True)` | 從大排到小      | 排名題                        |
| `sum(nums[i:j])`            | 子陣列總和      | 滑動視窗                       |
| `enumerate(zip(a,b))`       | 同時取兩個陣列和索引 | 比對兩筆資料                     |
| `any(x > 0 for x in nums)`  | 是否有正數      | 條件判斷                       |
