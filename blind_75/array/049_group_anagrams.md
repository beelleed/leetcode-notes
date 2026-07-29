# 🧩 LeetCode 49 - Group Anagrams（分組字母異位詞）
[題目連結](https://leetcode.com/problems/group-anagrams/)

---

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

### Step 1：sorted(s) 的複雜度

- s 的長度是 k

- Python 的排序是 Timsort

- 排序字元的時間複雜度是：O(k log k)

👉 這是整題最貴的操作

### Step 2：''.join(sorted(s)) 的複雜度

- 要把 k 個字元串成字串

- 時間複雜度是：O(k)

### Step 3：dict 操作的複雜度
```python
anagrams[key].append(s)
```

- dict 查找：O(1)（平均）

- list append：O(1)（平均）

👉 幾乎可以忽略不計

### 🔹 單一字串的總時間複雜度
```text
O(k log k) + O(k) ≈ O(k log k)
```
### 🔹 全部字串的時間複雜度

你對 n 個字串都做一樣的事：
```text
O(n × k log k)
```
✅ 最終時間複雜度
```text
O(n · k log k)
```
### 空間複雜度怎麼算？
#### 1️⃣ defaultdict(list)

- 最多會存 n 個字串

- 所有字串總長度是 n · k

#### 2️⃣ key（排序後的字串）

- 每個 key 長度是 k

- 最壞情況每個字串都是不同 anagram → n 個 key

#### ✅ 空間複雜度
```text
O(n · k)
```
（不包含輸入本身的話）

### 為什麼很多人會寫錯？

- 常見錯誤 ❌：

    - 「排序一次是 O(n log n)」

- 錯在：

    - 不是排序 n 個字串

    - 是對 每個長度為 k 的字串做排序

---

## 📚 我學到了什麼 | What I Learned

- 排序字串可以作為「判別異位詞」的唯一 key。

- 使用 defaultdict(list) 可快速建立資料結構。

- 字串處理與雜湊技巧結合是經典「群組」型問題做法。

---

## Code (freq)

```python
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)
        for word in strs:
            freq = [0] * 26
            for ch in word:
                freq[ord(ch) - ord('a')] += 1
            key = tuple(freq)
            anagrams[key].append(word)
        return list(anagrams.values())
```

## 程式碼（逐行解釋）

```python
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
```

建立 `Solution` 類別。

---

```python
anagrams = defaultdict(list)
```

建立 HashMap。

- Key：每個字串的 frequency tuple
- Value：所有屬於同一組 Anagram 的字串

例如：

```text
{
    (1,0,...,1): ["eat","tea","ate"]
}
```

---

```python
for word in strs:
```

依序處理每一個字串。

例如：

```
eat
tea
tan
ate
```

---

```python
freq = [0] * 26
```

建立長度 26 的 frequency array。

代表：

```
index 0 -> a
index 1 -> b
...
index 25 -> z
```

每個新字串都重新建立一次。

---

```python
for ch in word:
```

逐一走訪字串中的每個字元。

例如：

```
word = "eat"

↓

e
a
t
```

---

```python
freq[ord(ch) - ord('a')] += 1
```

利用 ASCII 計算字母的位置。

例如：

```
'e'

↓

ord('e') - ord('a')

↓

4
```

更新 frequency。

例如：

```
eat

↓

a = 1
e = 1
t = 1
```

---

```python
key = tuple(freq)
```

將 List 轉成 Tuple。

因為：

```
List
```

不能作為 Dictionary Key。

所以改成：

```
Tuple
```

例如：

```
[1,0,0,0,1,...]

↓

(1,0,0,0,1,...)
```

---

```python
anagrams[key].append(word)
```

將目前字串加入對應的 Anagram 群組。

例如：

```
key

↓

["eat"]

↓

["eat","tea"]

↓

["eat","tea","ate"]
```

---

```python
return list(anagrams.values())
```

回傳所有群組。

例如：

```
[
    ["eat","tea","ate"],
    ["tan","nat"],
    ["bat"]
]
```

---

### Time Complexity

假設：

```
n = 字串數量
k = 每個字串平均長度
```

每個字串：

```
建立 frequency
```

需要：

```
O(26)
```

掃描字元：

```
O(k)
```

因此每個字串：

```
O(26 + k)
```

因為：

```
26 是常數
```

所以化簡成：

```
O(k)
```

總時間：

```
O(n × k)
```

### Space Complexity

HashMap：

儲存所有字串：

```
O(n)
```

Frequency Array：

```
26
```

固定大小：

```
O(1)
```

總空間：

```
O(n)
```

---

## 程式碼(Counter)

```python
from collections import defaultdict, Counter

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)

        for word in strs:
            count = Counter(word)
            key = tuple(sorted(count.items()))
            anagrams[key].append(word)

        return list(anagrams.values())
```

---

## 程式碼逐行解釋

```python
from collections import defaultdict, Counter
```

匯入：

- `defaultdict`：自動建立空的 `list`
- `Counter`：統計每個字元出現的次數

---

```python
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
```

建立題目要求的函式。

輸入：

```text
List[str]
```

輸出：

```text
List[List[str]]
```

---

```python
anagrams = defaultdict(list)
```

建立 HashMap：

- `key`：字串的字元頻率
- `value`：具有相同字元頻率的字串群組

例如：

```text
{
    (('a', 1), ('e', 1), ('t', 1)):
    ["eat", "tea", "ate"]
}
```

---

```python
for word in strs:
```

依序處理每一個字串。

例如：

```text
["eat", "tea", "tan"]
```

會依序處理：

```text
"eat"
"tea"
"tan"
```

---

```python
count = Counter(word)
```

計算目前字串中，每個字元出現的次數。

例如：

```python
word = "eat"
```

得到：

```python
Counter({
    'e': 1,
    'a': 1,
    't': 1
})
```

如果：

```python
word = "aab"
```

得到：

```python
Counter({
    'a': 2,
    'b': 1
})
```

---

```python
count.items()
```

取得每個字元與出現次數。

例如：

```python
Counter("eat").items()
```

內容類似：

```text
('e', 1)
('a', 1)
('t', 1)
```

---

```python
sorted(count.items())
```

按照字元排序。

例如：

```text
[('e', 1), ('a', 1), ('t', 1)]
```

排序後：

```text
[('a', 1), ('e', 1), ('t', 1)]
```

必須排序，因為不同字串建立 `Counter` 時，字元的插入順序可能不同。

例如：

```text
"eat" → e, a, t
"tea" → t, e, a
```

排序後兩者才會產生相同順序。

---

```python
key = tuple(sorted(count.items()))
```

將排序後的 List 轉成 Tuple。

例如：

```text
[('a', 1), ('e', 1), ('t', 1)]
```

轉成：

```text
(('a', 1), ('e', 1), ('t', 1))
```

因為：

```text
List 是 mutable
```

不能當作 Dictionary Key。

而：

```text
Tuple 是 immutable
```

可以當作 Dictionary Key。

---

```python
anagrams[key].append(word)
```

將目前字串放進對應的 Anagram 群組。

例如：

```text
"eat"
```

加入後：

```text
key → ["eat"]
```

接著處理 `"tea"`，因為它產生相同的 key：

```text
key → ["eat", "tea"]
```

再處理 `"ate"`：

```text
key → ["eat", "tea", "ate"]
```

---

```python
return list(anagrams.values())
```

取得 HashMap 中的所有群組，並轉成 List 回傳。

例如：

```text
[
    ["eat", "tea", "ate"],
    ["tan", "nat"],
    ["bat"]
]
```

---

## 為什麼 Anagram 會有相同的 Key？

例如：

```text
"eat"
"tea"
"ate"
```

三個字串都有：

```text
a：1 次
e：1 次
t：1 次
```

因此排序後的 Counter items 都是：

```text
(('a', 1), ('e', 1), ('t', 1))
```

所以會被放進同一個 HashMap 群組。

### Time Complexity

假設：

```text
n = 字串數量
k = 每個字串的平均長度
m = 每個字串中不同字元的數量
```

### 建立 Counter

```python
count = Counter(word)
```

需要掃過字串中的每個字元：

```text
O(k)
```

### 排序不同字元

```python
sorted(count.items())
```

`Counter` 中共有 `m` 個不同字元，因此排序需要：

```text
O(m log m)
```


#### 每個字串

```text
O(k + m log m)
```

#### 所有字串

```text
O(n × (k + m log m))
```

其中：

```text
m ≤ k
```

最差情況下，每個字元都不相同：

```text
m = k
```

因此最差時間複雜度可以寫成：

```text
O(n × k log k)
```

如果字串很長，但只有少數不同字元：

```text
m << k
```

Counter 版本可能接近：

```text
O(n × k)
```

### Space Complexity

### 回傳結果與 HashMap

所有輸入字串都會被存入群組中：

```text
O(nk)
```

#### Counter

每個字串最多儲存 `m` 個不同字元：

```text
O(m)
```

#### Key

每個 key 包含 `m` 組：

```text
(character, count)
```

所有字串最差可能產生不同的 key，因此額外空間最差為：

```text
O(nm)
```

整體空間複雜度可寫成：

```text
O(nk)
```

因為輸出本身就需要保存所有字串。

---

## 三種方法比較

```text
排序字串：

key = ''.join(sorted(word))

Time：O(n × k log k)
適合：最簡單、支援 Unicode
```

```text
26 字母 Frequency Array：

freq = [0] * 26

Time：O(n × k)
適合：題目限定小寫英文字母
```

```text
Counter：

key = tuple(sorted(Counter(word).items()))

Time：O(n × (k + m log m))
適合：支援 Unicode，且不同字元種類 m 可能遠小於字串長度 k
```