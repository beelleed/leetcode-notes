# 📈 300. Longest Increasing Subsequence | 最長遞增子序列
[LeetCode 題目連結](https://leetcode.com/problems/longest-increasing-subsequence/)

---

## 🧩 題目說明 | Problem Description

- **中文：**  
  給定一個整數陣列 `nums`，請找出其中最長的 **嚴格遞增子序列** 長度。這個子序列中的元素 **不必是連續的**，但必須維持原始順序。

- **English:**  
  Given an integer array `nums`, return the length of the longest strictly increasing subsequence. The subsequence doesn’t have to be contiguous, but must preserve the original order.

### Examples
- Example 1:

    - Input: nums = [10,9,2,5,3,7,101,18]
    - Output: 4
    - Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.

- Example 2:

    - Input: nums = [0,1,0,3,2,3]
    - Output: 4

- Example 3:

    - Input: nums = [7,7,7,7,7,7,7]
    - Output: 1

---

## 🧠 解題思路 | Solution Ideas

### ✅ 方法一：動態規劃（DP） — O(n²)
- 建立陣列 `dp`，其中 `dp[i]` 表示以 `nums[i]` 結尾的 LIS 長度。
- 初始化 `dp[i] = 1`，因為每個元素至少能形成長度為 1 的子序列。
- 對於每個 `i`（從 1 到 n-1）逐一檢查所有 `j < i`：
  - 若 `nums[j] < nums[i]`，表示可以接在遞增序列後：  
    `dp[i] = max(dp[i], dp[j] + 1)`
- 最後答案為 `max(dp)`。

### 📌 程式碼：

```python
from typing import List

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0
        n = len(nums)
        dp = [1] * n
        for i in range(1, n):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)
```
```python
n = len(nums)
```
- 取出陣列長度，方便後續使用。
```python
dp = [1] * n
```
- 建立一個長度為 n 的 DP 陣列，初始值都設為 1。

- dp[i] 表示：以 nums[i] 作為結尾的最長遞增子序列的長度。

- 為什麼一開始都是 1？因為每個數字至少可以自己單獨成一個子序列。
```python
for i in range(1, n):
```
- 從頭到尾檢查每個數字 nums[i]，假設它是子序列的最後一個數字。
```python
for j in range(i):
```
- 用另一個指標 j 從 0 到 i-1，檢查在 nums[i] 之前的所有數字。
```python
if nums[j] < nums[i]:
```
- 如果前面的數字 nums[j] 小於現在的 nums[i]，表示 nums[i] 可以接在 nums[j] 後面 成為一個遞增子序列。
```python
dp[i] = max(dp[i], dp[j] + 1)
```
- 如果 nums[j] < nums[i]，表示我們可以考慮從 dp[j] 接續到 i，更新 dp[i] 為：

    - 原本的 dp[i]（可能是 1 或其他）

    - 或是 dp[j] + 1（從 j 接過來）

- 取兩者最大值。
```python
return max(dp)
```
- 最後，回傳整個 dp 陣列中最大值，也就是整個陣列的 最長遞增子序列長度。

### 🧪 範例演練

以 nums = [10, 9, 2, 5, 3, 7, 101, 18] 為例：
#### 📐 初始狀態

- dp = [1, 1, 1, 1, 1, 1, 1, 1] 每個位置初始化為 1（自己本身就是長度為 1 的遞增子序列）

#### 🔄 執行過程（逐步）
- i = 0

    - 無前面的數字可比，略過。

- i = 1

    - j = 0 → 9 < 10 ❌ 不成立
      ➜ dp[1] = 1

- i = 2

    - j = 0 → 2 < 10 ❌ 不成立

    - j = 1 → 2 < 9 ❌ 不成立
      ➜ dp[2] = 1

- i = 3（5）

    - j = 0 → 5 < 10 ❌

    - j = 1 → 5 < 9 ❌

    - j = 2 → 5 > 2 ✅ → dp[3] = max(1, 1+1) = 2
      ➜ dp[3] = 2

- i = 4（3）

    - j = 0 → 3 < 10 ❌

    - j = 1 → 3 < 9 ❌

    - j = 2 → 3 > 2 ✅ → dp[4] = max(1, 1+1) = 2

    - j = 3 → 3 < 5 ❌
      ➜ dp[4] = 2

- i = 5（7）

    - j = 0 ~ 1 ~ 2 → 皆不成立

    - j = 3 → 7 > 5 ✅ → dp[5] = max(1, 2+1) = 3

    - j = 4 → 7 > 3 ✅ → dp[5] = max(3, 2+1) = 3
      ➜ dp[5] = 3

- i = 6（101）

    - 最長可以接在 7（dp[5]=3）後面 → dp[6] = 4

- i = 7（18）

    - 最長可以接在 7（dp[5]=3）後面 → dp[7] = 4
```
最後得到：
```text
dp = [1, 1, 1, 2, 2, 3, 4, 4]
```
最大值是 4，所以答案是 4

- 最長遞增子序列長度為 4，對應序列可能是：

    - [2, 3, 7, 101]

    - [2, 3, 7, 18]

    - 或其他同樣長度的組合

---

### ⚡ 方法二：二分搜尋優化 — O(n log n)

- 建立一個 tails 陣列表示長度為 i+1 的遞增序列的最小結尾數字。

- 使用 bisect_left 找到可以替換的位置，確保結尾越小越好（未來可延伸性高）。

### 📌 程式碼：
```python
from bisect import bisect_left

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        tails = []
        for num in nums:
            idx = bisect_left(tails, num)
            if idx == len(tails):
                tails.append(num)
            else:
                tails[idx] = num
        return len(tails)
```
```python
from bisect import bisect_left
```
- 匯入 bisect_left，用來在排序列表中找插入點。
```python
tails = []
```
- 用來儲存每個長度的 LIS 尾端值，維持遞增且「越小越好」。
```python
for num in nums:
```
- 逐個檢查輸入數字。
```python
idx = bisect_left(tails, num)
```
- 在 tails 中找到第一個「大於等於 num」的 index。

- 意思是：num 可以當作這個長度子序列的更優結尾。

- idx = bisect_left(a, x)
    | 參數    | 說明                         |
    | ----- | -------------------------- |
    | `a`   | **已排序的 list**（必須是遞增序列）     |
    | `x`   | 想要插入的新值                    |
    | `idx` | 傳回「應插入的索引位置」，以保持 `a` 的遞增順序 |
    - Example
        ```python
        from bisect import bisect_left

        a = [1, 3, 5, 7]
        x = 4

        idx = bisect_left(a, x)
        print(idx)  # 👉 2
        ```
        - 插入 x=4 應該放在索引 2（介於 3 和 5 之間）
        - 因為 a[2] = 5 是第一個 ≥ 4 的位置。
```python
if idx == len(tails):
    tails.append(num)
```
- 如果 num 比 tails 中所有數字都大，就延長子序列長度，加入新一層。
    - Example
        ```python
        tails = [2, 5, 7]
        num = 8
        ```
        - bisect_left(tails, 8) → 會回傳 idx = 3，
        - 因為 8 比所有元素都大，應該放在最後一位（索引 3）。
        - idx == len(tails) 的意義
        
        | 條件                  | 意思                        | 動作                  |
        | ------------------- | ------------------------- | ------------------- |
        | `idx == len(tails)` | `num` 比 tails 中所有元素都大     | `tails.append(num)` |
        | `idx < len(tails)`  | 有更大的數存在，找到第一個 ≥ `num` 的位置 | `tails[idx] = num`  |

```python
else:
    tails[idx] = num
```
- 否則替換掉位置 idx 上的數字，表示「用一個更小的值更新 LIS 的尾端」。
```python
return len(tails)
```
- tails 的長度就是 LIS 的最大長度。

### 🧪 範例步驟

以 nums = [10,9,2,5,3,7,101,18] 為例：
#### 🔁 第一次：num = 10

- tails = []

- bisect_left([], 10) → idx = 0

- idx == len(tails) → tails.append(10)

- ✅ tails = [10]

#### 🔁 第二次：num = 9

- tails = [10]

- bisect_left([10], 9) → idx = 0

- idx != len(tails) → tails[0] = 9

- ✅ tails = [9]（替換掉 10，讓尾巴更小）

#### 🔁 第三次：num = 2

- tails = [9]

- bisect_left([9], 2) → idx = 0

- tails[0] = 2

- ✅ tails = [2]

#### 🔁 第四次：num = 5

- tails = [2]

- bisect_left([2], 5) → idx = 1

- tails.append(5)

- ✅ tails = [2, 5]

#### 🔁 第五次：num = 3

- tails = [2, 5]

- bisect_left([2, 5], 3) → idx = 1

- tails[1] = 3

- ✅ tails = [2, 3]

#### 🔁 第六次：num = 7

- tails = [2, 3]

- bisect_left([2, 3], 7) → idx = 2

- tails.append(7)

- ✅ tails = [2, 3, 7]

#### 🔁 第七次：num = 101

- tails = [2, 3, 7]

- bisect_left([2, 3, 7], 101) → idx = 3

- tails.append(101)

- ✅ tails = [2, 3, 7, 101]

#### 🔁 第八次：num = 18

- tails = [2, 3, 7, 101]

- bisect_left([2, 3, 7, 101], 18) → idx = 3

- tails[3] = 18

- ✅ tails = [2, 3, 7, 18]

#### ✅ 最終 tails = [2, 3, 7, 18]

- 這表示目前找到的最長遞增子序列的長度為 4

### 📌 優點與關鍵

- 每次選擇當前能延伸的最小結尾（貪心）

- 使用二分搜尋找到正確位置 → 時間複雜度 O(log n)

- tails 不代表實際子序列，但長度正確

---

## ⏱ 複雜度分析 | Time & Space Complexity
| 方法   | 時間複雜度      | 空間複雜度 |
| ---- | ---------- | ----- |
| DP   | O(n²)      | O(n)  |
| 二分搜尋 | O(n log n) | O(n)  |

---

## 📚 我學到了什麼 | What I Learned
### 中文：

- 經典 DP 方法幫助我理解如何為每個元素維護最長序列長度。

- 二分搜尋法（tails 概念）透過控制結尾最小值提升效率，特別精妙。

- LIS 是常見面試題，熟悉兩種寫法很重要。

### English：

- The DP method provides clarity and easy implementation.

- Binary search optimization introduces tails[], a clever way to track sequence ends efficiently.

- Understanding both approaches helps in both interviews and algorithm thinking.