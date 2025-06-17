# 🧠 Python min() / max() with key= 用法筆記
## 🔍 什麼是 min(strs, key=len)？

- 這是 Python 的一種進階寫法，意思是：

    - 對 strs 裡的每個字串 s

    - 用 len(s) 當作比較依據

    - 回傳長度最小的那一整個字串（而不是長度）

## ✅ 範例比較
```python
strs = ["apple", "banana", "kiwi"]

# 回傳 "kiwi"：因為長度最短
min(strs, key=len)

# 回傳 "banana"：因為長度最長
max(strs, key=len)
```

如果你只寫 min(strs)，會按照字母順序比較；加上 key=len 則按照長度比較。

## 📌 和 max(數字) 的差異？
| 用法                   | 比的是什麼 | 結果                       |
| -------------------- | ----- | ------------------------ |
| `max([1, 2, 3])`     | 數字大小  | `3`                      |
| `max(strs, key=len)` | 字串長度  | 長度最長的字串（e.g. `"banana"`） |
| `min(strs, key=len)` | 字串長度  | 長度最短的字串（e.g. `"kiwi"`）   |

##  延伸：key= 的其他應用

- 比較字串長度

- 比較物件的某個屬性

- 自訂排序條件時常見的技巧

```python
students = [
  {"name": "Alice", "score": 90},
  {"name": "Bob", "score": 85}
]
top = max(students, key=lambda x: x["score"])
# => 拿到 score 最高的 student dict
```

輸出結果會是：{"name": "Alice", "score": 90}

- 這行：top = max(students, key=lambda x: x["score"])

    - 對 students 裡的每個字典（{"name": ..., "score": ...}）

    - 用 lambda x: x["score"] 來當作比較的標準

    - 找出 score 最大的那個字典

- 如果你想要取出名字而不是整個字典，也可以寫：
```python
top_name = max(students, key=lambda x: x["score"])["name"]
# ➜ "Alice"
```