# 📍 LeetCode 1046 — Last Stone Weight / 最後一顆石頭的重量

🔗 [題目連結](https://leetcode.com/problems/last-stone-weight/)

---

## 📄 題目說明 | Problem Description
### 中文：

- 給定一個整數陣列 stones，每個數字代表一顆石頭的重量。
- 每一回合選擇 最重的兩顆石頭 x ≤ y，並進行粉碎：

    - 若 x == y：兩顆石頭都消失

    - 若 x < y：剩下一顆重量為 y - x 的石頭

- 重複此過程，直到剩下 0 或 1 顆石頭，回傳最後剩下的重量（或 0）。

### English:

Each turn, take the two heaviest stones and smash them together.
Return the weight of the last remaining stone, or 0 if none remain.

### Examples
- Example 1:

    - Input: stones = [2,7,4,1,8,1]
    - Output: 1
    - Explanation: 
        - We combine 7 and 8 to get 1 so the array converts to [2,4,1,1,1] then,
        - we combine 2 and 4 to get 2 so the array converts to [2,1,1,1] then,
        - we combine 2 and 1 to get 1 so the array converts to [1,1,1] then,
        - we combine 1 and 1 to get 0 so the array converts to [1] then that's the value of the last stone.
- Example 2:

    - Input: stones = [1]
    - Output: 1

---

## 🧠 解題思路 | Solution Idea
- 核心觀察

    - 每一回合都要 快速拿到目前最重的兩顆石頭

    - 這是一個典型的：

        - 反覆取最大值

        - 資料會動態改變

- 👉 非常適合使用 Heap（優先佇列）

- 為什麼用 Heap？

    - Python 的 heapq 是 Min Heap

    - 但題目需要 Max Heap

    - 解法：
        - 👉 把石頭重量取負號存進 heap

- 這樣：

    - 最重的石頭 → 最小的負數

    - heappop() 每次都能拿到「目前最重的石頭」

---

## 💻 程式碼實作 | Code (Python)
```python
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if not stones:
            return 0
        
        heap = []

        # 建立 max-heap（用負號）
        for num in stones:
            heapq.heappush(heap, -num)

        # 只要還有兩顆以上就繼續 smash
        while len(heap) >= 2:
            first = -heapq.heappop(heap)   # 最重
            second = -heapq.heappop(heap)  # 第二重
            remain = first - second

            if remain != 0:
                heapq.heappush(heap, -remain)

        # 最後可能剩 0 或 1 顆
        return -heap[0] if heap else 0
```
### 🔍 程式碼逐段說明 | Line-by-line Explanation
### 初始化 heap
```python
heap = []
```

- 使用 list 搭配 heapq

- 之後會存 負號的石頭重量

### 將所有石頭放入 heap
```python
for num in stones:
    heapq.heappush(heap, -num)
```

- 為什麼要取負號？

    - heapq 只能保證「最小值在最前面」

    - 用負號即可模擬 Max Heap

- 此時：

    - heap[0] 代表「目前最重的石頭（的負號）」

### Smash 的核心迴圈
```python
while len(heap) >= 2:
```

- 每回合需要 兩顆石頭

- heap 至少要有 2 個元素才能進行 smash

### 取出最重的兩顆
```python
first = -heapq.heappop(heap)
second = -heapq.heappop(heap)
```

- 第一次 pop：

    - 取出最小的負數 → 最大的石頭

- heapq 會自動重整 heap

- 第二次 pop：

    - 取出「剩下石頭中最重的」

- 👉 不需要自己重排 heap

### 計算剩餘重量
```python
remain = first - second
```

- 若 first == second：

    - remain = 0 → 兩顆都消失

- 若 first > second：

    - 剩下一顆重量 first - second

### 決定是否放回 heap
```python
if remain != 0:
    heapq.heappush(heap, -remain)
```

- 只有在還有剩餘石頭時才 push 回去

- 若 remain 為 0，代表兩顆石頭都消失

### 回傳結果
```python
return -heap[0] if heap else 0
```

- heap 空 → 沒有石頭 → 回傳 0

- heap 剩一顆 → 回傳該石頭重量（記得轉回正數）

---

## 🧪 範例流程 | Example Walkthrough

假設：
```text
stones = [2, 7, 4, 1, 8, 1]
```
### Step 1：建立 heap（負號）
```text
heap = [-8, -7, -4, -1, -2, -1]
```
### Step 2：第一次 smash
```python
first = 8
second = 7
remain = 1
```
```text
heap = [-4, -2, -1, -1, -1]
```
### Step 3：第二次 smash
```python
first = 4
second = 2
remain = 2
```
```text
heap = [-2, -1, -1, -1]
```
### Step 4：第三次 smash
```python
first = 2
second = 1
remain = 1
```
```text
heap = [-1, -1, -1]
```
### Step 5：第四次 smash
```python
first = 1
second = 1
remain = 0
```
```text
heap = [-1]
```
### Step 6：結束
```text
return 1
```

---

## ⏱ 複雜度分析 | Complexity Analysis

- 時間複雜度：

    - 建 heap：O(n log n)

    - 每回合 pop / push：O(log n)

    - 最多 n 次回合

    - 👉 O(n log n)

- 空間複雜度：

    - heap 最多存 n 個元素

    - 👉 O(n)

---

## ✍️ 我學到的東西 | What I Learned

- Python 的 heapq 只保證 root 是最小值

- 第二大的元素不是 heap[1]，而是靠第二次 heappop()

- heappop() 會自動重整 heap，不需要自己處理

- 看到「反覆拿最大 / 最小」→ 優先想到 heap

---

## 🧠 一句話總結

I use a max heap (implemented with negative values) to repeatedly remove the two heaviest stones. After smashing them, I push back the remaining weight if any, until at most one stone remains.