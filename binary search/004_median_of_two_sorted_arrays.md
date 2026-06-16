# 📍 LeetCode 4 — Median of Two Sorted Arrays

🔗 https://leetcode.com/problems/median-of-two-sorted-arrays/

## 📄 題目說明 | Problem Description

### 中文

* 給定兩個已排序的整數陣列：

```python
nums1
nums2
```

* 請找出兩個陣列合併後的中位數（median）。
* 要求時間複雜度：

```text
O(log(m+n))
```

* 其中：

```text
m = len(nums1)
n = len(nums2)
```

### English

* Given two sorted arrays `nums1` and `nums2`, return the median of the two sorted arrays.
* The overall run time complexity should be:

```text
O(log(m+n))
```

### Examples

#### Example 1

```python
nums1 = [1, 3]
nums2 = [2]
```

* Merged array:

```text
[1, 2, 3]
```

* Median:

```text
2
```

* Output:

```python
2.0
```

#### Example 2

```python
nums1 = [1, 2]
nums2 = [3, 4]
```

* Merged array:

```text
[1, 2, 3, 4]
```

* Median:

```text
(2 + 3) / 2 = 2.5
```

* Output:

```python
2.5
```

---

## 🧠 核心觀念 | Key Insight

* 這題不能真的把兩個陣列 merge 起來。
* 因為 merge 需要：

```text
O(m+n)
```

* 但題目要求：

```text
O(log(m+n))
```

* 所以要使用：

```text
Binary Search
```

* 中位數的本質是：

```text
把合併後的陣列切成左右兩半
```

* 而且要滿足：

```text
左半邊所有元素 <= 右半邊所有元素
```

* 例如：

```text
merged = [1, 2, 3, 4, 5]
```

* 可以切成：

```text
left half  = [1, 2, 3]
right half = [4, 5]
```

* 中位數是：

```text
3
```

* 如果總長度是偶數：

```text
merged = [1, 2, 3, 4]
```

* 可以切成：

```text
left half  = [1, 2]
right half = [3, 4]
```

* 中位數是：

```text
(max(left) + min(right)) / 2
= (2 + 3) / 2
= 2.5
```

---

## 🔑 Binary Search 在找什麼？

* 這題的 Binary Search 不是在找某個數字。
* 而是在找：

```text
正確的切割位置 partition
```

* 假設：

```text
A = nums1
B = nums2
```

* 我們會在比較短的陣列 `A` 上做 Binary Search。

---

## ✂️ Partition 定義

* 假設：

```python
i = A 的切割位置
j = B 的切割位置
```

* 意思是：

```text
A 左邊拿 i 個元素
B 左邊拿 j 個元素
```

* 兩邊加起來正好是左半邊大小。
* 左半邊總長度：

```python
half = (m + n + 1) // 2
```

* 所以：

```python
j = half - i
```

---

## 🧩 四個邊界值

* 切割後，只需要看四個值：

```text
Aleft   = A[i - 1]
Aright  = A[i]

Bleft   = B[j - 1]
Bright  = B[j]
```

* 圖像：

```text
A:  ... Aleft | Aright ...
B:  ... Bleft | Bright ...
```

* 正確切割要滿足：

```text
Aleft <= Bright
Bleft <= Aright
```

* 只要這兩個條件成立，代表：

```text
左半邊所有元素 <= 右半邊所有元素
```

---

## 🛡️ 邊界處理

* 如果 `i == 0`，代表 `A` 左邊沒有元素：

```python
Aleft = float('-inf')
```

* 如果 `i == m`，代表 `A` 右邊沒有元素：

```python
Aright = float('inf')
```

* `B` 也同理。
* 這樣做是為了避免 index out of range，也讓比較邏輯保持一致。

---

## 💻 Code

```python
class Solution:
    def findMedianSortedArrays(self, nums1, nums2):

        A, B = nums1, nums2

        if len(A) > len(B):
            A, B = B, A

        m, n = len(A), len(B)

        total = m + n
        half = (total + 1) // 2

        left, right = 0, m

        while left <= right:

            i = (left + right) // 2
            j = half - i

            Aleft = A[i - 1] if i > 0 else float('-inf')
            Aright = A[i] if i < m else float('inf')

            Bleft = B[j - 1] if j > 0 else float('-inf')
            Bright = B[j] if j < n else float('inf')

            if Aleft <= Bright and Bleft <= Aright:

                if total % 2 == 1:
                    return max(Aleft, Bleft)

                return (max(Aleft, Bleft) + min(Aright, Bright)) / 2

            elif Aleft > Bright:
                right = i - 1

            else:
                left = i + 1
```

---

## 🧾 程式碼逐行解釋 | Line-by-line Explanation

```python
A, B = nums1, nums2
```

* 先把兩個陣列命名成 `A` 和 `B`。
* 這樣後面寫 partition 時比較清楚。

---

```python
if len(A) > len(B):
    A, B = B, A
```

* 確保 `A` 是比較短的陣列。
* 因為我們要在 `A` 上做 Binary Search。
* 這樣可以讓時間複雜度變成：

```text
O(log(min(m, n)))
```

* 也可以避免 `j = half - i` 超出 `B` 的範圍。

---

```python
m, n = len(A), len(B)
```

* 取得兩個陣列長度。
* `m = A 的長度`
* `n = B 的長度`

---

```python
total = m + n
```

* 計算總元素數量。

---

```python
half = (total + 1) // 2
```

* 計算左半邊需要幾個元素。
* 這裡要 `+1` 是因為當總長度是奇數時，希望左半邊多一個元素。
* 例如：

```text
total = 5
half = (5 + 1) // 2 = 3
```

* 左半邊會有 3 個元素，右半邊有 2 個元素。
* 這樣中位數就是左半邊最大值。

---

```python
left, right = 0, m
```

* Binary Search 的範圍是 `A` 可以切的位置。
* 如果 `A` 長度是 `m`，切割位置可以是：

```text
0 ~ m
```

* 注意不是 `m - 1`。
* 因為切割位置不是 index，而是「左邊拿幾個元素」。

```text
A = [1, 2, 3]

| 1 2 3     i = 0
1 | 2 3     i = 1
1 2 | 3     i = 2
1 2 3 |     i = 3
```

---

```python
while left <= right:
```

* 開始 Binary Search。
* 只要搜尋範圍還存在，就繼續找正確 partition。

---

```python
i = (left + right) // 2
```

* 選擇 `A` 的切割位置。
* `i` 代表：

```text
A 左邊放幾個元素
```

---

```python
j = half - i
```

* 決定 `B` 的切割位置。
* 因為左半邊總共要有 `half` 個元素。
* 如果 `A` 左邊放了 `i` 個，那 `B` 左邊就要放：

```text
half - i
```

個。

---

```python
Aleft = A[i - 1] if i > 0 else float('-inf')
```

* 取得 `A` 左半邊的最大值。
* i - 1是A左半邊最大值的index。
* 如果 `i == 0`，代表 `A` 左邊沒有元素。
* 所以用 `float('-inf')`。
* 這樣可以避免 index out of range。
* 同時 `-inf` 不會影響最大值比較。

---

```python
Aright = A[i] if i < m else float('inf')
```

* 取得 `A` 右半邊的最小值。
* 如果 `i == m`，代表 `A` 右邊沒有元素。
* 所以用 `float('inf')`。
* 這樣可以避免 index out of range。
* 同時 `inf` 不會影響最小值比較。

---

```python
Bleft = B[j - 1] if j > 0 else float('-inf')
```

* 取得 `B` 左半邊的最大值。
* j - 1是B左半邊最大值的index。
* 如果 `j == 0`，代表 `B` 左邊沒有元素。
* 所以用 `float('-inf')`。

---

```python
Bright = B[j] if j < n else float('inf')
```

* 取得 `B` 右半邊的最小值。
* 如果 `j == n`，代表 `B` 右邊沒有元素。
* 所以用 `float('inf')`。

---

```python
if Aleft <= Bright and Bleft <= Aright:
```

* 判斷目前切割是否正確。
* 正確切割需要：

```text
Aleft <= Bright
Bleft <= Aright
```

* 意思是：

  * `A` 左邊的最大值不能大於 `B` 右邊的最小值。
  * `B` 左邊的最大值不能大於 `A` 右邊的最小值。
* 如果兩個條件都成立，代表：

```text
整個左半邊 <= 整個右半邊
```

---

```python
if total % 2 == 1:
    return max(Aleft, Bleft)
```

* 如果總長度是奇數，中位數就是左半邊最大值。
* 因為前面用：

```python
half = (total + 1) // 2
```

* 讓左半邊在奇數時多一個元素。
* 所以直接回傳：

```python
max(Aleft, Bleft)
```

---

```python
return (max(Aleft, Bleft) + min(Aright, Bright)) / 2
```

* 如果總長度是偶數，中位數是左半邊最大值與右半邊最小值的平均。
* 也就是：

```text
(max(left half) + min(right half)) / 2
```

---

```python
elif Aleft > Bright:
    right = i - 1
```

* 如果 `Aleft > Bright`，代表 `A` 左邊拿太多了。
* 因為 `A` 左邊最大值比 `B` 右邊最小值還大。
* 所以切割點 `i` 太右。
* 要往左找。
* 因此更新：

```python
right = i - 1
```

---

```python
else:
    left = i + 1
```

* 剩下情況是 `Bleft > Aright`。
* 代表 `A` 左邊拿太少了。
* 需要讓 `A` 多拿一些元素。
* 所以 `i` 要往右移。
* 因此更新：

```python
left = i + 1
```

---

## 🧪 Example Walkthrough

### Example 1

```python
nums1 = [1, 3]
nums2 = [2]
```

### Step 1：確保 A 比較短

* 原本：

```text
nums1 = [1, 3]
nums2 = [2]
```

* 因為 `nums1` 比 `nums2` 長，所以交換：

```text
A = [2]
B = [1, 3]
```

### Step 2：初始化

```text
m = 1
n = 2
total = 3
half = (3 + 1) // 2 = 2

left = 0
right = 1
```

### Round 1

```python
i = (0 + 1) // 2 = 0
j = half - i = 2 - 0 = 2
```

* 切割：

```text
A: | 2
B: 1 3 |
```

* 四個值：

```text
Aleft  = -inf
Aright = 2

Bleft  = 3
Bright = inf
```

* 判斷：

```text
Aleft <= Bright   ✅
Bleft <= Aright   ❌
```

* 因為：

```text
3 > 2
```

* 代表 `A` 左邊拿太少。
* 所以：

```python
left = i + 1 = 1
```

### Round 2

```python
i = (1 + 1) // 2 = 1
j = half - i = 2 - 1 = 1
```

* 切割：

```text
A: 2 |
B: 1 | 3
```

* 四個值：

```text
Aleft  = 2
Aright = inf

Bleft  = 1
Bright = 3
```

* 判斷：

```text
Aleft <= Bright   ✅
Bleft <= Aright   ✅
```

* 找到正確切割。
* 總長度是奇數：

```text
total = 3
```

* 所以：

```python
return max(Aleft, Bleft)
```

* 也就是：

```text
max(2, 1) = 2
```

* 答案：

```python
2.0
```

### Example 2

```python
nums1 = [1, 2]
nums2 = [3, 4]
```

* 總長度：

```text
4
```

* 正確切割後：

```text
left half  = [1, 2]
right half = [3, 4]
```

* 中位數：

```text
(max(left half) + min(right half)) / 2
= (2 + 3) / 2
= 2.5
```

---

## ⏱ Complexity Analysis

### Time Complexity

* Binary Search 在較短陣列上進行：

```text
O(log(min(m, n)))
```

### Space Complexity

* 只使用固定變數：

```text
O(1)
```

---

## 🎯 Interview Takeaways

* 看到：

```text
Two sorted arrays
Find median
Need O(log(m+n))
```

* 要想到：

```text
Binary Search on Partition
```

* 重點不是 merge，而是：

```text
找到一個切割點
讓左半邊所有元素 <= 右半邊所有元素
```

---

## ✍️ 我學到的東西 | What I Learned

* 不能真的 merge，因為會是 `O(m+n)`。
* 要把問題轉成找 partition。
* Binary Search 不是找值，而是找正確切割位置。
* 永遠在較短陣列上 Binary Search。
* `i` 是 `A` 的切割位置。
* `j = half - i` 是 `B` 的切割位置。
* 正確條件是：

```text
Aleft <= Bright
Bleft <= Aright
```

---

## 🏆 Cheat Sheet

```text
LeetCode 4

Two sorted arrays
↓
Find median
↓
Binary search partition

Aleft | Aright
Bleft | Bright

Valid if:
Aleft <= Bright
Bleft <= Aright

Odd:
max(Aleft, Bleft)

Even:
(max(Aleft, Bleft) + min(Aright, Bright)) / 2
```

---

## 🌟 One Sentence Summary

> Use binary search to find the correct partition between two sorted arrays, so that all elements on the left are smaller than or equal to all elements on the right.

> 使用 Binary Search 找到兩個排序陣列的正確切割點，使左半邊所有元素都小於等於右半邊，進而得到中位數。
