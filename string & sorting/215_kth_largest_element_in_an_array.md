# LeetCode 215: Kth Largest Element in an Array | 找出陣列中的第 k 大元素

## 🔗 Problem Link 題目連結
- [LeetCode 215 - Kth Largest Element in an Array](https://leetcode.com/problems/kth-largest-element-in-an-array/)

---

## 📖 Problem Description 題目描述

**English**  
Find the k-th largest element in an unsorted array.  
Note that it is the k-th largest element in **sorted order**, not the k-th distinct element.

**中文**  
在未排序的陣列中找出第 k 大的元素。  
請注意：這裡的「第 k 大」是指**排序後的位置**，而不是第 k 個不同的數字。

---

## ✅ (不符合題意) 解法一：排序法 | Solution 1: Sorting 

### 💡 解題思路 | Idea

**中文**  
- 將整個陣列做降序排序。
- 回傳排序後的第 `k - 1` 個元素（索引從 0 開始）。

**English**  
- Sort the entire array in descending order.
- Return the element at index `k - 1`.

### 🔍 程式碼 | Python Code 

```python
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums.sort(reverse=True)
        return nums[k - 1]
```

## ⏱️ 時間與空間複雜度 | Time and Space Complexity 
- Time Complexity（時間複雜度）: O(N log N) – due to sorting

- Space Complexity（空間複雜度）: O(1) – in-place sort

---

## ✅ 解法二：最小堆法 | Solution 2: Min Heap 

### 解題思路 | Idea

**中文** 
- 使用「最小堆」維持目前最大的前 k 個元素。

- 對每個數字都加入堆中。

- 若堆的大小超過 k，則移除堆頂（最小值）。

- 最後堆頂就是第 k 大的數字。

**English** 
- Use a min-heap to keep track of the largest k elements.

- For each number, push it into the heap.

- If the heap size exceeds k, pop the smallest.

- The top of the heap is the k-th largest element.

### 🔍 程式碼 | Python Code 
```python
import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []

        for num in nums:
            heapq.heappush(heap, num)
            if len(heap) > k:
                heapq.heappop(heap)

        return heap[0]
```
#### 🧠 解釋逐行邏輯：

1️⃣ for num in nums:
- 意義： 依序讀取陣列 nums 中的每個元素 num

- 目標： 處理所有數字，並用 heap 保留「目前最大的 k 個數字」

2️⃣ heapq.heappush(heap, num)
- 動作： 將 num 加入 heap 中

- 特性： heapq 是 最小堆（min-heap）：

    - heap[0] 會一直是目前 heap 中最小的數字

- 目標： 動態加入數字到堆中

3️⃣ if len(heap) > k:
- 檢查： 堆的大小是否超過 k

- 為什麼？

    - 我們只需要保留「最大的 k 個數」

    - 超過 k，就說明要淘汰掉其中「最小的那個」

4️⃣ heapq.heappop(heap)
- 動作： 把最小的元素（heap[0]）移除

- 效果：

    - 這樣堆中永遠只保留「目前最大的前 k 個數字」

5️⃣ return heap[0]
- 回傳： heap 中最小的元素（也是第 k 大的數）

- 為什麼？

    - 堆中有 k 個最大值，而其中最小的那個 = 排名第 k 的數

#### 📌 例子說明：
```python
nums = [3, 2, 1, 5, 6, 4]
k = 2
```
- 經過這段程式碼後，heap 中會只剩下 [5, 6]

- heap[0] = 5 → 就是第 2 大的元素 ✅

---

## ⏱️ 時間與空間複雜度 | Time and Space Complexity 
- Time Complexity（時間複雜度）: O(N log k) – insertion into heap

- Space Complexity（空間複雜度）: O(k) – heap size is k

---

## 🧠 我學到的東西 | What I Learned 

**中文** 
- 理解了排序法與最小堆法的差異。

- 當資料量大且 k 小時，用「最小堆」效能更佳。

- 學會使用 Python 的 heapq 來操作優先佇列。

**English** 
- The difference between sorting-based and heap-based approaches.

- Using a min-heap is more efficient for large datasets when k is small.

- How to use heapq in Python to implement a priority queue.

---

## 📌 總結 | Summary 
| Method 方法    | Time 時間複雜度 | Space 空間複雜度 | 適用場景      |
| ------------ | ---------- | ----------- | --------- |
| Sorting 排序法  | O(N log N) | O(1)        | 小量資料、簡單寫法 |
| Min Heap 最小堆 | O(N log k) | O(k)        | 大量資料、高效需求 |
