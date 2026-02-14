# 📍 LeetCode 13 — Roman to Integer

🔗 [題目連結] (https://leetcode.com/problems/roman-to-integer/)

---

## 📄 題目說明 | Problem Description
### 中文

- 給一個羅馬數字字串 s，請將它轉換成整數。

- 羅馬數字包含：

    - I = 1
    - V = 5
    - X = 10
    - L = 50
    - C = 100
    - D = 500
    - M = 1000


- 特殊情況：

    - IV = 4

    - IX = 9

    - XL = 40

    - XC = 90

    - CD = 400

    - CM = 900

### English
- Roman numerals are represented by seven different symbols:
    - I = 1
    - V = 5
    - X = 10
    - L = 50
    - C = 100
    - D = 500
    - M = 1000


- For example:

    - 2 is written as II in Roman numeral, just two ones added together.

    - 12 is written as XII, which is simply X + II.

    - 27 is written as XXVII, which is XX + V + II.

- Roman numerals are usually written largest to smallest from left to right. However, there are six instances where subtraction is used:

    - I can be placed before V (5) and X (10) to make 4 and 9.

    - X can be placed before L (50) and C (100) to make 40 and 90.

    - C can be placed before D (500) and M (1000) to make 400 and 900

### Examples
- Example 1:

    - Input: s = "III"
    - Output: 3
    - Explanation: III = 3.
- Example 2:

    - Input: s = "LVIII"
    - Output: 58
    - Explanation: L = 50, V= 5, III = 3.
- Example 3:

    - Input: s = "MCMXCIV"
    - Output: 1994
    - Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.

---

## 🧠 解題核心思路 | Idea
- 關鍵觀察

    - 其實沒有 6 種特判。

- 只有一條規則：如果目前數字 < 下一個數字 → 減
否則 → 加

- 例如：
```nginx
IV  → 1 < 5  → -1 + 5
IX  → 1 < 10 → -1 + 10
```

---

## 💻 程式碼 | Code
```python
class Solution:
    def romanToInt(self, s: str) -> int:
        roman = {
            'I': 1, 'V': 5, 'X': 10,
            'L': 50, 'C': 100,
            'D': 500, 'M': 1000
        }

        ans = 0

        for a, b in zip(s, s[1:]):
            if roman[a] < roman[b]:
                ans -= roman[a]
            else:
                ans += roman[a]

        return ans + roman[s[-1]]
```
### 1️⃣ 建立對照表
```python
roman = { ... }
```

- 用 dictionary 讓查詢 O(1)。

### 2️⃣ 同時看「現在」跟「下一個」
```python
for a, b in zip(s, s[1:]):
```

- zip(s, s[1:]) 會產生：
```text
("M","C")
("C","M")
("M","X")
...
```

- 這樣就能比較相鄰兩個字元。

### 3️⃣ 判斷加或減
```python
if roman[a] < roman[b]:
    ans -= roman[a]
else:
    ans += roman[a]
```

- 只要當前比下一個小，就減。

### 4️⃣ 為什麼最後要加 s[-1]？

- 因為最後一個字沒有被加進去。

- zip(s, s[1:]) 只處理到倒數第二個。

- 所以最後補：
```python
ans + roman[s[-1]]
```

---

## 🧪 範例流程

### Example: s = "MCMXCIV"

字串：
```mathematica
M C M X C I V
```
### Step 1：比較 M vs C

- 1000 > 100
- → 加 1000
- ans = 1000

### Step 2：C vs M

- 100 < 1000
- → 減 100
- ans = 900

### Step 3：M vs X

- 1000 > 10
- → 加 1000
- ans = 1900

### Step 4：X vs C

- 10 < 100
- → 減 10
- ans = 1890

### Step 5：C vs I

- 100 > 1
- → 加 100
- ans = 1990

### Step 6：I vs V

- 1 < 5
- → 減 1
- ans = 1989

### 最後加 V

- +5
- ans = 1994

---

## ⏱ 複雜度分析 | Complexity
- Time complexity is O(n) because we iterate through the string once.
- Space complexity is O(1) since the hashmap size is constant.
### 時間複雜度 | Time Complexity

- O(n)

- 掃一遍字串。

- zip(s, s[1:]) 會跑 n-1 次。

- 每次操作都是 O(1)（dictionary 查詢 + 加減）

### 空間複雜度 | Space Complexity
- O(1)

- dictionary 只有固定 7 個鍵值。

- 沒有建立額外與 n 成比例的資料結構。

- 只用了幾個變數。

---

## ✍️ 我學到的東西 | What I learned

- 不要被 6 種特殊情況騙

- 本質只是「相鄰比較」

- 看到「前後關係影響加減」 → 想到 zip(s, s[1:])

---

## 🧠 一句話總結

Compare each character with the next one. If smaller → subtract, otherwise add.