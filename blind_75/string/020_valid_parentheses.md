# 020. Valid Parentheses

[題目連結](https://leetcode.com/problems/valid-parentheses/)

---

## 🧩 題目描述 Problem Description

### 中文：
給定一個只包含 ()、[]、{} 的字串 s，請判斷是否為「有效的括號配對」。
有效的括號需同類型、順序正確，且成對閉合。

### English:
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']',
determine if the input string is valid.

A valid string must satisfy:

1.Open brackets are closed by the same type of brackets

2.Open brackets are closed in the correct order

3.Every closing bracket has a corresponding open bracket of the same type

### Examples
- Example 1:

    - Input: s = "()"

    - Output: true

- Example 2:

    - Input: s = "()[]{}"

    - Output: true

- Example 3:

    - Input: s = "(]"

    - Output: false

- Example 4:

    - Input: s = "([])"

    - Output: true

- Example 5:

    - Input: s = "([)]"

    - Output: false

 
---

## ❌ 嘗試錯誤一：左右括號處理方向寫反

```python
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = { "(":")" , "{":"}" , "[":"]"}
        for i in s:
            if i in mapping.values():  # ❌ 錯：應該是右括號才需要比對，這邊卻加進 stack
                stack.append(i)
            elif i in mapping:
                if not stack or stack[-1] != mapping[i]:  # ❌ 錯：這裡 mapping[i] 是右括號，但stack 放的是右括號
                    return False
                else:
                    stack.pop()
        return not stack
```
🔍 錯誤點說明：

1.這邊你是定義「左括號 → 右括號」的映射，代表用了「右括號進 stack」，其實應該是「左括號進 stack」

2.對映檢查方向錯誤：mapping[stack[-1]] 才會對照到對應的右括號

❗ Wrong logic: pushing closing brackets into stack and comparing with expected opening — direction is flipped.

---

##  answer 1: Left-to-Right Mapping

```python 
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = { "(":")" , "{":"}" , "[":"]"}
        for i in s:
            if i in mapping:  # 左括號 → 進 stack
                stack.append(i)
            elif i in mapping.values():  # 右括號
                if not stack or mapping[stack.pop()] != i:
                    return False
        return not stack
```
- 每遇到一個「左括號」 → 先放進堆疊（stack）

- 每遇到一個「右括號」 → 檢查堆疊頂端是不是對應的左括號

    - 如果不是 → 回傳 False（不合法）

    - 如果是 → 彈出那個左括號（配對成功）

- 為什麼最後不能直接 return True
    - 因為：即使沒有出錯，也不代表所有括號都關閉了
        - 範例 1️⃣： s = "("
            - 執行過程：

                - '(' → 放進 stack → stack = ['(']

                - 沒有右括號可配對 → 迴圈跑完

            - 這時候：

                - 程式沒有進入 return False（因為沒遇到不合法配對）

                - 但 stack 還有東西沒清空（'('）

                - 表示有「沒被關閉」的括號 → ❌ 不合法！
```python
return not stack
```
它等價於：
```python
if len(stack) == 0:
    return True
else:
    return False
```


---

## Examples
```python
s = "({[]})"
```
流程：

1. "(" → push → ["("]

2. "{" → push → ["(", "{"]

3. "[" → push → ["(", "{", "["]

4. "]" → 檢查 top 是否是 "[" ✔ → pop → ["(", "{"]

5. "}" → 檢查 top 是否是 "{" ✔ → pop → ["("]

6. ")" → 檢查 top 是否是 "(" ✔ → pop → []

7. stack 空了 → 回傳 True

---

## ✅ 時間與空間複雜度

1.時間：O(n) — 每個字元最多處理一次

2.空間：O(n) — stack 最多會裝 n 個字元（全為左括號時）

---

## 🧠 我學到的重點

1.左括號進 stack，右括號比對是否正確配對

2.括號對應要搞清楚方向：mapping[左括號] → 對應右括號

3.not stack 是判斷是否配對完畢的關鍵技巧

---

## answer 2: Right-to-Left Mapping(官方)

```python
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = { ")":"(" , "}":"{" , "]":"["}
        for i in s:
            if i in mapping.values():
                stack.append(i)
            elif i in mapping:
                if not stack or stack[-1] != mapping[i]:
                    return False
                else:
                    stack.pop()
        return not stack
```

## 🔍 說明Explanation：

右括號 → 對應的左括號

Uses a reverse mapping where every right bracket looks for its corresponding left bracket on the stack top.

## ✅ 解釋這個版本的邏輯

```python
mapping = {")": "(", "}": "{", "]": "["}
```

右括號 → 對應的左括號

代表：

遇到 )，需要 stack 有一個 ( 才合法

遇到 ]，需要 stack 有一個 [ 才合法

…以此類推

## 🔄 處理流程：
```python

if i in mapping.values():
    stack.append(i)
```
如果是左括號，先壓入 stack，等待之後配對。

```python

elif i in mapping:
    if not stack or stack[-1] != mapping[i]:
        return False
    else:
        stack.pop()
```

如果是右括號：

stack 必須不為空

stack[-1]（最上層）必須是對應的左括號

若符合就 pop()，表示這對括號成功配對

```python
return not stack
```

最後檢查 stack 是否為空：

	•	是空 → 所有括號都成功配對 → return True

	•	不空 → 還有左括號沒被關閉 → return False


## ✅ 優點
這種寫法比較容易判斷「右括號錯配或提早出現」的錯誤

mapping[右括號] → 對應左括號，比對時比較直覺（只看 stack top 是不是對應的）

---

## 📌 範例 | Examples
- s = "()[]{}"
### Step 1
```python
i = "("
```
是左括號 → push
```python
stack = ["("]
```
### Step 2
```python
i = ")"
```
是右括號

檢查：
```python
stack[-1] == mapping[")"]
"(" == "("
```
成立 → pop
```python
stack = []
```
### Step 3
```python
i = "["
```
push
```python
stack = ["["]
```
### Step 4
```python
i = "]"
```
檢查：
```python
"[" == mapping["]"]
```
成立 → pop
```python
stack = []
```
### Step 5
```python
i = "{"
```
push
```python
stack = ["{"]
```
### Step 6
```python
i = "}"
```
檢查成功 → pop
```python
stack = []
```
最後
```python
return not stack
```
stack 是空 → 回傳 True

## 📌 範例 2（錯誤案例）
- s = "(]"

### Step 1
```python
i = "("
```
push
```python
stack = ["("]
```
### Step 2
```python
i = "]"
```
檢查：
```python
stack[-1] == mapping["]"]
"(" == "["
```
不成立 → return False

## 📌 範例 3（多左括號）
- s = "((("

全部 push：
```python
stack = ["(", "(", "("]
```
最後：
```python
return not stack
```
stack 不是空 → False

---

## ⏱️ 時間複雜度（Time Complexity）
- O(n)，其中 n 是輸入字串 s 的長度：

    - 每個字元最多被處理一次（進 stack 一次、出 stack 一次）。

## 💾 空間複雜度（Space Complexity）

- O(n)：

    - 最壞情況下，所有字符都是左括號，都會被推入 stack 中，因此空間最多使用 n。  

