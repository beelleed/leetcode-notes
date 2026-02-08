# 📍 LeetCode 981 — Time Based Key-Value Store | 時間版本鍵值儲存

🔗[題目連結](https://leetcode.com/problems/time-based-key-value-store/)

---

## 📄 題目說明 | Problem Description
### 中文

- 你要設計一個 TimeMap，支援：

    - set(key, value, timestamp)：在某個時間存入值

    - get(key, timestamp)：取出 時間 ≤ timestamp 的最新值 如果沒有，回傳 ""

### English

Store (value, timestamp) for each key. get returns the value with the greatest timestamp ≤ given timestamp, or "" if none.

### Examples
- Example 1:

    - Input

        ["TimeMap", "set", "get", "get", "set", "get", "get"]
        
        [[], ["foo", "bar", 1], ["foo", 1], ["foo", 3], ["foo", "bar2", 4], ["foo", 4], ["foo", 5]]
    - Output
        
        [null, null, "bar", "bar", null, "bar2", "bar2"]

    - Explanation
        - TimeMap timeMap = new TimeMap();
        - timeMap.set("foo", "bar", 1);  // store the key "foo" and value "bar" along with timestamp = 1.
        - timeMap.get("foo", 1);         // return "bar"
        - timeMap.get("foo", 3);         // return "bar", since there is no value corresponding to foo at timestamp 3 and timestamp 2, then the only value is at timestamp 1 is "bar".
        - timeMap.set("foo", "bar2", 4); // store the key "foo" and value "bar2" along with timestamp = 4.
        - timeMap.get("foo", 4);         // return "bar2"
        - timeMap.get("foo", 5);         // return "bar2"

---

## 🧠 解題思路 | Solution Idea

- store[key] 是一個 list

- list 裡放 (timestamp, value)

- 因為題目保證同一個 key 的 timestamp 會遞增，所以 list 天然有序

- get 時用 binary search 找到：

    - 「最後一個 timestamp ≤ target 的位置」

---

## 💻 程式碼實作 | Code (Python)
```python
from collections import defaultdict
from typing import List
import bisect

class TimeMap:

    def __init__(self):
        self.store = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.store:
            return ""

        arr = self.store[key]

        # 找到第一個 timestamp > target 的位置
        idx = bisect.bisect_right(arr, (timestamp, chr(127))) - 1

        if idx >= 0:
            return arr[idx][1]
        return ""
```

### 1️⃣ 初始化資料結構
```python
self.store = defaultdict(list)
```

- store 是一個字典

- 每個 key 對應一個 list

- defaultdict(list) 的好處：第一次用 store[key] 時自動給空 list，不用先判斷 key 存不存在（你的 set 就吃到這個好處）

### 2️⃣ set：直接 append
```python
self.store[key].append((timestamp, value))
```

- 把 (timestamp, value) 加進 list

- 題目保證 timestamp 對同 key 遞增，所以：

    - append 之後 list 仍然是排序好的

    - 不用 sort

### 3️⃣ get：key 不存在直接回空字串
```python
if key not in self.store:
    return ""
```

- 如果從來沒有 set 過這個 key，就沒有答案

### 4️⃣ 取出該 key 的時間序列
```python
arr = self.store[key]
```

- arr 會長這樣：
```text
[(1, "bar"), (4, "bar2"), (10, "x"), ...]
```
### 5️⃣ 核心：用 bisect_right 找位置
```python
idx = bisect.bisect_right(arr, (timestamp, chr(127))) - 1
```
- ✅ bisect_right 在做什麼？

    - bisect_right(arr, target) 會回傳：

        - target 如果要插入 arr（保持排序），應該插在「最右邊」的位置

- 這裡的目標是：

    - 找到「最後一個 timestamp ≤ target」

- 方法就是：

    1. 先找「第一個 timestamp > target」的插入位置

    2. 再往左退一格（-1）就是 timestamp ≤ target 的最大那個

### 6️⃣ 為什麼 target 要寫 (timestamp, chr(127))？

- 因為 arr 裡的元素是 tuple (timestamp, value)，Python 會用 tuple lexicographic compare：

    - 先比第一個（timestamp）

    - timestamp 一樣才比第二個（value）

```python
(timestamp, chr(127))
```

- 意思是：

    - 我希望在 timestamp 相同時，插入點要在「同 timestamp 的最右邊」

    - chr(127) 是一個很大的字元，讓 (timestamp, chr(127)) 比 (timestamp, "任何一般字串") 都大 → bisect_right 會插在同 timestamp 的最後面

### 7️⃣ idx >= 0 才代表有找到合法答案
```python
if idx >= 0:
    return arr[idx][1]
return ""
```

- idx == -1 代表：

    - target 比 arr 裡最小 timestamp 還小

    - 沒有任何 timestamp ≤ target

    - 所以回傳 ""

- idx >= 0：

    - arr[idx] 就是最新且不超過 timestamp 的那筆

    - 回傳它的 value（tuple 的第 2 個）

---

## 🧪 範例流程 | Example Walkthrough

- 假設操作：
```text
set("foo", "bar", 1)
set("foo", "bar2", 4)
```

此時：
```text
arr = [(1, "bar"), (4, "bar2")]
```
### get("foo", 3)

- target = (3, chr(127))

- bisect_right(arr, target) 會回傳插入位置 1（因為 3 應該插在 (1) 後面、(4) 前面）

- idx = 1 - 1 = 0

- 回傳 arr[0][1] = "bar"

✅ 正確

### get("foo", 4)

- target = (4, chr(127))

- bisect_right 會回傳 2（插在所有 timestamp=4 的最右邊）

- idx = 2 - 1 = 1

- 回傳 arr[1][1] = "bar2"

✅ 正確

### get("foo", 0)

- bisect_right 回 0

- idx = -1 → 回 ""

✅ 正確

---

## ⏱ 複雜度分析 | Complexity Analysis

- 時間複雜度 | Time Complexity

    - set(key, value, timestamp)

        - 時間複雜度：O(1)

        - 原因：

            - 對應 key 的 list 直接 append

            - 題目保證 timestamp 遞增，不需要排序

    - get(key, timestamp)

        - 時間複雜度：O(log n)

        - 原因：

            - 對該 key 的時間序列做 binary search（bisect_right）

            - n 為該 key 底下儲存的時間筆數

- 空間複雜度 | Space Complexity

    - 空間複雜度：O(N)

    - 說明：

        - N 為所有 set 操作的總數

        - 每次 set 都會在 store 中存一筆 (timestamp, value)

        - 所有歷史版本都會被保留

---

## ✍️ 我學到的東西 | What I Learned

- 題目關鍵保證：「同一 key 的 timestamp 遞增」

    - → list 保持排序

    - → get 用二分搜

- bisect_right(...) - 1 是常用技巧：

    - 「找最後一個 ≤ target」

---

## 🧠 一句話總結

I store (timestamp, value) pairs for each key in a sorted list and use bisect_right to find the latest timestamp not exceeding the query time.