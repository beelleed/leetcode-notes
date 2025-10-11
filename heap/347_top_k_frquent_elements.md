# LeetCode 347: 出現次數最多的前 K 個元素 | Top K Frequent Elements

## 🔗 題目連結 | Problem Link
- [LeetCode 347 - Top K Frequent Elements](https://leetcode.com/problems/top-k-frequent-elements/)

---

## 📖 題目說明 | Problem Description

### 中文
給你一個整數陣列 `nums` 和一個整數 `k`，請找出出現次數最多的 `k` 個元素。答案順序不限。

### English
Given an integer array `nums` and an integer `k`, return the `k` most frequent elements.  
You may return the answer in any order.

### Examples
- Example 1:

    - Input: nums = [1,1,1,2,2,3], k = 2

    - Output: [1,2]

- Example 2:

    - Input: nums = [1], k = 1

    - Output: [1]

- Example 3:

    - Input: nums = [1,2,1,2,1,2,3,1,3,2], k = 2

    - Output: [1,2]

---

## ✅ 解法一：使用 `heapq.nlargest()` | Solution 1: Built-in nlargest

### 💡 解題思路
使用 `Counter` 統計每個數字出現次數，再用 `heapq.nlargest` 根據頻率抓出前 k 項。

### 💡 Idea 
Use `collections.Counter` to count frequency, then apply `heapq.nlargest` to get the top `k` frequent items.

---

### 🔍 程式碼與註解 | Code with Explanation

```python
from collections import Counter
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)  # 統計每個元素出現的次數
        return [item for item, _ in heapq.nlargest(k, count.items(), key=lambda x: x[1])]
```
1. count = Counter(nums) 回傳一個字典：key 是數字，value 是次數

    - 作用：

        - 把 nums 中每個元素出現的次數統計成一個字典

    - 範例：
    ```python
    nums = [1, 1, 1, 2, 2, 3]
    count = Counter(nums)
    # count = {1: 3, 2: 2, 3: 1}
    ```
    - 時間複雜度： O(n)

2. heapq.nlargest(k, count.items(), key=lambda x: x[1])

    - count.items()

        - 把字典轉成「(key, value)」對

        - 範例：[(1, 3), (2, 2), (3, 1)]

3. key=lambda x: x[1]

    - 說明要根據「value（出現次數）」來做排序

4. heapq.nlargest(k, ...)

    - 幫你選出出現次數最多的前 k 個 (num, freq) 組合

    - 底層是用最小堆維護前 k 大

    - 範例：

        - heapq.nlargest(2, [(1, 3), (2, 2), (3, 1)], key=lambda x: x[1])

        - ➜ [(1, 3), (2, 2)]

    - 時間複雜度： O(n log k)

5. [item for item, _ in ...]

    - 說明：

        - 把每對 (num, freq) 裡的數字 num 抽出來

    - 結果：

        - [1, 2]

6. key=lambda x: x[1]
    - 「排序（或選擇）時，根據**每個元素的第 1 個索引（也就是第二個值）來排序」
    - 範例
        - 假設有這樣的資料：
        ```python
        data = [(1, 5), (2, 3), (3, 10)]
        ```
        想根據第二個數字（也就是 5、3、10）來排序
        - 用 key=lambda x: x[1]
        ```python
        sorted(data, key=lambda x: x[1])
        # ➜ [(2, 3), (1, 5), (3, 10)]
        ```
        - 這表示：

            - 把每個 tuple 當作 x

            - 拿 x[1]（也就是第二個值）來排序

| 表達方式                 | 意義                         |
| -------------------- | -------------------------- |
| `lambda x: x[1]`     | 對每個元素取出第 1 個 index 的值（第二欄） |
| `key=lambda x: x[1]` | 用第 2 欄的值當排序或挑選依據           |

### 📘 範例說明 | Examples
```python
nums = [1,1,1,2,2,3]
k = 2

# count = {1: 3, 2: 2, 3: 1}
# heapq.nlargest(2, [(1,3), (2,2), (3,1)]) → [(1,3), (2,2)]
# 回傳結果 → [1, 2]
```

### ⏱️ 時間與空間複雜度 | Time & Space Complexity
- Time: O(n log k)

- Space: O(n) for the frequency map

---

## ✅ 解法二：手動維護最小堆 | Solution 2: Manual Min-Heap

💡 解題思路
用 heap 維持一個大小為 k 的最小堆。當堆超過 k 時就移除最小的頻率。

💡 Idea 
Use a min-heap of size k to store top frequent elements. Pop the smallest when the heap exceeds size k.

### 🔍 程式碼與註解 | Code with Explanation
```python 
from collections import Counter
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        heap = []
        for num, freq in count.items():
            heapq.heappush(heap, (freq, num))
            if len(heap) > k:
                heapq.heappop(heap)
        return [num for freq, num in heap]
```

```python
heap = []   # 建立一個空的最小堆
```
- 這個 heap 用來儲存「前 k 多的數字」

- 裡面存的是 (次數, 數字)，排序會根據次數（預設 min-heap）

```python
for num, freq in count.items():
    heapq.heappush(heap, (freq, num))  # 把 (頻率, 數字) 放入 heap

```
- 每個 (num, freq) 都被放入 heap

- 若 heap 長度超過 k，就移除最小的（出現次數最少的）
```python
if len(heap) > k:
    heapq.heappop(heap)  # 超過 k 時移除最小頻率的元素
```
- heapq.heappop 會彈出最小的 (freq, num)

- 保證 heap 中永遠只保留 前 k 多的元素

- 時間複雜度： 每次 push/pop 是 O(log k)，共 n 次 → O(n log k)

```python
return [num for freq, num in heap]  # 回傳 heap 中的所有數字
```
- 把 (freq, num) 中的 num 抽出來

- 回傳格式是 [數字1, 數字2, ..., 數字k]

### 📍 dict.items()

在 Python 中，dict.items() 會回傳一個 (key, value) 的迭代器。
```python
print(count.items())
# dict_items([(1, 3), (2, 2), (3, 1)])
```
所以它實際上是一個 tuple list：
```python
[(1,3), (2,2), (3,1)]
```

---

### 📍 for num, freq in count.items():

這裡 Python 幫你做了 tuple 拆包 (unpacking)：

- 第一次迴圈 → (1,3) → num = 1, freq = 3

- 第二次迴圈 → (2,2) → num = 2, freq = 2

- 第三次迴圈 → (3,1) → num = 3, freq = 1

所以：

- num = 元素 (字典的 key)

- freq = 出現次數 (字典的 value)

### ✅ 總結

- Counter(nums) → {元素: 次數}

- .items() → [(元素, 次數), (元素, 次數), ...]

- for num, freq in count.items(): → Python 自動把 (key, value) 拆成兩個變數

👉 所以 num 就是元素，freq 就是它出現的次數。

### heappush 用法
```python
heapq.heappush(heap, (freq, num))
```
- heap 會根據 freq (頻率) 排序 ✅

- 例子：[(3,1), (2,2), (1,3)]

- pop 出來時，會先丟掉最小頻率的 (1,3)，保留高頻的。

### 📍 那為什麼最後 return [num for freq, num in heap]？

因為 heap 裡存的是 (freq, num)，所以：

- freq 在前，用來讓 heap 正確排序。

- num 在後，才是題目要的答案。

- 回傳時只需要 num，所以解包成 [num for freq, num in heap]。

### ✅ 總結

- heap 要依據什麼排序，就把那個放在 tuple 前面。

- 這題要依照頻率排序，所以用 (freq, num)。

- 回傳時只需要數字，所以取 [num for freq, num in heap]。

👉 換句話說，freq 在前是為了 排序，num 在後是為了 輸出。

---

### 📘 範例說明 | Examples
```python
nums = [1, 1, 1, 2, 2, 3]
k = 2

# Counter: {1: 3, 2: 2, 3: 1}
# 插入 heap:
# → [(3, 1), (2, 2), (1, 3)]
# 移除最小的：保留 (3, 1), (2, 2)
# 回傳：[1, 2]
```

### ⏱️ 時間與空間複雜度 | Time & Space Complexity
- Time: O(n log k)

- Space: O(n + k) → O(n) (map) + O(k) (heap)

---

## ✅ 解法三：桶排序 Bucket Sort | Solution 3: Bucket Sort

💡 解題思路
建立一個桶陣列，桶的索引代表出現次數，把每個數字放入對應的桶，再由高頻往下找 k 個元素。

💡 Idea
Use a list of buckets indexed by frequency. Put numbers in the corresponding bucket and collect top k from highest frequency.

### 🔍 程式碼與註解 | Code with Explanation
```python
from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        bucket = [[] for _ in range(len(nums) + 1)]

        # 把每個數字放到對應次數的桶中
        for num, freq in count.items():
            bucket[freq].append(num)

        res = []
        # 從高頻開始往下找
        for freq in range(len(bucket) - 1, 0, -1):
            for num in bucket[freq]:
                res.append(num)
                if len(res) == k:
                    return res
```

```python
bucket = [[] for _ in range(len(nums) + 1)]
```
- 建立一個 bucket 陣列，index 代表出現的「次數」

- 為什麼要長度 len(nums) + 1？

    - 最多的數字最多也只會出現 n 次（假設全都一樣）

- 範例：bucket[3] = [1]，代表數字 1 出現了 3 次

```python
for num, freq in count.items():
    bucket[freq].append(num)
```
- 把每個數字根據「出現次數」放到對應的桶裡

- 範例：如果 1 出現 3 次，就放進 bucket[3] 裡

```python
res = []
for freq in range(len(bucket) - 1, 0, -1):
```
- 從最高頻率開始往下找（因為我們要找「最常出現」的）

- 例如從 bucket[6], bucket[5], ..., bucket[1]

```python:
for num in bucket[freq]:
    res.append(num)
    if len(res) == k:
        return res
```
- 把桶裡的數字一個個加入結果

- 一旦結果中有 k 個數字，就馬上回傳（不用再繼續）

### 📘 範例說明 | Examples
```python
nums = [1, 1, 1, 2, 2, 3]
k = 2
# Counter: {1: 3, 2: 2, 3: 1}
# bucket[3] = [1]
# bucket[2] = [2]
# bucket[1] = [3]

# 從 bucket[3] 開始取：res = [1]
# bucket[2]：res = [1, 2] → 長度 = k，return [1, 2]
```
### ⏱️ 時間與空間複雜度 | Time & Space Complexity
- Time: O(n) → 一次掃 nums + 一次掃 bucket

- Space: O(n) → Counter + bucket 陣列

---

## 🧠 學到的東西 | What I Learned

中文：

- 熟悉 Counter 如何統計次數

- 學會使用 heapq 處理 top-k 類型問題

- 了解 bucket sort 的核心概念與應用場景

English:

- Learned how to use Counter for frequency mapping

- Used heapq to solve top-k problems efficiently

- Understood the use of bucket sort for optimized frequency grouping

---

## 📌 方法比較 | Method Comparison

| 方法             | 時間複雜度      | 空間複雜度 | 優點（中文）      | Advantages (EN)                     |
| -------------- | ---------- | ----- | ----------- | ----------------------------------- |
| heapq.nlargest | O(n log k) | O(n)  | 寫法簡潔，快速上手   | Simple and concise                  |
| 手動 min-heap    | O(n log k) | O(n)  | 可自訂邏輯，控制彈性  | More control, flexible              |
| Bucket Sort    | O(n)       | O(n)  | 極高效率，適合大量資料 | Best performance for large datasets |
