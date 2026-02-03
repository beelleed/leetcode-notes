# 📍 LeetCode 287 — Find the Duplicate Number

🔗 [題目連結](https://leetcode.com/problems/find-the-duplicate-number/)

---

## 📄 題目說明 | Problem Description
### 中文：

- 給定一個長度為 n + 1 的整數陣列 nums，
- 其中每個數字都在 1 ~ n 的範圍內。

    - 只有 一個數字重複（可能出現多次）

    - 不能修改陣列

    - 只允許使用 O(1) 額外空間

- 請找出那個重複的數字。

### English:

Given an array containing n + 1 integers where each integer is between 1 and n inclusive, find the duplicate number without modifying the array and using only constant extra space.

### Examples
- Example 1:

    - Input: nums = [1,3,4,2,2]
    - Output: 2
- Example 2:

    - Input: nums = [3,1,3,4,2]
    - Output: 3
- Example 3:

    - Input: nums = [3,3,3,3,3]
    - Output: 3

---

## 🧠 解題核心轉換 | Key Insight
- 關鍵轉換（超重要）

    - 把陣列視為一個 linked list：

        - index 當作節點

        - nums[i] 當作 next 指標
```text
next(i) = nums[i]
```

- 為什麼一定會有 cycle？

    - index 範圍：0 ~ n（n+1 個節點）

    - value 範圍：1 ~ n（n 個可能的 next）

- 👉 依照 抽屜原理（Pigeonhole Principle）一定有兩個 index 指向同一個 value → 形成 cycle

### 關鍵結論

- 重複的數字 = cycle 的入口（cycle entry）

- 這和 hasCycle 找 cycle entry 的邏輯完全一樣。

---

## 🧠 對照 hasCycle 的解題流程
- hasCycle 的兩個階段

    - 1️⃣ 快慢指標在 cycle 中相遇
    - 2️⃣ 找出 cycle 的入口

- 👉 287 完全照這兩步做

---

## 💻 程式碼實作 | Code (Python)
```python
from typing import List

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # Phase 1: Find intersection point inside the cycle
        slow = nums[0]
        fast = nums[0]

        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break

        # Phase 2: Find the entrance of the cycle (duplicate number) 
        ptr1 = nums[0] # ptr1 = pointer 1
        ptr2 = slow

        while ptr1 != ptr2:
            ptr1 = nums[ptr1]
            ptr2 = nums[ptr2]

        return ptr1
```
### 🔍 程式碼逐段說明 | Line-by-line Explanation
### Phase 1：找 cycle 內的相遇點
```python
slow = nums[0]
fast = nums[0]
```

- 兩個指標都從 index 0 出發

- 對應到 linked list 的 head
```python
slow = nums[slow]
```

- slow 每次走 一步

- 等價於 slow = slow.next
```python
fast = nums[nums[fast]]
```

- fast 每次走 兩步

- 等價於 fast = fast.next.next
```python
if slow == fast:
    break
```

- 只要在 cycle 中相遇

- 就結束第一階段

### Phase 2：找 cycle 入口（duplicate）
```python
ptr1 = nums[0]
ptr2 = slow
```

- ptr1：從起點重新出發

- ptr2：停在 cycle 內的相遇點
```python
while ptr1 != ptr2:
    ptr1 = nums[ptr1]
    ptr2 = nums[ptr2]
```

- 兩個指標 同速前進

- 再次相遇的地方

- 就是 cycle 的入口
```python
return ptr1
```

- 回傳 cycle 入口的值

- 也就是 重複的數字

---

## 🧪 範例流程 | Example Walkthrough
### 範例 1
```python
nums = [1, 3, 4, 2, 2]
```

index 對應：
```text
index:  0  1  2  3  4
value:  1  3  4  2  2
```
#### Phase 1：找 cycle 內的相遇點（slow / fast）
程式碼對應
```python
slow = nums[0]
fast = nums[0]
```
初始化
```text
slow = 1
fast = 1
```
第一次 while 迴圈
```python
slow = nums[slow]
fast = nums[nums[fast]]
```

計算：
```text
slow = nums[1] = 3
fast = nums[nums[1]] = nums[3] = 2
```

狀態：
```text
slow = 3
fast = 2
```

→ 尚未相遇，繼續

##### 第二次 while 迴圈
```python
slow = nums[slow]
fast = nums[nums[fast]]
```
計算：
```text
slow = nums[3] = 2
fast = nums[nums[2]] = nums[4] = 2
```

狀態：
```text
slow = 2
fast = 2
```

- ✅ slow == fast，相遇，跳出 Phase 1

#### Phase 2：找 cycle 的入口（duplicate number）
程式碼對應
```python
ptr1 = nums[0]
ptr2 = slow
```

初始化：
```text
ptr1 = 1
ptr2 = 2
```
##### 第一次 while 迴圈
```python
ptr1 = nums[ptr1]
ptr2 = nums[ptr2]
```

計算：
```text
ptr1 = nums[1] = 3
ptr2 = nums[2] = 4
```

狀態：
```text
ptr1 = 3
ptr2 = 4
```

→ 尚未相遇

##### 第二次 while 迴圈
```python
ptr1 = nums[ptr1]
ptr2 = nums[ptr2]
```

計算：
```text
ptr1 = nums[3] = 2
ptr2 = nums[4] = 2
```

狀態：
```text
ptr1 = 2
ptr2 = 2
```

- ✅ ptr1 == ptr2，相遇

#### 🎯 最終結果
```python
return ptr1
```
回傳：
```text
2
```

---

### 🧪 範例 2
```python
nums = [2, 5, 9, 6, 9, 3, 8, 9, 7, 1]
```

index / value 對照表：
```text
index:  0  1  2  3  4  5  6  7  8  9
value:  2  5  9  6  9  3  8  9  7  1
```

#### Phase 1：尋找第一次相遇點（逐步 trace）
初始化
```python
slow = nums[0] = 2
fast = nums[0] = 2
```

狀態：
```text
slow = 2
fast = 2
```
##### 第 1 次 while
```python
slow = nums[slow] = nums[2] = 9
fast = nums[nums[fast]] = nums[nums[2]] = nums[9] = 1
```

狀態：
```text
slow = 9
fast = 1
```
##### 第 2 次 while
```python
slow = nums[9] = 1
fast = nums[nums[1]] = nums[5] = 3
```

狀態：
```text
slow = 1
fast = 3
```
##### 第 3 次 while
```python
slow = nums[1] = 5
fast = nums[nums[3]] = nums[6] = 8
```

狀態：
```text
slow = 5
fast = 8
```
##### 第 4 次 while
```python
slow = nums[5] = 3
fast = nums[nums[8]] = nums[7] = 9
```

狀態：
```text
slow = 3
fast = 9
```
##### 第 5 次 while
```python
slow = nums[3] = 6
fast = nums[nums[9]] = nums[1] = 5
```

狀態：
```text
slow = 6
fast = 5
```
##### 第 6 次 while
```python
slow = nums[6] = 8
fast = nums[nums[5]] = nums[3] = 6
```

狀態：
```text
slow = 8
fast = 6
```
##### 第 7 次 while
```python
slow = nums[8] = 7
fast = nums[nums[6]] = nums[8] = 7
```

狀態：
```text
slow = 7
fast = 7   ✅ 相遇
```
##### ✅ Phase 1 結果

- 第一次相遇點：7

- 意義是：

    - 我已經確定進入 cycle

    - 但我不知道 cycle 的入口在哪

⚠️ 此時 7 不是答案

#### Phase 2：找 cycle 入口（逐步 trace）
初始化
```python
ptr1 = nums[0] = 2
ptr2 = slow = 7
```

狀態：
```text
ptr1 = 2
ptr2 = 7
```
##### 第 1 次 while
```python
ptr1 = nums[2] = 9
ptr2 = nums[7] = 9
```

狀態：
```text
ptr1 = 9
ptr2 = 9   ✅ 相遇
```
##### 🎯 最終結果
```python
return 9
```
- 解釋：

    - 9 是 cycle 的入口

    - 也是被兩個不同 index 指到的 value

    - 👉 重複的數字

#### 📝 我的理解（直接可用在筆記）

- 在 Phase 1 中，我第一次相遇在 index = 7，這代表我已經確定站在 cycle 裡的一個位置。

- 但這個位置只是 cycle 中的其中一點，並不是 cycle 的起點。

- 因此我必須進入 Phase 2，讓一個指標從起點出發，
另一個指標從 cycle 內出發，兩者同速前進，最終相遇的地方才會是 cycle 的入口，也就是題目要求的重複數字。

---

## ⏱ 複雜度分析 | Complexity Analysis

- 時間複雜度：

    - Phase 1 + Phase 2 都是 O(n)

    - 👉 總計 O(n)

- 空間複雜度：

    - 只使用常數個指標

    - 👉 O(1)

---

## ✍️ 我學到的東西 | What I Learned

- 287 不是 frequency 題

- Counter / heap 方向是錯的

- 正確模型是 linked list cycle

- duplicate number = cycle entry

- 可以直接套用 hasCycle 的兩階段模板

---

## 🧠 一句話總結

Treat the array as a linked list where the duplicate number is the entry point of the cycle.