# 📍 LeetCode 763 - Partition Labels

**Difficulty:** Medium

**Topics:**

* Greedy
* Hash Map
* Two Pointers
* String

## 📄 題目說明 | Problem Description

### 中文

給定一個字串：

```python
s
```

我們需要將字串切割成盡可能多個片段，並且必須滿足：

> 同一個字母最多只能出現在其中一個片段裡。

換句話說，如果字母 `a` 出現在第一個片段，它之後就不能再出現在其他片段。

最後回傳：

```text
每個片段的長度
```

---

### English

You are given a string `s`.

Partition the string into as many parts as possible so that each letter appears in at most one part.

Return a list containing the size of each partition.

---

### Example 1

```python
s = "ababcbacadefegdehijhklij"
```

輸出：

```python
[9,7,8]
```

可以切成：

```text
ababcbaca | defegde | hijhklij
```

三個片段的長度分別是：

```text
9, 7, 8
```

---

### 為什麼不能切得更小？

第一個字母是：

```text
a
```

`a` 最後一次出現的位置是 index `8`。

所以第一個片段至少要包含到 index `8`。

但是在 index `1` 遇到字母：

```text
b
```

`b` 最後一次出現的位置是 index `5`。

在 index `4` 又遇到：

```text
c
```

`c` 最後一次出現的位置是 index `7`。

因此第一個片段的結尾必須涵蓋這些字母的最後出現位置。

最終第一段是：

```text
ababcbaca
```

長度：

```text
9
```

---

### Example 2

```python
s = "eccbbbbdec"
```

輸出：

```python
[10]
```

所有字母互相牽連，因此整個字串只能形成一個片段。

## 💻 Code

```python
class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        lastIndex = {}

        for i, c in enumerate(s):
            lastIndex[c] = i

        res = []
        size, end = 0, 0

        for i, c in enumerate(s):
            size += 1
            end = max(end, lastIndex[c])

            if i == end:
                res.append(size)
                size = 0

        return res
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

---

### 定義函式

```python
def partitionLabels(self, s: str) -> List[int]:
```

輸入：

```python
s
```

是一個只包含小寫英文字母的字串。

函式需要回傳：

```python
List[int]
```

也就是每個切割片段的長度。

例如：

```python
[9,7,8]
```

代表字串被切成三段，長度分別為：

```text
9、7、8
```

---

### 建立 Last Index Dictionary

```python
lastIndex = {}
```

建立一個 Dictionary，用來記錄：

```text
每個字母最後一次出現的位置
```

例如：

```python
s = "abaca"
```

每個字母最後出現的位置：

```python
lastIndex = {
    "a": 4,
    "b": 1,
    "c": 3
}
```

雖然 `a` 出現很多次，但 Dictionary 最後只保存最後一次的位置。

---

### 掃描字串

```python
for i, c in enumerate(s):
```

`enumerate(s)` 會同時提供：

```text
i：目前字母的 index
c：目前字母
```

例如：

```python
s = "abc"
```

會依序得到：

```text
i = 0, c = "a"
i = 1, c = "b"
i = 2, c = "c"
```

---

### 記錄字母最後出現的位置

```python
lastIndex[c] = i
```

每次看到字母 `c`，就把它的位置更新成目前的 `i`。

例如：

```python
s = "abaca"
```

第一次看到 `a`：

```python
lastIndex["a"] = 0
```

第二次看到 `a`：

```python
lastIndex["a"] = 2
```

第三次看到 `a`：

```python
lastIndex["a"] = 4
```

最後：

```python
lastIndex["a"] = 4
```

所以這個 Dictionary 保存的就是每個字母最後一次出現的位置。

---

### 為什麼一定要先知道最後位置？

假設目前片段中出現了字母：

```text
a
```

而 `a` 最後一次出現在 index `8`。

那麼目前片段就不能在 index `8` 之前結束。

否則同一個字母 `a` 會同時出現在：

```text
前一個片段
+
後一個片段
```

違反題目要求。

所以每遇到一個新字母，都必須知道：

```text
這個字母最後會出現在哪裡？
```

---

### 建立答案陣列

```python
res = []
```

`res` 用來保存每個片段的長度。

例如最後可能是：

```python
res = [9,7,8]
```

---

### 初始化 Size 和 End

```python
size, end = 0, 0
```

這一行等同於：

```python
size = 0
end = 0
```

---

### `size` 的用途

```python
size
```

表示：

> 目前正在建立的片段長度。

每處理一個字母：

```python
size += 1
```

當找到一個完整片段時，將 `size` 加入答案，再歸零。

---

### `end` 的用途

```python
end
```

表示：

> 目前這個片段最少必須延伸到的結尾位置。

它不是目前片段實際已經走到的位置。

目前走到的位置是：

```python
i
```

而 `end` 是根據片段中所有出現過的字母，算出的最遠最後位置。

---

### 第二次掃描字串

```python
for i, c in enumerate(s):
```

第一次掃描用來建立：

```python
lastIndex
```

第二次掃描才真正決定：

```text
每個片段應該在哪裡結束
```

每次取得：

```text
i：目前位置
c：目前字母
```

---

### 增加目前片段長度

```python
size += 1
```

每處理一個字母，目前片段長度就增加一。

例如目前正在處理：

```text
a b a
```

`size` 會依序變成：

```text
1 → 2 → 3
```

---

### 為什麼先增加 Size？

因為目前位置的字母也屬於目前片段。

例如片段從 index `0` 到 index `8`，包含：

```text
0,1,2,3,4,5,6,7,8
```

總共有：

```text
9
```

個字母。

所以每走到一個字母，都要立即：

```python
size += 1
```

---

### 更新目前片段的最遠結尾

```python
end = max(end, lastIndex[c])
```

這是整題最核心的一行。

目前字母：

```python
c
```

最後一次出現的位置是：

```python
lastIndex[c]
```

目前片段原本至少要走到：

```python
end
```

新的片段結尾應該是兩者較大值：

```python
max(end, lastIndex[c])
```

---

### 為什麼要使用 `max`？

假設目前：

```python
end = 8
```

現在遇到一個字母，它最後出現在 index `5`。

新的結尾仍然應該是：

```python
8
```

不能縮短成 `5`。

所以：

```python
end = max(8,5)
```

結果：

```python
end = 8
```

---

如果目前：

```python
end = 8
```

現在遇到新字母，而它最後出現在 index `15`。

那麼目前片段中已經包含了這個字母。

為了確保它不會出現在下一個片段，片段必須延伸到 index `15`。

所以：

```python
end = max(8,15)
```

結果：

```python
end = 15
```

---

### End 可能不斷向右延伸

例如目前片段從字母 `a` 開始：

```text
a 的最後位置是 8
```

一開始：

```python
end = 8
```

在走到 index `4` 時遇到字母 `x`：

```text
x 的最後位置是 12
```

所以：

```python
end = 12
```

之後在 index `10` 遇到字母 `y`：

```text
y 的最後位置是 15
```

所以：

```python
end = 15
```

這表示只要目前片段中出現的任何字母延伸得更遠，整個片段就必須跟著延伸。

---

### 判斷是否走到片段結尾

```python
if i == end:
```

當目前位置：

```python
i
```

等於目前片段要求的最遠位置：

```python
end
```

代表：

> 目前片段中出現過的所有字母，最後一次出現的位置都已經被包含。

因此可以在這裡安全切割。

---

### 為什麼不是 `i >= end`？

在掃描過程中：

```python
i
```

是逐步增加的。

而 `end` 一定至少等於目前位置或位於目前位置右側。

正常情況下，第一次能夠完成片段時一定是：

```python
i == end
```

所以直接使用相等判斷最清楚。

---

### 為什麼到達 End 就一定能切？

假設目前片段內出現過：

```text
a、b、c
```

它們最後出現的位置分別是：

```text
a → 8
b → 5
c → 7
```

因此：

```python
end = max(8,5,7)
```

得到：

```python
end = 8
```

當：

```python
i == 8
```

代表：

```text
a、b、c 的最後一次出現都已經被包含在目前片段中
```

後面的字串不會再出現 `a`、`b` 或 `c`。

所以可以安全切割。

---

### 將片段長度加入答案

```python
res.append(size)
```

當目前片段完成時，把其長度加入答案。

例如：

```python
size = 9
```

執行：

```python
res.append(9)
```

結果：

```python
res = [9]
```

---

### 將 Size 歸零

```python
size = 0
```

目前片段已經完成。

下一個字母將開始建立新的片段。

因此目前片段長度要重新從：

```python
0
```

開始計算。

---

### 為什麼不用重設 End？

這份程式沒有寫：

```python
end = 0
```

也沒有問題。

因為下一輪開始後：

```python
end = max(end, lastIndex[c])
```

新字母的最後出現位置一定不會在已完成片段的左邊。

假設上一段結束在：

```python
end = 8
```

下一個位置是：

```python
i = 9
```

新字母最後出現的位置至少是：

```python
9
```

所以：

```python
max(8, lastIndex[c])
```

自然會更新成新片段的結尾。

---

### 回傳答案

```python
return res
```

當整個字串處理完後，`res` 已經保存每個片段的長度。

例如：

```python
[9,7,8]
```

因此直接回傳。

## 🧠 核心觀念 | Key Insight

這題最重要的 Greedy 想法是：

> 一個片段必須延伸到片段內所有字母的最後出現位置。

我們每遇到一個字母，就查看它最後出現的位置：

```python
lastIndex[c]
```

並更新目前片段最遠需要到達的位置：

```python
end = max(end, lastIndex[c])
```

當目前 index：

```python
i
```

終於走到：

```python
end
```

就代表目前片段內所有字母都不會再出現在後面。

因此可以立刻切割。

---

### 為什麼這是 Greedy？

題目要求：

```text
切成盡可能多的片段
```

所以只要目前位置可以安全切割，就應該立刻切。

我們不需要為了等待更後面的字母而延長片段，因為那樣只會讓片段變大、片段數量變少。

因此：

```text
一到合法的最早切割點，就立刻切割
```

這就是 Greedy。

## 🧪 Example Walkthrough

使用：

```python
s = "ababcbacadefegdehijhklij"
```

---

### Step 1：建立 Last Index

每個字母最後出現的位置：

```python
lastIndex = {
    "a": 8,
    "b": 5,
    "c": 7,
    "d": 14,
    "e": 15,
    "f": 11,
    "g": 13,
    "h": 19,
    "i": 22,
    "j": 23,
    "k": 20,
    "l": 21
}
```

---

### 第一個片段

初始：

```python
size = 0
end = 0
```

---

### Index 0：`a`

```python
size = 1
```

`a` 最後出現在：

```python
8
```

所以：

```python
end = max(0,8)
```

得到：

```python
end = 8
```

目前：

```text
i = 0
end = 8
```

還不能切。

---

### Index 1：`b`

```python
size = 2
```

`b` 最後出現在：

```python
5
```

更新：

```python
end = max(8,5)
```

仍然是：

```python
8
```

---

### Index 2：`a`

```python
size = 3
```

`a` 最後位置是 `8`。

```python
end = max(8,8)
```

仍然是 `8`。

---

### Index 3：`b`

```python
size = 4
```

`end` 仍然是：

```python
8
```

---

### Index 4：`c`

```python
size = 5
```

`c` 最後位置是：

```python
7
```

更新：

```python
end = max(8,7)
```

仍然是：

```python
8
```

---

### Index 5：`b`

```python
size = 6
```

還沒到 `end`。

---

### Index 6：`a`

```python
size = 7
```

還沒到 `end`。

---

### Index 7：`c`

```python
size = 8
```

目前：

```text
i = 7
end = 8
```

還不能切。

---

### Index 8：`a`

```python
size = 9
```

目前：

```python
i = 8
end = 8
```

滿足：

```python
i == end
```

因此第一個片段完成：

```text
ababcbaca
```

加入：

```python
res = [9]
```

並重設：

```python
size = 0
```

---

### 第二個片段

從 index `9` 的：

```text
d
```

開始。

`d` 最後出現在 index `14`：

```python
end = 14
```

過程中遇到 `e`：

```text
e 最後出現在 index 15
```

所以結尾延伸成：

```python
end = 15
```

當走到 index `15` 時完成：

```text
defegde
```

長度：

```python
7
```

目前：

```python
res = [9,7]
```

---

### 第三個片段

剩下：

```text
hijhklij
```

最後走到 index `23` 時完成。

長度：

```python
8
```

最終：

```python
res = [9,7,8]
```

## 📊 第一個片段狀態變化

| Index | Character | Last Index | End | Size | 是否切割 |
| ----: | :-------: | ---------: | --: | ---: | :--: |
|     0 |     a     |          8 |   8 |    1 |   否  |
|     1 |     b     |          5 |   8 |    2 |   否  |
|     2 |     a     |          8 |   8 |    3 |   否  |
|     3 |     b     |          5 |   8 |    4 |   否  |
|     4 |     c     |          7 |   8 |    5 |   否  |
|     5 |     b     |          5 |   8 |    6 |   否  |
|     6 |     a     |          8 |   8 |    7 |   否  |
|     7 |     c     |          7 |   8 |    8 |   否  |
|     8 |     a     |          8 |   8 |    9 |   是  |

## 🤔 為什麼先掃描一次 Last Index？

如果不知道每個字母最後在哪裡出現，就無法判斷：

```text
目前是否可以安全切割
```

例如：

```python
s = "abac"
```

走到 index `1` 的 `b` 時，可能以為：

```text
ab
```

可以成為一個片段。

但 `a` 在 index `2` 又出現一次。

所以不能在 index `1` 切割。

先建立 `lastIndex` 後，我們知道：

```python
lastIndex["a"] = 2
```

因此第一個片段至少要走到 index `2`。

## 🤔 為什麼不能只看目前字母的最後位置？

因為目前片段可能包含多個字母。

例如：

```python
s = "abccaddbeffe"
```

假設第一個字母 `a` 的最後位置是：

```text
4
```

一開始可能認為片段到 index `4` 就能結束。

但是在 index `1` 遇到 `b`，而 `b` 最後出現在 index `7`。

所以片段必須延伸到 index `7`。

因此 `end` 必須保存：

```text
目前片段所有字母的最遠最後位置
```

使用：

```python
end = max(end, lastIndex[c])
```

## 🤔 為什麼不用 Set 記錄目前片段的字母？

也可以用 Set 記錄目前出現的字母，再不斷確認它們是否還會在後面出現。

但這樣每個位置可能需要重新檢查很多字母。

使用：

```python
end
```

只需要保存一個最遠 index。

每次更新都是：

```text
O(1)
```

更簡單也更有效率。

## 🤔 為什麼不能依照字母變化直接切割？

錯誤想法：

```text
字母變了就切割
```

例如：

```python
s = "abab"
```

如果依照字母改變切：

```text
a | b | a | b
```

同一個字母會出現在不同片段。

這不符合要求。

真正要看的是：

```text
字母最後一次出現的位置
```

而不是目前字母是否和上一個字母不同。

## 🤔 為什麼不需要排序？

字串本身的順序不能改變。

題目要求切割原始字串，而不是重新排列字母。

所以我們只能由左到右掃描。

這題不需要 Sorting，而是使用：

```text
Last Position + Greedy
```

## ⚠️ 常見錯誤 | Common Mistakes

### 錯誤一：只記錄第一次出現的位置

錯誤：

```python
if c not in lastIndex:
    lastIndex[c] = i
```

這會保存第一次出現的位置。

但這題需要的是：

```text
最後一次出現的位置
```

正確：

```python
lastIndex[c] = i
```

每次遇到相同字母都覆蓋舊位置。

---

### 錯誤二：直接使用目前字母的 Last Index

錯誤：

```python
end = lastIndex[c]
```

這可能讓 `end` 變小。

例如原本：

```python
end = 10
```

目前字母最後位置是：

```python
6
```

如果直接指定：

```python
end = 6
```

會錯誤縮短片段。

正確：

```python
end = max(end, lastIndex[c])
```

---

### 錯誤三：沒有在切割後重設 Size

如果漏掉：

```python
size = 0
```

下一個片段的長度會包含前一段的長度。

例如第一段長度 `9`，第二段長度 `7`，可能錯誤記成：

```text
9、16
```

---

### 錯誤四：在 `i < end` 時切割

只有在：

```python
i == end
```

才表示目前片段所有字母的最後位置都已包含。

如果：

```python
i < end
```

代表至少有某個字母還會在後面出現。

不能切。

---

### 錯誤五：使用字母出現次數決定切割

僅知道每個字母有幾次不夠。

我們還需要知道：

```text
最後一次出現的具體位置
```

因為切割是根據字串中的位置決定。

---

### 錯誤六：切割後手動跳過 Index

這題只需要正常逐字掃描。

當完成片段後，下一輪 `for` 迴圈自然會進入下一個字母。

不需要額外修改 `i`。

## 🧠 正確性說明 | Why This Works

假設目前片段從某個位置開始。

在掃描片段時，每遇到一個字母 `c`，就將：

```python
end
```

更新成：

```python
max(end, lastIndex[c])
```

因此 `end` 永遠代表：

> 目前片段內所有已看過字母的最後出現位置中，最遠的一個。

當：

```python
i < end
```

代表至少有一個目前片段中的字母還會在後面出現。

所以不能切割。

當：

```python
i == end
```

代表目前片段內所有字母的最後一次出現都已經包含在片段中。

後面的字串不會再出現這些字母，因此可以安全切割。

而我們在第一個合法位置就立即切割，所以能得到最多的片段數量。

## ⏱ Complexity Analysis

假設：

```text
n = 字串 s 的長度
```

---

### 建立 Last Index

```python
for i, c in enumerate(s):
```

需要掃描整個字串一次。

時間複雜度：

```text
O(n)
```

---

### 建立 Partitions

第二個迴圈再次掃描整個字串：

```python
for i, c in enumerate(s):
```

時間複雜度：

```text
O(n)
```

---

### 總時間複雜度

```text
O(n) + O(n) = O(n)
```

所以總時間複雜度是：

```text
O(n)
```

## 💾 Space Complexity

`lastIndex` 最多保存 26 個小寫英文字母：

```text
O(26)
```

常數可以忽略，因此可寫成：

```text
O(1)
```

如果字元種類不受限制，也可以寫成：

```text
O(k)
```

其中 `k` 是不同字元的數量。

答案陣列 `res` 不計入額外空間時，額外空間為：

```text
O(1)
```

## 🆚 763 vs 56 Merge Intervals

### LeetCode 56

需要先排序 intervals，然後合併重疊區間。

核心：

```text
Sorting + Interval Merge
```

---

### LeetCode 763

不需要排序。

每個字母可以想成一個 interval：

```text
[第一次出現位置, 最後一次出現位置]
```

如果這些字母的範圍互相重疊，就必須放在同一個片段。

核心：

```text
Last Occurrence + Greedy
```

---

### 共同點

兩題都在維護目前範圍的右邊界：

```python
end
```

只要新元素的範圍延伸得更遠，就更新右邊界。

## 🆚 763 vs 435 Non-overlapping Intervals

### LeetCode 435

目標是刪除最少 intervals，讓剩下區間不重疊。

通常按照：

```text
end
```

排序，再使用 Greedy。

---

### LeetCode 763

目標是把字串切成最多片段。

每個字母的出現範圍不能跨越不同片段。

兩題都使用 Greedy，但選擇方式不同：

```text
435：保留最早結束的 interval

763：到達目前最遠必要結尾時立即切割
```

## 🎯 Interview Takeaways

看到以下條件：

```text
同一個字母不能出現在不同片段
+
要求切成盡可能多段
```

可以想到：

```text
先找每個字母最後出現的位置
```

然後由左到右掃描：

```text
維護目前片段最遠結尾
```

當：

```python
i == end
```

就立刻切割。

---

### 面試時可以這樣說

```text
I first record the last occurrence of every character.

Then I scan the string again while maintaining the farthest last occurrence of all characters in the current partition.

Whenever the current index reaches that farthest position, every character in the current partition is fully contained within it, so I can safely close the partition.

By cutting at the earliest valid position, I maximize the number of partitions.
```

## 🗣 Interview English Version

```text
The key observation is that once a character is included in a partition, the partition must extend to that character's last occurrence.

I first build a map containing the last index of every character.

During the second pass, I maintain the farthest required ending index for the current partition.

When the current index equals that ending index, none of the characters in the partition appears later, so I record the partition size and start a new one.
```

## ✍️ What I Learned

### 1. 最後出現位置可以決定切割邊界

只要片段中出現某個字母，片段就必須包含該字母最後一次出現的位置。

---

### 2. End 代表目前片段最遠的必要位置

```python
end = max(end, lastIndex[c])
```

會將目前片段遇到的所有字母範圍包含進來。

---

### 3. 到達合法切割點就立刻切

題目要求最多片段，因此不需要繼續延長已經可以完成的片段。

---

### 4. Hash Map 和 Greedy 可以搭配

Hash Map 提供：

```text
每個字母的最後位置
```

Greedy 負責：

```text
在最早合法位置切割
```

---

### 5. 字串問題也可以視為 Interval 問題

每個字母都可以看成一個範圍：

```text
第一次出現位置 → 最後出現位置
```

互相重疊的範圍必須合併到同一個片段。

## 🏆 Cheat Sheet

### 建立最後位置

```python
lastIndex = {}

for i, c in enumerate(s):
    lastIndex[c] = i
```

---

### 初始化

```python
res = []
size, end = 0, 0
```

---

### 掃描字串

```python
for i, c in enumerate(s):
```

---

### 增加片段長度

```python
size += 1
```

---

### 更新最遠結尾

```python
end = max(end, lastIndex[c])
```

---

### 到達合法切割點

```python
if i == end:
```

---

### 保存片段長度

```python
res.append(size)
size = 0
```

---

### 回傳

```python
return res
```

## 🧭 解題流程圖

```text
第一次掃描字串
       |
       v
記錄每個字母最後出現位置
       |
       v
第二次由左到右掃描
       |
       v
size += 1
       |
       v
end = max(end, lastIndex[c])
       |
       v
目前 i 是否等於 end？
       |
   +---+---+
   |       |
  否       是
   |       |
繼續掃描   res.append(size)
           |
           v
        size = 0
           |
           v
       繼續下一段
```

## 🔑 Pattern Recognition

看到：

```text
每個元素只能屬於一個區段
+
元素可能重複出現
+
希望切成最多區段
```

先思考：

```text
每個元素最後一次出現在哪裡？
```

接著維護：

```text
目前區段的最遠必要邊界
```

完整 Pattern：

```text
Last Occurrence Map
+
Greedy Boundary
+
Linear Scan
```

## 🌟 One Sentence Summary

### English

> Record every character's last occurrence, extend the current partition to the farthest required index, and cut whenever the scan reaches that boundary.

### 中文

> 先記錄每個字母最後一次出現的位置，掃描時持續更新目前片段的最遠結尾，當 index 到達該結尾時就立即切割。

## ✅ Final Takeaway

這題最核心的兩行是：

```python
end = max(end, lastIndex[c])
```

以及：

```python
if i == end:
```

第一行表示：

```text
目前片段必須延伸到哪裡
```

第二行表示：

```text
目前是否已經到達最早可以安全切割的位置
```

最精簡記法：

```text
先找每個字母最後位置

一路擴張目前片段的 End

走到 End 就切
```
