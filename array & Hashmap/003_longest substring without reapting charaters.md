## 003. Longest Substring Without Repeating Characters
LeetCode Link: https://leetcode.com/problems/longest-substring-without-repeating-characters/

## 🧩 題目描述 | Problem Description
中文：給定一個字串 s，請找出不包含重複字元的「最長子字串」的長度。

EN：Given a string s, find the length of the longest substring without repeating characters.

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
## 💡 解題思路說明 | Logic Explanation

中文：

1.用雙指標 left 和 right 維持一個「無重複字元」的視窗。

2.若 s[right] 重複，就從左邊開始移除直到合法。

3.每次更新最大長度 right - left + 1。

English:

1.Use two pointers to maintain a sliding window with unique characters.

2.If s[right] is already in the window, shrink it from the left.

3.Update max_len each time with right - left + 1.

## ⏱️ 時間與空間複雜度 | Time & Space Complexity

時間：O(n)，每個字元最多進 set / 出 set 一次

空間：O(min(n, 字元種類數))，最壞情況為整個字串無重複

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