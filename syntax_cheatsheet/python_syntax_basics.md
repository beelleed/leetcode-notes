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

