# 🧗‍♂️ 70. Climbing Stairs

[LeetCode 題目連結](https://leetcode.com/problems/climbing-stairs/)

---

## 📘 題目描述 | Problem Description

### 中文：
你正在爬樓梯。需要 `n` 步才能到達樓頂，每次你可以爬 1 或 2 步。請問有多少種不同的方法可以爬到樓頂？

### English:
You are climbing a staircase. It takes `n` steps to reach the top. Each time you can climb either 1 or 2 steps. In how many distinct ways can you climb to the top?

### Examples
- Example 1:

    - Input: n = 2
    - Output: 2
    - Explanation: There are two ways to climb to the top.
        1. 1 step + 1 step
        2. 2 steps

- Example 2:

    - Input: n = 3
    - Output: 3
    - Explanation: There are three ways to climb to the top.
        1. 1 step + 1 step + 1 step
        2. 1 step + 2 steps
        3. 2 steps + 1 step

---

## ✅ 解法：動態規劃（Dynamic Programming）

```python
class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        F = [0] * (n + 1)
        F[1], F[2] = 1, 2
        for i in range(3, n + 1):
            F[i] = F[i - 1] + F[i - 2]
        return F[n]
```

## 🧠 解題思路 | Solution Explanation
- 每次可以選擇爬 1 或 2 階

- 要爬到第 n 階，可以從 n-1 踏一步，或從 n-2 踏兩步
- 初始條件：F[1] = 1, F[2] = 2

- 遞推公式為：F[n] = F[n-1] + F[n-2]

- 這是經典的費波那契問題變形

## 📝 n = 4 的實例分析
```python
n = 4
F = [0] * 5         ➜ [0, 0, 0, 0, 0]
F[1] = 1
F[2] = 2            ➜ [0, 1, 2, 0, 0]

for i in range(3, 5):
    F[3] = F[2] + F[1] = 3   ➜ [0, 1, 2, 3, 0]
    F[4] = F[3] + F[2] = 5   ➜ [0, 1, 2, 3, 5]

return F[4]  # ➜ 5
```
共 5 種走法：

- 1 + 1 + 1 + 1

- 1 + 2 + 1

- 2 + 1 + 1

- 1 + 1 + 2

- 2 + 2

## ✨ 我學到的 | What I Learned
| 中文學習點                        | English Takeaway                                 |
| ---------------------------- | ------------------------------------------------ |
| DP 要設定初始條件（F\[1] 與 F\[2]）    | Dynamic programming starts from base cases       |
| 陣列大小需設為 `n + 1` 才能索引到 `F[n]` | Always allocate `n + 1` space to access `F[n]`   |
| 不要從 i = 0 開始計算，應從 3 開始       | Avoid overwriting base cases; start from `i = 3` |
| 這題的狀況數 = 費波那契第 n 項           | This is a variation of Fibonacci sequence        |

## ⏱ 複雜度分析 | Time & Space Complexity
- 時間複雜度：O(n)

- 空間複雜度：O(n)