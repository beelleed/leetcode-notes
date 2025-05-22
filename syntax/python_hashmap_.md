# 🧠 Python HashMap 用法大全 | HashMap in Python Cheatsheet

---

## 🔰 什麼是 HashMap？

- Python 中的 `dict` 就是 HashMap（雜湊表），是一種以 **Key-Value** 形式儲存資料的資料結構。
- 常用於：
  - 記錄元素出現次數
  - 做條件判斷 / 快速查找
  - 計算差值、統計頻率、字元配對等

---

## 📌 基本操作 | Basic Usage

### 🔹 建立字典

```python
hashmap = {}  # 空字典
hashmap = {"a": 1, "b": 2}
```
## 🔹 讀取值
```python
value = hashmap["a"]        # 若 key 不存在，會報錯 KeyError
value = hashmap.get("a")    # 安全讀取，key 不存在則回傳 None
value = hashmap.get("a", 0) # key 不存在時，回傳預設值 0
```
## 🔹 設定 / 更新值
```python
hashmap["a"] = 3            # 若存在就更新，不存在就新增
```

## 🔄 出現次數統計常用技巧 | Count Frequency
## 🔸 標準寫法
```python

hashmap = {}
for x in nums:
    hashmap[x] = hashmap.get(x, 0) + 1
```
## 🔸 使用 defaultdict（更簡潔）
```python

from collections import defaultdict

hashmap = defaultdict(int)
for x in nums:
    hashmap[x] += 1
```
## ✅ 判斷是否存在某 key
``` python

if "a" in hashmap:
    print("found!")
```
## 🔁 遍歷 HashMap
```python

for key in hashmap:
    print(key, hashmap[key])

for key, val in hashmap.items():
    print(f"{key} => {val}")
```
## 💡 常見應用情境 | Common LeetCode Patterns
| 題型                      | 用法                                 |
| ----------------------- | ---------------------------------- |
| 計數字元 / 數字出現次數           | `hashmap[x] = hashmap.get(x, 0)+1` |
| Two Sum 類型              | `target - num in hashmap`          |
| Prefix Sum 差值計算         | `if prefix_sum - k in hashmap`     |
| 字串異位詞（Anagram）          | 字元頻率比對                             |
| 字元配對（Valid Parentheses） | `mapping = {')':'(', ']' :'['}`    |

## ✅ 總結
HashMap 是刷題中最常用的資料結構之一，學會以下幾招就能解很多題：

get(key, default) 避免 KeyError

prefix_sum - k in hashmap → 用於找差值是否出現

頻率統計搭配 += 1

defaultdict(int) / defaultdict(list) 是超好用的升級寫法！