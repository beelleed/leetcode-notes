# 🔁 Python 倒序迴圈與 range 用法筆記 | Reverse Loop in Python


## 📘 基本語法 | Syntax

### Python 的 range() 函式語法如下：

```python
range(start, stop, step)
```
| 參數    | 說明（中文）   | Description (English)       |
| ----- | -------- | --------------------------- |
| start | 起始值（包含）  | Starting number (inclusive) |
| stop  | 結束值（不包含） | Ending number (exclusive)   |
| step  | 每次增減的步長  | Step size (can be negative) |

### 🔁 倒序範例 | Reverse Loop Example
```python
for i in range(5, 0, -1):
    print(i)
```
📤 輸出（Output）：
```python
5
4
3
2
1
```
✅ 解釋：

- 從 5 開始，每次 -1，到 1 結束（不包含 0）

### 🧰 LeetCode 常見寫法：倒序掃頻率桶
```python
for freq in range(len(bucket) - 1, 0, -1):
    for ch in bucket[freq]:
        ...
```
💡 解釋：
- len(bucket) - 1 是最大頻率

- 0 是結束值（不包含）

- -1 是步長 ➜ 表示倒著掃

假設：
```python
bucket = [[], [], ['e'], ['a', 'b']]
len(bucket) = 4
```
那這一行就是：
```python
range(3, 0, -1)
# 會產生序列：3, 2, 1
```
表示從最大頻率開始，倒著遍歷到最小頻率（1），不包含 0，因為出現 0 次的字元不需要處理。

📥 常見用途 | Common Use Cases
| 用途情境（中文）     | 用法範例（Python）                                 |
| ------------ | -------------------------------------------- |
| 倒著列印序列       | `for i in range(n, 0, -1):`                  |
| 處理桶排序最大到最小順序 | `for freq in range(len(bucket) - 1, 0, -1):` |
| 二維陣列從右下角掃描   | `for i in range(rows - 1, -1, -1):`  `for j in range(cols - 1, -1, -1):`        |

### ⚠️ 注意事項 | Tips & Warnings
- stop 是「不包含的」，即使是倒序也一樣

- 負步長 -1 才能達成倒序，不能寫成 1 或 0

- 適用於處理「最大到最小」、「從尾到頭」的各種場景

### 🧠 學習總結 | Key Takeaways
- range(len(bucket) - 1, 0, -1) 是 Python 倒序迴圈的經典範例

- 常見於桶排序、字元頻率統計、反向遍歷陣列等題目

- 熟練使用這種寫法可以讓迴圈邏輯更清晰、程式碼更簡潔