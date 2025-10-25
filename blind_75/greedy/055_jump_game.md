# LeetCode 55 - Jump Game | 跳躍遊戲

🔗 [題目連結](https://leetcode.com/problems/jump-game/)

---

## 📘 題目說明 | Problem Description
### 中文：
給定一個整數陣列 nums，其中每個元素代表你在該位置最多可以跳幾步。你最初站在陣列的第一個位置，請判斷是否能跳到最後一個位置。

### English:
Given an array of non-negative integers nums, where each element represents your maximum jump length at that position. Determine if you can reach the last index starting from the first index.

### 🔍 範例 | Examples
```text
Input: nums = [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.

Input: nums = [3,2,1,0,4]
Output: false
Explanation: You will always arrive at index 3 with no way to jump to the last index.
```

---

## 🧠 解題思路 | Solution Strategy
✅ 核心想法：
- 使用貪婪法（Greedy）。

- 我們維護一個 maxReach，表示目前為止能跳到的最遠距離。

- 如果某個索引 i 超出 maxReach，表示跳不到，直接回傳 False。

- 如果遍歷整個陣列都沒有違規，就能跳到最後。

✅ Core Idea:
- Use a Greedy approach.

- Maintain a variable maxReach to store the farthest index you can reach so far.

- If at any index i, i > maxReach, then you can't reach that point → return False.

- If you finish the loop, then return True.

---

## 💻 程式碼 | Python Code
```python
from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        maxReach = 0
        for i, jump in enumerate(nums):
            if i > maxReach:
                return False
            maxReach = max(maxReach, i + jump)
        return True
```

### 🧾 程式碼解釋 | Code Explanation
1. for i, jump in enumerate(nums):
    
    逐一查看每個位置 i，jump = nums[i] 是在 i 能再往右跳的最大步數。

2. if i > maxReach: return False
    
    核心檢查：如果現在要處理的位置 i 本身到不了（因為我們的最遠可達 maxReach 還比 i 小），就
    直接失敗。

    👉 這維持了一個不變量：能被訪問/處理的 i 一定是可達的。一旦遇到不可達的 i，後面更不可能可達（因為我們是由左到右，跳躍都是往右）。

3. maxReach = max(maxReach, i + jump)
    
    在可達的前提下，用當前位置能延伸到的最遠點 i + jump 來擴張最遠可達範圍。

        直覺：到得了 i，再從 i 一跳，最遠可以去到 i + nums[i]。

        Greedy 精神：只記「目前為止能到的最遠地方」，不必記具體走法。

4. 迴圈結束 return True

    代表我們從 0 一路掃到尾，從未遇到不可達的位置。只要每個被掃到的位置都可達，就能一路走到最後 ⇒ True。
    
    （也可在過程中加早停：一旦 maxReach >= n-1 就可以立刻回 True）

## 範例 | Examples
- nums = [2, 3, 1, 1, 4]

### 🧠 初始狀態
| 變數         | 值               | 說明                     |
| ---------- | --------------- | ---------------------- |
| `nums`     | [2, 3, 1, 1, 4] | 給定陣列                   |
| `maxReach` | 0               | 目前為止能跳到的最遠位置（初始在第 0 格） |

### 🔁 進入 for 迴圈

### ➤ i = 0, jump = 2

| 步驟                                | 狀態                             |
| --------------------------------- | ------------------------------ |
| `i > maxReach` ? → `0 > 0` ❌      | 沒問題，表示目前這個位置可以到達。              |
| 更新：`maxReach = max(0, 0 + 2)` → 2 | 代表「從 index 0」出發，最遠能跳到 index 2。 |

✅ 現在可達範圍是：[0, 2]

### ➤ i = 1, jump = 3

| 步驟                                | 狀態                    |
| --------------------------------- | --------------------- |
| `i > maxReach` ? → `1 > 2` ❌      | 可以到達 index 1          |
| 更新：`maxReach = max(2, 1 + 3)` → 4 | 從 index 1 能跳到 index 4 |

✅ 現在可達範圍是：[0, 4]

    🎯 其實這時已經能到最後一格（index 4），可以直接確定 True。

### ➤ i = 2, jump = 1

| 步驟                                | 狀態     |
| --------------------------------- | ------ |
| `i > maxReach` ? → `2 > 4` ❌      |        |
| 更新：`maxReach = max(4, 2 + 1)` → 4 | 還是能到 4 |

### ➤ i = 3, jump = 1

| 步驟                                | 狀態 |
| --------------------------------- | -- |
| `i > maxReach` ? → `3 > 4` ❌      |    |
| 更新：`maxReach = max(4, 3 + 1)` → 4 | 不變 |

### ➤ i = 4, jump = 4

| 步驟                                | 狀態 |
| --------------------------------- | -- |
| `i > maxReach` ? → `4 > 4` ❌      |    |
| 更新：`maxReach = max(4, 4 + 4)` → 8 |    |

✅ 迴圈結束

沒有遇到 i > maxReach 的情況，代表整條路都能走完。
所以最後：

```python
return True
```

---

## ⏱ 時間與空間複雜度 | Time & Space Complexity
- 時間複雜度 Time Complexity: O(n)

- 空間複雜度 Space Complexity: O(1)

---

## 📌 學到什麼 | What I Learned
- 「跳躍遊戲」是一道貪婪策略的經典題。

- 記得：我們不需要實際模擬跳的過程，只要看「能不能跳到」。

- 如果一個位置你永遠跳不到，就整題失敗。

- 這種「範圍更新」或「最遠可到達」的技巧，常見於區間問題或跳躍類題型。