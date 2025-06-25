# 🐍 Python List Comprehension 筆記：`item for item` 教學

---

## 📖 什麼是 List Comprehension？

### 中文說明
List Comprehension（列表生成式）是一種 Python 簡潔寫法，用來快速建立一個新的 list。最常見形式為：

### English
List Comprehension is a Python syntax that allows you to generate a new list in a single line, often replacing traditional for-loops with a more concise expression:

```python
[new_item for item in iterable]
```
它能夠取代傳統的 for 迴圈與 .append() 寫法，讓程式更精簡、易讀。

## 🔍 基本語法格式
```python
[expression for item in iterable if condition (optional)]
```

## ✅ 常見範例與用法

1️⃣ 複製一個 List（Copy a List）
```python
nums = [1, 2, 3]
copy = [x for x in nums]
# ➜ [1, 2, 3]
```

## 2️⃣ 資料處理（平方）
```python
nums = [1, 2, 3]
squares = [x**2 for x in nums]
# ➜ [1, 4, 9]
```

## 3️⃣ 加入條件過濾（Filter）
```python
nums = [1, 2, 3, 4, 5]
even = [x for x in nums if x % 2 == 0]
# ➜ [2, 4]
```

## 4️⃣ 拆解 Tuple 結構
```python
pairs = [(1, 'a'), (2, 'b'), (3, 'c')]
first_column = [x for x, _ in pairs]
# ➜ [1, 2, 3]
```

## 5️⃣ LeetCode 實戰：Top K 頻率元素
```python
# 取出前 k 個最常出現的數字（只要數字，不要次數）
[item for item, _ in heapq.nlargest(k, count.items(), key=lambda x: x[1])]
```

## 📌 小技巧總表
| 目的            | 寫法範例                         |
| ------------- | ---------------------------- |
| 複製列表          | `[x for x in nums]`          |
| 每個元素平方        | `[x**2 for x in nums]`       |
| 篩選條件          | `[x for x in nums if x > 0]` |
| 只取 tuple 的第一欄 | `[x for x, _ in tuple_list]` |
| 結合函式/運算       | `[f(x) for x in nums]`       |

## 🧠 學習建議
- 熟練使用後可應用於：字串處理、資料轉換、矩陣展平、條件過濾

- 推薦搭配學習：

    - lambda

    - map() / filter()

    - zip() / enumerate()

## 📚 延伸閱讀
- LeetCode 常見應用題：

    347. Top K Frequent Elements

    451. Sort Characters by Frequency

    692. Top K Frequent Word