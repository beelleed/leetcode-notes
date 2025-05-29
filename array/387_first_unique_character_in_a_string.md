
#  387. First Unique Character in a String

[題目連結](https://leetcode.com/problems/first-unique-character-in-a-string/)

---

## 📌 題目描述 | Problem Description

### 中文：
給定一個只包含小寫英文字母的字串 `s`，請找出第一個只出現一次的字元，並回傳它的 index。如果沒有，請回傳 -1。

### English:
Given a string `s`, find the first non-repeating character in it and return its index. If it does not exist, return -1.

---
## 📌 解題思路 | Solution Strategy
    1.先統計每個字元出現的次數，使用 dictionary（HashMap）。

    2.再逐一檢查字串，找出第一個 count[char] == 1 的字元。

    3.使用 dict.get(key, default) 是避免 KeyError 的好技巧。

    4.這類題通常需要「兩次走訪」字串：第一次統計，第二次判斷。

---

## ✅ 解法：字元次數統計法（HashMap）

```python
class Solution:
    def firstUniqChar(self, s: str) -> int:
        count = {}
        for c in s:
            count[c] = count.get(c, 0) + 1

        for i, c in enumerate(s):
            if count[c] == 1:
                return i

        return -1
```

## ✅ 中英文逐行解釋
| 程式碼                              | 中文說明               | English Description              |
| -------------------------------- | ------------------ | -------------------------------- |
| `count = {}`                     | 初始化字典用來計數          | Create a dict to store frequency |
| `count[c] = count.get(c, 0) + 1` | 若字元存在就 +1，否則從 0 開始 | Use `get()` to avoid KeyError    |
| 第二個 `for`                        | 找第一個出現次數為 1 的字元    | Find the first char with count 1 |

## 🧠 重點觀念
- 使用 dict.get(key, default) 是安全的計數方法

- 題目常見模式：兩次走訪字串（第一次統計，第二次找目標）

- 若 dict[c] == 1，即為第一個唯一字元

## ⏱ 時間與空間複雜度
- 時間：O(n)

- 空間：O(1)（最多 26 個小寫英文字母）

## 🧠 學到的東西 | What I Learned
- 這題不能用 Sliding Window，因為不是找「連續區間」

- 字串出現次數的統計可以用 dict.get() 快速完成
