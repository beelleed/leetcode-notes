# 📍 LeetCode 846 - Hand of Straights

**Difficulty:** Medium

**Topics:**

* Greedy
* Hash Map
* Heap / Priority Queue
* Counting
* Sorting

---

# 📄 題目說明 | Problem Description

## 中文

給你一組牌：

```python
hand
```

以及一個整數：

```python
groupSize
```

你需要判斷能不能把所有牌分成若干組。

每一組都必須：

```text
剛好有 groupSize 張牌
```

並且牌的數字必須：

```text
連續遞增
```

例如：

```python
hand = [1,2,3,6,2,3,4,7,8]
groupSize = 3
```

可以分成：

```text
[1,2,3]
[2,3,4]
[6,7,8]
```

所以回傳：

```python
True
```

---

## English

You are given an integer array `hand`, where each value represents a card.

You are also given an integer `groupSize`.

Return `True` if the cards can be rearranged into groups of size `groupSize`, where every group contains consecutive values.

Otherwise, return `False`.

---

# 📚 Example 1

```python
hand = [1,2,3,6,2,3,4,7,8]
groupSize = 3
```

Output:

```python
True
```

可以分成：

```text
[1,2,3]
[2,3,4]
[6,7,8]
```

每組都有三張牌，並且數字連續。

---

# 📚 Example 2

```python
hand = [1,2,3,4,5]
groupSize = 4
```

Output:

```python
False
```

總共有五張牌。

無法完整分成每組四張。

---

# 📚 Example 3

```python
hand = [1,2,3,4]
groupSize = 2
```

Output:

```python
True
```

可以分成：

```text
[1,2]
[3,4]
```

---

# 💻 Corrected Code

```python
import heapq

class Solution:
    def isNStraightHand(
        self,
        hand: List[int],
        groupSize: int
    ) -> bool:

        if len(hand) % groupSize:
            return False

        count = {}

        for n in hand:
            count[n] = 1 + count.get(n, 0)

        minH = list(count.keys())

        heapq.heapify(minH)

        while minH:

            first = minH[0]

            for i in range(first, first + groupSize):

                if i not in count:
                    return False

                count[i] -= 1

                if count[i] == 0:

                    if i != minH[0]:
                        return False

                    heapq.heappop(minH)

        return True
```

---

# 🧠 核心觀念 | Key Insight

這題最重要的 Greedy 想法是：

> 每次都從目前最小的牌開始組一組連續牌。

例如目前剩下：

```python
[1,2,3,4,6,7,8]
```

如果：

```python
groupSize = 3
```

最小的牌是：

```python
1
```

那它一定要放在：

```text
[1,2,3]
```

不能放在：

```text
[0,1,2]
```

因為 `0` 不存在。

也不能跳著放。

所以只要目前最小的牌還存在，就必須從它開始建立一組：

```text
first
first + 1
first + 2
...
first + groupSize - 1
```

---

# 🧠 為什麼一定從最小牌開始？

假設剩下：

```python
[1,2,3,4]
```

並且：

```python
groupSize = 3
```

最小的牌：

```python
1
```

它不可能出現在：

```text
[2,3,4]
```

因為這組沒有 `1`。

它唯一合理的位置，就是某一組的起點。

所以必須先嘗試：

```text
[1,2,3]
```

如果 `2` 或 `3` 不存在，就不可能完成分組。

這就是 Greedy：

```text
先處理目前最小、最沒有彈性的牌。
```

---

# 🧠 為什麼需要 Count Dictionary？

`hand` 中可能有重複牌。

例如：

```python
hand = [1,2,2,3,3,4]
```

每個數字的出現次數：

```python
1 → 1 次
2 → 2 次
3 → 2 次
4 → 1 次
```

所以需要：

```python
count
```

記錄：

```text
牌的數字 → 剩餘張數
```

得到：

```python
count = {
    1: 1,
    2: 2,
    3: 2,
    4: 1
}
```

---

# 🧠 為什麼需要 Min Heap？

我們每次都需要知道：

```text
目前剩餘牌中，最小的牌是什麼？
```

可以使用：

```python
minH[0]
```

快速取得最小值。

Heap 裡面只放：

```text
不同的牌面數字
```

例如：

```python
hand = [1,1,2,2,3]
```

Heap 不需要放：

```python
[1,1,2,2,3]
```

只需要放：

```python
[1,2,3]
```

實際張數由：

```python
count
```

負責記錄。

---

# 🧠 Hash Map 和 Heap 分別負責什麼？

## Hash Map

```python
count
```

負責：

```text
每張牌還剩幾張
```

例如：

```python
count[3] = 2
```

代表數字 `3` 還剩兩張。

---

## Min Heap

```python
minH
```

負責：

```text
目前還有剩餘數量的最小牌是什麼
```

Heap Top：

```python
minH[0]
```

就是目前最小的牌。

---

# 🧾 程式碼逐行解釋 | Line-by-line Explanation

---

## 匯入 Heap

```python
import heapq
```

Python 使用：

```python
heapq
```

實作 Min Heap。

常見操作：

```python
heapq.heapify(list)
```

把 List 轉換成 Heap。

```python
heapq.heappop(heap)
```

移除並回傳 Heap 中最小值。

```python
heap[0]
```

查看最小值，但不移除。

---

## 建立 Solution Class

```python
class Solution:
```

LeetCode 固定要求將解法寫在：

```python
class Solution
```

裡面。

---

## 定義函式

```python
def isNStraightHand(
    self,
    hand: List[int],
    groupSize: int
) -> bool:
```

輸入：

```python
hand
```

代表所有牌。

輸入：

```python
groupSize
```

代表每組要有幾張牌。

回傳：

```python
True
```

或：

```python
False
```

---

# 第一個判斷：牌數能不能整除

```python
if len(hand) % groupSize:
    return False
```

假設：

```python
len(hand) = 9
groupSize = 3
```

計算：

```python
9 % 3 = 0
```

可以分成：

```text
3 組
```

---

如果：

```python
len(hand) = 5
groupSize = 4
```

計算：

```python
5 % 4 = 1
```

代表無法完整分組。

所以直接：

```python
return False
```

---

## 為什麼條件沒有寫 `!= 0`？

Python 中：

```python
0
```

會被視為：

```python
False
```

其他非零整數會被視為：

```python
True
```

所以：

```python
if len(hand) % groupSize:
```

等同於：

```python
if len(hand) % groupSize != 0:
```

---

## 為什麼這個檢查一定要先做？

如果總牌數不是 `groupSize` 的倍數，無論牌面數字如何，都不可能完整分組。

例如：

```python
hand = [1,2,3,4,5]
groupSize = 3
```

總共五張牌。

不可能全部分成每組三張。

因此可以提早結束，避免後面的運算。

---

# 建立 Count Dictionary

```python
count = {}
```

建立空字典，用來記錄每個數字出現幾次。

---

## 統計每張牌

```python
for n in hand:
```

逐一走訪所有牌。

例如：

```python
hand = [1,2,2,3]
```

迴圈依序得到：

```text
n = 1
n = 2
n = 2
n = 3
```

---

## 更新出現次數

```python
count[n] = 1 + count.get(n, 0)
```

`count.get(n, 0)` 表示：

```text
如果 n 已經在 count 中，取得目前次數。
如果 n 不在 count 中，回傳 0。
```

---

### 第一次看到某張牌

例如第一次看到：

```python
n = 2
```

此時：

```python
count.get(2, 0)
```

得到：

```python
0
```

所以：

```python
count[2] = 1 + 0
```

結果：

```python
count[2] = 1
```

---

### 再次看到相同牌

第二次看到：

```python
n = 2
```

此時：

```python
count.get(2, 0)
```

得到：

```python
1
```

所以：

```python
count[2] = 1 + 1
```

結果：

```python
count[2] = 2
```

---

## 建立完成後

假設：

```python
hand = [1,2,3,6,2,3,4,7,8]
```

得到：

```python
count = {
    1: 1,
    2: 2,
    3: 2,
    4: 1,
    6: 1,
    7: 1,
    8: 1
}
```

---

# 將所有不同牌面放入 Heap

```python
minH = list(count.keys())
```

`count.keys()` 取得所有不同的牌面。

例如：

```python
count = {
    1: 1,
    2: 2,
    3: 2,
    4: 1
}
```

`count.keys()`：

```python
dict_keys([1,2,3,4])
```

轉成 List：

```python
minH = [1,2,3,4]
```

---

## 為什麼只放 Keys？

Heap 的目的只是找：

```text
目前最小的牌面
```

不需要重複放相同數字。

例如牌：

```python
[1,1,1,2,2,3]
```

Heap 只需要：

```python
[1,2,3]
```

數量由：

```python
count
```

管理。

---

# 將 List 轉成 Heap

```python
heapq.heapify(minH)
```

這行把：

```python
minH
```

轉成合法的 Min Heap。

完成後：

```python
minH[0]
```

一定是最小值。

---

## 為什麼不能只使用 List？

一般 List 的第一個元素不一定是最小值。

例如：

```python
minH = [6,1,4,2]
```

`minH[0]` 是：

```python
6
```

但最小值其實是：

```python
1
```

經過：

```python
heapq.heapify(minH)
```

Heap Top 才會變成最小值。

---

# 只要 Heap 還有牌就繼續

```python
while minH:
```

只要 Heap 不為空，代表仍然有牌尚未使用完。

所以必須繼續建立新的連續群組。

---

## 什麼時候 Heap 會空？

當某張牌的數量變成：

```python
0
```

而且它剛好是 Heap Top 時，就會：

```python
heapq.heappop(minH)
```

當所有牌都被移除後：

```python
minH = []
```

代表所有牌都成功分組。

最後回傳：

```python
True
```

---

# 找目前最小的牌

```python
first = minH[0]
```

`minH[0]` 是目前尚未使用完的最小牌。

例如：

```python
minH = [1,2,3,6,7,8]
```

則：

```python
first = 1
```

接下來必須建立：

```text
1,2,3
```

假設：

```python
groupSize = 3
```

---

## 為什麼不直接 Pop First？

因為數字 `first` 可能有多張。

例如：

```python
count[1] = 2
```

表示 `1` 還需要出現在兩個不同群組。

所以不能一看到 `1` 就直接從 Heap 移除。

必須等：

```python
count[1] == 0
```

才可以 Pop。

---

# 建立一組連續數字

```python
for i in range(first, first + groupSize):
```

假設：

```python
first = 2
groupSize = 3
```

則：

```python
range(2, 5)
```

產生：

```text
2
3
4
```

正好是一組：

```text
[2,3,4]
```

---

## 為什麼終點是 `first + groupSize`？

Python 的 `range` 不包含右端點。

所以：

```python
range(first, first + groupSize)
```

實際最後一個值是：

```python
first + groupSize - 1
```

例如：

```python
range(2, 5)
```

得到：

```python
2,3,4
```

總共有三個數。

---

# 判斷連續牌是否存在

```python
if i not in count:
    return False
```

假設目前想建立：

```text
[3,4,5]
```

但 `5` 從來沒有出現在 hand 中。

此時：

```python
5 not in count
```

成立。

因此無法組成連續群組。

直接：

```python
return False
```

---

## 為什麼只檢查 `i not in count` 還不夠？

因為某個數字可能存在於 Dictionary，但數量已經變成：

```python
0
```

不過在這個演算法中，只要數量歸零，它應該會在正確時機從 Heap 移除。

更清楚的寫法也可以寫：

```python
if i not in count or count[i] == 0:
    return False
```

但原本這個 Heap 邏輯會透過後面的順序檢查維護一致性。

---

# 使用一張牌

```python
count[i] -= 1
```

每建立一組，就代表使用一張數字 `i` 的牌。

例如：

```python
count[2] = 2
```

使用一張後：

```python
count[2] = 1
```

再使用一張：

```python
count[2] = 0
```

---

## 為什麼這行不能漏掉？

如果沒有：

```python
count[i] -= 1
```

每張牌的數量永遠不會減少。

Heap 也永遠不會清空。

程式可能進入無限迴圈。

所以這行非常重要。

---

# 如果某張牌被用完

```python
if count[i] == 0:
```

代表數字 `i` 的所有牌都已經被使用完。

例如：

```python
count[3] = 1
```

減一後：

```python
count[3] = 0
```

這張牌之後不應該再被視為剩餘牌。

所以需要從 Heap 移除。

---

# 檢查是否按最小值順序耗盡

```python
if i != minH[0]:
    return False
```

這是整題最關鍵、也最難理解的一行。

---

## 這一行在檢查什麼？

當：

```python
count[i] == 0
```

代表 `i` 已經完全用完。

如果要從 Min Heap 移除 `i`，它必須正好是：

```python
minH[0]
```

也就是目前 Heap 中最小的牌。

因為 Heap 只能有效率地移除 Heap Top。

---

## 為什麼如果不是 Heap Top 就代表失敗？

假設目前 Heap：

```python
[2,3,4]
```

最小值是：

```python
2
```

現在在組一個群組時，發現：

```python
count[3] == 0
```

但：

```python
count[2] > 0
```

這表示：

```text
數字 3 已經用完，
但更小的數字 2 還剩下。
```

之後剩下的 `2` 必須組成：

```text
[2,3,...]
```

可是 `3` 已經沒有牌了。

所以未來一定無法完成分組。

因此直接：

```python
return False
```

---

## Example

假設：

```python
hand = [1,2,2,3]
groupSize = 2
```

Count：

```python
{
    1: 1,
    2: 2,
    3: 1
}
```

先建立：

```text
[1,2]
```

使用後：

```python
count[1] = 0
count[2] = 1
```

`1` 是 Heap Top，所以可以 Pop。

剩下：

```text
2,3
```

可以建立：

```text
[2,3]
```

成功。

---

反過來，如果某個較大的數字先歸零，但較小數字仍有剩餘，就會造成無法再往後配對。

---

# 從 Heap 移除已用完的牌

```python
heapq.heappop(minH)
```

因為前面已確認：

```python
i == minH[0]
```

所以 Heap Top 就是已經用完的牌 `i`。

將它移除。

---

## 為什麼不用指定要刪除哪一個值？

`heapq.heappop(minH)` 永遠只移除最小值。

前面已經確認：

```python
i == minH[0]
```

所以移除的正是 `i`。

---

# 全部成功後回傳 True

```python
return True
```

只有在以下情況都沒有發生時，才會走到這裡：

* 牌數不能整除
* 需要的連續牌不存在
* 某張牌提前用完造成順序衝突

當 Heap 空了，代表所有牌都被成功分成連續群組。

所以回傳：

```python
True
```

---

# 🧪 Example Walkthrough

使用：

```python
hand = [1,2,3,6,2,3,4,7,8]
groupSize = 3
```

---

## Step 1：檢查總牌數

```python
len(hand) = 9
```

```python
9 % 3 = 0
```

可以繼續。

---

## Step 2：建立 Count

```python
count = {
    1: 1,
    2: 2,
    3: 2,
    4: 1,
    6: 1,
    7: 1,
    8: 1
}
```

---

## Step 3：建立 Heap

```python
minH = [1,2,3,4,6,7,8]
```

Heap Top：

```python
1
```

---

# 第一組

```python
first = 1
```

需要：

```text
1,2,3
```

---

## 使用 1

```python
count[1] -= 1
```

得到：

```python
count[1] = 0
```

因為：

```python
1 == minH[0]
```

所以 Pop `1`。

Heap：

```python
[2,3,4,6,7,8]
```

---

## 使用 2

```python
count[2] = 2 → 1
```

還沒有歸零，所以不 Pop。

---

## 使用 3

```python
count[3] = 2 → 1
```

還沒有歸零。

---

第一組完成：

```text
[1,2,3]
```

目前：

```python
count = {
    1: 0,
    2: 1,
    3: 1,
    4: 1,
    6: 1,
    7: 1,
    8: 1
}
```

---

# 第二組

Heap Top：

```python
2
```

所以：

```python
first = 2
```

需要：

```text
2,3,4
```

---

## 使用 2

```python
count[2] = 1 → 0
```

`2` 是 Heap Top。

Pop `2`。

---

## 使用 3

```python
count[3] = 1 → 0
```

現在 Heap Top 是：

```python
3
```

所以可以 Pop `3`。

---

## 使用 4

```python
count[4] = 1 → 0
```

現在 Heap Top 是：

```python
4
```

所以 Pop `4`。

---

第二組完成：

```text
[2,3,4]
```

Heap 剩下：

```python
[6,7,8]
```

---

# 第三組

Heap Top：

```python
6
```

需要：

```text
6,7,8
```

---

## 使用 6

```python
count[6] = 1 → 0
```

Pop `6`。

---

## 使用 7

```python
count[7] = 1 → 0
```

Pop `7`。

---

## 使用 8

```python
count[8] = 1 → 0
```

Pop `8`。

---

Heap：

```python
[]
```

所有牌都成功分組。

回傳：

```python
True
```

---

# 📊 Count 和 Heap 變化

| Group | 使用的牌      | Count 歸零 | Heap 移除 |
| ----- | --------- | -------- | ------- |
| 1     | `[1,2,3]` | `1`      | `1`     |
| 2     | `[2,3,4]` | `2,3,4`  | `2,3,4` |
| 3     | `[6,7,8]` | `6,7,8`  | `6,7,8` |

---

# 🧪 Failure Example

```python
hand = [1,2,3,4,5]
groupSize = 4
```

總牌數：

```python
5
```

計算：

```python
5 % 4 = 1
```

無法完整分組。

直接回傳：

```python
False
```

---

# 🧪 Missing Number Example

```python
hand = [1,2,4,5,6,7]
groupSize = 3
```

Count：

```python
{
    1: 1,
    2: 1,
    4: 1,
    5: 1,
    6: 1,
    7: 1
}
```

Heap Top：

```python
1
```

需要建立：

```text
1,2,3
```

但：

```python
3 not in count
```

因此回傳：

```python
False
```

---

# 🤔 為什麼這是 Greedy？

每次選擇：

```python
first = minH[0]
```

也就是目前最小的牌。

接著強制建立：

```text
[first, first + 1, ..., first + groupSize - 1]
```

這是一個局部選擇。

而這個選擇是安全的，因為目前最小的牌不可能放進任何更早開始的群組。

所以它只能成為目前某一組的起點。

---

# 🤔 為什麼不能從任意牌開始？

例如：

```python
hand = [1,2,3,4,5,6]
groupSize = 3
```

如果先從 `2` 開始：

```text
[2,3,4]
```

剩下：

```text
[1,5,6]
```

無法分組。

但正確方式應該是：

```text
[1,2,3]
[4,5,6]
```

所以必須從最小牌開始。

---

# 🤔 為什麼不能只排序後每 groupSize 張切一組？

例如：

```python
hand = [1,2,2,3,3,4]
groupSize = 3
```

排序後：

```python
[1,2,2,3,3,4]
```

如果直接切：

```text
[1,2,2]
[3,3,4]
```

都不是連續。

但其實可以分成：

```text
[1,2,3]
[2,3,4]
```

所以不能直接每 `groupSize` 張切一組。

---

# 🤔 為什麼 Heap 只放 Unique Values？

如果 Heap 放所有牌：

```python
[1,1,2,2,3,3]
```

會有很多重複值。

但我們真正需要的只是：

```text
目前最小的尚未用完數字
```

所以只放：

```python
[1,2,3]
```

更方便。

數量則透過：

```python
count
```

管理。

---

# 🤔 為什麼 `count[i] == 0` 時要立刻處理？

如果某個數字用完了，它不應該繼續留在 Heap Top。

否則下一次：

```python
first = minH[0]
```

可能取得一個已經沒有剩餘牌的數字。

這會造成錯誤或無限迴圈。

所以當數量變成 `0` 時，就要按照正確順序 Pop。

---

# ⚠️ 原始程式碼的兩個錯誤

你原本的程式碼有：

```python
if i != min[0]:
```

這裡的：

```python
min
```

是 Python 的內建函式，不是 Heap。

應該改成：

```python
if i != minH[0]:
```

---

另外原始程式碼少了：

```python
count[i] -= 1
```

如果沒有減少數量：

```python
count[i]
```

永遠不會變成 `0`。

Heap 也不會被 Pop。

`while minH` 可能永遠執行。

所以一定要補上。

---

# 🆚 846 vs 659

## LeetCode 659 - Split Array into Consecutive Subsequences

兩題都處理：

```text
連續數字
```

但要求不同。

---

## 846

每組長度必須：

```python
剛好等於 groupSize
```

例如：

```text
[1,2,3]
```

---

## 659

每個 subsequence 長度必須：

```text
至少 3
```

不一定固定。

可能是：

```text
[1,2,3]
[4,5,6,7]
```

659 通常使用：

```text
Count + Need / Tails
```

846 則可以使用：

```text
Count + Min Heap
```

---

# 🆚 846 vs 1296

LeetCode 1296：

```text
Divide Array in Sets of K Consecutive Numbers
```

其實和 846 幾乎是同一題。

差別主要是題目背景不同：

* 846：撲克牌
* 1296：整數陣列

核心方法完全一樣：

```text
Count + Greedy + Smallest Number
```

---

# ⏱ Complexity Analysis

假設：

```text
n = hand 的牌數
m = 不同牌面數量
```

---

## 建立 Count

```python
for n in hand:
```

需要走訪所有牌。

時間：

```text
O(n)
```

---

## 建立 Heap

```python
heapq.heapify(minH)
```

Heap 中有 `m` 個不同數字。

時間：

```text
O(m)
```

---

## 處理所有牌

每張牌都會被使用一次：

```python
count[i] -= 1
```

總共：

```text
O(n)
```

每個不同數字最多從 Heap Pop 一次。

每次 Pop：

```text
O(log m)
```

總計：

```text
O(m log m)
```

---

## 總時間複雜度

```text
O(n + m log m)
```

最差情況每張牌都不同：

```text
m = n
```

所以可以寫成：

```text
O(n log n)
```

---

# 💾 Space Complexity

Count Dictionary：

```text
O(m)
```

Min Heap：

```text
O(m)
```

總空間：

```text
O(m)
```

最差情況：

```text
O(n)
```

---

# 🎯 Interview Takeaways

看到以下關鍵字：

```text
分成固定大小的群組
+
每組數字連續
+
可能有重複數字
```

想到：

```text
Count Frequency
+
每次從最小數字開始
+
Greedy
```

---

## 面試時可以這樣解釋

```text
First, the number of cards must be divisible by groupSize.

I count the frequency of every card value.

Then I build a min heap containing all distinct card values.

The smallest remaining card must be the beginning of a consecutive group, so I repeatedly take the heap minimum and try to use one card from each value in the required range.

Whenever a card's frequency becomes zero, it must be the current heap minimum before I remove it.

If a required value is missing or values are exhausted in the wrong order, the grouping is impossible.
```

---

# 🗣 Interview English Version

```text
The key greedy observation is that the smallest remaining card must start a new group.

I first count the frequency of every value and create a min heap of all distinct values.

While the heap is not empty, I take the smallest value and try to build a consecutive group of length groupSize.

For every required value, I decrement its frequency.

If its frequency becomes zero, it must be the current smallest value in the heap; otherwise, a smaller value would remain without enough consecutive cards to complete a future group.

If all cards are consumed successfully, I return true.
```

---

# ✍️ What I Learned

## 1. 最小元素通常限制最大

目前最小的牌沒有更小的牌可以和它組合。

所以它必須成為一個群組的起點。

---

## 2. Count 和 Heap 可以分工

Count：

```text
記錄數量
```

Heap：

```text
取得目前最小值
```

---

## 3. Heap 不需要放所有重複元素

只放 Unique Keys。

數量交給 Dictionary。

---

## 4. 數量歸零的順序很重要

如果較大的牌先被用完，但更小的牌還有剩餘，未來就無法再建立連續群組。

因此需要檢查：

```python
i == minH[0]
```

---

## 5. 先檢查能否整除

簡單的數學條件可以快速排除不可能情況。

```python
len(hand) % groupSize != 0
```

直接回傳 False。

---

# 🏆 Cheat Sheet

## 檢查牌數

```python
if len(hand) % groupSize:
    return False
```

---

## 建立 Count

```python
count = {}

for n in hand:
    count[n] = 1 + count.get(n, 0)
```

---

## 建立 Min Heap

```python
minH = list(count.keys())
heapq.heapify(minH)
```

---

## 每次從最小牌開始

```python
first = minH[0]
```

---

## 建立一組連續牌

```python
for i in range(first, first + groupSize):
```

---

## 缺少需要的牌

```python
if i not in count:
    return False
```

---

## 使用一張牌

```python
count[i] -= 1
```

---

## 牌用完時檢查順序

```python
if count[i] == 0:

    if i != minH[0]:
        return False

    heapq.heappop(minH)
```

---

# 🧭 解題流程圖

```text
牌數是否能被 groupSize 整除？
             |
       +-----+-----+
       |           |
      否           是
       |           |
   return False    v
              建立 Count
                   |
                   v
              建立 Min Heap
                   |
                   v
             Heap 是否為空？
              /          \
            是            否
            |             |
       return True    取最小值 first
                          |
                          v
            建立 first 到 first+groupSize-1
                          |
                          v
                 需要的牌存在嗎？
                    /          \
                  否            是
                  |             |
             return False   count[i] -= 1
                                  |
                                  v
                           count[i] == 0？
                             /         \
                           否           是
                           |            |
                       繼續下一張   i == Heap Top？
                                        /      \
                                      否        是
                                      |         |
                                 return False  Pop
```

---

# 🔑 Pattern Recognition

看到：

```text
固定長度的連續群組
```

可以先想：

```text
最小元素是不是必須成為起點？
```

如果是：

```text
Greedy
```

如果有重複元素：

```text
Frequency Map
```

如果要一直找目前最小值：

```text
Min Heap
```

完整 Pattern：

```text
Frequency Count
+
Min Heap
+
Greedy
```

---

# 🌟 One Sentence Summary

## English

> Always start a group from the smallest remaining card, consume one copy of every consecutive value, and use a frequency map with a min heap to ensure cards are exhausted in the correct order.

## 中文

> 每次都從目前最小的牌開始建立固定長度的連續群組，使用 Count 記錄剩餘數量，並用 Min Heap 確保牌按照正確的最小值順序被用完。

---

# ✅ Final Takeaway

這題最重要的不是 Heap 操作本身，而是這個 Greedy 觀察：

```text
目前最小的牌一定只能成為某個群組的起點。
```

所以流程可以固定為：

```text
1. 找目前最小牌

2. 從它開始取 groupSize 個連續數字

3. 每張牌數量減一

4. 用完的牌必須按照最小值順序移除

5. 重複直到所有牌用完
```
