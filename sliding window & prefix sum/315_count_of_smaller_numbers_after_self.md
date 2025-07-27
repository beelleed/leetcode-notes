# LeetCode 315 - 計算右側小於當前元素的個數（Count of Smaller Numbers After Self）

🔗 [題目連結 | Problem Link](https://leetcode.com/problems/count-of-smaller-numbers-after-self/) 

---

## 📘 題目說明 | Problem Description

**中文：**  
給你一個整數陣列 `nums`，請你回傳一個新的整數陣列 `counts`，其中 `counts[i]` 表示在 `nums[i]` 右邊有幾個數字比它小。

**English:**  
You are given an integer array `nums`, and you need to return an array `counts` such that `counts[i]` is the number of smaller elements to the right of `nums[i]`.

### 🧩 範例 | Example

```python
Example 1:

Input: nums = [5,2,6,1]
Output: [2,1,1,0]
Explanation:
    To the right of 5 there are 2 smaller elements (2 and 1).
    To the right of 2 there is only 1 smaller element (1).
    To the right of 6 there is 1 smaller element (1).
    To the right of 1 there is 0 smaller element.

Example 2:

Input: nums = [-1]
Output: [0]

Example 3:

Input: nums = [-1,-1]
Output: [0,0]
```

---

## 💡 解法思路 | Solution Approach：Merge Sort

### 中文邏輯：
1. 使用 index 陣列記住原始索引位置。

2. 利用改良版 Merge Sort 的過程，在「合併階段」統計每個元素右邊有幾個比它小。

3. 當從右邊插入數時，就累積 right_counter。

4. 當從左邊插入數時，就將當前的 right_counter 加進對應的 result 裡。

### English Logic:
1. Use an index array to track each element’s original position.

2. During the merge phase of Merge Sort, count how many smaller elements pass from the right side.

3. Every time a right-side element is inserted before a left-side one, increase right_counter.

4. When inserting from the left side, add right_counter to the result for that index.

---

## 💻 Python 程式碼 | Python Code
```python
from typing import List

class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        result = [0] * len(nums)
        index = list(range(len(nums)))

        def merge_sort(start, end):
            if end - start <= 1:
                return
            mid = (start + end) // 2
            merge_sort(start, mid)
            merge_sort(mid, end)

            temp = []
            i, j = start, mid
            right_counter = 0

            while i < mid and j < end:
                if nums[index[j]] < nums[index[i]]:
                    temp.append(index[j])
                    right_counter += 1
                    j += 1
                else:
                    temp.append(index[i])
                    result[index[i]] += right_counter
                    i += 1

            while i < mid:
                temp.append(index[i])
                result[index[i]] += right_counter
                i += 1

            while j < end:
                temp.append(index[j])
                j += 1

            index[start:end] = temp

        merge_sort(0, len(nums))
        return result
```

### 📘 程式碼逐段說明
```python
result = [0] * len(nums)
index = list(range(len(nums)))
```
- result: 儲存每個位置的答案，初始化為 0。

- index: 用來追蹤原本的索引位置。因為我們之後會對 index 做排序，但要記得哪個 index 對應 nums 的哪個值。

#### 🔁 主體：Merge Sort 遞迴函式
```python
def merge_sort(start, end):
    if end - start <= 1:
        return
```
- 遞迴終止條件：如果子陣列長度 ≤ 1，則返回。
```python
mid = (start + end) // 2
merge_sort(start, mid)
merge_sort(mid, end)
```
- 把 index[start:end] 切成左右兩半，分別遞迴處理。

#### 🧩 合併過程（核心邏輯）：
```python
temp = []
i, j = start, mid
right_counter = 0
```
- i 指向左半邊，j 指向右半邊

- right_counter 計算目前右邊有多少元素小於左邊的某個值（這是答案的關鍵）

```python
while i < mid and j < end:
    if nums[index[j]] < nums[index[i]]:
        temp.append(index[j])
        right_counter += 1
        j += 1
    else:
        temp.append(index[i])
        result[index[i]] += right_counter
        i += 1
```
- 如果 nums[index[j]] < nums[index[i]] → 說明右邊的值比左邊小，先把 j 加進結果，並記錄「右邊有一個更小的數」。

- 如果不是，就把 i 的 index 加入，並在它的 result[index[i]] 裡加上目前已經出現的 right_counter。

```python
while i < mid:
    temp.append(index[i])
    result[index[i]] += right_counter
    i += 1
```
- 如果左邊還沒走完，說明剩下的左邊元素也要加上目前的 right_counter（因為這些右邊更小的數都已經出現了）

```python
while j < end:
    temp.append(index[j])
    j += 1
```
- 把右邊剩下的值也補進去（不影響計數）
```python
index[start:end] = temp
```
- 將排序好的索引值複製回原來的 index 中，這樣下一層 merge 可以正確使用。

#### 🔚 呼叫合併排序並回傳結果
```python
merge_sort(0, len(nums))
return result
```
- 從整個 nums 開始排序

- 最後回傳結果 result，每個位置記錄的是對應 nums[i] 右邊小於它的個數

#### ✅ 總結重點
| 概念                   | 說明                         |
| -------------------- | -------------------------- |
| 使用合併排序               | 透過排序同時計算右邊有多少數字比自己小        |
| 使用 `index`           | 保持追蹤原始 `nums[i]` 在排序過程中的位置 |
| 核心在於 `right_counter` | 每次從右邊插入值時記錄比左邊小的數量，並累積給左邊  |

---

## 🔄 Merge Sort 合併過程流程圖 | Merge Sort Execution Flow
以 nums = [5, 2, 6, 1] 為例  
Given `nums = [5, 2, 6, 1]`

初始 nums: [5, 2, 6, 1]
初始 index: [0, 1, 2, 3]
初始 result: [0, 0, 0, 0]

### 📍 分割與合併階段一 | Phase 1: Merge [5, 2]

- 對應 index: `[0, 1]` → nums[0] = 5, nums[1] = 2
- 分割為 [5] (index: [0]) 和 [2] (index: [1])
- 合併時：
  - 比較 `nums[1]=2 < nums[0]=5` → ✅
    - `right_counter += 1 → 1`
    - `temp = [1]`
  - 將 nums[0] 放入 temp：
    - `result[0] += right_counter → result[0] = 1`
    - `temp = [1, 0]`
- 合併後 index: `[1, 0]`

### 📍 分割與合併階段二 | Phase 2: Merge [6, 1]

- 對應 index: `[2, 3]` → nums[2] = 6, nums[3] = 1
- 分割為 [6] (index: [2]) 和 [1] (index: [3])
- 合併時：
  - 比較 `nums[3]=1 < nums[2]=6` → ✅
    - `right_counter += 1 → 1`
    - `temp = [3]`
  - 將 nums[2] 放入 temp：
    - `result[2] += right_counter → result[2] = 1`
    - `temp = [3, 2]`
- 合併後 index: `[3, 2]`

### 📍 合併全體 | Final Merge: [1, 0] + [3, 2]

- index 左：`[1, 0]` → nums: [2, 5]
- index 右：`[3, 2]` → nums: [1, 6]
- 合併順序如下：
  - 比較 `nums[3]=1 < nums[1]=2` → ✅
    - `right_counter += 1 → 1`
    - `temp = [3]`
  - 比較 `nums[2]=6 < nums[1]=2` → ❌
    - `result[1] += right_counter → result[1] = 1`
    - `temp = [3, 1]`
  - 比較 `nums[2]=6 < nums[0]=5` → ❌
    - `result[0] += right_counter → result[0] = 2`
    - `temp = [3, 1, 0]`
  - 將剩餘 nums[2]=6 加入：
    - `temp = [3, 1, 0, 2]`
- 最終 index: `[3, 1, 0, 2]`

### ✅ 最終結果 | Final result

```python
nums = [5, 2, 6, 1]
result = [2, 1, 1, 0]
```

### 📌 說明
- right_counter：在合併過程中，當右半部的元素小於左半部的元素時，累加的計數器。

- result[index[i]] += right_counter：將目前累積的 right_counter 加到對應的原始位置上，表示該位置右側有多少個比它小的元素。

---

## ⏱ 時間與空間複雜度 | Time & Space Complexity
- 時間複雜度 | Time: O(n log n)

- 空間複雜度 | Space: O(n)

---

## 📚 學到什麼 | What I Learned

**中文：**

- 我學到了如何透過「改良版的合併排序」來解決與位置相關的統計問題。
- 使用 `index` 陣列來追蹤原始位置是一個重要技巧，讓我們可以一邊排序、一邊記錄結果。
- 在合併的過程中統計「右邊有幾個比左邊小」的數量，能有效把時間複雜度從 O(n²) 降到 O(n log n)。
- 學會了如何在排序過程中搭配額外邏輯（如 counter）來達到同時處理排序與統計。

**English:**

- I learned how to solve position-based counting problems using a modified merge sort.
- Using an `index` array to track the original positions is a key technique to separate data sorting from result tracking.
- Counting the number of smaller elements on the right during the merge step helps reduce time complexity from O(n²) to O(n log n).
- I also learned how to combine sorting with additional logic like counters to handle two problems at once.

---

## 🗣 重點 |  Highlights
- 這題看似 O(n²) 暴力比大小，但其實可以用排序技巧優化到 O(n log n)。

- 核心在於「合併階段就計數」而不是事後遍歷。

- 使用 index 陣列幫我們追蹤原始位置，避免排序影響答案。