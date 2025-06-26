# 🧠 Python 字串乘法 × 列表生成式 筆記 | String Multiplication & List Comprehension

## 📘 基本語法 | Basic Syntax

### 中文
在 Python 中，可以直接對字串使用乘法 `*`，將字串重複多次。

### English
In Python, you can use `*` to repeat a string multiple times.

```python
"abc" * 3  ➜ "abcabcabc"
```

## ✅ 常見搭配：ch * freq for ch, freq in ...
範例：
```python
sorted_items = [('a', 3), ('b', 2)]
[ch * freq for ch, freq in sorted_items]
# ➜ ['aaa', 'bb']
```
再用 join() 拼接：
```python
''.join([ch * freq for ch, freq in sorted_items])
# ➜ 'aaabb'
```

## 🧠 常見用途 | Common Use Cases
| 用途（中文）     | Python 寫法範例                              |
| ---------- | ---------------------------------------- |
| 重複字元按頻率拼字串 | `ch * freq for ch, freq in items`        |
| 數字平方後輸出    | `[x**2 for x in nums]`                   |
| 條件篩選並處理    | `[x*2 for x in nums if x > 0]`           |
| 字串展開為重複結構  | `''.join([c * f for c, f in freq_list])` |

## ⚠️ 注意事項 | Tips & Notes
- ch * freq 中 freq 必須是整數，否則會錯誤。

- 這是 Python 獨有的簡化寫法，其他語言通常要用迴圈實作。

- 可與 join() 搭配，快速組成結果字串。
