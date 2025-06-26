# 🔗 Python `''.join()` 用法 | String Join in Python

## 📘 基本語法 | Syntax

```python
'連接符號'.join(可迭代物件)
```
| 元素       | 中文說明            | English Description               |
| -------- | --------------- | --------------------------------- |
| `''`     | 欲使用的連接字串（常為空字串） | The string to join with (e.g. '') |
| `join()` | 方法名稱            | Method name                       |
| iterable | 一串字串列表          | A list of strings to combine      |

## 🧪 範例 | Examples
```python
res = ['a', 'b', 'c']
''.join(res)     ➜ 'abc'
'-'.join(res)    ➜ 'a-b-c'
' '.join(res)    ➜ 'a b c'
```
## ❌ 與 + 的差異 | Why not use +?
錯誤但常見的做法：
```python
result = ''
for ch in res:
    result += ch
```
- 缺點：每次 += 都會產生新的字串，效能差（O(n²)）

正確高效的做法：
```python
''.join(res)
```
- 優點：內部使用記憶體最佳化，效能高（O(n)）

## 🧰 LeetCode 常見用法 | LeetCode Usage

1️⃣ 字元頻率排序題
```python
''.join([ch * freq for ch, freq in sorted_items])
```

2️⃣ 列表拼字
```python
words = ['hello', 'world']
' '.join(words) ➜ 'hello world'
```

3️⃣ 字元逆序
```python
s = "abc"
''.join(reversed(s)) ➜ 'cba'
```

## 🧠 常見錯誤 | Common Mistakes
| 錯誤類型          | 原因與說明                             |
| ------------- | --------------------------------- |
| `TypeError`   | 要 `join` 的必須是「字串列表」，不能是 int 或混合類型 |
| 使用 `+` 串接大量字串 | 效能差，會不必要建立多個中間字串                  |

## ✅ 小結 | Summary
- ''.join(res) 是 Python 處理字串拼接的 標準且推薦寫法

- 對比 + 來說效能更好、語法更簡潔

- 在 LeetCode 中的字串處理題、頻率排序、token 合併等場景中非常常見

## 📚 延伸學習 | Further Reading
- LeetCode 題目：

    - 451.Sort Characters by Frequency

    - 344.Reverse String

    - 6.Zigzag Conversion