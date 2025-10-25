# LeetCode 39 - Combination Sum
🔗 [題目連結](https://leetcode.com/problems/combination-sum/)

---

## 📘 題目說明 | Problem Description
### 中文說明：
給定一個不包含重複數字的陣列 candidates 和一個整數 target，找出所有加總為 target 的組合。每個數字可以被重複選取任意次。

### English：
Given an array of distinct integers candidates and a target integer target, return all unique combinations of candidates where the chosen numbers sum to target. You may reuse the same number as many times as needed.

### Examples
- Example 1:

    - Input: candidates = [2,3,6,7], target = 7
    - Output: [[2,2,3],[7]]
    - Explanation: 
        - 2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times.
        - 7 is a candidate, and 7 = 7.
        - These are the only two combinations.
- Example 2:

    - Input: candidates = [2,3,5], target = 8
    - Output: [[2,2,2,2],[2,3,3],[3,5]]
- Example 3:

    - Input: candidates = [2], target = 1
    - Output: []

---

## 🧠 解題思路 | Solution Strategy
### 中文說明：
- 每一個數字都有兩種選擇：選 或 不選，這是一個 回溯法（Backtracking） 的典型應用。

- 透過遞迴嘗試加入目前候選數字，若 target 為 0 表示成功組合。

- 若 target 小於 0，表示超出目標，這條路不通需 剪枝回溯。

- 回溯時從「當前索引」開始，因為數字可以 重複使用。

### English Explanation:
- Each number has two choices: pick or not pick, which is a classic Backtracking scenario.

- We recursively try to add the current candidate. If target == 0, it means a valid combination is found.

- If target < 0, it means the sum exceeds the target — we prune this path and backtrack.

- We start the recursion from the current index so that each number can be used multiple times.

邏輯圖解：
```markdown
Start: []
選 2 → [2]
再選 2 → [2,2]
再選 2 → [2,2,2]
再選 2 → [2,2,2,2] ❌ 超過 target 回溯
選 3 → [2,2,3] ✅
...
```

---

## 🔍 Python 程式碼 | Python Code
```python
ffrom typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        def backtrack(start: int, path: List[int], remaining: int):
            if remaining == 0:
                res.append(path[:])
                return
            elif remaining < 0:
                return  # 超過目標就剪枝

            for i in range(start, len(candidates)):
                path.append(candidates[i])
                backtrack(i, path, remaining - candidates[i])
                path.pop()  # 回溯

        backtrack(0, [], target)
        return res
```
```python
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
```
- 這是主函數 combinationSum。
    - candidates: 代表候選數字的清單。

    - target: 要湊成的總和。

    - res: 存放所有合法組合的結果列表。

```python
def backtrack(start: int, path: List[int], remaining: int):
```
- 這是內部定義的遞迴函數 backtrack。

    - start: 從哪個 index 開始選擇（避免重複、確保組合不重排）。

    - path: 當前累積的組合。

    - remaining: 剩餘要湊的目標值。
```python
if remaining == 0:
    res.append(path[:])
    return
```
- 如果 remaining 剛好等於 0，表示目前這個 path 組合成功，可以加入 res。

    - 用 path[:] 是為了避免引用，確保存的是 path 的拷貝。
```python
elif remaining < 0:
    return
```
- 如果總和超過目標值，這條路就無法繼續了，直接返回。
```python
for i in range(start, len(candidates)):
```
- 這是一個迴圈，從 start 開始。這樣可以避免重複，並允許重複使用同一個數字（不加 +1 的話可重複使用）。
```python
path.append(candidates[i])
```
- 加入當前候選數字進 path。
```python
backtrack(i, path, remaining - candidates[i])
```
- 這是遞迴呼叫：從當前 index i 繼續遞迴（可以重複使用相同數字），並更新剩餘 target 值。
    - i:「下一層」遞迴可以繼續使用相同的數字。
    - i + 1: 「下一層」遞迴不可以繼續使用相同的數字。
```python
path.pop()
```
回溯的核心！把剛才加進去的數字移除，回到上一層，繼續嘗試下一個數字。
```python
backtrack(0 ,[], target)
return res
```
- 呼叫 backtrack，從 index 0 開始，初始 path 是空列表，初始剩餘值是 target。

- 最後回傳結果 res，包含所有成功組合。

### 🧠 補充說明：為什麼用 start 控制
- 使用 start 是為了避免重複組合（例如 [2,3,2] 跟 [2,2,3] 是一樣的組合，但順序不同）。

- 用 i 傳入遞迴，讓我們能從目前 index 繼續選，達到「可以重複使用數字」的需求。

### 🌳 回溯樹狀圖解
以 candidates = [2, 3, 6, 7]，target = 7 為例的回溯樹狀圖解：
```mathematica
Start: []
├── Choose 2 → [2]
│   ├── Choose 2 → [2, 2]
│   │   ├── Choose 2 → [2, 2, 2]
│   │   │   ├── Choose 2 → [2, 2, 2, 2] (Sum = 8 > 7) → Backtrack
│   │   │   └── Choose 3 → [2, 2, 2, 3] (Sum = 9 > 7) → Backtrack
│   │   └── Choose 3 → [2, 2, 3] (Sum = 7) → ✅ Add to result
│   └── Choose 3 → [2, 3] (Sum = 5)
│       ├── Choose 3 → [2, 3, 3] (Sum = 8 > 7) → Backtrack
│       └── Choose 6 → [2, 3, 6] (Sum = 11 > 7) → Backtrack
├── Choose 3 → [3]
│   ├── Choose 3 → [3, 3] (Sum = 6)
│   │   └── Choose 3 → [3, 3, 3] (Sum = 9 > 7) → Backtrack
│   └── Choose 6 → [3, 6] (Sum = 9 > 7) → Backtrack
├── Choose 6 → [6]
│   └── Choose 6 → [6, 6] (Sum = 12 > 7) → Backtrack
└── Choose 7 → [7] (Sum = 7) → ✅ Add to result
```
#### 🧠 解釋說明
- 每個節點代表一次選擇，從 candidates 中選擇一個數字加入當前組合。

- 若當前組合的總和等於 target，則將該組合加入結果列表。

- 若總和超過 target，則回溯（Backtrack），撤銷上一次選擇，嘗試其他可能。

- 透過這種方式，探索所有可能的組合，找到所有符合條件的解。

#### ✅ 結果
- 根據上述回溯過程，我們找到的所有符合條件的組合為：

    - [2, 2, 3]

    - [7]

---

## ⏱ 時間與空間複雜度 | Complexity
| 分析項目  | 數值                           |
| ----- | ---------------------------- |
| 時間複雜度 | O(2^target) — 每個分支都有選與不選兩種可能 |
| 空間複雜度 | O(target) — 遞迴深度與目標值成正比      |

---

## 📌 學習重點 | What I Learned
- 回溯是一種探索所有可能解法的有效技巧，尤其適合「所有組合」這類題目。

- 寫法中 path.pop() 是實現回溯的關鍵動作。

- 用 start 控制遞迴層級避免重複組合。

- 注意剪枝條件 if remaining < 0，可以有效優化程式。