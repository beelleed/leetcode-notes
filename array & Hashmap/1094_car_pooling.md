# 📍 LeetCode 1094 — Car Pooling | 拼車載客（差分 / Sweep Line）

🔗 [題目連結](https://leetcode.com/problems/car-pooling/)

---

## 📄 題目說明 | Problem Description
### 中文

- 你有一台車，容量是 capacity

- 給你 trips，每筆是 [numPassengers, from, to]

    - from：上車地點（含）

    - to：下車地點（不含，到了 to 乘客就不在車上）

- 車子沿著地點數字由小到大行駛

- 問：是否能完成所有行程，且任何時刻車上人數不超過 capacity？

### English

Given trips [passengers, start, end), check if the car’s passenger count ever exceeds capacity while moving along increasing locations.

### Examples
- Example 1:

    - Input: trips = [[2,1,5],[3,3,7]], capacity = 4
    - Output: false
- Example 2:

    - Input: trips = [[2,1,5],[3,3,7]], capacity = 5
    - Output: true

---

## 🧠 看到這題為什麼會想到「差分 / Sweep Line」？
- ✅ 這題的核心不是路徑，是「人數變化」

- 每個 trip 其實只有兩個事件：

    - 在 from：人數 +numPassengers

    - 在 to：人數 -numPassengers

- 我們不需要模擬每一段路坐了誰，只需要知道：

    - 每個地點「上下車」造成的人數變化，然後累加看會不會爆容量

- 這就是典型的 差分（difference array）/ 掃描線（sweep line）。

---

## 💻 程式碼實作 | Code (Python)（程式碼範例）
```python
from typing import List

class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        diff = [0] * 1001  # locations are within 0..1000

        for passengers, start, end in trips:
            diff[start] += passengers
            diff[end] -= passengers

        curr = 0
        for x in diff:
            curr += x
            if curr > capacity:
                return False

        return True
```

### 1️⃣ 建立差分陣列 diff
```python
diff = [0] * 1001
```

- diff[i] 表示：在地點 i 這一站，乘客數量會「改變多少」

- 這題地點範圍通常在 0..1000（題目約束）

- 所以直接開 1001 長度最簡單

### 2️⃣ 把每筆 trip 轉成兩個事件（上車 + 下車）
```python
for passengers, start, end in trips:
    diff[start] += passengers
    diff[end] -= passengers
```

- 對每個 trip [passengers, start, end]：

    - 在 start 站：乘客上車 → +passengers

    - 在 end 站：乘客下車 → -passengers

- ⚠️ 為什麼 end 是減？
    - 因為題目是 [start, end)：到 end 的時候，人已經不在車上了。

### 3️⃣ 掃描所有地點，累加得到「當下車上總人數」
```python
curr = 0
for x in diff:
    curr += x
    if curr > capacity:
        return False
```

- curr 表示：目前車上乘客總數

- curr += x：把該站的上下車變化加進來

- 每一站都檢查一次是否超過 capacity

    - 只要某一站超過 → 立刻回 False

### 4️⃣ 全部掃完都沒爆容量 → 回 True
```python
return True
```

---

## 🧪 範例流程 | Example Walkthrough

### Example 1
```text
trips = [[2,1,5],[3,3,7]]
capacity = 4
```
### Step 1：建立 diff（初始全 0）
```text
diff[0..] 全是 0
```
### Step 2：處理第一筆 [2,1,5]
```python
diff[1] += 2
diff[5] -= 2
```

- 表示：

    - 站 1 上車 2 人

    - 站 5 下車 2 人

### Step 3：處理第二筆 [3,3,7]
```python
diff[3] += 3
diff[7] -= 3
```

- 表示：

    - 站 3 上車 3 人

    - 站 7 下車 3 人

### Step 4：開始掃描 diff，計算 curr

只列出會變動的站：

| 站點 i | diff[i] | curr（累加後） | 是否 > capacity=4 |
| ---- | ------: | --------: | --------------- |
| 0    |       0 |         0 | 否               |
| 1    |      +2 |         2 | 否               |
| 2    |       0 |         2 | 否               |
| 3    |      +3 |         5 | ✅ 是 → 回 False   |

所以答案是 False。

### Example 2
```text
trips = [[2,1,5],[3,5,7]]
capacity = 4
```

- 事件：

    - 站 1：+2

    - 站 5：-2（第一筆下車） +3（第二筆上車） → diff[5] = +1

    - 站 7：-3

- 掃描關鍵站：

| 站點 i | diff[i] | curr |
| ---- | ------: | ---: |
| 1    |      +2 |    2 |
| 5    |      +1 |    3 |
| 7    |      -3 |    0 |

- curr 最大只有 3 ≤ 4 → 回 True

---

## ⏱ 複雜度分析 | Complexity Analysis 
### 時間複雜度 | Time Complexity

- 建 diff：O(T)（T = trips 數量）

- 掃描地點：O(1001)（常數上限）

- 總時間：O(T + 1000)，通常簡寫成 O(T)

### 空間複雜度 | Space Complexity

- diff 長度 1001：O(1000)（常數）

- 總空間：O(1)（以題目範圍固定來看）

---

## ✍️ 我學到的東西 | What I Learned

- 題目重點不是「路怎麼走」，而是「每站上下車造成的人數變化」

- 看到這種格式 [num, start, end)：

    - start 加

    - end 減

    - 再做 prefix sum（累加）

- 這是差分陣列的典型用法

---

## 🧠 一句話總結

I record passenger changes at each location using a difference array, then sweep through locations with a running sum to ensure it never exceeds capacity.