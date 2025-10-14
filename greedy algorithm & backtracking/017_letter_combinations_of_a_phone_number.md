# 📞 LeetCode 17 — Letter Combinations of a Phone Number / 電話號碼字母組合
🔗 [題目連結](https://leetcode.com/problems/letter-combinations-of-a-phone-number/)

---

## 📄 題目描述 | Problem Description

### 中文  
給定一個數字字串 `digits`（只包含 '2' 到 '9'），返回該數字可能代表的所有字母組合（遵從電話鍵盤映射）。如果輸入為空字串，返回空列表。

![](../images/17_1200px-telephone-keypad2svg.png)

鍵盤映射如下：  
- 2 → "abc"  
- 3 → "def"  
- 4 → "ghi"  
- 5 → "jkl"  
- 6 → "mno"  
- 7 → "pqrs"  
- 8 → "tuv"  
- 9 → "wxyz"

### English  
Given a string `digits` containing digits from '2' to '9', return all possible letter combinations that the number could represent, in any order. If the input is an empty string, return an empty list.

### Examples
- Example 1:

    - Input: digits = "23"
    - Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]

- Example 2:

    - Input: digits = ""
    - Output: []

- Example 3:

    - Input: digits = "2"
    - Output: ["a","b","c"]
 
---

## 🧠 解法思路 | Solution Idea

這題是典型的「組合 / 回溯 / DFS」問題：  
- 每一個數字對應一組字母，對於每個可能的字母，都要接續下一個數字的可能字母做組合。  
- 我們透過 DFS 或 Backtracking 枚舉所有可能組合。  
- 或者也可以用迭代的方式，一步步把已有的組合和新的字母拼起來。

---

## 💻 程式碼範例（DFS + Backtracking 版本）

```python
from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        # 數字到字母的映射
        digit_to_letters = {
            '2': "abc",
            '3': "def",
            '4': "ghi",
            '5': "jkl",
            '6': "mno",
            '7': "pqrs",
            '8': "tuv",
            '9': "wxyz"
        }

        results: List[str] = []

        def backtrack(index: int, path: List[str]):
            # 如果已經使用完所有 digits
            if index == len(digits):
                # 將 path（字母列表）組成字串加入結果
                results.append("".join(path))
                return

            # 取出當前 digit 對應的所有可能字母
            letters = digit_to_letters[digits[index]]
            for ch in letters:
                path.append(ch)            # 選擇這個字母
                backtrack(index + 1, path)  # 繼續處理下一個 digit
                path.pop()                  # 回溯，撤銷選擇

        backtrack(0, [])
        return results
```
| 程式碼區段                                                            | 中文說明                                       | English Explanation                                                 |
| ---------------------------------------------------------------- | ------------------------------------------ | ------------------------------------------------------------------- |
| `if not digits: return []`                                       | 如果輸入空字串，直接回傳空列表                            | Handle edge case: empty input                                       |
| `digit_to_letters = {...}`                                       | 建立數字到字母的映射字典                               | Mapping from digit char to possible letters                         |
| `results: List[str] = []`                                        | 存放最終的字母組合                                  | Container for all combinations                                      |
| `def backtrack(index, path)`                                     | 回溯函數，`index` 是目前處理第幾個 digit，`path` 是目前組合字母 | Recursion function: `index` for digit pos, `path` for built letters |
| `if index == len(digits): results.append("".join(path)); return` | 當 index 超過最後一個 digit，代表一條完整組合已構造好          | If we've built a full combination, add to results                   |
| `letters = digit_to_letters[digits[index]]`                      | 拿當前 digit 能映射的字母集合                         | Get possible letters for current digit                              |
| `for ch in letters: ...`                                         | 對每個可能字母做遞迴選擇                               | Try each letter, recurse, then backtrack                            |
| `path.append(ch); backtrack(...); path.pop()`                    | 遞迴探索 + 回溯撤銷                                | Choose → recurse → undo choice                                      |

---

## 🧪 範例演算

- 假設 digits = "23"

    - 第 0 個 digit 是 '2' → 映射字母 "abc"

    - 第 1 個 digit 是 '3' → 映射字母 "def"

- 回溯的流程如下（部分示意）：

    1. 選 'a' 作為第一位 → path = ['a']

        - 選 'd' → path = ['a','d'] → index = 2（等於 len）→ add "ad"

        - 回溯 → path 回到 ['a']

        - 選 'e' → path = ['a','e'] → add "ae"

        - 回溯 → 回 ['a']

        - 選 'f' → path = ['a','f'] → add "af"

        - 回溯

    2. 回到第一層，選 'b' → path = ['b']

        - 選 'd', 'e', 'f' 分析同上 → "bd", "be", "bf"

    3. 回到第一層，選 'c' → path = ['c']

        - 選 'd', 'e', 'f' → "cd", "ce", "cf"

- 結果：["ad","ae","af","bd","be","bf","cd","ce","cf"]

---

## ⏱ 複雜度分析 | Complexity

- 時間複雜度：O(4^n × n)

    - 在最壞情況，每個 digit 對應 4 個字母（比如 '7' 或 '9'）

    - 所以組合數量最多是 4^n，每條組合要做字串拼接、複製等操作（長度 n）

- 空間複雜度：𝑂(𝑛)（排除結果佔的空間）

    - 遞迴深度為 n，path 最長長度也為 n

---

## ✍ 我學到了什麼 / What I Learned

- 這題是回溯的經典題型，鍛鍊如何「選擇 → 探索 → 撤銷」的邏輯

- 使用 path 來記錄當前選擇，比操作整個字串更方便

- 處理空輸入是常見邊界要檢查的地方

