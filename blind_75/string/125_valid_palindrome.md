#  Palindrome Checker | 有效迴文判斷 — LeetCode 125

[LeetCode 題目連結](https://leetcode.com/problems/valid-palindrome/)

---

## 📘 題目說明 | Problem Description

- **中文：**  
  給定一個字串 `s`，請判斷它是否為**有效的迴文**（Palindrome）。在判斷的過程中，需忽略非字母數字字元，並且不區分大小寫。

- **English:**  
  Given a string `s`, return `true` if it is a palindrome, or `false` otherwise. When checking, **ignore non-alphanumeric characters** and **case differences**.

### Examples
- Example 1:

    - Input: s = "A man, a plan, a canal: Panama"
    - Output: true
    - Explanation: "amanaplanacanalpanama" is a palindrome.

- Example 2:

    - Input: s = "race a car"
    - Output: false
    - Explanation: "raceacar" is not a palindrome.

- Example 3:

    - Input: s = " "
    - Output: true
    - Explanation: s is an empty string "" after removing non-alphanumeric characters. Since an empty string reads the same forward and backward, it is a palindrome.
 
---

##  🧠 解題思路 | Solution Idea

### 中文思路：
1. 使用 **雙指標（Two Pointers）** 技巧，從字串左右兩端同時向中間遍歷。
2. 左指標 `l` 往右，右指標 `r` 往左。
   - 遇到非字母數字字符就跳過（`isalnum()` 用來判斷）。
   - 兩邊都是合法字符後再轉成小寫比對。
3. 若某一對字符不同，就不是迴文，立即回傳 `False`。
4. 若左右指標交錯或相遇且未發現不同字符，就可以確定是迴文。

### English Explanation:
1. Initialize two pointers (`left`, `right`) at ends of the string.
2. Move them inward:
   - Skip non-alphanumeric characters using `isalnum()`.
   - Compare lowercase versions of characters.
3. If a mismatch is found, return `False`.
4. If pointers cross without mismatches, return `True`.

---

##  Python 程式碼 | Code

```python
class Solution:
    def isPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1

        while left < right:
            # Skip non-alphanumeric characters
            while left < right and not s[left].isalnum():
                left += 1
            while left < right and not s[right].isalnum():
                right -= 1

            # Compare case-insensitive
            if s[left].lower() != s[right].lower():
                return False

            left += 1
            right -= 1

        return True
```
### 🔍 每行程式碼解析
```python
left, right = 0, len(s) - 1
```
- 初始化左右指標。

- left 從開頭開始，right 從結尾開始。
```python
while left < right:
```
- 當左右指標尚未交錯，繼續迴圈。
```python
while left < right and not s[left].isalnum():
    left += 1
```
- 如果左邊字符不是英數（例如空白、標點符號等），就跳過它。
```python
while left < right and not s[right]. isalnum():
    right -= 1
```
- 同樣，若右邊不是英數，也跳過它。
```python
if s[left].lower() != s[right].lower():
    return False
```
- 比較左右兩邊的「小寫字元」

- 如果不同 → 不是迴文 → 直接回傳 False
```python
left += 1
right -= 1
```
- 如果相同 → 移動指標，繼續比對下一組字元。
```python
return True
```
- 如果迴圈正常結束，表示每組字元都相等 → 是迴文！

---

## 🔁 範例說明
```python
s = "A man, a plan, a canal: Panama"
```
初始化：
```python
left = 0                     # 指向 'A'
right = len(s) - 1 = 29      # 指向 'a'
```
### 🔁 第 1 次外層 while 迴圈

- s[left] = 'A' 是英數 ✅

- s[right] = 'a' 是英數 ✅

- 比較：'A'.lower() == 'a'.lower() → ✅

- 移動：left = 1, right = 28

### 🔁 第 2 次

- s[1] = ' ' 空格 ❌ → left += 1 → 2

- s[2] = 'm' 是英數

- s[28] = 'm' 是英數

- 比較：'m' == 'm' ✅

- 移動：left = 3, right = 27

### 🔁 第 3 次

- s[3] = 'a', s[27] = 'a' ✅ → 相等

- left = 4, right = 26

### 🔁 第 4 次

- s[4] = 'n', s[26] = 'n' ✅ → 相等

- left = 5, right = 25

### 🔁 第 5 次

- s[5] = ',' 不是英數 ❌ → left += 1 → 6

- s[6] = ' ' 空格 ❌ → left += 1 → 7

- s[7] = 'a', s[25] = 'a' ✅

- left = 8, right = 24

### 🔁 後面繼續這樣比對，直到：

- left = 15

- right = 15

- 兩者相遇，說明所有相對位置字符皆符合條件

## ✅ 最後
```python
return True
```

### 📌 小筆記
| 流程階段     | 操作                  | 結果 |
| -------- | ------------------- | -- |
| 跳過空格、符號  | `isalnum()`         | ✅  |
| 忽略大小寫    | `lower()`           | ✅  |
| 從兩端往中間走  | `left++`, `right--` | ✅  |
| 比對不一致時結束 | `return False`      | ✖  |
| 比對完成沒錯誤  | `return True`       | ✅  |

---

### 🧩 關鍵技巧

- isalnum()：判斷字元是否為英文字母或數字

- .lower()：讓比較時不區分大小寫

- 雙指標：從兩側往中間靠攏，適合處理對稱性問題

---

## ⏱ 複雜度分析 | Time & Space Complexity
| 分析項目  | 複雜度               |
| ----- | ----------------- |
| 時間複雜度 | `O(n)`，單次遍歷整個字串   |
| 空間複雜度 | `O(1)`，僅使用了少量指標變數 |

---

## 📌 我學到了什麼 | What I Learned
### 中文：

- 在對字串做 palindrome 檢查時，雙指標是一個非常有效的方法。

- 使用 isalnum() 可以輕易跳過不重要的字符，讓程式只 focus 在字母或數字上。

- 比較時用 .lower() 可確保 case-insensitive，而且在回文問題中常常這樣做。

### English:

- Two-pointer technique is efficient for palindromic checks (outside-in comparison).

- Helper method isalnum() simplifies skipping non-alphanumeric characters.

- Converting to lowercase ensures comparisons are case-insensitive—a common requirement in palindrome problems.