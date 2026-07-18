# 📍 LeetCode 131 — Palindrome Partitioning

🔗 https://leetcode.com/problems/palindrome-partitioning/

## 📄 題目說明 | Problem Description

### 中文

給定一個字串 `s`。

請把字串切割成數個子字串，使得每一個子字串都是回文（Palindrome），並回傳所有可能的切割方式。

回文代表：

```text
從左往右讀

和

從右往左讀

完全相同
```

例如：

```text
"a"

"aa"

"aba"

"abba"
```

都是回文。

但：

```text
"ab"

"aab"

"abc"
```

不是回文。

---

### English

Given a string `s`, partition `s` such that every substring in the partition is a palindrome.

Return all possible palindrome partitionings of `s`.

A palindrome is a string that reads the same forward and backward.

---

### Examples

#### Example 1

Input

```python
s = "aab"
```

Output

```python
[
    ["a", "a", "b"],
    ["aa", "b"]
]
```

解釋：

第一種切法：

```text
"a" | "a" | "b"
```

其中：

```text
"a" 是回文

"a" 是回文

"b" 是回文
```

第二種切法：

```text
"aa" | "b"
```

其中：

```text
"aa" 是回文

"b" 是回文
```

但：

```text
"aab"
```

不是回文，所以不能直接作為一組答案。

---

#### Example 2

Input

```python
s = "a"
```

Output

```python
[
    ["a"]
]
```

因為單一字元一定是回文。

---

## 🧠 核心觀念 | Key Insight

這題也是 Backtracking。

但是它和 LeetCode 78、90、39、40 不同的地方是：

前面的題目通常是在：

```text
從陣列中選數字
```

這題則是在：

```text
決定字串要在哪裡切割
```

---

### 這題真正要做的是什麼？

假設：

```python
s = "aab"
```

我們需要嘗試所有可能的切割方式。

例如：

```text
a | a | b
```

或：

```text
aa | b
```

或：

```text
aab
```

但每切出一段，都必須先確認：

```text
這一段是不是回文
```

只有是回文的子字串，才可以放進 `path`。

---

### Backtracking 的選擇是什麼？

在 LeetCode 40 中：

```text
每一次選擇一個數字
```

在 LeetCode 131 中：

```text
每一次選擇一段子字串
```

例如：

```python
s = "aab"
```

從 index `0` 開始時，可以考慮：

```text
s[0:1] = "a"

s[0:2] = "aa"

s[0:3] = "aab"
```

這三個代表三種可能的第一段。

但只有：

```text
"a"

"aa"
```

是回文。

所以：

```text
"aab"
```

不能進入下一層遞迴。

---

### start 是什麼？

```python
def backtrack(start, path):
```

其中：

```text
start
```

代表：

```text
下一段子字串要從哪一個 index 開始切
```

例如：

```python
s = "aab"
```

一開始：

```python
start = 0
```

代表從：

```text
aab
↑
```

第一個字元開始切。

如果先選：

```text
"a"
```

下一層：

```python
start = 1
```

代表剩下：

```text
aab
 ↑
```

要從第二個字元開始切。

如果先選：

```text
"aa"
```

下一層：

```python
start = 2
```

代表剩下：

```text
aab
  ↑
```

要從 `b` 開始切。

---

### path 是什麼？

```text
path
```

代表：

```text
目前已經切好的回文字串
```

例如：

```python
path = []
```

代表尚未切出任何子字串。

選擇 `"a"`：

```python
path = ["a"]
```

再選擇 `"a"`：

```python
path = ["a", "a"]
```

再選擇 `"b"`：

```python
path = ["a", "a", "b"]
```

這時所有字元都已經使用完，所以這是一組完整答案。

---

### 什麼時候找到答案？

當：

```python
start == len(s)
```

代表：

```text
整個字串都已經切割完成
```

例如：

```python
s = "aab"
len(s) = 3
```

如果：

```python
start = 3
```

代表目前已經走到字串結尾。

此時：

```python
path
```

一定是一組完整的回文切割。

所以：

```python
res.append(path[:])
```

---

### 為什麼不是每一層都加入答案？

LeetCode 90 Subsets II 中：

```python
res.append(path[:])
```

會放在每一層遞迴的最前面。

因為：

```text
每一個部分選擇

本身就是一個合法 subset
```

例如：

```text
[]

[1]

[1,2]
```

全部都是合法子集合。

但是 LeetCode 131 不一樣。

假設：

```python
s = "aab"
path = ["a"]
```

目前只切掉第一個字元，後面的：

```text
"ab"
```

還沒有處理。

因此：

```python
["a"]
```

不是完整答案。

必須等到：

```python
start == len(s)
```

整個字串都切完，才能加入答案。

---

### 如何產生每一段子字串？

使用：

```python
for end in range(start + 1, len(s) + 1):
```

然後：

```python
substring = s[start:end]
```

注意 Python slicing：

```python
s[start:end]
```

包含：

```text
start
```

但不包含：

```text
end
```

例如：

```python
s = "aab"
```

如果：

```python
start = 0
end = 1
```

得到：

```python
s[0:1] = "a"
```

如果：

```python
start = 0
end = 2
```

得到：

```python
s[0:2] = "aa"
```

如果：

```python
start = 0
end = 3
```

得到：

```python
s[0:3] = "aab"
```

所以 `end` 必須跑到：

```python
len(s) + 1
```

才有機會取得包含最後一個字元的子字串。

---

### 為什麼 `end` 從 `start + 1` 開始？

因為我們至少要切出一個字元。

如果：

```python
end = start
```

那麼：

```python
s[start:end]
```

會得到：

```python
""
```

空字串。

這題不需要選擇空字串，所以：

```python
end
```

要從：

```python
start + 1
```

開始。

---

### 如何判斷回文？

最直覺的方法：

```python
substring == substring[::-1]
```

其中：

```python
substring[::-1]
```

代表將字串反轉。

例如：

```python
substring = "aba"
```

反轉後：

```python
substring[::-1] = "aba"
```

兩者相同，所以是回文。

例如：

```python
substring = "ab"
```

反轉後：

```python
substring[::-1] = "ba"
```

兩者不同，所以不是回文。

---

### 為什麼不是回文就 `continue`？

```python
if substring != substring[::-1]:
    continue
```

代表：

```text
目前切出的這一段不是回文

不能加入 path
```

但同一層還有其他更長的子字串可以嘗試。

例如：

```python
s = "aab"
start = 1
```

可以嘗試：

```text
"a"

"ab"
```

如果 `"ab"` 不是回文，只需要跳過 `"ab"`。

因此使用：

```python
continue
```

而不是：

```python
break
```

---

### 為什麼不能使用 break？

假設：

```python
s = "aba"
start = 0
```

依序檢查：

```text
"a"   → 回文

"ab"  → 不是回文

"aba" → 回文
```

如果看到：

```text
"ab"
```

不是回文就執行：

```python
break
```

那程式就不會繼續檢查：

```text
"aba"
```

但 `"aba"` 明明是合法回文。

所以這裡只能：

```python
continue
```

不能：

```python
break
```

因為：

```text
較短的字串不是回文

不代表更長的字串也不是回文
```

這和 LeetCode 40 的排序剪枝不同。

LeetCode 40 中，排序後如果目前數字已經太大，後面的數字一定更大，所以可以 `break`。

但字串回文沒有這種單調性。

---

### 標準 Backtracking 流程

每找到一段回文後：

```python
path.append(substring)
```

接著從 `end` 繼續切：

```python
backtrack(end, path)
```

最後恢復現場：

```python
path.pop()
```

完整流程：

```text
找到回文 substring

↓

加入 path

↓

從 substring 後面繼續切

↓

探索完後 pop

↓

嘗試其他切法
```

---

## 💻 Code

```python
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []

        def backtrack(start, path):
            if start == len(s):
                res.append(path[:])
                return

            for end in range(start + 1, len(s) + 1):
                substring = s[start:end]

                if substring != substring[::-1]:
                    continue

                path.append(substring)

                backtrack(end, path)

                path.pop()

        backtrack(0, [])

        return res
```

---

## 🧾 程式碼逐行解釋 | Line-by-line Explanation

```python
class Solution:
```

* 定義 LeetCode 使用的 `Solution` 類別。

---

```python
def partition(self, s: str) -> List[List[str]]:
```

* 定義主要函式 `partition`。
* `s` 是需要切割的原始字串。
* 回傳所有合法的回文切割方式。
* 回傳型態：

```python
List[List[str]]
```

代表答案中有很多組字串陣列。

例如：

```python
[
    ["a", "a", "b"],
    ["aa", "b"]
]
```

---

```python
res = []
```

* 建立答案陣列。
* 每一組完整的回文切割都會加入 `res`。

---

```python
def backtrack(start, path):
```

* 建立 Backtracking 函式。
* `start` 代表下一段子字串的起始 index。
* `path` 代表目前已經切出的回文字串。

例如：

```python
s = "aab"
start = 2
path = ["aa"]
```

代表：

```text
前面的 "aa" 已經切好

接下來要從 index 2 的 "b" 開始切
```

---

```python
if start == len(s):
```

* 判斷是否已經走到字串結尾。
* 如果 `start` 等於字串長度，代表每個字元都已經被完整切割。

例如：

```python
s = "aab"
len(s) = 3
start = 3
```

代表：

```text
index 0、1、2 都已經處理完成
```

---

```python
res.append(path[:])
```

* 將目前完整的切割方式複製後加入答案。

一定要使用：

```python
path[:]
```

不能直接：

```python
res.append(path)
```

因為所有遞迴層都共用同一個 `path`。

後續的：

```python
path.append(...)
path.pop()
```

會修改這個 list。

使用：

```python
path[:]
```

可以建立獨立副本，避免答案被後續操作修改。

---

```python
return
```

* 已經切完整個字串，所以結束目前這條分支。
* 不需要再繼續切割。

---

```python
for end in range(start + 1, len(s) + 1):
```

* 嘗試所有可能的子字串結尾位置。
* `end` 是 slicing 的右邊界，不包含在子字串內。

假設：

```python
s = "aab"
start = 0
```

`end` 會依序是：

```text
1

2

3
```

對應：

```python
s[0:1] = "a"

s[0:2] = "aa"

s[0:3] = "aab"
```

---

```python
substring = s[start:end]
```

* 取出目前考慮的子字串。

例如：

```python
s = "aab"
start = 0
end = 2
```

得到：

```python
substring = "aa"
```

---

```python
if substring != substring[::-1]:
```

* 判斷目前子字串是否不是回文。
* `substring[::-1]` 是反轉後的字串。

例如：

```python
substring = "aa"
substring[::-1] = "aa"
```

兩者相同，是回文。

例如：

```python
substring = "ab"
substring[::-1] = "ba"
```

兩者不同，不是回文。

---

```python
continue
```

* 如果目前子字串不是回文，就不選它。
* 跳到下一個 `end`，繼續嘗試其他更長的子字串。

不能使用 `break`，因為目前不是回文，不代表後面的更長子字串不是回文。

例如：

```text
"ab" 不是回文

但

"aba" 是回文
```

---

```python
path.append(substring)
```

* 將目前合法的回文字串加入 `path`。

例如：

```python
path = ["a"]
substring = "a"
```

加入後：

```python
path = ["a", "a"]
```

---

```python
backtrack(end, path)
```

* 從目前子字串的結尾位置繼續切割。
* 下一段子字串從 index `end` 開始。

例如：

```python
s = "aab"
substring = s[0:2] = "aa"
end = 2
```

下一層：

```python
backtrack(2, ["aa"])
```

代表接下來從：

```text
aab
  ↑
```

`b` 的位置開始切。

---

### 為什麼傳 `end`，不是 `end + 1`？

因為 Python slicing：

```python
s[start:end]
```

不包含 index `end`。

例如：

```python
s[0:2]
```

使用的是：

```text
index 0

index 1
```

不包含：

```text
index 2
```

所以 index `2` 還沒有被使用。

因此下一段必須從：

```python
end
```

開始，而不是：

```python
end + 1
```

如果使用 `end + 1`，會跳過一個字元。

---

```python
path.pop()
```

* 下一層遞迴探索完後，移除剛才加入的子字串。
* 恢復到做選擇之前的狀態。

例如：

原本：

```python
path = ["a"]
```

加入：

```python
path.append("a")
```

變成：

```python
path = ["a", "a"]
```

探索完後：

```python
path.pop()
```

恢復成：

```python
path = ["a"]
```

接著就可以嘗試其他切法。

---

```python
backtrack(0, [])
```

* 從字串 index `0` 開始。
* 一開始尚未切出任何子字串，所以 `path` 是空陣列。

初始狀態：

```python
start = 0
path = []
```

---

```python
return res
```

* 回傳所有完整的回文切割方式。

---

## 🧪 Example Walkthrough

### Example 1

Input：

```python
s = "aab"
```

字串 index：

```text
index:  0   1   2
        a   a   b
```

初始呼叫：

```python
backtrack(0, [])
```

目前：

```text
start = 0

path = []
```

---

### 第一層：從 index 0 開始切

```python
for end in range(1, 4):
```

所以 `end` 會依序是：

```text
1

2

3
```

---

### 選擇一：`end = 1`

取出：

```python
substring = s[0:1]
```

得到：

```python
substring = "a"
```

判斷回文：

```python
"a" == "a"[::-1]
```

成立。

所以：

```python
path.append("a")
```

目前：

```python
path = ["a"]
```

下一層：

```python
backtrack(1, ["a"])
```

---

### 第二層：從 index 1 開始切

目前：

```text
start = 1

path = ["a"]
```

剩下字串：

```text
aab
 ↑
```

可以嘗試：

```python
s[1:2] = "a"

s[1:3] = "ab"
```

---

### 第二層選擇一：`substring = "a"`

```python
end = 2
substring = s[1:2] = "a"
```

`"a"` 是回文。

加入：

```python
path = ["a", "a"]
```

下一層：

```python
backtrack(2, ["a", "a"])
```

---

### 第三層：從 index 2 開始切

目前：

```text
start = 2

path = ["a", "a"]
```

剩下：

```text
aab
  ↑
```

只有一種切法：

```python
s[2:3] = "b"
```

`"b"` 是回文。

加入：

```python
path = ["a", "a", "b"]
```

下一層：

```python
backtrack(3, ["a", "a", "b"])
```

---

### 到達字串結尾

現在：

```python
start = 3
len(s) = 3
```

所以：

```python
start == len(s)
```

成立。

加入答案：

```python
res = [
    ["a", "a", "b"]
]
```

然後 `return`。

---

### 第一次 Backtracking

回到：

```python
path = ["a", "a", "b"]
```

執行：

```python
path.pop()
```

恢復成：

```python
path = ["a", "a"]
```

第三層沒有其他子字串可選，所以返回上一層。

再次：

```python
path.pop()
```

恢復成：

```python
path = ["a"]
```

---

### 第二層選擇二：`substring = "ab"`

現在第二層繼續：

```python
end = 3
substring = s[1:3] = "ab"
```

反轉：

```python
"ab"[::-1] = "ba"
```

因為：

```python
"ab" != "ba"
```

所以不是回文。

執行：

```python
continue
```

不會加入 `path`，也不會進入下一層遞迴。

第二層結束。

回到第一層後：

```python
path.pop()
```

將：

```python
["a"]
```

恢復成：

```python
[]
```

---

### 第一層選擇二：`substring = "aa"`

現在：

```python
end = 2
substring = s[0:2] = "aa"
```

反轉後：

```python
"aa"[::-1] = "aa"
```

所以 `"aa"` 是回文。

加入：

```python
path = ["aa"]
```

下一層：

```python
backtrack(2, ["aa"])
```

---

### 從 index 2 開始

目前：

```text
start = 2

path = ["aa"]
```

可以取：

```python
substring = s[2:3] = "b"
```

`"b"` 是回文。

加入：

```python
path = ["aa", "b"]
```

下一層：

```python
backtrack(3, ["aa", "b"])
```

因為：

```python
start == len(s)
```

所以加入答案：

```python
res = [
    ["a", "a", "b"],
    ["aa", "b"]
]
```

---

### 第一層選擇三：`substring = "aab"`

Backtracking 回到：

```python
path = []
```

接著：

```python
end = 3
substring = s[0:3] = "aab"
```

反轉：

```python
"aab"[::-1] = "baa"
```

因為：

```python
"aab" != "baa"
```

所以不是回文。

執行：

```python
continue
```

搜尋結束。

---

### 最終答案

```python
[
    ["a", "a", "b"],
    ["aa", "b"]
]
```

---

### Recursion Tree

```text
                         []
                  /       |        \
                "a"      "aa"      "aab" ×
                /          \
             ["a"]        ["aa"]
             /   \           \
          "a"    "ab" ×       "b"
           |                   |
       ["a","a"]           ["aa","b"] ✓
           |
          "b"
           |
    ["a","a","b"] ✓
```

其中：

```text
"aab" ×
```

代表不是回文，所以不進入遞迴。

```text
"ab" ×
```

也代表不是回文，所以直接跳過。

---

## ⏱ Complexity Analysis

### Time Complexity

最壞情況下：

```text
每一個字元之間

都可以選擇切或不切
```

長度為 `n` 的字串中，有：

```text
n - 1
```

個可以切割的位置。

每個位置有兩種可能：

```text
切

或

不切
```

所以最多有：

```text
2^(n - 1)
```

種切割方式。

通常可以寫成：

```text
O(2^n)
```

但是目前程式每次判斷回文使用：

```python
substring == substring[::-1]
```

建立 substring 和反轉字串都可能需要：

```text
O(n)
```

每找到一組答案時，複製 `path` 也最多需要：

```text
O(n)
```

因此較完整的時間複雜度通常寫成：

```text
O(n × 2^n)
```

---

### Space Complexity

不包含輸出答案時：

遞迴深度最多為：

```text
O(n)
```

因為最細的切割方式是每個字元單獨一段：

```python
["a", "a", "b", ...]
```

`path` 最多也會存放 `n` 個子字串。

因此額外空間：

```text
O(n)
```

如果考慮 slicing 和反轉時建立的暫時字串，單條遞迴路徑中可能使用更多暫時空間，但面試通常仍將主要遞迴額外空間寫成：

```text
O(n)
```

如果包含輸出答案：

```text
O(n × 2^n)
```

---

## 🎯 Interview Takeaways

* 看到「回傳所有切割方式」通常想到 Backtracking。
* `start` 代表下一個子字串開始的位置。
* `end` 代表目前子字串的右邊界。
* Python slicing：

```python
s[start:end]
```

包含 `start`，不包含 `end`。

* 下一層遞迴要傳：

```python
backtrack(end, path)
```

而不是：

```python
backtrack(end + 1, path)
```

* 找到完整答案的條件：

```python
if start == len(s):
```

* 不是每一層都可以加入答案，必須整個字串都切完。
* 每次只選擇回文字串：

```python
if substring != substring[::-1]:
    continue
```

* 不能因為某個子字串不是回文就 `break`，因為更長的子字串仍可能是回文。
* Backtracking 標準流程：

```text
append

↓

recursive call

↓

pop
```

---

## ✍️ 我學到的東西 | What I Learned

* LeetCode 131 的選擇不是數字，而是一段子字串。
* `start` 表示目前還沒處理的字串起點。
* `end` 用來列舉所有可能的切割位置。
* 每次要先檢查目前子字串是否為回文。
* 只有回文才能加入 `path`。
* `path` 代表目前已經切出的所有回文字串。
* 當 `start == len(s)`，代表整個字串已經成功切完。
* 這時才能把 `path[:]` 加入答案。
* `path[:]` 是建立副本，避免後續 `pop()` 修改答案。
* `backtrack(end, path)` 表示下一段從目前 substring 後面繼續。
* 非回文使用 `continue`，不能使用 `break`。
* 一個短子字串不是回文，不代表延伸後的長子字串也不是回文。
* LeetCode 131 和 Subsets 題型相似，但 base case 不同。

---

## 🏆 Cheat Sheet

```text
LeetCode 131 — Palindrome Partitioning

Backtracking 狀態：

start
path

↓

完整切完字串：

if start == len(s):
    res.append(path[:])
    return

↓

嘗試所有結尾：

for end in range(start + 1, len(s) + 1):

↓

取 substring：

substring = s[start:end]

↓

不是回文：

if substring != substring[::-1]:
    continue

↓

做選擇：

path.append(substring)

↓

下一段從 end 開始：

backtrack(end, path)

↓

撤銷選擇：

path.pop()
```

### LeetCode 90 vs LeetCode 131

| 題目           | 每次選擇什麼 | 何時加入答案         |
| ------------ | ------ | -------------- |
| LeetCode 90  | 一個數字   | 每一層都是合法 subset |
| LeetCode 131 | 一段回文字串 | 整個字串切完時        |

### `continue` vs `break`

```python
if substring != substring[::-1]:
    continue
```

代表：

```text
目前這個 substring 不是回文

跳過它

但繼續嘗試其他 end
```

不能寫：

```python
break
```

因為：

```text
目前不是回文

不代表更長的 substring 不是回文
```

例如：

```text
"ab" 不是回文

但 "aba" 是回文
```

---

## 🌟 One Sentence Summary

> Use backtracking to try every possible substring starting at `start`, only choose it when it is a palindrome, and add the current partition when the entire string has been used.

> 使用 Backtracking 從 `start` 嘗試所有可能的子字串，只有回文才能加入 `path`，當整個字串都切割完成時，再把目前的切割方式加入答案。
