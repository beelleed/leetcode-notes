# 🧩 LeetCode 49 - Group Anagrams（分組字母異位詞）
[題目連結](https://leetcode.com/problems/group-anagrams/)


## 📘 題目描述 | Problem Description

### 中文：
給定一個字串陣列 `strs`，請將所有「字母異位詞」分組。異位詞指的是字母完全一樣但順序不同的字串。

### English:
Given an array of strings `strs`, group all anagrams together. You may return the answer in any order.

### Examples
- Example 1:

    - Input: strs = ["eat","tea","tan","ate","nat","bat"]

    - Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

    - Explanation:
        - There is no string in strs that can be rearranged to form "bat".
        - The strings "nat" and "tan" are anagrams as they can be rearranged to form each other.
        - The strings "ate", "eat", and "tea" are anagrams as they can be rearranged to form each other.

- Example 2:

    - Input: strs = [""]

    - Output: [[""]]

- Example 3:

    - Input: strs = ["a"]

    - Output: [["a"]]

- Constraints:

    - 1 <= strs.length <= 104
    - 0 <= strs[i].length <= 100
    - strs[i] consists of lowercase English letters.

---

## 💡 解題思路 | Solution Idea

### 中文
- 所有字母異位詞，**排序後會得到相同的字串**。
- 將排序後的字串當作 Key，對應原本的字串放入 value list 中。
- 使用 `defaultdict(list)` 自動幫你建立空 list，非常方便。

### English
- All anagrams will produce the same string when sorted.

- Use the sorted string as the key, and store the original strings in the value list.

- Using defaultdict(list) automatically initializes empty lists, which makes the code cleaner and more convenient.

🔑 **關鍵技巧**：  
排序字串當作雜湊 Key ➜ 找出同組的異位詞。

---

## 🧾 程式碼 | Python Code

```python
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)  # 建立一個自動初始化 list 的 dict

        for s in strs:
            key = ''.join(sorted(s))  # 排序字串當作 key，例如 eat → aet
            anagrams[key].append(s)   # 加入對應的群組

        return list(anagrams.values())  # 回傳所有異位詞群組
```

### 🔍 程式逐行解析 | Step-by-Step Explanation
| 行數 | 程式碼                                   | 功能說明                          |
| -- | ------------------------------------- | ----------------------------- |
| 1  | `from collections import defaultdict` | 匯入 defaultdict，可自動建立空 list    |
| 4  | `anagrams = defaultdict(list)`        | 建立字典，key 是排序後字串，value 是列表     |
| 6  | `for s in strs:`                      | 遍歷輸入字串陣列                      |
| 7  | `key = ''.join(sorted(s))`            | 將字串排序後轉成 key，例如 “eat” → “aet” |
| 8  | `anagrams[key].append(s)`             | 把原字串加進對應群組                    |
| 10 | `return list(anagrams.values())`      | 回傳所有群組的 list                  |

### 🧪 範例說明 | Example Walkthrough

input: strs = ["eat","tea","tan","ate","nat","bat"]

| 字串 s  | 排序後 key | 放入群組                   |
| ----- | ------- | ---------------------- |
| "eat" | "aet"   | \["eat"]               |
| "tea" | "aet"   | \["eat", "tea"]        |
| "tan" | "ant"   | \["tan"]               |
| "ate" | "aet"   | \["eat", "tea", "ate"] |
| "nat" | "ant"   | \["tan", "nat"]        |
| "bat" | "abt"   | \["bat"]               |

output: [["eat","tea","ate"],["tan","nat"],["bat"]]

---

## 🧩 補充：為什麼使用 `defaultdict`？

### ✅ 問題背景

在這題中，我們需要把相同異位詞的字串放在同一個 list 中，也就是：

- **Key**：排序後的字串
- **Value**：對應的字串 list

如果使用普通 `dict`，必須先檢查 key 是否存在：

```python
if key not in group:
    group[key] = []
group[key].append(s)
```
但使用 defaultdict(list)，會自動初始化空 list，讓程式碼更簡潔：
```python
group[key].append(s)
```

---

## 📌defaltdict vs dict
| 項目        | defaultdict 寫法      | dict 寫法                    |
| --------- | ------------------- | -------------------------- |
| 初始化方式     | `defaultdict(list)` | `dict()`                   |
| 是否要檢查 key | ❌ 不用，會自動生成          | ✅ 需要 `if key not in dict:` |
| 程式碼簡潔度    | 更簡潔                 | 稍微冗長                       |
| 容易出錯性     | 低（不會 KeyError）      | 高（忘記初始化會 KeyError）         |

✅ 判斷點：要「分組」或「累加」的題目

像這題 LeetCode 49：

    把屬於同一組的字串（anagrams）聚集起來成 list

- 這種需求通常會需要一個：

    - key → 判斷是否屬於同一組

    - value → 對應的字串列表（需不斷 .append()）

如果你使用一般的 dict，每次新增前都要檢查 key 是否存在：
```python
if key not in group:
    group[key] = []
group[key].append(s)
```
但用 defaultdict(list)，可以自動初始化空 list：
```python
group[key].append(s)
```
更簡潔、也避免 KeyError。

### 🧠 通用經驗法則
| 類型            | 常用結構                | 為什麼                      |
| ------------- | ------------------- | ------------------------ |
| 分組（群組問題）      | `defaultdict(list)` | 每個 key 對應一組項目，append 最方便 |
| 計數問題（字元/元素頻率） | `defaultdict(int)`  | 每個 key 對應一個數量，+= 1 超簡單   |

### 🧪 類似題目也用過 defaultdict

- LeetCode 347: Top K Frequent Elements

- LeetCode 451: Sort Characters by Frequency

- LeetCode 49: Group Anagrams

- LeetCode 30: Substring with Concatenation of All Words

### 📚 我學到了什麼

- 當你需要「一個 key 對應多個 value」的時候，特別是：

    - 需要 自動初始化容器（list, set, int 等）

    - 避免寫 if-checks

- 就是使用 collections.defaultdict 的最佳時機！

---

## ⏱ 複雜度分析 | Time & Space Complexity

- 時間複雜度: O(n * k log k)

    - n 為字串數量，k 為每個字串平均長度（排序成本）

- 空間複雜度: O(n * k)

    - 儲存 hash map 和結果陣列

---

## 📚 我學到了什麼 | What I Learned

- 排序字串可以作為「判別異位詞」的唯一 key。

- 使用 defaultdict(list) 可快速建立資料結構。

- 字串處理與雜湊技巧結合是經典「群組」型問題做法。