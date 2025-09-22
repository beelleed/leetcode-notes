# 📊 LeetCode 239 – Sliding Window Maximum
🔗 題目連結 | Problem Link: [https://leetcode.com/problems/sliding-window-maximum/](https://leetcode.com/problems/sliding-window-maximum/)

---

## 📄 題目說明 | Problem Description

- **中文**：給定整數陣列 `nums` 和一個滑動視窗大小 `k`，這個視窗從陣列最左邊移動到最右邊，每次移動一步。每個視窗的當下包含 `k` 個元素，求每一個視窗的最大值，回傳這些最大值組成的陣列。  
- **English**: Given an integer array `nums` and a window size `k`, there is a sliding window which moves from the very left of the array to the very right. You can only see the `k` numbers inside the window at any time. Each time the window moves right by one, return the maximum value in the current window. Produce an array of these maximums.

- **Examples**:
    - Example 1:

        - Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
        - Output: [3,3,5,5,6,7]
        - Explanation: 
        ```markdown
        Window position                Max
        ---------------               -----
        [1  3  -1] -3  5  3  6  7       3
        1 [3  -1  -3] 5  3  6  7       3
        1  3 [-1  -3  5] 3  6  7       5
        1  3  -1 [-3  5  3] 6  7       5
        1  3  -1  -3 [5  3  6] 7       6
        1  3  -1  -3  5 [3  6  7]      7
        ```

    - Example 2:

        - Input: nums = [1], k = 1
        - Output: [1]

---

## 🧠 解題思路 | Solution Ideas

有幾種方法可以做這題：

### 方法一：Brute‑Force（暴力法）

- 滑動視窗每移動一步就檢查該 window 裡所有 `k` 個元素，找出最大值。  
- 時間複雜度是 `O(n * k)`，n = `nums.length`。當 `n` 和 `k` 都大時會太慢。

### 方法二：使用 Priority Queue（最大堆 / 堆 + 索引）

- 用 max‑heap（或 Python 與 `heapq` 結合負值 trick／儲值＋索引）來維持當前視窗元素。  
- 當滑窗移動時，把新元素加入 heap，同時把過期（離開視窗範圍）的元素從 heap 中彈掉。  
- 對每個視窗位置，heap 的頂端是最大值。  
- 時間複雜度約 `O(n log k)`。

### 方法三（最佳）：使用 Monotonic Deque（單調雙端佇列）

- 用一個雙端佇列存儲「可能成為窗口中最大值的元素索引」，並維持其內部對應值是**從大到小排列**（從前端到後端）。  
- 每次滑動窗口，加一個新元素：從 deque 後端去掉所有比新元素小的元素（因為這些小的元素不可能在往後 window 中成為最大值）。  
- 當視窗左邊移出一個元素時，如果該元素的索引正是 deque 的前端，就把它 `popleft()`。  
- 當視窗已經滿 `k` 大小時，把 deque 的前端（最大值）放入結果陣列。  
- 時間複雜度 `O(n)`，空間複雜度 `O(k)`。

---

## 💻 最優方案程式碼（Python + Deque）

```python
from collections import deque
from typing import List

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        dq = deque()  # 存放 **索引**，對應 nums 的值會單調遞減
        res = []
        for i, num in enumerate(nums):
            # 移除 deque 前端中已經離開 window 的索引
            if dq and dq[0] < i - k + 1:
                dq.popleft()

            # 移除 deque 後端所有對應值比 nums[i] 小的索引
            while dq and nums[dq[-1]] < num:
                dq.pop()

            # 把當前索引加入 deque
            dq.append(i)

            # 只有當 i >= k - 1，window 完整時才記錄最大值
            if i >= k - 1:
                res.append(nums[dq[0]])

        return res
```
```python
from collections import deque
from typing import List

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        dq = deque()  # 存放 **索引**，對應 nums 的值會單調遞減
        res = []
```
- 用 deque (雙端佇列) 存放「索引」而不是存放值。

- dq 用來維持一條「可能為窗口最大值候選」的索引隊列，其對應的 nums 值從前到後是單調遞減（大 → 小 → …）。

- res 用來儲存每個滿窗口的最大值。
```python
for i, num in enumerate(nums):
```
- 用 i 是目前遍歷到的索引，num = nums[i] 是當前值。
```python
if dq and dq[0] < i - k + 1:
    dq.popleft()
```
- 當窗口從左邊滑動時，某些索引會變得不再屬於當前窗口（過期）。

- 當 dq[0]（隊首）索引小於 i - k + 1，意味它已經不在當前窗口內，應該被移除。
```python
while dq and nums[dq[-1]] < num:
    dq.pop()
```
- 新進的元素 num 如果比現有隊列在尾端的那些元素值大，那些小的元素不可能在以後的窗口中成為最大值（因為 num 一旦進來，它會比它們後面較早失效或被擠出窗口時還大）。

- 所以把這些小的值對應的索引從尾端 pop 出去。
```python
dq.append(i)
```
- 把目前索引 i 推進隊尾。
```python
if i >= k - 1:
    res.append(nums[dq[0]])
```
- 當 i >= k - 1 時，表示從第 i - k + 1 到 i 的那個窗口是第一個「完整」窗口。

- 此時，隊首 dq[0] 對應的 nums[dq[0]] 是當前窗口內最大的元素，因為隊列是單調遞減的，所以前端永遠是最大值。
```python
return res
```
- 回傳所有窗口的最大值陣列。

---

## 🧪 實例流程對照

假設：
```ini
nums = [1, 3, -1, -3, 5, 3, 6, 7]
k = 3
```
| i | num\[i] | dq（存索引）                                                                   | 說明                               | 當 i ≥ k−1 時 res 增加哪個值             |
| - | ------- | ------------------------------------------------------------------------- | -------------------------------- | --------------------------------- |
| 0 | 1       | \[0]                                                                      | 加索引 0                            | —                                 |
| 1 | 3       | pop 因為 nums\[0]<3 → `[]` → append 1 → \[1]                                | 移除小值 1 的索引                       | —                                 |
| 2 | −1      | \[1,2]                                                                    | 新元素 −1 比末端的小的沒有 → append         | i=2 ≥2 → res.append(nums\[1]) = 3 |
| 3 | −3      | \[1,2,3]                                                                  | 移除過期索引？隊首 1 不過期                  | res.append(nums\[1]) = 3          |
| 4 | 5       | pop 尾端 −3, −1, pop 2 → pop 1（因為 nums\[1]<5） → then \[ ] → append 4 → \[4] | 新元素 5 很大，把後面小的都移除                | res.append(nums\[4]) = 5          |
| 5 | 3       | \[4,5]（索引 4,5 → 值 5,3）                                                    | nums\[4]=5≥3 保留，append 5 →\[4,5] | res.append(nums\[4]) = 5          |
| 6 | 6       | pop 5（nums\[5]<6），pop 4（nums\[4]<6） → then \[] → append 6 → \[6]          | 新元素 6 把前面小的都落後                   | res.append(nums\[6]) = 6          |
| 7 | 7       | similarly → \[7]                                                          | 新元素 7 更大                         | res.append(nums\[7]) = 7          |

最後 res = [3,3,5,5,6,7]

---

## ⏱ 時間 & 空間複雜度分析 | Time & Space Complexity

- 時間複雜度 (Time Complexity)：O(n)，因為每個元素的索引只會被 append 一次，也只會被 pop（從後端或前端）最多一次。整體操作為線性的。

- 空間複雜度 (Space Complexity)：O(k)，deque 最壞情況存放最多 k 個索引。

---

## ✍️ 我學到了什麼 | What I Learned

- 單調雙端佇列（Monotonic Deque / Monotonic Queue）是處理滑動視窗最大／最小問題的常見且高效的工具。

- 要維持「單調遞減隊列」：新的元素若比隊尾小的都 pop 掉，因為這些小的元素在未來窗口中永遠不會成為最大。

- 使用索引而非值，可以知道哪些元素已經過期（不在當前視窗中）。

- 在面試中講這題時，要清楚交代為什麼 pop 後端、為什麼 pop 前端、以及什麼時候開始 append 到結果（i >= k‑1）。