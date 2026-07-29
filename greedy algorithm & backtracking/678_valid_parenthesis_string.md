# 📍 LeetCode 678 - Valid Parenthesis String

**Difficulty:** Medium

**Topics:**

* Greedy
* String
* Range Tracking
* Parentheses

## 📄 題目說明 | Problem Description

### 中文

給定一個字串：

```python
s
```

字串只包含三種字元：

```text
(
)
*
```

其中：

```text
(
```

代表左括號。

```text
)
```

代表右括號。

而：

```text
*
```

可以被當成三種可能：

```text
左括號 (
右括號 )
空字串
```

題目要求判斷：

> 是否存在一種 `*` 的替換方式，使整個字串成為合法括號字串。

---

### 合法括號字串的條件

合法括號字串需要滿足：

```text
1. 每一個右括號都必須有前面的左括號可以配對

2. 最後所有左括號都必須被配對完
```

例如：

```python
"()"
```

是合法的。

```python
"(())"
```

是合法的。

```python
"())"
```

不合法，因為最後一個右括號沒有左括號可以配對。

```python
"(()"
```

不合法，因為最後還剩下一個左括號沒有被關閉。

---

### English

You are given a string `s` containing only:

```text
(
)
*
```

The `*` character can represent:

```text
an opening parenthesis (
a closing parenthesis )
an empty string
```

Return `True` if the string can be transformed into a valid parenthesis string.

Otherwise, return `False`.

---

### Example 1

```python
s = "()"
```

輸出：

```python
True
```

因為括號可以直接配對。

---

### Example 2

```python
s = "(*)"
```

輸出：

```python
True
```

`*` 可以當成空字串：

```text
()
```

所以合法。

也可以理解成 `*` 有不同選擇，但至少存在一種方式使字串合法即可。

---

### Example 3

```python
s = "(*))"
```

輸出：

```python
True
```

可以把 `*` 當成左括號：

```text
(())
```

所以合法。

---

### Example 4

```python
s = "(*)))"
```

輸出：

```python
False
```

即使把 `*` 當成左括號，也只有：

```text
(())
```

可以配對前四個字元。

最後仍然多一個右括號，因此不合法。

## 💻 Code

```python
class Solution:
    def checkValidString(self, s: str) -> bool:
        leftMin, leftMax = 0, 0

        for c in s:
            if c == '(':
                leftMin, leftMax = leftMin + 1, leftMax + 1

            elif c == ')':
                leftMin, leftMax = leftMin - 1, leftMax - 1

            else:
                leftMin, leftMax = leftMin - 1, leftMax + 1

            if leftMax < 0:
                return False

            if leftMin < 0:
                leftMin = 0

        return leftMin == 0
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
def checkValidString(self, s: str) -> bool:
```

輸入：

```python
s
```

是一個包含：

```text
(
)
*
```

的字串。

函式最後回傳：

```python
True
```

或：

```python
False
```

代表是否存在某種 `*` 的解釋方式，使字串成為合法括號字串。

---

### 初始化 Left Minimum 和 Left Maximum

```python
leftMin, leftMax = 0, 0
```

這一行等同於：

```python
leftMin = 0
leftMax = 0
```

這兩個變數是整題最核心的概念。

它們不是單純記錄某一種情況下剩餘多少左括號。

而是記錄：

```text
處理到目前位置時，

未配對左括號數量可能存在的範圍
```

---

### `leftMin` 的意思

```python
leftMin
```

表示：

> 目前所有可能的 `*` 解釋方式中，最少可能剩下多少個未配對左括號。

也就是：

```text
minimum possible number of unmatched left parentheses
```

---

### `leftMax` 的意思

```python
leftMax
```

表示：

> 目前所有可能的 `*` 解釋方式中，最多可能剩下多少個未配對左括號。

也就是：

```text
maximum possible number of unmatched left parentheses
```

---

### 為什麼要記錄一個範圍？

因為：

```python
*
```

有三種可能。

例如：

```python
s = "(*)"
```

處理到 `*` 時，它可以是：

```text
(
)
空字串
```

所以剩餘左括號數量不是唯一值。

可能是：

```text
0
1
2
```

我們不需要真的列出所有可能性。

只需要記錄：

```text
最小可能值
最大可能值
```

也就是：

```python
[leftMin, leftMax]
```

---

### 一開始為什麼都是 0？

在還沒處理任何字元時：

```text
沒有任何未配對左括號
```

所以：

```python
leftMin = 0
leftMax = 0
```

範圍是：

```text
[0,0]
```

---

### 逐字掃描字串

```python
for c in s:
```

每次取得字串中的一個字元：

```python
c
```

`c` 可能是：

```text
(
)
*
```

---

### 遇到左括號

```python
if c == '(':
```

如果目前字元是：

```text
(
```

不論之前如何解釋 `*`，現在都一定多出一個尚未配對的左括號。

所以最少剩餘左括號數量和最多剩餘左括號數量都要加一。

---

### 更新左括號範圍

```python
leftMin, leftMax = leftMin + 1, leftMax + 1
```

等同於：

```python
leftMin += 1
leftMax += 1
```

例如原本範圍：

```text
[0,2]
```

遇到：

```text
(
```

之後變成：

```text
[1,3]
```

因為所有可能情況都多了一個左括號。

---

### Example

假設目前：

```python
leftMin = 0
leftMax = 2
```

代表未配對左括號可能是：

```text
0、1、2
```

遇到新的：

```text
(
```

每種情況都加一：

```text
1、2、3
```

所以新範圍：

```python
leftMin = 1
leftMax = 3
```

---

### 遇到右括號

```python
elif c == ')':
```

如果目前字元是：

```text
)
```

它需要和一個之前的左括號配對。

因此所有可能情況中的未配對左括號數量都要減一。

---

### 更新左括號範圍

```python
leftMin, leftMax = leftMin - 1, leftMax - 1
```

等同於：

```python
leftMin -= 1
leftMax -= 1
```

例如原本範圍：

```text
[1,3]
```

遇到右括號後：

```text
[0,2]
```

因為每種可能性都使用掉一個左括號。

---

### 為什麼右括號會讓兩者都減一？

因為 `)` 沒有選擇。

它一定是右括號。

所以無論是哪一種 `*` 的解釋方式，都必須嘗試配對一個左括號。

---

### Example

原本可能剩餘：

```text
1、2、3
```

遇到：

```text
)
```

之後變成：

```text
0、1、2
```

所以：

```python
leftMin = 0
leftMax = 2
```

---

### 遇到星號

```python
else:
```

因為字串只包含：

```text
(
)
*
```

前面已經排除：

```text
(
)
```

所以 `else` 代表：

```python
c == '*'
```

---

### 星號的三種解釋

```python
*
```

可以是：

```text
1. 右括號 )

2. 空字串

3. 左括號 (
```

---

### 更新最小可能左括號數

```python
leftMin - 1
```

為了讓剩餘左括號數量盡可能小，我們把 `*` 當成：

```text
右括號 )
```

它可以消耗一個左括號。

所以：

```python
leftMin -= 1
```

---

### 更新最大可能左括號數

```python
leftMax + 1
```

為了讓剩餘左括號數量盡可能大，我們把 `*` 當成：

```text
左括號 (
```

所以：

```python
leftMax += 1
```

---

### 完整更新

```python
leftMin, leftMax = leftMin - 1, leftMax + 1
```

例如原本範圍：

```text
[1,2]
```

遇到 `*`：

```text
最小值：把 * 當成 )，變成 0
最大值：把 * 當成 (，變成 3
```

所以新範圍：

```text
[0,3]
```

---

### 那把 `*` 當空字串呢？

空字串會讓未配對左括號數量不變。

例如原本可能是：

```text
1、2
```

三種選擇後可能得到：

```text
把 * 當 )：0、1
把 * 當空字串：1、2
把 * 當 (：2、3
```

合併後可能範圍是：

```text
0、1、2、3
```

所以只需要記錄：

```text
最小值 0
最大值 3
```

空字串的情況自然包含在範圍中，不需要另外處理。

---

### 判斷最大可能左括號數是否小於 0

```python
if leftMax < 0:
```

這代表：

> 即使我們盡可能把之前的 `*` 都當成左括號，仍然沒有足夠的左括號配對目前的右括號。

這時字串一定不合法。

---

### 為什麼只看 `leftMax`？

`leftMax` 是最樂觀的情況。

它代表：

```text
目前最多能有多少左括號
```

如果連最多的情況都小於 `0`，代表右括號數量已經太多。

沒有任何 `*` 的替換方式可以拯救。

---

### Example

```python
s = "())"
```

開始：

```text
leftMin = 0
leftMax = 0
```

遇到 `(`：

```text
[1,1]
```

遇到第一個 `)`：

```text
[0,0]
```

遇到第二個 `)`：

```text
[-1,-1]
```

此時：

```python
leftMax = -1
```

表示即使最樂觀情況也沒有左括號可以配對。

因此：

```python
return False
```

---

### 立即回傳 False

```python
return False
```

當：

```python
leftMax < 0
```

後面即使還有很多 `*` 或 `(`，也不能修復之前已經出現的無效右括號。

合法括號要求：

```text
任何 prefix 中，右括號都不能超過可用左括號
```

所以可以立即結束。

---

### 為什麼後面的左括號不能救前面的右括號？

例如：

```python
")("
```

雖然總共有一個左括號和一個右括號，但順序錯誤。

第一個字元 `)` 出現時，前面沒有左括號可以和它配對。

後面的 `(` 不能回頭配對前面的 `)`。

所以只要某個 prefix 已經不合法，整個字串就不合法。

---

### 將 `leftMin` 修正為 0

```python
if leftMin < 0:
    leftMin = 0
```

`leftMin` 代表：

```text
最少可能剩餘多少左括號
```

但實際上未配對左括號數量不可能是負數。

所以當它小於 `0` 時，要修正成：

```python
0
```

---

### 為什麼 `leftMin` 可能變成負數？

例如：

```python
s = "*"
```

開始：

```text
leftMin = 0
leftMax = 0
```

遇到 `*`：

```python
leftMin = -1
leftMax = 1
```

`leftMin = -1` 是把 `*` 當成右括號的結果。

但前面根本沒有左括號可以配對。

這個選擇是無效的。

不過 `*` 還可以當：

```text
空字串
```

所以最少合法剩餘左括號數量應該是：

```text
0
```

因此修正：

```python
leftMin = 0
```

---

### 為什麼不能直接回傳 False？

當：

```python
leftMin < 0
```

只代表：

```text
某些解釋方式不合法
```

但不代表所有解釋方式都不合法。

例如：

```python
s = "*"
```

如果把 `*` 當成右括號，確實不合法。

但是把它當成空字串，就合法。

所以不能因為 `leftMin < 0` 就回傳 False。

只需要把不可能的負數情況排除：

```python
leftMin = 0
```

---

### `leftMax < 0` 和 `leftMin < 0` 的差別

```python
leftMax < 0
```

代表：

```text
所有可能性都失敗
```

所以直接：

```python
return False
```

---

```python
leftMin < 0
```

代表：

```text
最小的某些可能性失敗，但其他可能性仍然可能成功
```

所以只需要：

```python
leftMin = 0
```

---

### 最後檢查最小可能左括號數

```python
return leftMin == 0
```

掃描完整個字串後，需要確認：

> 是否至少存在一種解釋方式，使未配對左括號數量為 0。

`leftMin` 是最少可能剩餘的左括號數量。

如果：

```python
leftMin == 0
```

表示存在某種替換方式，可以將所有左括號完整配對。

所以回傳：

```python
True
```

---

### 如果 `leftMin > 0`

代表即使我們盡量把 `*` 當成右括號，也仍然剩下左括號沒有被配對。

例如：

```python
s = "(("
```

處理後：

```text
leftMin = 2
leftMax = 2
```

沒有任何方式可以關閉這兩個左括號。

因此：

```python
leftMin == 0
```

不成立。

回傳：

```python
False
```

---

### 為什麼最後不檢查 `leftMax == 0`？

因為 `leftMax` 是最多可能剩餘的左括號。

即使它大於 `0`，仍然可能存在另一種 `*` 的解釋方式，使剩餘左括號為 `0`。

例如：

```python
s = "*"
```

處理後修正範圍：

```text
[0,1]
```

`leftMax = 1`，表示把 `*` 當成 `(` 時會剩一個左括號。

但 `leftMin = 0`，表示把 `*` 當空字串時可以合法。

所以最後要檢查：

```python
leftMin == 0
```

而不是：

```python
leftMax == 0
```

## 🧠 核心觀念 | Key Insight

這題不能只維護一個：

```text
leftCount
```

因為每個 `*` 有三種解釋方式。

如果對每個 `*` 都分別嘗試：

```text
(
)
空字串
```

會產生大量分支。

這份解法不追蹤每一個具體狀態，而是維護一個可能範圍：

```text
[leftMin, leftMax]
```

其中：

```text
leftMin = 最少可能的未配對左括號數

leftMax = 最多可能的未配對左括號數
```

每個字元只需要更新這個範圍。

---

### 狀態更新規則

遇到：

```text
(
```

所有可能性都多一個左括號：

```text
leftMin + 1
leftMax + 1
```

---

遇到：

```text
)
```

所有可能性都少一個左括號：

```text
leftMin - 1
leftMax - 1
```

---

遇到：

```text
*
```

最小情況把它當成 `)`：

```text
leftMin - 1
```

最大情況把它當成 `(`：

```text
leftMax + 1
```

---

### 判斷失敗

如果：

```python
leftMax < 0
```

代表右括號太多，所有可能性都失敗。

---

### 判斷成功

最後如果：

```python
leftMin == 0
```

代表至少存在一種方式可以完成所有配對。

## 🧪 Example Walkthrough

使用：

```python
s = "(*))"
```

---

### 初始狀態

```python
leftMin = 0
leftMax = 0
```

可能的未配對左括號數量：

```text
[0,0]
```

---

### 第一個字元：`(`

遇到：

```text
(
```

更新：

```python
leftMin = 0 + 1
leftMax = 0 + 1
```

得到：

```text
[1,1]
```

代表目前一定剩下一個左括號。

---

### 第二個字元：`*`

遇到：

```text
*
```

更新：

```python
leftMin = 1 - 1
leftMax = 1 + 1
```

得到：

```text
[0,2]
```

可能情況：

```text
把 * 當成 )：剩 0 個左括號

把 * 當空字串：剩 1 個左括號

把 * 當成 (：剩 2 個左括號
```

---

### 第三個字元：`)`

更新：

```python
leftMin = 0 - 1
leftMax = 2 - 1
```

暫時得到：

```text
[-1,1]
```

`leftMax` 沒有小於 `0`，所以仍然有合法可能性。

但：

```python
leftMin < 0
```

所以修正：

```python
leftMin = 0
```

新範圍：

```text
[0,1]
```

---

### 第四個字元：`)`

更新：

```python
leftMin = 0 - 1
leftMax = 1 - 1
```

得到：

```text
[-1,0]
```

`leftMax = 0`，沒有小於 `0`。

修正：

```python
leftMin = 0
```

最後範圍：

```text
[0,0]
```

---

### 最後判斷

```python
leftMin == 0
```

成立。

因此回傳：

```python
True
```

實際替換方式是把 `*` 當成：

```text
(
```

字串變成：

```text
(())
```

## 📊 狀態變化表

使用：

```python
s = "(*))"
```

| Character | LeftMin 更新 | LeftMax 更新 |  修正後範圍  |
| :-------: | :--------: | :--------: | :-----: |
|     初始    |      0     |      0     | `[0,0]` |
|    `(`    |   `0 + 1`  |   `0 + 1`  | `[1,1]` |
|    `*`    |   `1 - 1`  |   `1 + 1`  | `[0,2]` |
|    `)`    |   `0 - 1`  |   `2 - 1`  | `[0,1]` |
|    `)`    |   `0 - 1`  |   `1 - 1`  | `[0,0]` |

最終：

```python
leftMin == 0
```

所以答案是：

```python
True
```

## 🧪 Failure Walkthrough

使用：

```python
s = "(*)))"
```

---

### 處理前四個字元

前四個字元：

```text
(*))
```

處理完後範圍是：

```text
[0,0]
```

---

### 最後一個字元：`)`

更新：

```python
leftMin = 0 - 1
leftMax = 0 - 1
```

得到：

```text
[-1,-1]
```

此時：

```python
leftMax < 0
```

成立。

代表即使前面的 `*` 盡可能當成左括號，也沒有足夠左括號配對最後的右括號。

所以立即：

```python
return False
```

## 🤔 為什麼不能用普通 Left Count？

假設只使用：

```python
leftCount
```

遇到 `*` 時就不知道應該：

```text
+1
-1
還是不變
```

例如：

```python
s = "(*))"
```

如果一開始把 `*` 當空字串，可能會以為失敗。

但其實把它當成左括號可以成功。

因此不能在看到 `*` 時立刻固定選擇一種角色。

要保留可能範圍：

```python
[leftMin, leftMax]
```

## 🤔 為什麼這是 Greedy？

這題的 Greedy 不是真的在每個 `*` 當下選定它是什麼。

而是同時維護兩個極端：

```text
最少可能剩餘左括號

最多可能剩餘左括號
```

對 `leftMin` 而言：

```text
盡可能把 * 當成右括號
```

對 `leftMax` 而言：

```text
盡可能把 * 當成左括號
```

只要這個可能範圍中仍然包含合法狀態，就繼續掃描。

最後只需要確認：

```text
0 是否仍在可能範圍內
```

## 🤔 為什麼範圍中間的值都可以成立？

假設目前：

```text
leftMin = 1
leftMax = 4
```

這表示未配對左括號可能是：

```text
1、2、3、4
```

不是只有 `1` 和 `4` 兩個值。

因為每個 `*` 可以造成：

```text
-1、0、+1
```

這些選擇會形成連續的可能值範圍。

所以只需要保存上下界，不需要保存所有數字。

## 🤔 為什麼 `leftMin` 不能小於 0？

未配對左括號數量的實際意義是：

```text
目前還有多少個左括號等待配對
```

它不可能是負數。

負數表示某個假設中使用了過多的右括號。

這種假設應該被捨棄。

因此：

```python
if leftMin < 0:
    leftMin = 0
```

相當於移除不可能的負數狀態。

## 🤔 為什麼掃描中只檢查 `leftMax < 0`？

合法括號有一個重要條件：

```text
在任何 prefix 中，右括號都不能超過可用左括號
```

`leftMax` 代表最樂觀情況下的左括號數量。

如果：

```python
leftMax < 0
```

表示這個 prefix 在所有情況下都已經有太多右括號。

所以一定失敗。

而 `leftMin < 0` 只表示某些情況失敗，還有其他情況可能成功。

## 🤔 為什麼最後只檢查 `leftMin == 0`？

處理完整個字串後：

```text
不能剩下任何未配對左括號
```

如果最少可能剩餘數量是：

```text
0
```

就表示至少有一種 `*` 替換方式可以完全配對。

如果：

```python
leftMin > 0
```

表示所有可能性至少都剩下一個左括號。

因此一定不合法。

## ⚠️ 常見錯誤 | Common Mistakes

### 錯誤一：遇到 `*` 固定當成空字串

錯誤：

```python
if c == '*':
    continue
```

例如：

```python
s = "(*))"
```

必須把 `*` 當成左括號才能成功。

固定當空字串會得到錯誤答案。

---

### 錯誤二：遇到 `*` 固定當成左括號

例如：

```python
s = "(*)"
```

如果固定把 `*` 當左括號：

```text
(()
```

會不合法。

但其實把它當空字串即可成功。

---

### 錯誤三：遇到 `*` 固定當成右括號

例如：

```python
s = "*"
```

固定當右括號會不合法。

但把它當空字串即可。

---

### 錯誤四：`leftMin < 0` 時直接回傳 False

錯誤：

```python
if leftMin < 0:
    return False
```

例如：

```python
s = "*"
```

處理後 `leftMin` 暫時為 `-1`。

但字串其實可以把 `*` 當成空字串。

所以正確是：

```python
leftMin = 0
```

---

### 錯誤五：忘記檢查 `leftMax < 0`

如果右括號過多，就必須立即失敗。

例如：

```python
s = ")("
```

如果沒有檢查 `leftMax < 0`，可能錯誤地繼續處理後面的左括號。

但前面的右括號已經無法配對。

---

### 錯誤六：最後檢查 `leftMax == 0`

錯誤：

```python
return leftMax == 0
```

例如：

```python
s = "*"
```

最後範圍：

```text
[0,1]
```

`leftMax` 是 `1`，但字串其實合法。

正確：

```python
return leftMin == 0
```

---

### 錯誤七：只檢查左右括號總數

例如：

```python
s = ")("
```

左右括號總數相同。

但順序不合法。

所以不能只比較總數。

必須保證每個 prefix 都有足夠左括號。

---

### 錯誤八：使用 Stack 但不處理 `*` 的多重角色

普通括號題可以用 Stack。

但這題的 `*` 有三種可能，單純 Push 或 Pop 無法完整表示所有狀態。

可以使用兩個 Stack 的其他解法，但這份程式使用範圍 Greedy 更簡潔。

## 🧠 正確性說明 | Why This Works

在掃描每個 prefix 後：

```python
leftMin
```

表示最少可能的未配對左括號數量。

```python
leftMax
```

表示最多可能的未配對左括號數量。

每個字元按照它對左括號數量的影響更新範圍：

```text
(  → [+1,+1]

)  → [-1,-1]

*  → [-1,+1]
```

如果：

```python
leftMax < 0
```

表示連最多左括號的情況都無法配對目前的右括號。

因此不存在合法解。

當：

```python
leftMin < 0
```

只需要將它修正成 `0`，因為負數狀態不可能，但其他非負狀態仍然有效。

最後：

```python
leftMin == 0
```

表示可能範圍中包含 `0`，因此存在一種 `*` 的替換方式，使所有括號完整配對。

## 🆚 暴力法 vs Greedy

### 暴力法

每遇到一個 `*`，分成三種情況：

```text
(
)
空字串
```

如果有 `k` 個星號，最多可能有：

```text
3^k
```

種替換方式。

時間複雜度會非常高。

---

### Greedy Range

不列出每一種替換方式。

只記錄：

```text
最小可能左括號數

最大可能左括號數
```

每個字元只處理一次。

時間複雜度：

```text
O(n)
```

## 🆚 678 vs 20 Valid Parentheses

### LeetCode 20

字串只包含一般括號：

```text
()
[]
{}
```

每個字元的角色固定。

通常使用：

```text
Stack
```

---

### LeetCode 678

包含：

```text
*
```

而 `*` 有三種角色。

需要同時處理多種可能性。

這份解法使用：

```text
Greedy Range
```

---

### 共同點

兩題都必須確保：

```text
每個右括號都有前面的左括號配對
```

並且最後不能剩下左括號。

## 🆚 678 vs 921 Minimum Add to Make Parentheses Valid

### LeetCode 921

沒有 `*`。

題目要求：

```text
最少加入多少括號才能合法
```

可以直接計算未配對括號數量。

---

### LeetCode 678

題目不是加入括號，而是決定 `*` 的角色。

所以要維護：

```text
可能的左括號數量範圍
```

## ⏱ Complexity Analysis

假設：

```text
n = 字串 s 的長度
```

---

### 掃描字串

```python
for c in s:
```

每個字元只處理一次。

每次只做常數次比較和加減。

時間複雜度：

```text
O(n)
```

---

### 總時間複雜度

```text
O(n)
```

## 💾 Space Complexity

只使用兩個整數：

```python
leftMin
leftMax
```

沒有隨輸入大小增加的資料結構。

所以額外空間複雜度：

```text
O(1)
```

## 🎯 Interview Takeaways

看到：

```text
括號
+
萬用字元
+
萬用字元可以有多種角色
```

可以思考：

```text
能不能追蹤狀態範圍，而不是列舉所有狀態？
```

本題維護：

```text
最小可能未配對左括號數

最大可能未配對左括號數
```

---

### 面試時可以這樣說

```text
Instead of deciding what each star represents immediately, I maintain a range of possible unmatched opening-parenthesis counts.

leftMin is the minimum possible count, and leftMax is the maximum possible count.

An opening parenthesis increases both values, while a closing parenthesis decreases both.

For a star, the minimum decreases because it may act as a closing parenthesis, and the maximum increases because it may act as an opening parenthesis.

If leftMax becomes negative, every possible interpretation has too many closing parentheses.

I clamp leftMin to zero because the number of unmatched opening parentheses cannot be negative.

At the end, the string is valid if leftMin is zero.
```

## 🗣 Interview English Version

```text
The key is to track a range rather than a single number of unmatched opening parentheses.

leftMin represents the minimum possible number of unmatched opening parentheses, while leftMax represents the maximum.

For an opening parenthesis, both increase by one.

For a closing parenthesis, both decrease by one.

For a star, leftMin decreases by one because the star may be a closing parenthesis, and leftMax increases by one because it may be an opening parenthesis.

If leftMax becomes negative, no interpretation can make the current prefix valid.

I clamp leftMin to zero because negative unmatched opening parentheses are impossible.

Finally, leftMin must be zero for a valid interpretation to exist.
```

## ✍️ What I Learned

### 1. 不一定要立即決定 `*` 的角色

可以延後決定，並維護所有可能狀態的上下界。

---

### 2. 一個範圍可以代表大量分支

```python
[leftMin, leftMax]
```

取代了暴力法中大量的 `*` 替換組合。

---

### 3. `leftMax` 用來判斷前綴是否已經必敗

如果連最樂觀情況都沒有足夠左括號：

```python
leftMax < 0
```

就一定不合法。

---

### 4. `leftMin` 用來判斷最後能否完全配對

最後：

```python
leftMin == 0
```

代表至少存在一種方式不剩任何左括號。

---

### 5. 負的 `leftMin` 不代表整體失敗

它只代表某些選擇不合法。

將其修正為：

```python
0
```

即可保留其他合法可能性。

## 🏆 Cheat Sheet

### 初始化可能範圍

```python
leftMin, leftMax = 0, 0
```

---

### 遇到左括號

```python
leftMin += 1
leftMax += 1
```

---

### 遇到右括號

```python
leftMin -= 1
leftMax -= 1
```

---

### 遇到星號

```python
leftMin -= 1
leftMax += 1
```

---

### 所有可能性都失敗

```python
if leftMax < 0:
    return False
```

---

### 排除不可能的負數狀態

```python
if leftMin < 0:
    leftMin = 0
```

---

### 最後判斷

```python
return leftMin == 0
```

## 🧭 解題流程圖

```text
初始化 leftMin = 0, leftMax = 0
                |
                v
           逐字掃描 s
                |
                v
        目前字元是哪一種？
        /          |          \
      (            )           *
      |            |           |
  Min + 1      Min - 1     Min - 1
  Max + 1      Max - 1     Max + 1
        \          |          /
                |
                v
          leftMax < 0？
             /      \
           是        否
           |         |
      return False   v
               leftMin < 0？
                 /       \
               是         否
               |          |
          leftMin = 0    繼續
                 \       /
                    |
                    v
              掃描結束
                    |
                    v
            leftMin == 0？
               /       \
             是         否
             |          |
           True       False
```

## 🔑 Pattern Recognition

看到：

```text
萬用字元有多種解釋
+
只需要判斷是否存在一種合法方式
+
狀態可以表示成連續範圍
```

可以想到：

```text
Range Tracking
+
Greedy
```

完整 Pattern：

```text
Minimum Possible State
+
Maximum Possible State
+
Linear Scan
```

## 🌟 One Sentence Summary

### English

> Track the minimum and maximum possible numbers of unmatched opening parentheses, reject the string if even the maximum becomes negative, and ensure the minimum can be zero at the end.

### 中文

> 維護未配對左括號數量的最小值與最大值，如果最大值小於零代表所有可能性都失敗，最後最小值為零則存在合法解。

## ✅ Final Takeaway

這題最核心的不是決定每一個 `*` 到底是什麼，而是維護：

```text
目前可能剩餘左括號數量的範圍
```

最重要的三個判斷：

```python
leftMin, leftMax = leftMin - 1, leftMax + 1
```

表示 `*` 可以讓可能範圍向兩側擴張。

```python
if leftMax < 0:
    return False
```

表示連最樂觀情況都無法配對右括號。

```python
return leftMin == 0
```

表示最後至少存在一種方式可以完全配對。

最精簡記法：

```text
( 讓範圍一起 +1

) 讓範圍一起 -1

* 讓 Min -1、Max +1

Max < 0 直接失敗

Min 最低只能是 0

最後 Min 必須等於 0
```
