# 🐍 Python Lambda 函式教學 | Lambda Function in Python

---

## ❓ 什麼是 Lambda？| What is Lambda?

在 Python 中，`lambda` 是一種「匿名函式（anonymous function）」，意思是：
- 不需要使用 `def` 命名函式
- 通常用於**一行內可完成的簡單邏輯**

In Python, `lambda` is an anonymous function. That means:
- It has no name (unlike regular functions)
- It's typically used for simple one-line operations

---

## 🧠 語法 | Syntax

```python
lambda 參數: 表達式
lambda arguments: expression
```
- lambda 會建立一個臨時函式

- 可以把它指定給變數、作為參數傳入其他函式

---

## 📌 基本範例 | Basic Examples
### 傳統函式
def add(x, y):
    return x + y

### lambda 寫法
add = lambda x, y: x + y
print(add(3, 4))  # 輸出 7

---

## 📦 常見用途 | Common Use Cases
1. 搭配 sorted() 排序 key
```python
pairs = [(1, 3), (2, 2), (3, 1)]
pairs.sort(key=lambda x: x[1])  # 根據第二個值排序
print(pairs)  # [(3, 1), (2, 2), (1, 3)]
```

2. 搭配 filter()、map()、reduce()
```python
nums = [1, 2, 3, 4, 5]
evens = list(filter(lambda x: x % 2 == 0, nums))  # 篩選偶數
print(evens)  # [2, 4]
```

---

## 📌 特性 | Features
| 特性      | 說明              |
| ------- | --------------- |
| 匿名函式    | 無需 `def`，適合臨時用途 |
| 單一表達式限制 | 只能寫一行運算邏輯       |
| 適合簡潔處理  | 非常適合當作排序條件或篩選器  |

---

## ✅ 什麼時候該用 lambda？
| 使用時機        | 建議                 |
| ----------- | ------------------ |
| 僅一行小邏輯，不重複用 | 👍 適合用 lambda      |
| 多行、重複使用邏輯   | ❗ 用 `def` 寫成一般函式更好 |

---

## 🧠 小結 | Summary
- lambda 是一種快速撰寫簡單函式的方式

- 常見於排序、篩選、轉換資料等場景

- 避免過度使用，保留可讀性是第一原則

