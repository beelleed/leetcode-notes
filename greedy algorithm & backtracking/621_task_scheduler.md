# 📍 LeetCode 621 — Task Scheduler / 任務調度器

🔗 [題目連結](https://leetcode.com/problems/task-scheduler/)

---

## 📄 題目說明 | Problem Description
### 中文：

- 給定一個任務列表 tasks，每個任務用一個大寫字母表示。
- 同一種類的任務之間必須至少間隔 n 個時間單位。

- 每個時間單位只能執行一個任務或 idle。
- 請回傳完成所有任務所需的 最少時間單位數。

### English:

Given a list of tasks and a non-negative integer n representing the cooldown period,
return the minimum number of time units needed to finish all tasks.

### Examples
- Example 1:

    - Input: tasks = ["A","A","A","B","B","B"], n = 2

    - Output: 8

    - Explanation: A possible sequence is: A -> B -> idle -> A -> B -> idle -> A -> B.

        - After completing task A, you must wait two intervals before doing A again. The same applies to task B. In the 3rd interval, neither A nor B can be done, so you idle. By the 4th interval, you can do A again as 2 intervals have passed.

- Example 2:

    - Input: tasks = ["A","C","A","B","D","B"], n = 1

    - Output: 6

    - Explanation: A possible sequence is: A -> B -> C -> D -> A -> B.

        - With a cooling interval of 1, you can repeat a task after just one other task.

- Example 3:

    - Input: tasks = ["A","A","A", "B","B","B"], n = 3

    - Output: 10

    - Explanation: A possible sequence is: A -> B -> idle -> idle -> A -> B -> idle -> idle -> A -> B.

        - There are only two types of tasks, A and B, which need to be separated by 3 intervals. This leads to idling twice between repetitions of these tasks.

---

## 🔁 第一種解法 Greedy
### 🧠 解題思路 | Solution Idea（核心觀念）
- 關鍵觀察

    - 題目沒有要求真的排出順序

    - 只問：最少需要幾個時間單位

    - 冷卻時間的瓶頸 來自「出現最多次的任務」

👉 本題本質是 貪心 + 數學下界問題

---

## 🧠 核心概念 | Key Insight

- 影響答案的只有三個數：

    1. maxFreq：出現次數最多的任務出現了幾次

    2. maxCount：有幾個任務的出現次數 = maxFreq

    3. len(tasks)：任務總數

---

## 🧩 框架（Skeleton）思維

假設出現最多的是任務 A，出現 maxFreq 次：
```text
A _ _   A _ _   A _ _   ...   A
```

- 相同任務之間必須隔 n 個時間單位

- 一共有 maxFreq - 1 個間隔

- 每個間隔長度至少是 n

👉 先建立一個「最小不可突破的時間框架」

### 🧮 框架下界怎麼算？
### Step 1：每一段的長度

每一段可視為：
```text
[A + n 個空位]
```
### Step 2：段數
```text
maxFreq - 1
```
### Step 3：最後一段

- 如果有多個任務都達到 maxFreq（例如 A、B、C）
- 最後一段需要放 maxCount 個任務

### 🔢 框架下界公式
```text
(min_time_by_cooldown)
= (maxFreq - 1) * (n + 1) + maxCount
```
### ❓ 為什麼還要跟 len(tasks) 取 max？

- 如果其他任務很多，可以把所有空位補滿

- 根本不需要 idle

- 此時最少時間就是 任務總數

👉 真正答案是兩個下界的最大值：
```text
answer = max(
    (maxFreq - 1) * (n + 1) + maxCount,
    len(tasks)
)
```

---

## 💻 程式碼實作 | Code (Python)
```python
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)

        maxFreq = max(count.values())
        maxCount = sum(1 for v in count.values() if v == maxFreq)

        return max((maxFreq - 1) * (n + 1) + maxCount, len(tasks))
```
### 🔍 程式碼逐段說明 | Line-by-line Explanation（公式解）
```python
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
```

- 定義 leastInterval 函式

- tasks：任務列表

- n：同一任務之間的冷卻時間
```python
count = Counter(tasks)
```

- 使用 Counter 統計每個任務出現的次數

- 得到一個 dictionary：
    ```text
    任務 → 出現次數
    ```
- 假設：
    ```text
    tasks = ["A","A","A","B","B","B","C"]
    ```

- 那：
    ```text
    count = {
    "A": 3,
    "B": 3,
    "C": 1
    }
    ```

count.values() 就是：
```text
[3, 3, 1]
```
```python
maxFreq = max(count.values())
```

- 找出「出現次數最多」的任務

- maxFreq 代表：任何一個任務最多被執行了幾次

- 這個值決定了排程的最小骨架長度
```python
maxCount = sum(1 for v in count.values() if v == maxFreq)
```

- 計算有多少個任務的出現次數等於 maxFreq

#### v == maxFreq

假設你前面算出：
```python
maxFreq = 3
```

那條件：
```python
v == maxFreq
```

意思是：「 這個任務的出現次數，是不是等於 3？」

####  1 for v in count.values() if v == maxFreq

- 這是一個 generator expression，意思是：

    - 每遇到一個 v == maxFreq

    - 就產生一個 1

- 對上面的例子：
```text
v = 3  → 產生 1
v = 3  → 產生 1
v = 1  → 不產生
```
#### sum(...)

最後：
```python
sum(1, 1) = 2
```

所以：
```python
maxCount = 2
```

👉 表示 有 2 個任務（A 和 B）都出現了最多次 3 次


- 這代表在最後一段排程中，需要放入 maxCount 個任務
```python
return max((maxFreq - 1) * (n + 1) + maxCount, len(tasks))
```
- 這一行是整題的核心公式
#### 🔹 第一部分：
```text
(maxFreq - 1) * (n + 1) + maxCount
```

- (maxFreq - 1)：

    - 出現最多的任務之間，形成的間隔數量

- (n + 1)：

    - 每個間隔至少需要 1 個任務 + n 個冷卻時間

- + maxCount：

    - 最後一排需要放入所有出現次數同為 maxFreq 的任務

👉 這是「冷卻時間所造成的最小時間下界」

#### 🔹 第二部分：
```text
len(tasks)
```

- 任務總數

- 如果其他任務足夠填滿所有冷卻空位

- 就不需要任何 idle

- 此時最少時間 = 任務數量本身

#### 🔹 為什麼取 max？

- 有時冷卻時間會造成 idle（第一項較大）

- 有時任務夠多，不需要 idle（第二項較大）

👉 真正答案是兩個下界的最大值

---

## 🧪 範例流程 | Example Walkthrough
- Example 1
```text
tasks = ["A","A","A","B","B","B"]
n = 2
```

- maxFreq = 3

- maxCount = 2

- len(tasks) = 6

框架下界：
```text
(3 - 1) * (2 + 1) + 2 = 8
```

答案：
```text
max(8, 6) = 8
```
- Example 2（種類多但仍需要 idle）
```text
tasks = ["A","A","A","A","B","C","D"]
n = 2
```

- maxFreq = 4

- maxCount = 1

- len(tasks) = 7
```text
(4 - 1) * (2 + 1) + 1 = 10
```

👉 即使種類多，最多的任務仍然決定瓶頸

---

## ⏱ 複雜度分析 | Complexity Analysis

- 時間複雜度：

    - Counter 掃描一次 tasks

    - 👉 O(n)

- 空間複雜度：

    - Counter 儲存任務次數

    - 👉 O(1)（任務種類最多 26 個）

---

## ✍️ 我學到的東西 | What I Learned

- 這題不是排程題，而是「算下界」的問題

- 真正造成 idle 的不是種類數，而是 最大出現次數

- 不需要 heap，反而公式更乾淨、風險更低

- 題目問「最少時間」→ 想下界，而不是模擬

---

## 🧠 一句話總結（面試用）

The most frequent tasks determine the scheduling skeleton,
and the answer is the maximum between this cooldown-based lower bound and the total number of tasks.

---

## 🔁 第二種解法 Heap + Cooldown Queue 模擬法

### 🧠 解題想法 | Idea

- 每一個時間單位只能執行一個任務或 idle

- 每個任務執行後，需要等待 n 個時間單位才能再次被執行

- 我們需要 動態選擇「目前可以執行且剩餘次數最多的任務」

- 👉 關鍵工具：

    1. Max Heap：隨時拿到剩餘次數最多的任務

    2. Queue（Cooldown Queue）：暫存還在冷卻中的任務

    3. Time Simulation：一格一格模擬時間前進

---

## 🧩 資料結構設計 | Data Structures
### 1️⃣ Max Heap（用負號）
```text
heap = [(-freq, task)]
```

- 存「還可以執行的任務」

- 每次 pop 都拿到剩餘次數最多的任務

### 2️⃣ Cooldown Queue
```text
queue = deque([(ready_time, -freq, task)])
```

- ready_time：此任務最早什麼時候可以再執行

- 任務冷卻結束後，會被丟回 heap

### 3️⃣ Time
```text
time = 0
```

- 每次 loop 代表一個時間單位

### 🔄 模擬流程 | Simulation Loop

- 在每一個時間單位，我們都做三件事：

#### Step 1️⃣：處理冷卻完成的任務

- 若 queue 的最前面任務 ready_time == time

- 把它放回 heap（代表現在可以再執行）

#### Step 2️⃣：執行任務（若可能）

- 如果 heap 不空：

    - pop 一個任務執行一次（freq - 1）

    - 若該任務還有剩餘次數：

        - 丟進 cooldown queue

        - ready_time = time + n + 1

- 如果 heap 為空：

    - 代表只能 idle（但 time 仍然前進）

#### Step 3️⃣：時間前進
```text
time += 1
```

---

## 💻 程式碼實作 | Code (Python)
```python
from typing import List
from collections import Counter, deque
import heapq

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)

        # max heap: store (-freq, task)
        heap = [(-freq, task) for task, freq in count.items()]
        heapq.heapify(heap)

        # cooldown queue: (ready_time, -freq, task)
        cooldown = deque()

        time = 0

        while heap or cooldown:
            time += 1

            # 1) if the front task in cooldown is ready, move it back to heap
            if cooldown and cooldown[0][0] == time:
                ready_time, freq, task = cooldown.popleft()
                heapq.heappush(heap, (freq, task))

            # 2) execute one task if available
            if heap:
                freq, task = heapq.heappop(heap)  # freq is negative
                freq += 1  # one execution done: e.g., -3 -> -2

                # if still remaining, push it into cooldown
                if freq != 0:
                    cooldown.append((time + n + 1, freq, task))

        return time

```
### 🔍 程式碼逐段說明 | Line-by-line Explanation
#### 統計任務次數
```python
count = Counter(tasks)
```

- 例如 ["A","A","A","B","B","B"]

- count = {"A": 3, "B": 3}

#### 建 max heap（用負號）
```python
heap = [(-freq, task) for task, freq in count.items()]
heapq.heapify(heap)
```

- heapq 只能做 min-heap

- 用 -freq 讓「freq 最大」的任務變成「最小的負數」，優先被 pop

例如：
```text
[(-3, 'A'), (-3, 'B')]
```
#### cooldown queue 記錄不能用的任務
```python
cooldown = deque()
```

裡面每個元素格式：
```text
(ready_time, -freq, task)
```

- ready_time：最早可以再被執行的時間（這裡就是面試最好講的點）

- -freq：剩餘次數（仍用負號）

- task：任務字母

#### time 代表目前時間（從 1 開始跑）
```python
time = 0
while heap or cooldown:
    time += 1
```

- 每次迴圈代表「過了一個時間單位」

- 只要還有任務未完成（在 heap 或 cooldown），就繼續

#### Step 1：冷卻結束的任務回到 heap
```python
if cooldown and cooldown[0][0] == time:
    ready_time, freq, task = cooldown.popleft()
    heapq.heappush(heap, (freq, task))
```

- 如果 queue 最前面那個任務的 ready_time == time

- 代表它冷卻完成了，現在可以重新被執行

- 把它丟回 heap，變成候選任務

✅ 面試小提醒：更嚴謹可用 while，但這個版本已經很清楚。

#### Step 2：執行 heap 裡剩餘次數最多的任務
```python
if heap:
    freq, task = heapq.heappop(heap)
    freq += 1
```

- pop 出 freq 最小（最負）的 → 原本 freq 最大的任務

- freq += 1 是因為 freq 是負號 例如 -3 + 1 = -2，代表還剩 2 次

#### 如果還沒做完，放入 cooldown
```python
if freq != 0:
    cooldown.append((time + n + 1, freq, task))
```
- ⭐ 這裡是面試最容易講的點

    - 如果你在 time = t 執行任務 X

    - 冷卻要求：中間要有 n 個時間單位不能做 X

    - 所以 X 最早可再執行時間是：
```text
t + n + 1
```

- 例如 n = 2：

    - t+1、t+2 不能做

    - t+3 才能做

- 所以直接寫 time + n + 1 最直覺、最不會被追問。

#### return time
```python
return time
```

- 當 heap 與 cooldown 都空

- 代表所有任務都完成

- time 就是總花費時間

---

## 🧪 範例流程 | Example Walkthrough
- Example
```text
tasks = ["A","A","A","B","B","B"]
n = 2
```

- 初始：

    - heap: [(-3,A), (-3,B)]

    - cooldown: []

    - time = 0


### time = 1

1. cooldown 回收：無

2. heap pop：做 A（-3 → -2）

3. A 放 cooldown：ready_time = 1 + 2 + 1 = 4

    - heap: [(-3,B)]

    - cooldown: [(4,-2,A)]

### time = 2

1. cooldown 回收：無（4 != 2）

2. heap pop：做 B（-3 → -2）

3. B 放 cooldown：ready_time = 2 + 2 + 1 = 5

    - heap: []

    - cooldown: [(4,-2,A), (5,-2,B)]

### time = 3

1. cooldown 回收：無（4 != 3）

2. heap 空 → idle

    - heap: []

    - cooldown: [(4,-2,A), (5,-2,B)]

### time = 4

1. cooldown 回收：A 回 heap

2. heap pop：做 A（-2 → -1）

3. A 放 cooldown：ready_time = 4 + 2 + 1 = 7

    - heap: []

    - cooldown: [(5,-2,B), (7,-1,A)]

### time = 5

1. cooldown 回收：B 回 heap

2. heap pop：做 B（-2 → -1）

3. B 放 cooldown：ready_time = 5 + 2 + 1 = 8

    - heap: []

    - cooldown: [(7,-1,A), (8,-1,B)]

### time = 6

- heap 空 → idle

### time = 7

- 回收 A → 做 A（-1 → 0）→ 不再放回

### time = 8

- 回收 B → 做 B（-1 → 0）→ 不再放回

- heap & cooldown 都空 → 結束

✅ 回傳 time = 8

---

## ⏱ 複雜度分析 | Complexity

- heap 裡最多 26 種任務

- 每次執行涉及 pop/push（log 26 幾乎常數）

- 時間複雜度：O(T log 26) ≈ O(T)（T 包含 idle）

- 空間：O(26)

---

## 🤔 什麼時候用這個方法？
- ✅ 適合用 Heap 模擬法的情況

    - 題目要求 輸出實際執行順序

    - 每個任務有不同 cooldown

    - 任務有執行時間 / 權重

    - 題目規則會變動（公式不再適用）

- ❌ 本題為什麼不推薦當主解？

    - 題目只問「最少時間」

    - 公式解更短、更穩、錯誤率低

---

## 🧠 一句話總結（Heap 版）

I simulate the scheduling process using a max heap to always pick the task with the highest remaining count and a queue to handle cooldowns.