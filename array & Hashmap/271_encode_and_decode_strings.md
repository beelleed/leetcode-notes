# 📍 LeetCode 271 - Encode and Decode Strings

**Difficulty:** Medium

**Topics:**

* String
* Design
* Encoding
* Two Pointers
* String Parsing

## 📄 題目說明 | Problem Description

### 中文

給定一個字串陣列：

```python
strs
```

我們需要設計兩個函式：

```python
encode
```

和：

```python
decode
```

---

### Encode

```python
encode
```

需要把一組字串：

```python
List[str]
```

編碼成一個單一字串：

```python
str
```

例如：

```python
["hello", "world"]
```

可能被編碼成：

```text
5#hello5#world
```

---

### Decode

```python
decode
```

需要把編碼後的字串還原成原本的字串陣列。

例如：

```text
5#hello5#world
```

解碼後得到：

```python
["hello", "world"]
```

---

### 題目的核心要求

我們需要保證：

```python
decode(encode(strs)) == strs
```

也就是：

> 經過編碼再解碼後，必須完整還原原本的所有字串。

---

### English

Design an algorithm to encode a list of strings into a single string and decode that string back into the original list.

The encoded string must preserve:

```text
the number of strings
the content of each string
empty strings
special characters
```

The two functions must satisfy:

```python
decode(encode(strs)) == strs
```

---

### Example 1

輸入：

```python
strs = ["hello", "world"]
```

編碼：

```text
5#hello5#world
```

解碼：

```python
["hello", "world"]
```

---

### Example 2

輸入：

```python
strs = ["neet", "code", "love", "you"]
```

每個字串長度：

```text
"neet" → 4
"code" → 4
"love" → 4
"you"  → 3
```

編碼結果：

```text
4#neet4#code4#love3#you
```

解碼後：

```python
["neet", "code", "love", "you"]
```

---

### Example 3：包含空字串

輸入：

```python
strs = ["", "abc", ""]
```

第一個空字串長度是：

```text
0
```

所以編碼為：

```text
0#
```

完整編碼：

```text
0#3#abc0#
```

解碼後：

```python
["", "abc", ""]
```

---

### Example 4：字串本身包含 `#`

輸入：

```python
strs = ["a#b", "hello"]
```

第一個字串：

```text
a#b
```

長度是：

```text
3
```

編碼：

```text
3#a#b5#hello
```

雖然字串內容中也有 `#`，仍然可以正確解碼。

因為 `decode` 不會把所有 `#` 都當成分隔符號。

它只會把：

```text
長度數字後遇到的第一個 #
```

當成長度與內容之間的分隔符號。

接著根據長度讀取固定數量的字元。

## 💻 Code

```python
class Solution:

    def encode(self, strs: List[str]) -> str:
        result = []

        for word in strs:
            words = str(len(word)) + '#' + word
            result.append(words)

        return ''.join(result)

    def decode(self, s: str) -> List[str]:
        result = []
        i = 0

        while i < len(s):
            j = i

            while s[j] != '#':
                j += 1

            length = int(s[i:j])
            word = s[j + 1: j + 1 + length]

            result.append(word)
            i = j + 1 + length

        return result
```

## 🧾 逐行解釋 | Line-by-line Explanation

### 建立 Solution Class

```python
class Solution:
```

LeetCode 固定要求將解法寫在：

```python
class Solution
```

裡面。

這題需要在同一個 Class 中實作：

```python
encode
```

以及：

```python
decode
```

兩個函式。

---

### 定義 Encode 函式

```python
def encode(self, strs: List[str]) -> str:
```

輸入：

```python
strs
```

是一個字串陣列。

例如：

```python
["hello", "world"]
```

函式回傳：

```python
str
```

也就是一個單一的編碼字串。

例如：

```text
5#hello5#world
```

---

### 建立 Result List

```python
result = []
```

建立一個空 List，用來保存每一個字串編碼後的結果。

例如之後可能變成：

```python
result = [
    "5#hello",
    "5#world"
]
```

最後再使用：

```python
''.join(result)
```

把所有部分連接成一個字串。

---

### 為什麼使用 List？

也可以直接寫：

```python
result = ""
```

然後不斷做：

```python
result += encoded_word
```

但是 Python 的 String 是 Immutable。

每次使用：

```python
+=
```

都有可能建立新的字串。

當資料很多時，效率可能較差。

使用 List 收集所有部分，最後一次：

```python
''.join(result)
```

通常更有效率。

---

### 逐一處理每個 Word

```python
for word in strs:
```

逐一取得：

```python
strs
```

中的每個字串。

例如：

```python
strs = ["hello", "world"]
```

迴圈會依序取得：

```python
word = "hello"
```

接著：

```python
word = "world"
```

---

### 建立每個字串的編碼格式

```python
words = str(len(word)) + '#' + word
```

這一行是整個 Encode 的核心。

每一個字串都被編碼成：

```text
字串長度 + # + 原始字串
```

也就是：

```text
length#word
```

---

### 計算字串長度

```python
len(word)
```

例如：

```python
word = "hello"
```

則：

```python
len(word)
```

得到：

```python
5
```

---

### 將長度轉成字串

```python
str(len(word))
```

`len(word)` 回傳的是 Integer。

例如：

```python
5
```

但是後面要和：

```python
'#'
```

以及：

```python
word
```

做字串連接。

所以需要先將 Integer 轉成 String：

```python
"5"
```

---

### 為什麼不能直接寫？

錯誤：

```python
len(word) + '#' + word
```

因為：

```python
len(word)
```

是 Integer。

而：

```python
'#'
```

是 String。

Python 不允許直接將 Integer 和 String 相加。

會出現：

```text
TypeError
```

所以必須寫：

```python
str(len(word))
```

---

### 加入分隔符號

```python
'#'
```

`#` 用來分隔：

```text
字串長度
```

和：

```text
字串內容
```

例如：

```python
word = "hello"
```

得到：

```text
5#hello
```

其中：

```text
5
```

表示字串長度。

```text
#
```

表示長度數字結束。

```text
hello
```

是原始字串內容。

---

### 為什麼需要分隔符號？

假設只有長度和內容：

```text
5hello
```

讀取時可能還算容易。

但是如果長度超過一位數，例如：

```text
12abcdefghijkl
```

我們不知道長度數字是：

```text
1
```

還是：

```text
12
```

所以需要一個特殊符號標示：

```text
長度數字在哪裡結束
```

例如：

```text
12#abcdefghijkl
```

看到 `#` 就知道：

```text
12
```

是完整長度。

---

### 為什麼變數叫 `words`？

```python
words = str(len(word)) + '#' + word
```

這個變數實際上保存的是：

```text
單一 word 編碼後的結果
```

所以更直覺的名稱可以是：

```python
encoded_word
```

例如：

```python
encoded_word = str(len(word)) + '#' + word
```

不過原本的：

```python
words
```

也不影響程式正確性。

---

### 將編碼結果加入 List

```python
result.append(words)
```

例如：

```python
words = "5#hello"
```

執行後：

```python
result = ["5#hello"]
```

下一個字串：

```python
words = "5#world"
```

執行後：

```python
result = [
    "5#hello",
    "5#world"
]
```

---

### 合併所有編碼結果

```python
return ''.join(result)
```

`join` 會將 List 中所有字串連接起來。

前面的：

```python
''
```

表示：

```text
中間不加入任何額外字元
```

例如：

```python
result = [
    "5#hello",
    "5#world"
]
```

執行：

```python
''.join(result)
```

得到：

```text
5#hello5#world
```

---

### 如果使用其他 Join 字元

例如：

```python
'-'.join(result)
```

會得到：

```text
5#hello-5#world
```

但這份編碼格式不需要額外的分隔符號。

因為每一個字串本身都已經包含：

```text
length#
```

所以直接使用空字串 Join 即可。

---

### 定義 Decode 函式

```python
def decode(self, s: str) -> List[str]:
```

輸入：

```python
s
```

是由 `encode` 產生的單一編碼字串。

例如：

```text
5#hello5#world
```

函式需要回傳原始字串陣列：

```python
["hello", "world"]
```

---

### 建立 Decode Result

```python
result = []
```

建立一個空 List，用來保存解碼後的每個字串。

例如最後：

```python
result = [
    "hello",
    "world"
]
```

---

### 初始化 Pointer `i`

```python
i = 0
```

`i` 表示：

> 下一段編碼資料開始的位置。

一開始從編碼字串的第一個字元開始。

例如：

```text
5#hello5#world
^
i
```

此時：

```python
i = 0
```

---

### 只要還有資料就繼續解碼

```python
while i < len(s):
```

只要：

```python
i
```

還沒有走到字串結尾，就代表還有尚未解碼的字串。

例如：

```python
s = "5#hello5#world"
```

長度是：

```python
14
```

只要：

```python
i < 14
```

就繼續處理。

---

### 如果編碼字串是空字串

假設原本：

```python
strs = []
```

Encode 結果：

```python
""
```

Decode 時：

```python
len(s) = 0
i = 0
```

條件：

```python
i < len(s)
```

也就是：

```python
0 < 0
```

不成立。

所以直接回傳：

```python
[]
```

正確還原空 List。

---

### 建立 Pointer `j`

```python
j = i
```

`j` 從目前資料開始的位置出發。

它的任務是：

> 找到接下來的 `#`。

也就是找出長度數字的結尾。

例如：

```text
12#abcdefghijkl
^
i
j
```

`j` 會一路往右移，直到找到：

```text
#
```

---

### 尋找 `#`

```python
while s[j] != '#':
    j += 1
```

只要目前字元不是：

```text
#
```

就繼續向右移動。

---

### Example

假設：

```python
s = "5#hello"
```

初始：

```python
i = 0
j = 0
```

目前：

```python
s[j] = "5"
```

不是 `#`。

所以：

```python
j += 1
```

得到：

```python
j = 1
```

此時：

```python
s[1] = "#"
```

停止迴圈。

---

### 多位數長度 Example

假設：

```python
s = "12#abcdefghijkl"
```

初始：

```python
i = 0
j = 0
```

---

第一步：

```python
s[0] = "1"
```

不是 `#`。

所以：

```python
j = 1
```

---

第二步：

```python
s[1] = "2"
```

不是 `#`。

所以：

```python
j = 2
```

---

第三步：

```python
s[2] = "#"
```

找到分隔符號。

此時：

```text
s[i:j] = s[0:2] = "12"
```

所以長度是：

```python
12
```

---

### 取得字串長度

```python
length = int(s[i:j])
```

`s[i:j]` 取得：

```text
從 i 開始，到 j 之前的所有字元
```

這部分就是字串長度。

---

### Example

假設：

```python
s = "5#hello"
i = 0
j = 1
```

則：

```python
s[i:j]
```

也就是：

```python
s[0:1]
```

得到：

```text
"5"
```

接著：

```python
int("5")
```

得到 Integer：

```python
5
```

所以：

```python
length = 5
```

---

### 為什麼需要轉成 Integer？

從字串切片取得的：

```python
s[i:j]
```

是 String。

例如：

```python
"5"
```

但是稍後要用它計算切片終點：

```python
j + 1 + length
```

所以必須轉成 Integer：

```python
5
```

---

### 找到 Word 的起點

`j` 指向：

```text
#
```

所以真正的字串內容從：

```python
j + 1
```

開始。

例如：

```text
5#hello
  ^
 j + 1
```

---

### 根據 Length 取出完整 Word

```python
word = s[j + 1: j + 1 + length]
```

這是 Decode 最核心的一行。

起點：

```python
j + 1
```

終點：

```python
j + 1 + length
```

因為 Python Slice 不包含右端點，所以這樣剛好取得：

```text
length 個字元
```

---

### Example

假設：

```python
s = "5#hello5#world"
j = 1
length = 5
```

起點：

```python
j + 1 = 2
```

終點：

```python
j + 1 + length
= 1 + 1 + 5
= 7
```

所以：

```python
s[2:7]
```

取得：

```text
hello
```

---

### Python Slice 不包含右端點

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

所以：

```python
s[2:7]
```

實際取得 index：

```text
2,3,4,5,6
```

剛好五個字元。

---

### 為什麼不能找下一個 `#` 當 Word 結尾？

因為原始字串本身可能包含：

```text
#
```

例如：

```python
word = "a#b"
```

編碼：

```text
3#a#b
```

如果 Decode 使用：

```text
找下一個 #
```

來判斷字串內容結束位置，就會錯誤地把：

```text
a
```

當成完整字串。

正確方法是：

```text
先讀取長度 3
再固定讀取三個字元
```

得到：

```text
a#b
```

所以內容中的特殊字元完全不影響解碼。

---

### 將 Word 加入結果

```python
result.append(word)
```

例如：

```python
word = "hello"
```

執行後：

```python
result = ["hello"]
```

下一次解碼出：

```python
word = "world"
```

執行後：

```python
result = [
    "hello",
    "world"
]
```

---

### 更新 Pointer `i`

```python
i = j + 1 + length
```

這一行讓：

```python
i
```

移動到下一段編碼資料的起點。

---

### 為什麼新位置是 `j + 1 + length`？

目前字串內容開始於：

```python
j + 1
```

內容長度是：

```python
length
```

所以內容結束後的下一個位置是：

```python
j + 1 + length
```

這正好是下一個字串長度的起點。

---

### Example

編碼字串：

```text
5#hello5#world
```

Index：

```text
0 1 2 3 4 5 6 7 8 9 10 11 12 13
5 # h e l l o 5 # w  o  r  l  d
```

第一段：

```python
j = 1
length = 5
```

新位置：

```python
i = 1 + 1 + 5
```

得到：

```python
i = 7
```

Index `7` 的字元是：

```text
5
```

正好是下一個字串長度的開始。

---

### 為什麼不是 `i += length`？

因為除了字串內容外，還需要跳過：

```text
長度數字
```

以及：

```text
#
```

例如：

```text
5#hello
```

總長度是：

```text
7
```

不是只有內容長度：

```text
5
```

所以直接：

```python
i += length
```

會移到錯誤位置。

---

### 回傳解碼結果

```python
return result
```

當：

```python
i == len(s)
```

表示已經解碼完所有資料。

此時：

```python
result
```

保存原始所有字串。

例如：

```python
["hello", "world"]
```

所以直接回傳。

## 🧠 核心觀念 | Key Insight

這題最大的問題是：

> 如何知道每個字串在哪裡開始、在哪裡結束？

如果只使用一般分隔符號，例如：

```text
hello#world
```

當原始字串本身也包含：

```text
#
```

就會產生歧義。

---

### 錯誤的普通分隔符號方法

假設：

```python
strs = ["a#b", "hello"]
```

如果直接：

```python
'#'.join(strs)
```

得到：

```text
a#b#hello
```

Decode 時無法知道應該切成：

```python
["a", "b", "hello"]
```

還是：

```python
["a#b", "hello"]
```

---

### 正確方法：Length Prefix

每個字串先保存長度：

```text
length#word
```

例如：

```python
"a#b"
```

長度是：

```text
3
```

編碼：

```text
3#a#b
```

Decode 時：

```text
先找到 #
讀出長度 3
再固定讀三個字元
```

所以內容可以包含任何字元，不會造成歧義。

---

### 編碼格式

```text
長度#內容
```

多個字串直接串接：

```text
長度#內容長度#內容長度#內容
```

例如：

```python
["cat", "hello", ""]
```

編碼：

```text
3#cat5#hello0#
```

## 🧪 Example Walkthrough

使用：

```python
strs = ["neet", "code", "love", "you"]
```

### Encode 初始狀態

```python
result = []
```

---

### 第一個 Word：`"neet"`

長度：

```python
len("neet") = 4
```

編碼：

```python
words = "4" + "#" + "neet"
```

得到：

```text
4#neet
```

加入：

```python
result = ["4#neet"]
```

---

### 第二個 Word：`"code"`

長度：

```python
4
```

編碼：

```text
4#code
```

加入後：

```python
result = [
    "4#neet",
    "4#code"
]
```

---

### 第三個 Word：`"love"`

編碼：

```text
4#love
```

目前：

```python
result = [
    "4#neet",
    "4#code",
    "4#love"
]
```

---

### 第四個 Word：`"you"`

長度：

```python
3
```

編碼：

```text
3#you
```

目前：

```python
result = [
    "4#neet",
    "4#code",
    "4#love",
    "3#you"
]
```

---

### Join

```python
''.join(result)
```

得到：

```text
4#neet4#code4#love3#you
```

## 🧪 Decode Walkthrough

輸入：

```python
s = "4#neet4#code4#love3#you"
```

---

### 初始狀態

```python
result = []
i = 0
```

---

### 解碼第一個字串

目前：

```text
4#neet4#code4#love3#you
^
i
```

設定：

```python
j = i
```

所以：

```python
j = 0
```

---

### 找到 `#`

```python
s[0] = "4"
```

不是 `#`。

所以：

```python
j = 1
```

此時：

```python
s[1] = "#"
```

停止。

---

### 取得長度

```python
length = int(s[0:1])
```

得到：

```python
length = 4
```

---

### 取得字串

字串起點：

```python
j + 1 = 2
```

字串終點：

```python
j + 1 + length = 6
```

所以：

```python
word = s[2:6]
```

得到：

```text
neet
```

加入：

```python
result = ["neet"]
```

---

### 更新 `i`

```python
i = j + 1 + length
```

得到：

```python
i = 6
```

此時 index `6` 是下一個：

```text
4
```

---

### 解碼第二個字串

從：

```python
i = 6
```

開始。

找到：

```text
#
```

讀取長度：

```python
4
```

讀取四個字元：

```text
code
```

加入：

```python
result = [
    "neet",
    "code"
]
```

---

### 解碼第三、第四個字串

依照相同步驟得到：

```text
love
you
```

最後：

```python
result = [
    "neet",
    "code",
    "love",
    "you"
]
```

當：

```python
i == len(s)
```

結束迴圈並回傳。

## 📊 Decode Pointer 變化

對：

```text
4#neet4#code4#love3#you
```

| Round | `i` |  `j` 指向 | Length |  Word  | 新的 `i` |
| ----: | --: | :-----: | -----: | :----: | -----: |
|     1 |   0 | 第一個 `#` |      4 | `neet` |      6 |
|     2 |   6 | 第二個 `#` |      4 | `code` |     12 |
|     3 |  12 | 第三個 `#` |      4 | `love` |     18 |
|     4 |  18 | 第四個 `#` |      3 |  `you` |     23 |

## 🧪 Empty String Walkthrough

輸入：

```python
strs = ["", "abc"]
```

### Encode

第一個字串：

```python
word = ""
```

長度：

```python
0
```

編碼：

```text
0#
```

第二個字串：

```python
word = "abc"
```

編碼：

```text
3#abc
```

完整結果：

```text
0#3#abc
```

---

### Decode 第一個空字串

初始：

```python
i = 0
```

找到：

```text
#
```

位於：

```python
j = 1
```

長度：

```python
length = int(s[0:1])
```

得到：

```python
0
```

切片：

```python
word = s[2:2]
```

當 Slice 起點等於終點時，得到：

```python
""
```

所以成功還原空字串。

更新：

```python
i = 2
```

接著繼續解碼：

```text
3#abc
```

最後得到：

```python
["", "abc"]
```

## 🧪 Word Contains `#` Walkthrough

輸入：

```python
strs = ["a#b"]
```

### Encode

長度：

```python
3
```

編碼：

```text
3#a#b
```

---

### Decode

找到第一個 `#`：

```text
3#a#b
 ^
```

讀出長度：

```python
3
```

接著固定讀取三個字元：

```text
a#b
```

內容中的第二個 `#` 只是普通字元。

它不會被誤認為分隔符號。

所以可以正確得到：

```python
["a#b"]
```

## 🤔 為什麼不能只使用逗號分隔？

例如：

```python
','.join(strs)
```

如果：

```python
strs = ["hello", "world"]
```

得到：

```text
hello,world
```

看起來可以。

但是如果：

```python
strs = ["hello,world", "abc"]
```

得到：

```text
hello,world,abc
```

Decode 時無法知道原本是：

```python
["hello", "world", "abc"]
```

還是：

```python
["hello,world", "abc"]
```

所以單純分隔符號不夠安全。

## 🤔 為什麼 Length Prefix 不會有歧義？

因為 Decode 的流程固定是：

```text
1. 找到第一個 #
2. # 前面是長度
3. # 後固定讀取 length 個字元
4. 下一個位置就是下一段編碼的開始
```

即使字串內容包含：

```text
#
逗號
數字
空白
換行
```

都不影響解碼。

因為內容的邊界是由：

```text
length
```

決定，而不是由內容中的特殊字元決定。

## 🤔 為什麼 `#` 前面一定是數字？

因為 Encode 固定使用：

```python
str(len(word)) + '#' + word
```

所以每一段編碼都一定從：

```text
字串長度
```

開始。

Decode 只會處理由 Encode 產生的有效格式。

因此：

```python
s[i:j]
```

一定可以轉成 Integer。

## 🤔 如果字串長度超過 9 呢？

這個方法仍然有效。

例如字串長度是：

```python
12
```

編碼：

```text
12#abcdefghijkl
```

Decode 使用：

```python
while s[j] != '#':
    j += 1
```

會完整找到：

```text
12
```

而不是只讀取第一個數字。

所以支援任意位數的長度。

## 🤔 為什麼需要兩個 Pointer？

### Pointer `i`

```python
i
```

表示：

```text
目前這一段編碼的起點
```

---

### Pointer `j`

```python
j
```

表示：

```text
搜尋 # 的位置
```

---

### 兩者的配合

```text
i 到 j 之前：長度

j：#

j + 1 開始：字串內容
```

所以：

```python
s[i:j]
```

取得長度。

```python
s[j + 1:j + 1 + length]
```

取得內容。

## 🤔 為什麼 Decode 不需要 Backtracking？

因為每段資料的結構非常明確：

```text
length#word
```

讀到 length 後，就能直接知道 Word 的確切終點。

不存在多種切割可能性。

因此只要線性掃描即可，不需要：

```text
Backtracking
Dynamic Programming
```

## 🤔 為什麼 Encode 和 Decode 都是線性的？

Encode 只走訪每個字串並處理所有字元一次。

Decode 也只讓 Pointer 從左到右移動。

不會回頭，也不會重複處理同一段內容很多次。

所以整體與所有字串的總字元數成正比。

## ⚠️ 常見錯誤 | Common Mistakes

### 錯誤一：只使用特殊符號 Join

錯誤：

```python
return '#'.join(strs)
```

如果原始字串中包含 `#`，就無法正確還原。

---

### 錯誤二：沒有保存字串長度

如果只保存內容和分隔符號，內容可能包含相同分隔符號。

正確做法：

```python
str(len(word)) + '#' + word
```

---

### 錯誤三：Decode 找到所有 `#` 來 Split

錯誤：

```python
s.split('#')
```

例如：

```python
s = "3#a#b"
```

Split 後可能得到：

```python
["3", "a", "b"]
```

但原始字串應該是：

```python
["a#b"]
```

所以不能直接 Split。

---

### 錯誤四：Length 沒有轉成 Integer

錯誤：

```python
length = s[i:j]
```

此時：

```python
length
```

是 String。

後面：

```python
j + 1 + length
```

會因為 Integer 和 String 相加而出錯。

正確：

```python
length = int(s[i:j])
```

---

### 錯誤五：Word Slice 終點少了 `j + 1`

錯誤：

```python
word = s[j + 1:length]
```

`length` 是字串長度，不是絕對 index。

正確：

```python
word = s[j + 1:j + 1 + length]
```

---

### 錯誤六：更新 `i` 時少算長度資訊

錯誤：

```python
i += length
```

這只跳過字串內容，沒有正確跳過：

```text
長度數字 + #
```

正確：

```python
i = j + 1 + length
```

---

### 錯誤七：沒有處理空字串

如果使用普通分隔符號，可能無法分辨：

```python
[]
```

和：

```python
[""]
```

這份 Length Prefix 方法可以區分：

```python
[] → ""
```

```python
[""] → "0#"
```

---

### 錯誤八：把所有數字都當成 Length

只有：

```text
從 i 到下一個 # 之前
```

的數字代表 Length。

字串內容本身也可能包含數字。

例如：

```python
["123"]
```

編碼：

```text
3#123
```

內容中的 `123` 不代表下一段長度。

## 🧠 正確性說明 | Why This Works

每一個字串都被 Encode 成：

```text
length#word
```

其中：

```text
length
```

精確表示 `word` 包含多少個字元。

Decode 時：

```text
1. 從 i 開始找到第一個 #
2. 將 i 到 # 前面的字元解析成 length
3. 從 # 後讀取剛好 length 個字元
4. 將 Pointer 移到下一段開始
```

因為每段內容的長度已知，所以無論內容中出現任何特殊字元，都不會影響字串邊界。

每次 Decode 都能唯一確定下一個 Word。

因此最終可以完整還原原本的字串陣列。

## 🆚 普通 Delimiter vs Length Prefix

### 普通 Delimiter

格式：

```text
word#word#word
```

問題：

```text
如果 word 本身包含 #，就會有歧義
```

---

### Length Prefix

格式：

```text
length#word
```

優點：

```text
內容可以包含任何字元
```

因為 Decode 根據長度讀取，而不是根據分隔符號切內容。

---

### 比較

| 方法            | 可處理內容包含分隔符號 | 可處理空字串 | 是否有歧義 |
| ------------- | :---------: | :----: | :---: |
| 單純 Join       |      否      |  容易出錯  |   有   |
| Length Prefix |      是      |    是   |   無   |

## 🆚 271 vs Serialization

這題其實是一種簡單的：

```text
Serialization
```

也就是把複雜資料：

```python
List[str]
```

轉換成可以儲存或傳輸的單一格式：

```python
str
```

Decode 則是：

```text
Deserialization
```

將單一格式還原成原始資料結構。

---

### 常見的 Serialization 應用

```text
API 傳輸資料
儲存檔案
網路通訊
資料庫欄位
物件轉換
```

本題使用的是：

```text
Length-Prefixed Encoding
```

## 🆚 271 vs 297 Serialize and Deserialize Binary Tree

### LeetCode 271

資料結構：

```python
List[str]
```

使用：

```text
Length Prefix
```

來保留每個字串的邊界。

---

### LeetCode 297

資料結構：

```text
Binary Tree
```

通常使用：

```text
Preorder / BFS
+
Null Marker
```

來保存 Tree Structure。

---

### 共同點

兩題都需要保證：

```text
Deserialize(Serialize(data)) == data
```

核心都是：

```text
設計一個沒有歧義的資料格式
```

## ⏱ Complexity Analysis

假設所有輸入字串的總字元數為：

```text
n
```

字串數量為：

```text
k
```

---

### Encode

```python
for word in strs:
```

每個字串都需要：

```text
計算長度
建立編碼內容
加入結果
```

所有字串內容總共包含 `n` 個字元。

最後 Join 也需要處理所有輸出字元。

所以時間複雜度：

```text
O(n)
```

如果將長度前綴的位數也算入，則更精確可以表示為：

```text
O(n + k log n)
```

通常簡化為：

```text
O(n)
```

其中 `n` 代表完整編碼結果的長度。

---

### Decode

`i` 和 `j` 都只向右移動。

每個字元最多被檢查常數次。

所以時間複雜度：

```text
O(n)
```

---

### 總時間複雜度

Encode：

```text
O(n)
```

Decode：

```text
O(n)
```

## 💾 Space Complexity

### Encode

```python
result
```

保存編碼後的所有內容。

空間複雜度：

```text
O(n)
```

回傳字串本身也需要：

```text
O(n)
```

---

### Decode

```python
result
```

保存所有還原的字串。

空間複雜度：

```text
O(n)
```

若不計算回傳結果所需空間，額外 Pointer 空間只有：

```text
O(1)
```

## 🎯 Interview Takeaways

看到以下問題：

```text
將多個字串轉成一個字串
+
原始字串可能包含任何特殊字元
+
之後必須完整還原
```

應該想到：

```text
不能只使用普通 Delimiter
```

更安全的方式是：

```text
Length Prefix
```

也就是：

```text
字串長度 + 分隔符號 + 字串內容
```

---

### 面試時可以這樣說

```text
A delimiter-only approach is ambiguous because the original strings may contain the delimiter.

Instead, I encode every string using its length followed by a separator and the string itself.

During decoding, I first scan until the separator to parse the string length.

Then I read exactly that many characters as the original string.

Because the content boundary is determined by the stored length, the strings may contain any character, including the separator.
```

## 🗣 Interview English Version

```text
I use a length-prefixed encoding format.

For each string, I append its length, a hash symbol, and the string itself.

To decode, I use one pointer to mark the start of the length and another pointer to find the hash symbol.

The characters before the hash give me the string length.

Then I read exactly that many characters after the hash and move to the beginning of the next encoded string.

This avoids ambiguity even when the original strings contain hash symbols or are empty.
```

## ✍️ What I Learned

### 1. 普通分隔符號可能產生歧義

原始資料可能包含相同的分隔符號。

所以只使用：

```python
'#'.join(strs)
```

不夠安全。

---

### 2. Length Prefix 可以準確保留資料邊界

格式：

```text
length#word
```

讓 Decode 可以直接知道內容長度。

---

### 3. 內容可以包含任何字元

因為內容不是靠特殊符號結束。

而是靠：

```text
固定字元數量
```

決定終點。

---

### 4. Two Pointers 很適合解析格式化字串

```python
i
```

表示目前區塊起點。

```python
j
```

尋找長度與內容之間的分隔符號。

---

### 5. Slice 的終點不包含在結果中

```python
s[j + 1:j + 1 + length]
```

可以準確讀取：

```text
length 個字元
```

---

### 6. Encode 和 Decode 必須使用完全相同的格式規則

Encode 使用：

```text
length#word
```

Decode 就必須按照：

```text
先讀 length，再讀 word
```

來解析。

格式不一致就無法還原。

## 🏆 Cheat Sheet

### Encode 初始化

```python
result = []
```

---

### 逐一處理 Word

```python
for word in strs:
```

---

### 編碼格式

```python
words = str(len(word)) + '#' + word
```

格式：

```text
length#word
```

---

### 保存編碼區塊

```python
result.append(words)
```

---

### 合併結果

```python
return ''.join(result)
```

---

### Decode 初始化

```python
result = []
i = 0
```

---

### 處理每一段編碼

```python
while i < len(s):
```

---

### 尋找 `#`

```python
j = i

while s[j] != '#':
    j += 1
```

---

### 取得 Length

```python
length = int(s[i:j])
```

---

### 取得 Word

```python
word = s[j + 1:j + 1 + length]
```

---

### 保存 Word

```python
result.append(word)
```

---

### 移動到下一段

```python
i = j + 1 + length
```

---

### 回傳結果

```python
return result
```

## 🧭 解題流程圖

```text
Encode
  |
  v
建立 result List
  |
  v
逐一讀取 word
  |
  v
計算 len(word)
  |
  v
建立 length#word
  |
  v
加入 result
  |
  v
Join 所有區塊
  |
  v
回傳單一字串
```

```text
Decode
  |
  v
初始化 i = 0
  |
  v
i 是否小於 s 長度？
  |
  +------否------> 回傳 result
  |
  是
  |
  v
設定 j = i
  |
  v
向右找到 #
  |
  v
解析 s[i:j] 成 length
  |
  v
讀取 # 後 length 個字元
  |
  v
加入 result
  |
  v
i 移到下一段開頭
  |
  v
繼續迴圈
```

## 🔑 Pattern Recognition

看到：

```text
多筆資料
+
需要轉成單一字串
+
內容可能包含任意字元
+
必須無歧義還原
```

可以想到：

```text
Serialization
+
Length Prefix
+
String Parsing
```

完整 Pattern：

```text
Encode:
Length + Separator + Content

Decode:
Find Separator
→ Parse Length
→ Read Fixed-Length Content
```

## 🌟 One Sentence Summary

### English

> Encode each string as its length followed by `#` and the string itself, then decode by parsing the length and reading exactly that many characters.

### 中文

> 將每個字串編碼成「長度 + `#` + 內容」，解碼時先讀取長度，再依照長度取出固定數量的字元。

## ✅ Final Takeaway

這題最核心的格式是：

```text
length#word
```

Encode：

```python
str(len(word)) + '#' + word
```

Decode：

```python
length = int(s[i:j])
word = s[j + 1:j + 1 + length]
```

最重要的觀念是：

```text
# 只負責標示長度結束

真正的字串內容邊界由 length 決定
```

最精簡記法：

```text
Encode：

長度 + # + 字串


Decode：

找到 #

讀出長度

再讀固定長度的字串

Pointer 移到下一段
```
