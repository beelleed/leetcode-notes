## 003. Longest Substring Without Repeating Characters
LeetCode Link: https://leetcode.com/problems/longest-substring-without-repeating-characters/

## 🧩 題目描述 | Problem Description
中文：給定一個字串 s，請找出不包含重複字元的「最長子字串」的長度。

EN：Given a string s, find the length of the longest substring without repeating characters.

---

## 💡 解題思路說明 | Logic Explanation

中文：

1.用雙指標 left 和 right 維持一個「無重複字元」的視窗。

2.若 s[right] 重複，就從左邊開始移除直到合法。

3.每次更新最大長度 right - left + 1。

English:

1.Use two pointers to maintain a sliding window with unique characters.

2.If s[right] is already in the window, shrink it from the left.

3.Update max_len each time with right - left + 1.

---

## ✅ 正確解法：滑動視窗 + Set | Sliding Window + Set

``` python
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        left = 0
        max_len = 0

        for right in range(len(s)):
            while s[right] in seen:
                seen.remove(s[left])
                left += 1
            seen.add(s[right])
            max_len = max(max_len, right - left + 1)

        return max_len
```

```python
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        left = 0
        max_len = 0

        for right, ch in enumerate(s):
            while ch in seen:
                seen.remove(s[left])
                left += 1
            seen.add(ch)
            max_len = max(max_len, right - left + 1)

        return max_len
```

---

## 範例 | Example

s = "abcabcbb"

| right | char | seen        | left | 視窗  | ans |
| ----- | ---- | ----------- | ---- | --- | --- |
| 0     | a    | {a}         | 0    | a   | 1   |
| 1     | b    | {a,b}       | 0    | ab  | 2   |
| 2     | c    | {a,b,c}     | 0    | abc | 3   |
| 3     | a    | 重複 → 移 left | 1    | bca | 3   |
| 4     | b    | 重複 → 移 left | 2    | cab | 3   |


## ⏱️ 時間與空間複雜度 | Time & Space Complexity

時間：O(n)，每個字元最多進 set / 出 set 一次

空間：O(min(n, 字元種類數))，最壞情況為整個字串無重複

---

## ❌ 錯誤版本與問題分析 | Wrong Approach and Explanation

``` python
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        left = 0
        max_len = 0
        for right in range(len(s)):
            while s[right] not in seen:
                seen.add(s[right])
                max_len = max(max_len, right - left + 1)
        return max_len
```

---

## 🧨 問題說明 | What's Wrong?

1.while 條件只處理「非重複情況」，當字元重複時不會進入 while，什麼都沒做。

2.沒有處理 seen 中的重複字元 → 不收縮視窗 → 重複仍然存在。

3.left 沒有更新 → 無法保證當前視窗是合法的不重複子字串。

4.right 是 for 控制的，所以雖然 while 不執行，right 還是會往下跑。

## 🧪 錯誤案例分析 | Wrong Example Walkthrough
輸入 s = "pwwkew"，正確答案是 3（"wke"），但這段錯誤的程式碼流程如下：

right=0, 'p' ➜ 加入 set, 長度=1 ✅

right=1, 'w' ➜ 加入 set, 長度=2 ✅

right=2, 'w' ➜ already in set → while 不成立 → ❌ 不做任何事

right=3, 'k' ➜ 加入 set, 長度=4 ❌

right=4, 'e' ➜ 加入 set, 長度=5 ❌

right=5, 'w' ➜ again duplicate → 跳過

🛑 結果錯誤地回傳了 5，原因在於視窗未正確縮小。

### 錯誤方法二
```python
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        seen = set()
        left = 0
        max_len = 0
        for right in range(n):
            if s[right] in seen:
                seen.remove(s[left])
                left += 1
            seen.add(s[right])
            max_len = max(max_len, right - left + 1)
        return max_len
```
#### 1️⃣ if 在做什麼？
```python
if s[right] in seen:
    ...
```

- 語意是： 「如果現在違規一次，我就修正一次」

👉 不保證修完

#### 2️⃣ while 在做什麼？
```python
while s[right] in seen:
    ...
```

- 語意是： 「只要還違規，我就一直修，直到合法為止」

👉 保證修到合法狀態

#### 3️⃣ Sliding Window 的核心不變量（超重要）

>>不變量（Invariant）：
>>seen 裡的字元，永遠不能有重複

- while 版本：

    - 每一輪結束後 👉 不變量一定成立

- if 版本：

    - 每一輪結束後 👉 不變量「可能還是壞的」

#### 4️⃣ 用一句話記住（這句一定要背）

>>if 是「嘗試修一次」，
>>while 是「修到條件成立為止」

- 在 sliding window 題目中：

    - 只要你是在「修正違規」

    - 99% 都要用 while

---


## 📌 額外筆記建議（Extra Notes）| Notes and Takeaways

1.i = left, j = right：視窗的兩端

2.滑動視窗通則：「右邊擴張，左邊在需要時收縮」

3.為什麼需要收縮視窗？為了保證 set 中沒有重複字元，符合題目要求

---
## 🧠 我學到的重點 | What I Learned
- while not in set: 看似合理，其實是錯的思維

- 滑動視窗題目一定要搭配「縮窗邏輯」

- set 是很適合這種「唯一性檢查」的資料結構