# 📍 LeetCode 804 — Unique Morse Code Words | 不重複的摩斯密碼表示

🔗 [題目連結](https://leetcode.com/problems/unique-morse-code-words/)

---

## 📄 題目說明 | Problem Description
### 中文

- 給定一個字串陣列 words，每個字串只包含小寫英文字母。
- 每個字母都有對應的摩斯密碼表示。

- 請將每個單字轉換成摩斯密碼後，回傳「不同的摩斯密碼表示有幾種」。

### English

Given an array of strings words, return the number of different transformations among all words, where each letter is mapped to its Morse code.

### Examples
- Example 1:

    - Input: words = ["gin","zen","gig","msg"]
    - Output: 2
    - Explanation: The transformation of each word is:
        - "gin" -> "--...-."
        - "zen" -> "--...-."
        - "gig" -> "--...--."
        - "msg" -> "--...--."
        - There are 2 different transformations: "--...-." and "--...--.".
- Example 2:

    - Input: words = ["a"]
    - Output: 1
    
---

## 🧠 解題思路 | Solution Idea（標準正解）
- 這題在問什麼？ 有幾種「不一樣」的轉換結果

- 關鍵字只有一個：👉 unique

- 為什麼用 set？

    -  題目 不在乎順序

    - 只在乎：轉換後的摩斯密碼 有沒有重複

- set 的特性正好是：

    - 自動去重

    - 不重複才會保留

---

## 💻 程式碼實作 | Code (Python)
```python
class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        morse = [
            ".-", "-...", "-.-.", "-..", ".", "..-.", "--.",
            "....", "..", ".---", "-.-", ".-..", "--", "-.",
            "---", ".--.", "--.-", ".-.", "...", "-", "..-",
            "...-", ".--", "-..-", "-.--", "--.."
        ]

        seen = set()

        for word in words:
            code = ""
            for ch in word:
                code += morse[ord(ch) - ord('a')]
            seen.add(code)

        return len(seen)
```
### 🔍 程式碼逐段說明 | Line-by-line Explanation
### 摩斯密碼表
```python
morse = [".-", "-...", "-.-.", ... , "--.."]
```

- index 0 → 'a'

- index 1 → 'b'

- ...

- index 25 → 'z'

### 建立 set
```python
seen = set()
```

- 用來存放「轉換後的摩斯字串」

- 自動去除重複結果

### 逐字轉換每個單字
```python
for word in words:
    code = ""
```

- code 用來累積該單字的摩斯密碼

### 字母 → 摩斯密碼
```python
for ch in word:
    code += morse[ord(ch) - ord('a')]
```

- ord(ch) - ord('a')：

    - 把字母轉成 0～25 的 index

- 再用 index 去查 morse 表

### 存進 set
```python
seen.add(code)
```

- 如果 code 已存在：

    - set 不會重複存

- 如果是新結果：

    - 自動加入

### 回傳不重複的數量
```python
return len(seen)
```

---

## 🧪 範例流程 | Example Walkthrough
### Input
```text
words = ["gin", "zen", "gig", "msg"]
```
### Step 0：初始狀態
```text
seen = {}
```
### Step 1：處理第一個 word = "gin"
#### 1️⃣ 進入外層 loop
```python
word = "gin"
code = ""
```
#### 2️⃣ ch = 'g'
```python
ord('g') - ord('a') = 6
morse[6] = "--."
code = "--."
```
#### 3️⃣ ch = 'i'
```python
ord('i') - ord('a') = 8
morse[8] = ".."
code = "--..."
```
#### 4️⃣ ch = 'n'
```python
ord('n') - ord('a') = 13
morse[13] = "-."
code = "--...-."
```
#### 5️⃣ 存進 set
```python
seen.add("--...-.")
```
```text
seen = {"--...-."}
```
### Step 2：處理第二個 word = "zen"
```python
word = "zen"
code = ""
```
#### ch = 'z'
```python
ord('z') - ord('a') = 25
morse[25] = "--.."
code = "--.."
```
#### ch = 'e'
```python
ord('e') - ord('a') = 4
morse[4] = "."
code = "--..."
```
#### ch = 'n'
```python
morse[13] = "-."
code = "--...-."
```
#### 存進 set
```python
seen.add("--...-.")
```

⚠️ 已存在，不會新增
```text
seen = {"--...-."}
```
### Step 3：處理第三個 word = "gig"
```python
word = "gig"
code = ""
```
#### ch = 'g'
```text
"--."
```
#### ch = 'i'
```text
"--..."
```
#### ch = 'g'
```text
"--...--."
```
#### 存進 set
```python
seen.add("--...--.")
```
```text
seen = {
  "--...-.",
  "--...--."
}
```
### Step 4：處理第四個 word = "msg"
```python
word = "msg"
code = ""
```
#### ch = 'm'
```text
"--"
```
#### ch = 's'
```text
"--..."
```
#### ch = 'g'
```text
"--...--."
```
#### 存進 set
```python
seen.add("--...--.")
```

⚠️ 已存在，不新增
```text
seen = {
  "--...-.",
  "--...--."
}
```
### Step 5：回傳結果
```python
return len(seen)
```
```text
len(seen) = 2
```
### ✅ 最終輸出
```text
2
```

---

## ⏱ 複雜度分析 | Complexity Analysis

- 設：

    - n = 單字數量

    - k = 單字平均長度

- 時間複雜度: O(n × k)

    - 每個單字要轉換每個字母

- 空間複雜度: O(n × k)

    - 最多存 n 個摩斯字串

---

## ✍️ 我學到的東西 | What I Learned

- 這題的核心不是「轉換」，而是 去重

- 當題目出現：

    - 「多少種不同的結果」

    - 「unique」

    - 「distinct」
    
    - 👉 第一時間想到 set

- Stack 適合處理：

    - 順序

    - 前後關係

    - 👉 不適合做全局去重

---

## 🧠 一句話總結

I transform each word into its Morse representation and use a set to count how many unique transformations there are.