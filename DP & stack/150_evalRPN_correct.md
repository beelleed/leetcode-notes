# 150. Evaluate Reverse Polish Notation  
## 150. 評估逆波蘭表示法

[LeetCode 題目連結](https://leetcode.com/problems/evaluate-reverse-polish-notation/)

---

## 📌 題目描述 Description

**中文**  
給一個以倒序波蘭表示法 (Reverse Polish Notation, RPN) 寫成的字串陣列 `tokens`，請計算並回傳其結果。可包含整數與四則運算符 `+`, `-`, `*`, `/`。每個運算符僅會對其前兩個操作數進行計算。

**English**  
Given an array of strings `tokens` representing an arithmetic expression in Reverse Polish Notation, evaluate the expression and return its integer result.  
Valid operators are `+`, `-`, `*`, and `/`. Each operator applies to the two most recent operands.

---

## ✅ 解題思路 Solution Outline

1. **初始化一個空 stack**  
2. 依序瀏覽 `tokens`:
   - **如果是數字**，轉為 `int` 後 `push` 進 stack。
   - **如果是運算符**，`pop` 出 `b = stack.pop()`（右操作數），接著 `pop` 出 `a = stack.pop()`（左操作數），計算 `a op b`，將結果 `push` 回 stack。
3. 最終 stack 中只會剩一個整數值，即為答案 `return stack[-1]`。

---

## 🧠 思路流程圖（文字版）

start
↳ for each token in tokens:
↳ is token a number?
↳ YES → convert to int and push to stack
↳ NO (it's an operator):
↳ pop b (right operand)
↳ pop a (left operand)
↳ compute result = a op b
↳ push result back to stack
end loop
↳ return the single element in stack

---
## 🧠 範例 + 遞進流程
- 以例子 ["2", "1", "+", "3", "*"] 為例：

    - 遇到 "2" → push → stack = [2]

    - 遇到 "1" → push → stack = [2, 1]

    - 遇到 "+" → pop → right = 1, left = 2 → evaluate 2 + 1 = 3 → push → stack = [3]

    - 遇到 "3" → push → stack = [3, 3]

    - 遇到 "*" → pop → right = 3, left = 3 → evaluate 3 * 3 = 9 → push → stack = [9]

- 最後 stack 裡只剩 [9]，就是結果。

---

## 📘 程式碼實作 Implementation
```python
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token in {"+", "-", "*", "/"}:
                b = stack.pop()      # 右值
                a = stack.pop()      # 左值
                if token == "+":
                    val = a + b
                elif token == "-":
                    val = a - b
                elif token == "*":
                    val = a * b
                else:
                    val = int(a / b)  # 向 0 收斂的整数除
                stack.append(val)
            else:
                stack.append(int(token))
        return stack[-1]
```
## 🧠 核心學習重點 Key Takeaways
- Stack LIFO 原理：最後 push 的先 pop → 運算使用的順序是右值先出。

- 數字轉整數儲存：int(token) 讓後續可運算。

- 四則運算選擇：a op b 必須保持操作順序一致。

- 處理除法方向：使用 int(a / b) 保證 LeetCode 所需「向 0 收斂」。

- 效率：只有一個迴圈 → 時間 O(n)，而且順序簡單。

--- 

## ⏱️ 複雜度分析 Complexity
- 時間複雜度 Time: O(n) — 每個元素僅遍歷一次。

- 空間複雜度 Space: O(n) — 最差情況下 stack 儲存所有數字。

---

## 🧪 LIFO實際例子解釋：
``` python
tokens = ["4", "2", "-"]
```
處理步驟如下：

    遇到 "4" → stack = [4]

    遇到 "2" → stack = [4, 2]

    遇到 "-" → 這時要從 stack 中取出兩個數來相減

如果寫：
```python
a = stack.pop()
b = stack.pop()
result = a - b
```
那就是：a = 2, b = 4 → 2 - 4 = -2 ❌

但實際上應該是：4 - 2 = 2 ✅

正確順序應該是：
```python
right = stack.pop()  # 先出來的 = 右邊數
left = stack.pop()   # 後出來的 = 左邊數
```
這樣才會：
```python
left - right = 4 - 2 = 2 ✅
```
## 📌 總結
| 名稱       | 說明                     |
| -------- | ---------------------- |
| Left     | 第二個 pop 的值（較早進 stack）  |
| Right    | 第一個 pop 的值（較晚進 stack）  |
| Stack 特性 | LIFO：Last In First Out |

---