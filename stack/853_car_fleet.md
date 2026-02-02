# 📍 LeetCode 853 — Car Fleet / 車隊

🔗 [題目連結](https://leetcode.com/problems/car-fleet/)

---

## 📄 題目說明 | Problem Description
### 中文：

- 有 n 台車在同一條單向道路上，終點位置為 target。
- 第 i 台車的起始位置為 position[i]，速度為 speed[i]。

    - 所有車同時朝終點行駛

    - 車不能超車

    - 若後車在終點前追上前車，兩車會合併成一個「車隊（fleet）」

    - 合併後車隊的速度由 最慢的車 決定

- 請回傳最後到達終點的 車隊數量。

### English:

- Cars are driving toward a target. Faster cars cannot pass slower cars ahead.
- If a car catches up to a car in front, they form a fleet and travel together.
Return the number of car fleets that arrive at the target.
### Examples
- Example 1:

    - Input: target = 12, position = [10,8,0,5,3], speed = [2,4,1,1,3]

    - Output: 3

    - Explanation:

        - The cars starting at 10 (speed 2) and 8 (speed 4) become a fleet, meeting each other at 12. The fleet forms at target.
        - The car starting at 0 (speed 1) does not catch up to any other car, so it is a fleet by itself.
        - The cars starting at 5 (speed 1) and 3 (speed 3) become a fleet, meeting each other at 6. The fleet moves at speed 1 until it reaches target.
- Example 2:

    - Input: target = 10, position = [3], speed = [3]

    - Output: 1

    - Explanation:

        - There is only one car, hence there is only one fleet.
- Example 3:

    - Input: target = 100, position = [0,2,4], speed = [4,2,1]

    - Output: 1

    - Explanation:

        - The cars starting at 0 (speed 4) and 2 (speed 2) become a fleet, meeting each other at 4. The car starting at 4 (speed 1) travels to 5.
        - Then, the fleet at 4 (speed 2) and the car at position 5 (speed 1) become one fleet, meeting each other at 6. The fleet moves at speed 1 until it reaches target.

---

## 🧠 方法一: 解題思路 | Solution Idea
- 核心觀察

    - 不需要模擬車子怎麼開

    - 只要判斷一件事：

        - 後面的車，能不能在終點前追上前面的車？

- 關鍵轉換

    - 對每台車計算「到終點所需時間」：

        - time = (target - position) / speed

---

## 🧠 方法一: 核心策略 | Key Strategy

1. 依 position 由大到小排序（越靠近終點的車先看）

2. 從前往後掃描：

    - 如果後車到終點的時間 ≤ 前方車隊的時間 → 一定追得上 → 合併成同一個 fleet

    - 如果 > 前方車隊的時間 → 追不上 → 形成新的 fleet

---

## 💡 方法一: 關鍵直覺（很重要）

- 一個 fleet 的到達時間，取決於 裡面最慢的那台車

- 從靠近終點的車往後看，車隊的「到達時間」會是 單調遞增

- 👉 所以其實不一定要真的用 stack
- 👉 用一個變數記住「目前車隊的最大時間」就夠了

---

## 💻 方法一: 程式碼實作 | Code (Python)
```python
from typing import List

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # 將車子依照位置由大到小排序（靠近終點先處理）
        cars = sorted(zip(position, speed), reverse=True)

        fleets = 0
        cur_time = 0.0  # 目前前方車隊到終點所需時間（最慢）

        for p, s in cars:
            time = (target - p) / s
            # 若這台車無法追上前方車隊，形成新車隊
            if time > cur_time:
                fleets += 1
                cur_time = time
            # 否則 time <= cur_time，會追上並合併，不增加 fleet

        return fleets
```
## 🔍 程式碼逐段說明 | Line-by-line Explanation
```python
cars = sorted(zip(position, speed), reverse=True)
```

- 將 (position, speed) 配對

- 依照 position 由大到小排序

- 確保 先處理靠近終點的車
```python
fleets = 0
cur_time = 0.0
```

- fleets：目前車隊數量

- cur_time：前方車隊到終點所需的最慢時間
```python
for p, s in cars:
    time = (target - p) / s
```

- 計算該車單獨到終點的時間
```python
if time > cur_time:
```

- 代表這台車 追不上前方車隊

- 必須形成一個新的 fleet
```python
fleets += 1
cur_time = time
```

- 新增一個車隊

- 更新目前車隊的到達時間（之後的車都要跟它比）
```python
# else: time <= cur_time
```

- 表示這台車可以在終點前追上前車

- 會被迫減速 → 合併成同一個車隊

- 不增加 fleet 數量

---

## 🧪 範例流程 | Example Walkthrough
### Input
```text
target = 12
position = [10, 8, 0, 5, 3]
speed    = [2,  4, 1, 1, 3]
```
### Step 1：計算到終點時間
| 位置 | 速度 | 時間 |
| -- | -- | -- |
| 10 | 2  | 1  |
| 8  | 4  | 1  |
| 5  | 1  | 7  |
| 3  | 3  | 3  |
| 0  | 1  | 12 |

### Step 2：依位置由大到小處理

- (10,2) → time=1

    - 1 > 0 → 新 fleet（fleets=1, cur_time=1）

- (8,4) → time=1

    - 1 <= 1 → 追上 → 合併

- (5,1) → time=7

    - 7 > 1 → 新 fleet（fleets=2, cur_time=7）

- (3,3) → time=3

    - 3 <= 7 → 合併

- (0,1) → time=12

    - 12 > 7 → 新 fleet（fleets=3）

### ✅ 最終答案
```text
3
```

---

## ⏱ 方法一: 複雜度分析 | Complexity Analysis

- 時間複雜度：

    - 排序：O(n log n)

    - 單次掃描：O(n)

    - 👉 總計：O(n log n)

- 空間複雜度：

    - 排序所需額外空間

    - 👉 O(n)

---

## ✍️ 方法一: 我學到的東西 | What I Learned

- 這題不需要模擬車子實際移動

- 關鍵在於「到終點所需時間」的比較

- 從靠近終點的車往後看，問題會變得單調

- 看起來像 stack 題，但其實只需要一個變數

---

## 🧠 一句話總結

A new car fleet is formed only when a car cannot catch up to the fleet in front before reaching the target.

---

## 🧠 方法二: 解題思路 | Solution Idea（Stack 視角）
- 核心觀察（非常重要）

    - 每台車可以先獨立計算「到終點需要多久」

    - 一個車隊的到達時間，取決於 裡面最慢的那台車

    - 從「離終點最近的車」往後看，
車隊的到達時間會呈現 單調遞增

- 👉 這正是 單調 stack（Monotonic Stack） 的典型應用。

---

## 🧠 方法二: Stack 在這題扮演的角色

- stack 裡存的不是車子

- 而是「車隊到達終點的時間」

- stack 維持的性質是：stack 從底到頂，時間是遞增的

---

## 🧮 方法二: 關鍵轉換 | Key Transformation

- 對每台車計算「到終點所需時間」：

    - time = (target - position) / speed

- 這個 time 就是 stack 中要比較的關鍵值。

---

## 💻 方法二: 程式碼實作 | Code (Python, Stack)
```python
from typing import List

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # 1. 依位置由大到小排序（靠近終點先處理）
        cars = sorted(zip(position, speed), reverse=True)

        stack = []  # stack 裡存的是「到終點所需時間」

        for p, s in cars:
            time = (target - p) / s
            stack.append(time)

            # 2. 若後車追得上前車，合併成同一個 fleet
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()  # 後車被前車吸收，移除

        return len(stack)
```
## 🔍 程式碼逐段說明 | Line-by-line Explanation
```python
cars = sorted(zip(position, speed), reverse=True)
```

- 把 (position, speed) 配對

- 依 position 由大到小排序

- 為什麼？

    - 因為靠近終點的車，一定是先形成車隊的基準
```python
stack = []
```

- stack 裡存的是：每一個「已形成車隊」的到達終點時間

- stack 的長度 = 目前車隊數量
```python
time = (target - p) / s
```

- 假設這台車「自己一個人」開到終點

- 需要多久時間
```python
stack.append(time)
```

- 先假設：
    - 👉 這台車會形成一個新的 fleet

- 所以先放進 stack
```python
if len(stack) >= 2 and stack[-1] <= stack[-2]:
```

- 這一行是整題的 靈魂判斷。

- 在問什麼？

    - stack[-1]：後面那台車（或新加入的車）

    - stack[-2]：前方那個 fleet

- 若：後車到終點時間 ≤ 前車到終點時間


- 代表：

    - 後車速度比較快

    - 一定能在終點前追上前車

    - 會被迫減速 → 合併成同一個 fleet
```python
stack.pop()
```

- 把後車那個 time 移除

- 因為：

    - 它不會形成新的 fleet

    - 它被吸收到前一個 fleet
```python
return len(stack)
```

- stack 裡剩下的每一個 time

- 就代表一個獨立的車隊

---

## 🧪 範例流程 | Example Walkthrough
### Input
```text
target = 12
position = [10, 8, 0, 5, 3]
speed    = [2,  4, 1, 1, 3]
```
### Step 1：計算並排序

- 依 position 由大到小：

| 車 | 位置 | 速度 | time |
| - | -- | -- | ---- |
| A | 10 | 2  | 1    |
| B | 8  | 4  | 1    |
| C | 5  | 1  | 7    |
| D | 3  | 3  | 3    |
| E | 0  | 1  | 12   |

### Step 2：依序處理 stack
#### A（time=1）
```text
stack = [1]
```
#### B（time=1）
```text
stack = [1, 1]
1 <= 1 → 合併 → pop
stack = [1]
```
#### C（time=7）
```text
stack = [1, 7]
7 > 1 → 新 fleet
```
#### D（time=3）
```text
stack = [1, 7, 3]
3 <= 7 → 合併 → pop
stack = [1, 7]
```
#### E（time=12）
```text
stack = [1, 7, 12]
12 > 7 → 新 fleet
```
#### ✅ 最終 stack
```text
[1, 7, 12]
```
👉 車隊數量 = 3

---

## ⏱ 方法二: 複雜度分析 | Complexity Analysis

- 時間複雜度：

    - 排序：O(n log n)

    - 單次掃描 + stack 操作：O(n)

    - 👉 總計：O(n log n)

- 空間複雜度：

    - stack 最多存 n 個時間

    - 👉 O(n)

---

## 🧠 Stack 解法的本質理解（筆記用）

- stack 維持的是「車隊到終點的最慢時間」

- 一旦後車能追上前車：

    - 後車的 time 就沒有意義

- 這是一題 單調遞增 stack（Monotonic Increasing Stack）

---

## ✍️ 我學到的東西 | What I Learned

- 853 可以用 stack 解

- 但 stack 裡存的是「時間」，不是車

- 本質是在維持單調性

- stack 版可以再壓縮成 O(1) 變數解

---

## 🧠 一句話總結

Cars form a new fleet only when their arrival time is strictly greater than the fleet ahead; otherwise, they merge.