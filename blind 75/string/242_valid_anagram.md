# 🔤 LeetCode 242 – Valid Anagram
🔗 題目連結：[https://leetcode.com/problems/valid-anagram/](https://leetcode.com/problems/valid-anagram/)

---

## 📄 題目說明 | Problem Description

- **中文**：給兩個字串 `s` 和 `t`，判斷 `t` 是否是 `s` 的字母異位詞（anagram），也就是兩者包含完全一樣的字符及次數，只是順序可能不同。
- **English**: Given two strings `s` and `t`, determine if `t` is an anagram of `s` — that means `t` must use exactly the same characters with the same frequencies as `s`, though possibly in a different order.

### Examples
- Example 1:

    - Input: s = "anagram", t = "nagaram"

    - Output: true

- Example 2:

    - Input: s = "rat", t = "car"

    - Output: false

---

## 🧠 解題思路 | Solution Idea

- 如果兩字串長度不同 → 直接回傳 `false`  
- 用一個頻率表（hash map 或固定大小陣列針對特定字符集）記錄 `s` 中每個字符出現次數  
- 遍歷 `t`，對應字符在頻率表中減一，若某次變成負數 → `false`  
- 如果遍歷完畢且沒有錯誤 → 回傳 `true`

---

## 💻 程式碼實作 | Code

```python
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # 長度不同直接 false
        if len(s) != len(t):
            return False

        # 建頻率表
        freq = {}
        for ch in s:
            freq[ch] = freq.get(ch, 0) + 1

        # 減去 t 中字符
        for ch in t:
            if ch not in freq:
                return False
            freq[ch] -= 1
            if freq[ch] < 0:
                return False

        return True
```
### 1️⃣ 長度檢查
```python
if len(s) != len(t):
    return False
```
- 如果兩字串長度不同，一定不能是 anagram（異位字串），因為字符數量不一樣就不可能有一樣的頻率。

- 提前排除這種情況，可以提高效率。

### 2️⃣ 建立頻率表（Frequency Map）
```python
freq = {}
for ch in s:
    freq[ch] = freq.get(ch, 0) + 1
```
- freq 是一個字典，用來記錄每個字母在 s 裡出現的次數。

- freq.get(ch, 0) 的作用是：如果 ch 在字典中沒出現過，就拿 0；然後再 +1。

- 最後 freq[ch] 表示在 s 中，字母 ch 出現了多少次。
### 3️⃣ 遍歷 t 字串，減少頻率
```python
for ch in t:
    if ch not in freq:
        return False
    freq[ch] -= 1
    if freq[ch] < 0:
        return False
```
這部分是關鍵判斷：

- 檢查 ch in freq：如果 t 中有某個字母 ch 沒在 s 中出現過，那就不是 anagram → 直接回傳 False。

- 減少頻率 freq[ch] -= 1：表示「用掉一個」這個字符。

- 如果減後頻率變成負數：表示 t 用得比 s 擁有的還多 → 也不是 anagram → return False。
### 4️⃣ 全部過程無誤，回傳 True
```python
return True
```
- 如果遍歷完 t 的所有字符都沒有遇到 “沒有這個字符” 或 “頻率變負”的情況，代表 t 中每個字母都在 s 中有足夠的頻率 → 是 anagram。

---

## 🧪 範例

假設：
```ini
s = "anagram"
t = "nagaram"
```
### ✅ 步驟解說

1. 長度檢查
    len(s) = 7, len(t) = 7 → 長度相等，繼續。

2. 建立 freq 字典頻率表（用 s）
    遍歷字串 s = "anagram"：

    - 'a' → freq['a'] = 1

    - 'n' → freq['n'] = 1

    - 'a' → freq['a'] = 2

    - 'g' → freq['g'] = 1

    - 'r' → freq['r'] = 1

    - 'a' → freq['a'] = 3

    - 'm' → freq['m'] = 1

最後 freq 表為：
```arduino
{
  'a': 3,
  'n': 1,
  'g': 1,
  'r': 1,
  'm': 1
}
```
3. 遍歷字串 t（"nagaram"），扣減頻率：
| 處理字元 ch | 原 freq | 扣減後 freq\[ch] | 是否 < 0 或不存在？ |
| ------- | ------ | ------------- | ------------ |
| 'n'     | 1      | 0             | 否            |
| 'a'     | 3      | 2             | 否            |
| 'g'     | 1      | 0             | 否            |
| 'a'     | 2      | 1             | 否            |
| 'r'     | 1      | 0             | 否            |
| 'a'     | 1      | 0             | 否            |
| 'm'     | 1      | 0             | 否            |

在整個過程中，沒有字元是“不在 freq 字典中”，也沒有哪一次扣減後變成負值。

4. 全部處理完成 → 回傳 True。

---

## ⏱ 複雜度分析 | Complexity

- 時間複雜度 Time：O(n)，n 是字串長度。建頻率表 + 遍歷 t 都是線性

- 空間複雜度 Space：O(k)，k 是字符種類數（若只考慮小寫英文字母，k 最多 26，可視為常數）

---

## 📝 我學到了什麼 | What I Learned

- 使用字母頻率計數比排序更有效率，尤其在長度很大時

- 提早檢查長度或減一過程中發現頻率為負可以快速退出，加速程序

- 型別提示與簡潔字典操作使程式碼易讀又乾淨