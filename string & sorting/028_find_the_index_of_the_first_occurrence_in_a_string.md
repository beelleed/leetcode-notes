# 028. Find the Index of the First Occurrence in a String  
[LeetCode 題目連結](https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/)

---

## 🧩 題目描述 | Problem Description

給定兩個字串 `haystack` 和 `needle`，找出 `needle` 第一次出現在 `haystack` 中的索引位置。若沒有出現，回傳 -1。  

Given two strings `haystack` and `needle`, return the index of the first occurrence of `needle` in `haystack`, or `-1` if `needle` is not part of `haystack`.

---

## ✅ 解法：使用字串切片比較 | Solution: Slicing Approach

```python
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        for i in range(len(haystack) - len(needle) + 1):
            if haystack[i:i + len(needle)] == needle:
                return i
        return -1
```

## 🔍 解題思路 | Solution Explanation
- 這題的核心是「固定長度的滑動視窗」比對

- 每次從 haystack 中截取長度與 needle 相同的子字串

- 比較該子字串與 needle 是否一致

- 一旦找到就回傳起始位置 i，否則最後回傳 -1

This solution uses a sliding window of length len(needle) to compare substrings in haystack.
If any substring matches needle, return the start index. Otherwise, return -1.

## ⏱️ 時間與空間複雜度 | Time & Space Complexity
- 時間複雜度 Time: O(n * m)（最壞情況需比較 n-m 次，每次比較 m 個字元）

- 空間複雜度 Space: O(1)

## 📌 學到的技巧 | Key Takeaways
- 字-串比較可以使用切片 str[i:i+len(sub)]

- 如果題目問「是否包含某段文字」或「找出索引」，可以嘗試這種滑動視窗技巧

- for i in range(len(...)) 是拿到索引的常見方法，避免直接 for char in str 無法取得 index