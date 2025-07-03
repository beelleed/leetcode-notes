# ✅ LeetCode 155 - Min Stack 正確解法 | Correct Solution

🔗 題目連結：[https://leetcode.com/problems/min-stack/](https://leetcode.com/problems/min-stack/)

## 📘 題目說明 | Problem Description

請設計一個支援以下操作的「最小堆疊」：
- `push(x)`：將元素 x 推入堆疊中
- `pop()`：移除堆疊頂端元素
- `top()`：取得堆疊頂端元素
- `getMin()`：取得堆疊中最小值（**O(1)** 時間）

---

## 🧠 解題思路 | Solution Strategy

我們使用兩個 stack：
1. `stack`：存放所有值
2. `min_stack`：存放每個狀態下的最小值

每次 push：
- `stack` 加入新值
- `min_stack` 加入「新值 vs 目前最小值」中較小者

---

## 🧾 程式碼與註解 | Code with Explanation

```python
class MinStack:
    def __init__(self):
        self.stack = []       # 主堆疊
        self.min_stack = []   # 紀錄最小值的輔助堆疊

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.min_stack:
            self.min_stack.append(val)
        else:
            self.min_stack.append(min(val, self.min_stack[-1]))

    def pop(self) -> None:
        self.stack.pop()
        self.min_stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]
```

```python
def __init__(self):
    self.stack = []
    self.min_stack = []
```
- 這是建構子（constructor），每次你建立一個 MinStack() 物件時都會被呼叫。

- self.stack：用來存你真正 push 進來的值。

- self.min_stack：這是技巧的核心 → 它同步 push「當下最小值」，讓 getMin() 可以在 O(1) 時間拿到。

```python
def push(self, val:int) -> None:
    selff.stack.append(val)
```
- 把這個值 val 加進主堆疊。

```python
if not self.min_stack:
    self.min_stack.append(val)
```
- 如果這是第一個元素（min_stack 是空的），那這個值本身就是目前最小值，直接加進去。
```python
else:
    self.min_stack.append(min(val, self.min_stack[-1]))
```
- 否則就比較「這個新值」和「目前最小值（min_stack[-1]）」哪個小，然後把較小者記錄到 min_stack。

- 為什麼這麼做？這樣才能讓我們每次 pop 時也能正確同步對應的最小值。

```python
def pop(self) -> None:
    self.stack.pop()
    self.min_stack.pop()
```
- 每次從主堆疊移除值時，也要同步移除 min_stack 最上面對應的最小值。

```python
def top(self) -> int:
    return self.stack[-1]
```
-回傳 stack 頂端的元素（最後一個被放進來的值）。

- [-1] 是 Python 中取「最後一項」的語法。

```python 
def getMin(self) -> int:
    return self.min_stack[-1]
```
- 回傳目前堆疊中的最小值。

- 因為 min_stack 永遠記錄著「當前 push 進來時的最小值」，所以直接取頂端就行。

### 🧠 為什麼這樣做是 O(1)？
| 操作         | 說明                       |
| ---------- | ------------------------ |
| `push()`   | 同步 push 到兩個 stack，O(1)   |
| `pop()`    | 同步 pop，O(1)              |
| `top()`    | 回傳 stack\[-1]，O(1)       |
| `getMin()` | 直接從 min\_stack 拿頂部值，O(1) |

### 🧪 範例：
```python
stack = MinStack()
stack.push(3)   # min = 3
stack.push(5)   # min = 3
stack.push(2)   # min = 2
stack.pop()     # 移除 2，min 回到 3
```

每一步：

- self.stack: [3, 5, 2]

- self.min_stack: [3, 3, 2]

pop 後：

- self.stack: [3, 5]

- self.min_stack: [3, 3]

---

## 📌 為什麼最小值的邏輯要放在 `push()`，而不是 `getMin()`？

### ❗ 錯誤的想法 | The Wrong Approach

可能會寫：
```python
def getMin(self):
    return min(self.stack)  # ❌ 這是 O(n)，不符合題目要求
```
- 這樣做雖然能算出最小值，但每次呼叫都會「遍歷整個堆疊」。

- 時間複雜度是 O(n)，在資料筆數多的情況下會超時（TLE）。

### ✅ 正確設計方式 | Correct Design
- 在 push() 的時候，順便記錄目前的最小值，放進 min_stack：
```python
if not self.min_stack:
    self.min_stack.append(val)
else:
    self.min_stack.append(min(val, self.min_stack[-1]))
```
這樣設計的好處是：

- getMin() 時只要看 min_stack[-1]

- 不需要重新掃整個 stack

- 時間複雜度為 O(1)，符合題目要求

### 📦 比較表 | Comparison
| 方法                               | 時間複雜度  | 說明                    |
| -------------------------------- | ------ | --------------------- |
| 在 `getMin()` 用 `min(self.stack)` | O(n) ❌ | 每次都要掃整個 stack         |
| 在 `push()` 時儲存最小值                | O(1) ✅ | 每次只要看 `min_stack[-1]` |

### 🧠 總結 | Summary
- getMin() 應該是一個「查詢」操作，而不是「計算」操作

- 若要做到 O(1)，就必須讓 push() 同時幫你記住「當下最小值」

- 這就是設計資料結構時最重要的觀念之一：「提前儲備，減少重算」

---

## ⏱️ 時間與空間複雜度 | Complexity
| 操作     | 時間複雜度 | 空間複雜度 |
| ------ | ----- | ----- |
| push   | O(1)  | O(n)  |
| pop    | O(1)  | O(1)  |
| top    | O(1)  | O(1)  |
| getMin | O(1)  | O(1)  |

---

## 📌 學到的觀念 | Key Takeaways
- O(1) 取得最小值的技巧是「同步 push 進 min_stack」

- Python 中記得用 self. 來表示實例變數