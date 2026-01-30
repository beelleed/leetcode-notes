# 📍 LeetCode 973 — K Closest Points to Origin / 最接近原點的 K 個點

🔗 [題目連結](https://leetcode.com/problems/word-ladder/)

---

## 📄 題目說明 | Problem Description

### 中文：
給定一個二維平面上的點集合 points，其中每個點為 [x, y]，以及一個整數 k。
請找出距離原點 (0,0) 最近的 k 個點，回傳順序不限。

### English:
Given an array of points where points[i] = [xi, yi], return the k points closest to the origin (0,0). The distance between two points is the Euclidean distance. You may return the answer in any order.

### Examples
- Example 1:

    ![](../images/973_closestplane1.jpg)
    
    - Input: points = [[1,3],[-2,2]], k = 1
    - Output: [[-2,2]]
    - Explanation:
        - The distance between (1, 3) and the origin is sqrt(10).
        - The distance between (-2, 2) and the origin is sqrt(8).
        - Since sqrt(8) < sqrt(10), (-2, 2) is closer to the origin.
        - We only want the closest k = 1 points from the origin, so the answer is just [[-2,2]].
- Example 2:

    - Input: points = [[3,3],[5,-1],[-2,4]], k = 2
    - Output: [[3,3],[-2,4]]
    - Explanation: The answer [[-2,4],[3,3]] would also be accepted.
 

---

## 🧠 解題思路 | Solution Idea（完全對應你的程式碼）

- 核心想法是：

    - 我們只關心「距離最近的 k 個點」

    - 不需要把所有點都排序（那會是 O(n log n)）

    - 只要維持一個大小為 k 的 heap

    - heap 裡永遠存「目前最接近的 k 個點」

- 為什麼用 Heap？

    - 每加入一個新點：

        - 如果 heap 還沒滿 k → 直接放

        - 如果 heap 滿了 →

            - 把「目前最遠的那個點」踢掉

    - 最後 heap 裡留下來的，就是答案

---

## 💻 程式碼實作 | Code (Python)
```python
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        result = []
        for x, y in points:
            dist = x * x + y * y
            heapq.heappush(heap, (-dist, x, y))
            if len(heap) > k:
                heapq.heappop(heap)
        for item in heap:
            dist, x, y = item
            result.append([x, y])
        return result
```
### 🔍 程式碼逐段說明 | Line-by-line Explanation
```python
heap = []
result = []
```

- heap：用來維持「距離最近的 k 個點」

- result：最後要回傳的答案

```python
for x, y in points:
```
等價於：
```python
for point in points:
    x = point[0]
    y = point[1]
```
👉 這叫做 tuple / list unpacking（解包）

- 只要右邊「每個元素的長度 = 左邊變數個數」，就可以這樣寫。

- 逐一走訪每一個點

- 每個點是一個狀態 (x, y)
```python
dist = x * x + y * y
```

- 計算該點到原點的距離平方

- 不需要開根號

    - 因為距離比較只看大小

    - √d1 < √d2 ⇔ d1 < d2

```python
heapq.heappush(heap, (-dist, x, y))
```

- Python 的 heapq 是 Min Heap

- 但我們想要的是：

    - 「距離最遠的點」能最快被踢掉

- 所以：

    - 把距離取負號 -dist

    - 模擬 Max Heap

- 此時 heap 的意義是：

    - heap[0] 永遠是「目前 heap 裡最遠的點」
```python
if len(heap) > k:
    heapq.heappop(heap)
```

- 一旦 heap 超過 k 個元素

- 就把「最遠的那個點」移除

- 這樣 heap 大小永遠 ≤ k

- 為什麼 pop 掉的是最遠的？

    - 因為 heap 存的是：
    ```text
    (-distance, x, y)
    ```

    - distance 越大 → -distance 越小

    - Min Heap 會先 pop -distance 最小的

    - 等價於 pop「距離最大的點」
```python
for item in heap:
    dist, x, y = item
    result.append([x, y])
```
- heap 裡的每一個元素都是一個 tuple
- 這裡的 item 就是：
```python
item = (-dist, x, y)
```

再把它「解包」成：
```python
dist = item[0]
x    = item[1]
y    = item[2]
```

所以可以直接寫成一行（功能完全一樣）：
```python
for _, x, y in heap:
    result.append([x, y])
```
👉 _ 表示「我不要這個值」

- heap 裡剩下的，就是距離最近的 k 個點

- 不需排序，直接收集即可
```python
return result
```

- 回傳任意順序都可（題目允許）

#### 🔁 原本寫法（較直觀）
```python
result = []
for item in heap:
    dist, x, y = item
    result.append([x, y])
return result
```
#### ✅較 Pythonic
```python
return [[x, y] for (_, x, y) in heap]
```
- heap 中的每個元素格式為 (−distance, x, y)

- −distance 僅用於 heap 比較，不影響輸出結果

- 使用 list comprehension 搭配 tuple unpacking：

    - _ 表示忽略不使用的值

    - 只取出 x, y 組成輸出

- 程式碼更簡潔，語意也更清楚

---

## 🧪 範例流程 | Example Walkthrough
假設：
```text
points = [[1,3], [-2,2], [5,8], [0,1]]
k = 2
```
### Step 1：處理 [1,3]

- dist = 1² + 3² = 10

- heap = [(-10, 1, 3)]

### Step 2：處理 [-2,2]

- dist = 8

- heap = [(-10,1,3), (-8,-2,2)]

- heap size = 2 → OK

### Step 3：處理 [5,8]

- dist = 89

- push → heap = [(-89,5,8), (-8,-2,2), (-10,1,3)]

- heap size = 3 > k

- pop → 移除 (-89,5,8)

👉 最遠的點被踢掉

### Step 4：處理 [0,1]

- dist = 1

- push → heap = [(-10,1,3), (-8,-2,2), (-1,0,1)]

- size > k → pop (-10,1,3)

heap 最終內容
```text
(-8, -2, 2)
(-1,  0, 1)
```

→ 對應點：

```text
[-2,2], [0,1]
```

---

## ⏱ 複雜度分析 | Complexity Analysis

- 時間複雜度：

    - 每個點最多一次 push + pop

    - heap size ≤ k

    - 👉 O(n log k)

- 空間複雜度：

    - heap 最多存 k 個元素

    - 👉 O(k)

---

## ✍️ 我學到的東西 | What I Learned

- Python 的 heapq 只有 Min Heap

- 想要 Max Heap → 把比較值取負號

- 維持大小為 k 的 heap，可以避免全排序

- 只要題目出現：

    - 「Top K」

    - 「K 個最大 / 最小」

    - 「資料量很大」

👉 優先想到 Heap

---

## 🧠 一句話總結

I maintain a max heap of size k using a min heap with negative distances.
Whenever the heap exceeds size k, I remove the farthest point, so the heap always contains the k closest points seen so far.