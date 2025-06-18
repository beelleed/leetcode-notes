# Python 解題語法速查表

Python 語法速查清單。  
適用於：Stack、Dict、Set、DP 陣列、邏輯判斷與常見資料處理。

---

## ✅ Stack（堆疊操作）

```python
stack = []              # 建立空 stack
stack.append(x)         # 加入元素（push）
stack.pop()             # 拿出最後一個元素（pop）
stack[-1]               # 看 stack 頂端元素（不刪）
if not stack:           # 判斷 stack 是否為空
```

---
## ✅ Dict（字典對應）

```python
mapping = {')': '(', ']': '[', '}': '{'}
if key in mapping:      # 判斷 key 是否存在
value = mapping[key]    # 取出對應的 value
```

---
## ✅ Set（集合操作）

```python
seen = set()            # 建立空集合
seen.add(x)             # 加入元素
if x in seen:           # 是否出現過
```

---

## ✅ 常見 Loop 結構

```python
for i in range(len(nums)):      # 走訪 index
for i, val in enumerate(nums): # 同時拿 index + 值（最常用）
```

---

## ✅ String 操作技巧

```python
s[::-1]                # 字串反轉
s.isdigit()            # 是否為數字
s.isalpha()            # 是否為字母
if s == s[::-1]:       # 判斷是否為回文
``` 

---

## ✅ DP 常見語法

```python
dp = [0] * (n+1)       # 建立 dp 陣列，初始為 0
dp[i] = max(dp[i-1], ...)  # 狀態轉移
```

---

## ✅ 判斷結構與技巧

```python
if not stack or stack[-1] != x:  # 空或不匹配（括號題常用）
if target - num in hashmap:      # two sum 技巧
```

---

## Python 字串切片技巧：`haystack[i:i + len(needle)]`

### 🔍 語法說明 | Syntax Explanation

```python
haystack[i:i + len(needle)]
```

這是 Python 中的字串切片語法，意思是：

- 從 haystack 中的 第 i 個位置開始（包含）

- 往後取 len(needle) 個字元

- 結果是 haystack 中的一段子字串

### 📘 舉例說明 | Example
```python
haystack = "leetcode"
needle = "code"
```
```python
i = 4
haystack[4:4 + len(needle)] → haystack[4:8]
```
haystack[4:8] ➜ code

因為：

    haystack[4] = "c"

    haystack[5] = "o"

    haystack[6] = "d"

    haystack[7] = "e"

注意：Python 切片是「前閉後開」的範圍，所以 end 的位置（8）不會包含在結果內。

### ✅ 使用時機 | When to Use

這種寫法常見於：

    - 比對子字串是否與目標字串相符（如題目 028）

    - 滑動視窗技巧中的固定長度視窗

### 📌 小技巧整理 | Key Takeaways

| 語法       | 說明                |
| -------- | ----------------- |
| `s[i:j]` | 取出 s 的第 i 到 j-1 位 |
| `s[:j]`  | 開始到第 j-1 位        |
| `s[i:]`  | 第 i 位到結尾          |
| `s[-1]`  | 最後一個字元            |

---

