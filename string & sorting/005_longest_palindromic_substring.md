# 🔍 LeetCode 5 — Longest Palindromic Substring / 最長回文子字串
🔗 [題目連結](https://leetcode.com/problems/longest-palindromic-substring/)

---

## 📄 題目說明 | Problem Description

- **中文**：給你一個字串 `s`，請找出這個字串中 **最長的回文子字串**，並回傳該子字串。回文子字串指的是讀起來正反相同的連續子串。
- **English**: Given a string `s`, return the longest palindromic substring in `s`.

- **Examples**
    - Example 1:

        - Input: s = "babad"
        - Output: "bab"
        - Explanation: "aba" is also a valid answer.

- Example 2:

    - Input: s = "cbbd"
    - Output: "bb"

---

## 🧠 解題思路 | Solution Ideas

有幾種常見方法：

1. **中心擴展法（Expand Around Center）**  
   對每一個位置及每一對鄰近位置視為回文中心，向左右擴展判斷最大回文。時間複雜度 \(O(n^2)\)、空間 \(O(1)\)。

2. **動態規劃（DP）法**  
   用 2D 表 `dp[i][j]` 表示子字串 `s[i..j]` 是否為回文。若 `s[i] == s[j]` 且 `dp[i+1][j-1]` 為真，則 `dp[i][j] = True`。在構建時記錄最長回文的起點與長度。時間 \(O(n^2)\)，空間 \(O(n^2)\)。 :contentReference[oaicite:0]{index=0}

3. **Manacher’s 演算法**（線性時間）  
   較複雜但能在 \(O(n)\) 時間內解決，適用於字串長度大的情況。略過細節，這裡不深入講。 :contentReference[oaicite:1]{index=1}

---

## 💻 程式碼範例：中心擴展法（Expand Around Center）

```python
class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""
        start, end = 0, 0

        def expand(left: int, right: int) -> (int, int):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            # 回到最後一個合法的位置：left+1 到 right-1
            return left + 1, right - 1

        for i in range(len(s)):
            # 以 i 為中心的奇數長度回文
            l1, r1 = expand(i, i)
            # 以 i, i+1 為中心的偶數長度回文
            l2, r2 = expand(i, i + 1)

            if r1 - l1 > end - start:
                start, end = l1, r1
            if r2 - l2 > end - start:
                start, end = l2, r2

        return s[start : end + 1]
```

## 🔍 分段詳細解釋
class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""
        start, end = 0, 0

        def expand(left: int, right: int) -> (int, int):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            # 回到最後一個合法的位置：left+1 到 right-1
            return left + 1, right - 1

        for i in range(len(s)):
            # 以 i 為中心的奇數長度回文
            l1, r1 = expand(i, i)
            # 以 i, i+1 為中心的偶數長度回文
            l2, r2 = expand(i, i + 1)

            if r1 - l1 > end - start:
                start, end = l1, r1
            if r2 - l2 > end - start:
                start, end = l2, r2

        return s[start : end + 1]

---

## 🧪 根據程式碼的

s = "babad"

### 初始
```python
start, end = 0, 0  # 最長回文的起始與結束位置
```
### 🔁 i = 0
```python
expand(0, 0) → s[0] == s[0] → 'b'
→ left=-1, right=1 → 結束
→ 回傳 (0, 0) → 回文："b"

expand(0, 1) → s[0] != s[1] → 'b' ≠ 'a'
→ 回傳 (1, 0) → 無效區間
```

最大回文長度維持：start=0, end=0（"b"）

### 🔁 i = 1
```python
expand(1, 1) → s[1] == s[1] → 'a'
→ s[0] == s[2] → 'b' == 'b' → 成功
→ left=-1, right=3 → 結束
→ 回傳 (0, 2) → 回文："bab"

expand(1, 2) → s[1] ≠ s[2] → 'a' ≠ 'b'
→ 回傳 (2, 1)
```

新回文長度為 2（2-0），比舊的大 → 更新：
```python
start = 0, end = 2  → 回文："bab"
```
### 🔁 i = 2
```python
expand(2, 2) → s[2] == s[2] → 'b'
→ s[1] == s[3] → 'a' == 'a'
→ left=0, right=4 → s[0] ≠ s[4] → 'b' ≠ 'd'
→ 回傳 (1, 3) → 回文："aba"

expand(2, 3) → s[2] ≠ s[3] → 'b' ≠ 'a'
→ 回傳 (3, 2)
```

長度仍是 2（3-1），與現有一樣 → 保持 "bab" 或 "aba" 都可

### 🔁 i = 3
```python
expand(3, 3) → s[3] == s[3] → 'a'
→ s[2] ≠ s[4] → 'b' ≠ 'd'
→ 回傳 (3, 3) → 回文："a"

expand(3, 4) → s[3] ≠ s[4] → 'a' ≠ 'd'
→ 回傳 (4, 3)
```

無更長回文

### 🔁 i = 4
```python
expand(4, 4) → s[4] == s[4] → 'd'
→ s[3] ≠ s[5] → right 越界
→ 回傳 (4, 4) → 回文："d"

expand(4, 5) → right 越界
→ 回傳 (5, 4)
```

無更長回文

### ✅ 最後回傳：
```python
return s[start:end+1]  # s[0:3] → "bab"
```

也可能是 "aba"，依實作細節而定，但都是正確解。

---

## ⏱ 複雜度分析 | Complexity Analysis

- 時間複雜度：O(n²)，因為對每個位置做向外擴展可能長達 O(n)

- 空間複雜度：O(1)，僅使用常數額外空間

## ✍️ 我學到的東西 | What I Learned

- 中心擴展法很直觀，是處理回文子串常用的技巧，能兼顧奇數與偶數回文。

- 在擴展時要注意邊界檢查（left >= 0, right < len(s)）。

- 更新最長回文子串時比較 r1 - l1 vs end - start 而不是直接比較字串。

- 除了中心法與 DP，對於長字串可以考慮 Manacher’s 演算法來降時間複雜度。