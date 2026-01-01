# 🔍 LeetCode 767 – Reorganize String

[題目連結](https://leetcode.com/problems/reorganize-string/)

---

## 📘 題目說明 | Problem Description
### 中文：

給定一個字串 s，請重新排列字元，使得任意兩個相鄰字元都不相同。若無法做到，回傳空字串 ""。

### English:

Given a string s, rearrange the characters so that no two adjacent characters are the same.
If not possible, return an empty string.

### Examples

- Example 1:

    - Input: s = "aab"

    - Output: "aba"

- Example 2:

    - Input: s = "aaab"

    - Output: ""

---

## 💡 解題思路 | Solution Idea
- 核心觀察

    - 若某個字元出現次數過多，其他字元不足以把它隔開，則一定無解。

    - 若可行，則需要一種方式：

        - 每一步都選擇「目前剩餘次數最多、且不等於上一個字元」的字元。

- 使用策略

    - Greedy（貪婪）：優先處理最危險（次數最多）的字元

    - Max Heap / Priority Queue：快速取得目前剩餘最多的字元

    - prev 技巧：避免相鄰放到同一個字元

---

## 🧠 可行性判斷 | Feasibility Check
- 設：

    - n = len(s)

    - maxFreq = 字元最大出現次數

- 為什麼需要？

    - 要隔開 maxFreq 個相同字元，需要：

        - maxFreq - 1 個「其他字元」作為隔板

        - 而實際只有 n - maxFreq 個其他字元

### ❌ 不可能條件
```text
maxFreq - 1 > n - maxFreq
```

等價於：
```text
maxFreq > (n + 1) // 2
```

👉 一旦成立，直接回傳 ""

---

## 🧾 程式碼 | Python Code
```python
from collections import Counter
import heapq

class Solution:
    def reorganizeString(self, s: str) -> str:
        if not s:
            return ""

        count = Counter(s)
        n = len(s)
        maxFreq = max(count.values())

        # Feasibility check
        if n - maxFreq < maxFreq - 1:
            return ""

        # Build max heap
        heap = []
        for ch, freq in count.items():
            heapq.heappush(heap, (-freq, ch))

        res = []
        prev_freq, prev_ch = 0, ""

        while heap:
            freq, ch = heapq.heappop(heap)
            res.append(ch)

            # Push back previous char if still available
            if prev_freq < 0:
                heapq.heappush(heap, (prev_freq, prev_ch))

            # Use one occurrence of current char
            freq += 1
            prev_freq, prev_ch = freq, ch

        # Safety check
        if prev_freq < 0:
            return ""

        return "".join(res)
```
---

## 🔍 程式逐步解析 | Step-by-Step Explanation
```python
count = Counter(s)
```

- 統計每個字元出現次數。

```python
if n - maxFreq < maxFreq - 1:
    return ""
```

- 提前排除「理論上不可能」的情況。

```python
heapq.heappush(heap, (-freq, ch))
```

- 使用負號模擬 max heap，確保每次取出剩餘次數最多的字元。

```python
prev_freq, prev_ch = 0, ""
```

- 記錄「上一輪用過的字元」，避免馬上再用。

```python
freq, ch = heapq.heappop(heap)
res.append(ch)
```

- 取出目前剩餘最多的字元並加入結果。

```python
if prev_freq < 0:
    heapq.heappush(heap, (prev_freq, prev_ch))
```

- 將上一個字元放回 heap（若還有剩）。

```python
freq += 1
prev_freq, prev_ch = freq, ch
```

- 用掉一次當前字元（負數向 0 靠近），並設為新的 prev。

```python
if prev_freq < 0:
    return ""
```

- Safety check：避免最後只剩一個無法隔開的字元。

---

## 🔍 範例解析 | Example Walkthrough
```python
s = "aaabbc"
```

### 初始 count

- a:3, b:2, c:1

### 初始 heap（概念上）

- [(-3,'a'), (-2,'b'), (-1,'c')]
- prev = (0,'')
- res = []

---

### Round 1

1. pop → (-3,'a')

2. res = ['a']

3. prev 沒剩（0）→ 不 push

4. freq += 1 → -2

5. prev = (-2,'a') heap 剩：[(-2,'b'), (-1,'c')]

---

### Round 2

1. pop → (-2,'b')

2. res = ['a','b']

3. prev 有剩（-2）→ push (-2,'a')

4. freq += 1 → -1

5. prev = (-1,'b') heap：[(-2,'a'), (-1,'c')]

---

### Round 3

1. pop → (-2,'a')

2. res = ['a','b','a']

3. push prev (-1,'b')

4. freq += 1 → -1

5. prev = (-1,'a') heap：[(-1,'b'), (-1,'c')]

---

### Round 4

1. pop → (-1,'b')

2. res = ['a','b','a','b']

3. push prev (-1,'a')

4. freq += 1 → 0

5. prev = (0,'b') heap：[(-1,'a'), (-1,'c')]

---

### Round 5

1. pop → (-1,'a')

2. res = ['a','b','a','b','a']

3. prev 是 0 → 不 push

4. freq += 1 → 0

5. prev = (0,'a') heap：[(-1,'c')]

---

### Round 6

1. pop → (-1,'c')

2. res = ['a','b','a','b','a','c']

3. prev 是 0 → 不 push

4. freq += 1 → 0

5. prev = (0,'c') heap：[]

- 結束：heap 空且 prev_freq=0 → OK
- 答案可能是 "ababac"（合法）

---

## ⏱ 複雜度分析 | Time & Space Complexity
| 項目    | 複雜度          |
| ----- | ------------ |
| 時間複雜度 | `O(n log σ)` |
| 空間複雜度 | `O(σ)`       |

σ = 不同字元數（英文小寫字母時 ≤ 26）

---

## ⚠️ 常見錯誤 | Common Pitfalls

- ❌ 用「字元種類數」判斷可不可行

- ❌ feasibility 寫成 <=（會錯殺 "aaabc"）

- ❌ pop 後立刻 push 回 heap（會重複字元）

- ❌ 忘記 freq 是負數（應該 freq += 1）

- ❌ 忘記最後 join 或 safety check

---

## 📚 我學到了什麼 | What I Learned

- 是否可行取決於「數量能不能隔開」，而不是字元種類。

- prev 技巧是避免相鄰重複的關鍵。

- Greedy + Heap 是處理「重新排列 / 排程」問題的通用模板。

- Feasibility check 是 necessary condition，safety check 是 defensive programming。

### 🎯 面試 30 秒標準講法

“I first count character frequencies.
If the maximum frequency minus one is greater than the number of remaining characters, it’s impossible.
Otherwise, I use a greedy approach with a max heap, always picking the character with the highest remaining count while holding back the previously used character to avoid adjacency.”