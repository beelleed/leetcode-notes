# 📍 LeetCode 287 — Find the Duplicate Number

🔗 https://leetcode.com/problems/find-the-duplicate-number/

---

# 📄 題目說明 | Problem Description

## 中文

給定一個長度為：

```text
n + 1
```

的陣列 `nums`。

其中：

* 每個數字都介於 `1 ~ n`
* 只有一個數字重複（可能出現多次）
* 不可以修改陣列
* 只能使用 `O(1)` 額外空間

請找出重複的數字。

---

## English

Given an array containing `n + 1` integers where each integer is between `1` and `n` inclusive, return the duplicate number.

Constraints:

* Do not modify the array.
* Use only constant extra space.

---

# 🧠 核心觀念 | Key Insight

這題不要把它想成：

```text
Array Problem
```

而要轉換成：

```text
Linked List Cycle Problem
```

---

# 🔄 陣列轉 Linked List

把：

```python
nums[i]
```

看成：

```text
next pointer
```

也就是：

```python
next(i) = nums[i]
```

---

例如：

```python
nums = [1,3,4,2,2]
```

Index：

```text
0 1 2 3 4
```

Value：

```text
1 3 4 2 2
```

可以畫成：

```text
0 → 1
    ↓
    3
    ↓
    2
    ↓
    4
    ↑
    └───
```

形成一個 Cycle。

---

# ❓ 為什麼一定有 Cycle？

Index 數量：

```text
0 ~ n
```

共有：

```text
n + 1
```

個位置。

---

Value 數量：

```text
1 ~ n
```

只有：

```text
n
```

個可能。

---

依據：

```text
Pigeonhole Principle
抽屜原理
```

一定有：

```text
兩個 index 指向同一個 value
```

因此：

```text
一定形成 Cycle
```

---

# 🎯 最重要結論

```text
Duplicate Number
=
Cycle Entrance
```

重複數字就是環的入口。

---

# 🐢🐇 Floyd Cycle Detection

又稱：

```text
Tortoise and Hare Algorithm
龜兔賽跑演算法
```

---

# Phase 1️⃣ 找相遇點

初始化：

```python
slow, fast = 0, 0
```

---

Slow 每次走一步：

```python
slow = nums[slow]
```

---

Fast 每次走兩步：

```python
fast = nums[nums[fast]]
```

---

程式碼：

```python
while True:
    slow = nums[slow]
    fast = nums[nums[fast]]

    if slow == fast:
        break
```

---

# ❓ 為什麼一定會相遇？

進入環後：

```text
slow 每輪 +1

fast 每輪 +2
```

所以：

```text
fast 每輪都比 slow 多走 1 格
```

距離會一直縮小。

最終：

```text
一定在環裡相遇
```

就像操場跑步：

```text
跑比較快的人
一定會追上
跑比較慢的人
```

---

# ⚠️ 相遇點不是答案

例如：

```python
nums = [1,3,4,2,2]
```

第一次相遇：

```text
index = 4
```

但答案：

```text
duplicate = 2
```

所以：

```text
Phase 1
只是確認已經進入 Cycle
```

還不知道入口在哪。

---

# Phase 2️⃣ 找 Cycle Entrance

建立：

```python
slow2 = 0
```

---

兩個指標同速前進：

```python
while True:
    slow = nums[slow]
    slow2 = nums[slow2]

    if slow == slow2:
        return slow
```

---

# ❓ 為什麼這樣能找到入口？

設：

```text
a = 起點到入口距離

b = 入口到相遇點距離

c = 相遇點到入口距離
```

```text
          b
      ┌──────● 相遇點
      │      │
入口 ●       │
      │      │
      └──────┘
          c
```

---

當 slow 和 fast 相遇時：

```text
slow 走了：

a + b
```

---

```text
fast 走了：

a + b + n(b+c)
```

---

因為：

```text
fast = 2 × slow
```

推導可得：

```text
a = c
```

---

# 🎯 超重要結論

```text
起點 → 入口距離

=

相遇點 → 入口距離
```

---

因此：

一個從：

```text
0
```

出發。

另一個從：

```text
相遇點
```

出發。

---

兩人：

```text
每次走一步
```

最後一定在：

```text
Cycle Entrance
```

相遇。

---

而入口就是：

```text
Duplicate Number
```

---

# 💻 程式碼

```python
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:

        slow, fast = 0, 0

        # Phase 1
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]

            if slow == fast:
                break

        # Phase 2
        slow2 = 0

        while True:
            slow = nums[slow]
            slow2 = nums[slow2]

            if slow == slow2:
                return slow
```

---

# 🧪 Example Trace

## Input

```python
nums = [1,3,4,2,2]
```

---

### 初始化

```text
slow = 0
fast = 0
```

---

## Phase 1

### Round 1

```python
slow = nums[0] = 1

fast = nums[nums[0]]
     = nums[1]
     = 3
```

```text
slow = 1
fast = 3
```

---

### Round 2

```python
slow = nums[1] = 3

fast = nums[nums[3]]
     = nums[2]
     = 4
```

```text
slow = 3
fast = 4
```

---

### Round 3

```python
slow = nums[3] = 2

fast = nums[nums[4]]
     = nums[2]
     = 4
```

```text
slow = 2
fast = 4
```

---

### Round 4

```python
slow = nums[2] = 4

fast = nums[nums[4]]
     = nums[2]
     = 4
```

```text
slow = 4
fast = 4
```

✅ 相遇

---

# Phase 2

初始化：

```python
slow2 = 0
```

---

### Round 1

```python
slow = nums[4] = 2

slow2 = nums[0] = 1
```

```text
slow = 2
slow2 = 1
```

---

### Round 2

```python
slow = nums[2] = 4

slow2 = nums[1] = 3
```

```text
slow = 4
slow2 = 3
```

---

### Round 3

```python
slow = nums[4] = 2

slow2 = nums[3] = 2
```

```text
slow = 2
slow2 = 2
```

✅ 相遇

---

# 🎯 最終答案

```python
return 2
```

---

# ⏱ Complexity Analysis

## Time Complexity

Phase 1：

```text
O(n)
```

Phase 2：

```text
O(n)
```

總計：

```text
O(n)
```

---

## Space Complexity

只用了：

```python
slow
fast
slow2
```

因此：

```text
O(1)
```

---

# 🎯 Interview Takeaways

看到：

```text
Length = n + 1

Values = 1 ~ n

Cannot modify array

O(1) extra space
```

立刻想到：

```text
Linked List Cycle

Floyd Cycle Detection

Tortoise and Hare

Cycle Entrance
```

---

# ✍️ 我學到的東西

* 287 不是 Frequency 題
* Counter 方向錯
* Heap 方向錯
* Sort 不能用
* Duplicate Number = Cycle Entrance
* Floyd 分成兩階段
* Phase 1 找相遇點
* Phase 2 找入口

---

# 🏆 Cheat Sheet

```text
287

nums[i]
↓
next pointer

Duplicate
↓
Cycle Entrance

Phase 1
Find Meeting Point

Phase 2
Find Entrance

Answer
=
Duplicate Number
```

---

# 🌟 One Sentence Summary

> Treat the array as a linked list, use Floyd's Cycle Detection to find the cycle entrance, and that entrance is the duplicate number.

> 將陣列視為 Linked List，利用龜兔賽跑找到 Cycle 的入口，而入口就是重複數字。
