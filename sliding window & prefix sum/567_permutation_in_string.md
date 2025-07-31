# 🔄 LeetCode 567 – Permutation in String (全排列子串判定)
🔗 [題目連結](https://leetcode.com/problems/permutation-in-string/)

---

## 題目描述 | Problem Description  
- 給定兩個字串 `s1` 和 `s2`，判斷 `s2` 是否包含 `s1` 的任一排列作為子字串。  
- Given strings `s1` and `s2`, check if `s2` contains any permutation of `s1` as a substring.

### Examples
- Example 1:

    - Input: s1 = "ab", s2 = "eidbaooo"
    - Output: true
    - Explanation: s2 contains one permutation of s1 ("ba").
- Example 2:

    - Input: s1 = "ab", s2 = "eidboaoo"
    - Output: false

---

## 🧠 解題思路 | Problem Solving Approach

### 中文說明：

這題的關鍵在於利用滑動窗口（Sliding Window）與字元統計（Counter）技巧：

1. 計算 `s1` 中每個字元的出現次數，記錄在 `need` 字典中。
2. 建立一個長度為 `len(s1)` 的滑動窗口，在 `s2` 上向右滑動。
3. 使用另一個字典 `window` 來記錄當前窗口內的字元頻率。
4. 每次移動窗口：
   - 加入新的右邊字元（更新 `window`）
   - 移除左邊多出來的字元（保持長度一致）
   - 比較 `window` 與 `need` 是否完全相同
5. 若找到一個相同的窗口，即表示找到了 `s1` 的排列，回傳 `True`

### English Explanation:

The key to this problem is using the **sliding window** technique combined with character frequency counting:

1. Count the frequency of each character in `s1` and store it in a `need` dictionary.
2. Use a fixed-size window of `len(s1)` and slide it over `s2`.
3. Maintain a `window` dictionary that keeps track of character counts inside the current window.
4. For each new character added:
   - Update the count in `window`
   - Remove the leftmost character if window size exceeds `len(s1)`
   - Compare `window` and `need` to see if they match
5. If a matching window is found, return `True` immediately.

✅ Otherwise, return `False` after scanning through the string.

---

## Python 實作範例

```python
from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        len1, len2 = len(s1), len(s2)
        if len1 > len2:
            return False

        need = Counter(s1)
        window = Counter(s2[:len1])

        if window == need:
            return True

        for i in range(len1, len2):
            # 加入右邊字元
            window[s2[i]] += 1
            # 移除左邊字元
            left_char = s2[i - len1]
            window[left_char] -= 1
            if window[left_char] == 0:
                del window[left_char]

            # 檢查是否符合
            if window == need:
                return True

        return False
```
```python
len1, len2 = lwn(s1), len(s2)
if len1 > len2:
    return False
```
- 基本檢查：若 s1 比 s2 還長，代表根本不可能有排列存在，直接回傳 False
```python
need = Counter(s1)
```
-  建立一個 need 字典，記錄 s1 每個字元出現的次數，這是「目標頻率」。
```python
window = Counter(s2[:len1])
```
- 建立初始視窗，抓 s2 的前 len(s1) 個字元，並計算其頻率
```python
if window == need:
    return True
```
- 若剛好一開始的視窗就和 s1 的排列一樣，直接回傳 True
```python
for i in range(len1, len2):
```
- 開始滑動視窗：從第 len1 個字元（視窗右邊界）開始往右移動
```python
window[s2[i]] += 1
```
- 加入新的字元（右邊界）
```python
left_char = s2[i - len1]
window[left_char] -= 1
if window[left_char] == 0:
    del window[left_char]
```
-  移除視窗左邊的字元（使視窗長度保持為 len(s1)）

    - 如果某字元減到 0，從字典中刪除，保持 window 精簡，方便比較
```python
if window == need:
    return True
```
- 每次滑動後，檢查視窗頻率是否與目標一致 → 若一致代表有排列 → 回傳 True
```python
return False
```
-  如果全部滑完還沒找到符合的視窗，就回傳 False

---

## 📊 流程圖 | Flowchart
```pgsql
Start
 ↓
若 len(s1) > len(s2) → 回傳 False
If len(s1) > len(s2) → return False
 ↓
建立 s1 的字元頻率表 need = Counter(s1)
Build frequency dict of s1 → need = Counter(s1)
 ↓
初始化 window = Counter(s2[:len1])
Initialize the first window of s2
 ↓
window == need ?
 ↙           ↘
True        False
↓             ↓
Return True  開始滑動窗口（從 index = len1 開始）
             Start sliding window (from index = len1)
 ↓
每次加入 s2[i] 到 window
Add s2[i] to window
 ↓
移除 s2[i - len1] 從 window（左邊界）
Remove s2[i - len1] from window (left boundary)
 ↓
window == need ?
 ↙           ↘
True        False
↓             ↓
Return True  繼續下一輪迴圈
             Continue loop
 ↓
結束迴圈後都沒找到 → 回傳 False
Return False if no match found
```

---

## ⏱ 時間與空間複雜度 | Time and Space Complexity

### 時間複雜度（Time Complexity）

- 初始建立 `Counter(s1)` 與 `Counter(s2[0:len(s1)])`：O(n)，其中 n = len(s1)
- 接下來遍歷 `s2` 的長度為 m，每次滑動窗口進行：
  - 加入新字元 O(1)
  - 移除舊字元 O(1)
  - 比較兩個 Counter → 最多 26 種小寫字母 → O(1)
- 總時間複雜度：**O(m + n)**，其中 m = len(s2)，n = len(s1)

### 空間複雜度（Space Complexity）

- 使用兩個 Counter，最多儲存 26 種小寫字母 → O(1)
- 不需額外資料結構（空間固定）

✅ 所以最終空間複雜度為：**O(1)**

---

## 📚 我學到了什麼 | What I Learned
### 🧠 中文總結：
- 滑動窗口技巧能高效處理「子字串比對」類型問題。

- **Counter（字元頻率表）**可以快速判斷排列關係。

- 固定長度窗口搭配加入 / 移除機制，避免重複計算。

- 記得控制視窗大小！這題必須保持與 s1 相同長度。

### 💡 English Summary:
- Learned how to use the sliding window technique to solve substring matching problems efficiently.

- Used Counter to compare character frequency for permutation detection.

- Maintaining a fixed-size window avoids unnecessary recomputation.

- Always manage the window size to match the length of s1.