# 📍 LeetCode 253 — Meeting Rooms II

## 📄 題目說明 | Problem Description

### 中文

給定一組會議時間區間：

```python
intervals: List[Interval]
```

每個 `Interval` 物件包含：

```python
interval.start
interval.end
```

請計算至少需要多少間會議室，才能讓所有會議順利進行。

兩場時間重疊的會議不能使用同一間會議室。

如果一場會議剛好在另一場結束時開始，則可以使用同一間會議室。

---

### English

Given a list of meeting intervals, return the minimum number of conference rooms required.

Meetings that overlap must use different rooms.

If one meeting starts exactly when another meeting ends, they may use the same room.

---

### Example 1

```python
intervals = [(0, 30), (5, 10), (15, 20)]
```

Output：

```python
2
```

可能的安排：

```text
Room 1：

[0, 30]

Room 2：

[5, 10] → [15, 20]
```

---

### Example 2

```python
intervals = [(7, 10), (2, 4)]
```

Output：

```python
1
```

排序後：

```python
[(2, 4), (7, 10)]
```

第一場在 `4` 結束，第二場在 `7` 開始，所以可以使用同一間會議室。

---

## 🧠 核心觀念 | Key Insight

LeetCode 252 只需要回答：

```text
有沒有任何會議重疊？
```

但 LeetCode 253 要回答：

```text
同一時間最多有幾場會議正在進行？
```

同一時間進行幾場會議，就需要幾間會議室。

---

### 為什麼先按照開始時間排序？

```python
intervals.sort(
    key=lambda interval: interval.start
)
```

排序後，我們可以按照時間順序處理每一場新會議。

每遇到一場新會議，就問：

> 現在有沒有一間舊會議室已經空出來？

如果有：

```text
重複使用舊房間
```

如果沒有：

```text
增加一間新房間
```

---

### Heap 裡面放什麼？

```python
min_heap = []
```

Heap 中只放：

```text
目前各個會議室的會議結束時間
```

例如：

```python
min_heap = [10, 30]
```

表示目前有兩間會議室正在被管理：

```text
其中一場會議在 10 結束

另一場會議在 30 結束
```

---

### 為什麼使用 Min Heap？

每一場新會議開始時，我們最想知道：

```text
哪一場舊會議最早結束？
```

Min Heap 的頂端：

```python
min_heap[0]
```

永遠是最小的結束時間。

也就是：

```text
最早可以空出來的會議室
```

---

### 為什麼只看最早結束的會議？

假設：

```python
min_heap = [10, 20, 30]
```

代表目前三間房間分別在：

```text
10、20、30
```

結束。

新會議在：

```python
start = 8
```

開始。

因為最早結束的房間都要到 `10` 才空：

```python
8 < 10
```

所以其他在 `20`、`30` 結束的房間當然也還沒有空。

因此需要新增房間。

如果新會議在：

```python
start = 15
```

開始：

```python
10 <= 15
```

代表最早結束的房間已經空出來，可以重複使用。

---

### 什麼時候可以重複使用房間？

```python
if min_heap[0] <= interval.start:
```

代表：

```text
最早結束的會議

已經在目前會議開始前結束
```

或剛好同時結束。

所以可以移除舊的結束時間：

```python
heapq.heappop(min_heap)
```

---

### 為什麼是 `<=`？

假設：

```text
舊會議：[1, 5]

新會議：[5, 10]
```

舊會議在 `5` 結束，新會議也在 `5` 開始。

同一間房間可以立刻接著使用。

所以條件必須包含相等：

```python
5 <= 5
```

---

### 每一場新會議都要 push

無論有沒有舊房間可以重複使用，目前的新會議都會占用一間房間。

所以要加入目前會議的結束時間：

```python
heapq.heappush(
    min_heap,
    interval.end
)
```

---

### 有空房間時

```python
heapq.heappop(min_heap)
heapq.heappush(min_heap, interval.end)
```

先移除已經結束的舊會議，再放入新會議。

Heap 大小不變，表示：

```text
重複使用同一間會議室
```

---

### 沒有空房間時

只執行：

```python
heapq.heappush(min_heap, interval.end)
```

Heap 大小增加一，表示：

```text
需要增加一間會議室
```

---

### 為什麼只 pop 一次？

因為目前只處理一場新會議。

即使有很多間房間都已經空出來，目前這場會議也只需要其中一間。

例如：

```python
min_heap = [3, 4, 5]
interval.start = 10
```

雖然三間房間都空了，但是現在只有一場新會議。

所以只需要：

```python
heappop()
```

一次。

---

### 為什麼最後可以回傳 Heap 大小？

每當沒有房間可以重複使用時：

```python
heappush()
```

會讓 Heap 大小增加。

每當有房間可以重複使用時：

```python
heappop()
heappush()
```

Heap 大小不變。

因此最後的：

```python
len(min_heap)
```

就是總共需要的會議室數量。

---

## 💻 Code

```python
import heapq


class Solution:
    def minMeetingRooms(
        self,
        intervals: List[Interval]
    ) -> int:
        if not intervals:
            return 0

        intervals.sort(
            key=lambda interval: interval.start
        )

        min_heap = []

        for interval in intervals:
            if (
                min_heap
                and min_heap[0] <= interval.start
            ):
                heapq.heappop(min_heap)

            heapq.heappush(min_heap, interval.end
            )

        return len(min_heap)
```

---

## 🧾 程式碼逐行解釋 | Line-by-line Explanation

```python
import heapq
```

匯入 Python 的 Heap 模組。

Python 的 `heapq` 是：

```text
Min Heap
```

所以：

```python
min_heap[0]
```

永遠是 Heap 中最小的值。

---

```python
class Solution:
```

定義 LeetCode 使用的 `Solution` 類別。

---

```python
def minMeetingRooms(
    self,
    intervals: List[Interval]
) -> int:
```

定義主要函式。

輸入是一組：

```python
Interval
```

物件。

回傳最少需要的會議室數量。

---

```python
if not intervals:
    return 0
```

如果沒有任何會議，就不需要會議室。

所以回傳：

```python
0
```

---

```python
intervals.sort(
    key=lambda interval: interval.start
)
```

按照每場會議的開始時間排序。

例如：

```python
[(15, 20), (0, 30), (5, 10)]
```

排序後：

```python
[(0, 30), (5, 10), (15, 20)]
```

---

```python
min_heap = []
```

建立 Min Heap。

Heap 中放的是：

```python
interval.end
```

也就是各會議室目前會議的結束時間。

---

```python
for interval in intervals:
```

依照開始時間順序處理每一場會議。

目前會議的開始時間：

```python
interval.start
```

目前會議的結束時間：

```python
interval.end
```

---

```python
if (
    min_heap
    and min_heap[0] <= interval.start
):
```

這個條件包含兩部分。

第一部分：

```python
min_heap
```

確認 Heap 中至少有一場舊會議。

第二部分：

```python
min_heap[0] <= interval.start
```

確認最早結束的會議已經結束。

如果成立，代表有一間會議室可以重複使用。

---

```python
heapq.heappop(min_heap)
```

移除最早結束的會議時間。

意思是：

```text
這間會議室已經空出來
```

---

```python
heapq.heappush(
    min_heap,
    interval.end
)
```

將目前新會議的結束時間放入 Heap。

代表目前會議已經占用一間房間。

---

```python
return len(min_heap)
```

回傳 Heap 的大小。

這就是最少需要的會議室數量。

---

## 🧪 Example Walkthrough

輸入：

```python
intervals = [
    Interval(0, 30),
    Interval(5, 10),
    Interval(15, 20)
]
```

---

### 排序

排序後：

```text
[0, 30]

[5, 10]

[15, 20]
```

初始：

```python
min_heap = []
```

---

### 處理 `[0, 30]`

Heap 是空的，所以不能重複使用舊房間。

加入：

```python
30
```

Heap：

```python
[30]
```

目前需要：

```text
1 間房間
```

---

### 處理 `[5, 10]`

目前會議開始：

```python
interval.start = 5
```

最早結束：

```python
min_heap[0] = 30
```

比較：

```python
30 <= 5
```

不成立。

代表原本的會議還沒結束。

加入目前結束時間：

```python
10
```

Heap：

```python
[10, 30]
```

目前需要：

```text
2 間房間
```

---

### 處理 `[15, 20]`

目前會議開始：

```python
15
```

最早結束：

```python
10
```

比較：

```python
10 <= 15
```

成立。

所以移除：

```python
10
```

Heap 剩下：

```python
[30]
```

再加入目前會議結束時間：

```python
20
```

Heap：

```python
[20, 30]
```

Heap 大小仍然是：

```python
2
```

代表重複使用了原本的房間。

---

### 最終答案

```python
len(min_heap)
```

等於：

```python
2
```

所以回傳：

```python
2
```

---

## 🆚 LeetCode 252 vs LeetCode 253

### LeetCode 252

問題：

```text
能不能參加所有會議？
```

只需要檢查：

```python
current.start < previous.end
```

如果重疊：

```python
return False
```

---

### LeetCode 253

問題：

```text
最少需要幾間會議室？
```

需要使用 Min Heap 追蹤：

```text
每間房間最早何時空出來
```

如果沒有空房間：

```text
新增一間
```

如果有空房間：

```text
重複使用
```

---

### 兩題比較表

| 題目           | 問題       | 資料結構          | 核心判斷                            |
| ------------ | -------- | ------------- | ------------------------------- |
| LeetCode 252 | 能否參加全部會議 | 排序            | `current.start < previous.end`  |
| LeetCode 253 | 最少需要幾間房間 | 排序 + Min Heap | `earliest_end <= current.start` |

---

## ⏱ Complexity Analysis

### Time Complexity

排序：

```text
O(n log n)
```

每場會議執行 Heap 操作：

```text
O(log n)
```

處理 `n` 場會議：

```text
O(n log n)
```

所以總時間複雜度：

```text
O(n log n)
```

---

### Space Complexity

最壞情況下，所有會議都重疊。

Heap 最多存入：

```text
n 個結束時間
```

所以空間複雜度：

```text
O(n)
```

---

## 🎯 Interview Takeaways

* 先按照 `interval.start` 排序。
* Min Heap 儲存 `interval.end`。
* `min_heap[0]` 是最早結束的會議。
* 如果：

```python
min_heap[0] <= interval.start
```

代表可以重複使用房間。

* 有空房間時先 `pop`。
* 每一場會議都要把 `end` 加入 Heap。
* 最後 `len(min_heap)` 就是房間數。
* 開始時間相等於前一場結束時間時，可以共用房間。
* LeetCode 252 不需要 Heap。
* LeetCode 253 需要管理多個同時進行的會議。

---

## ✍️ 我學到的東西 | What I Learned

* `interval.start` 表示開始時間。
* `interval.end` 表示結束時間。
* 先按照開始時間排序。
* Heap 中只需要放結束時間。
* Min Heap 可以快速找到最早空出的房間。
* `end <= start` 表示可以重複使用房間。
* 有空房間時，Heap 先 pop 再 push，大小不變。
* 沒有空房間時，只 push，Heap 大小增加。
* Heap 大小增加代表需要新增會議室。
* 最後 Heap 大小就是最少房間數。
* LeetCode 252 是判斷有沒有重疊。
* LeetCode 253 是計算最大同時重疊數量。

---

## 🏆 Cheat Sheet

```text
按照開始時間排序

↓

建立 Min Heap

↓

Heap 儲存：

每個房間目前會議的 end

↓

處理每一場會議

↓

最早會議已結束：

min_heap[0] <= interval.start

↓

可以重複使用：

heappop()

↓

加入目前會議：

heappush(interval.end)

↓

答案：

len(min_heap)
```

核心程式：

```python
intervals.sort(
    key=lambda interval: interval.start
)

min_heap = []

for interval in intervals:
    if (
        min_heap
        and min_heap[0] <= interval.start
    ):
        heapq.heappop(min_heap)

    heapq.heappush(
        min_heap,
        interval.end
    )

return len(min_heap)
```

---

## 🌟 One Sentence Summary

> Sort meetings by start time, use a min heap to track the earliest ending meeting, reuse a room when possible, and return the heap size.

> 將會議依開始時間排序，使用 Min Heap 追蹤最早結束的會議，能重複使用房間時先移除舊結束時間，最後 Heap 大小就是所需房間數。

---

## 🆚 LeetCode 253 和 LeetCode 435 的差別

這兩題都和會議區間重疊有關，也都會先排序。

但它們問的問題不同，所以排序方式和後續做法也不同。

### LeetCode 253 — Meeting Rooms II

問題是：

```text
如果所有會議都要保留，

至少需要幾間會議室？
```

遇到重疊時：

```text
不能刪除會議
```

而是需要：

```text
增加一間會議室
```

所以要同時追蹤多間會議室的結束時間。

通常使用：

```text
開始時間排序 + Min Heap
```

---

### LeetCode 435 — Non-overlapping Intervals

問題是：

```text
最少要刪除幾個區間，

才能讓剩下的區間都不重疊？
```

遇到重疊時：

```text
可以刪除其中一個區間
```

我們希望保留越多區間越好，因此要選擇：

```text
結束時間比較早的區間
```

通常使用：

```text
結束時間排序 + Greedy
```

---

## 🎯 核心差別

| 題目           | 目標           | 遇到重疊時 |
| ------------ | ------------ | ----- |
| LeetCode 253 | 保留所有會議，計算房間數 | 新增房間  |
| LeetCode 435 | 讓剩下區間不重疊     | 刪除區間  |

---

## 🔍 為什麼 LeetCode 253 按開始時間排序？

LeetCode 253 要按照會議發生的順序，逐一安排房間。

所以先按照：

```python
interval.start
```

排序。

每遇到一場新會議，就檢查：

```text
最早結束的會議室是否已經空出來
```

如果已經空出來：

```text
重複使用房間
```

如果還沒空：

```text
增加新房間
```

核心判斷：

```python
earliest_end <= current_start
```

代表最早結束的會議已經結束，可以重複使用房間。

---

## 🔍 為什麼 LeetCode 435 按結束時間排序？

LeetCode 435 的目標是：

```text
保留最多不重疊區間
```

為了替後面的區間留下更多空間，我們應該優先保留：

```text
結束時間最早的區間
```

例如有兩個重疊區間：

```python
[1, 10]
[2, 3]
```

如果保留：

```python
[1, 10]
```

後面時間 `3` 到 `10` 之間的區間都可能無法選。

如果保留：

```python
[2, 3]
```

它很快就結束，後面還能放更多區間。

所以 LeetCode 435 會按照：

```python
interval.end
```

排序。

---

## 💻 LeetCode 253 Code

如果題目給的是普通 List：

```python
import heapq


class Solution:
    def minMeetingRooms(
        self,
        intervals: List[List[int]]
    ) -> int:
        if not intervals:
            return 0

        intervals.sort(
            key=lambda interval: interval[0]
        )

        min_heap = []

        for start, end in intervals:
            if (
                min_heap
                and min_heap[0] <= start
            ):
                heapq.heappop(min_heap)

            heapq.heappush(min_heap, end)

        return len(min_heap)
```

### LeetCode 253 核心

```python
intervals.sort(
    key=lambda interval: interval[0]
)
```

按照開始時間排序。

Heap 儲存：

```text
每一間會議室目前會議的結束時間
```

判斷：

```python
min_heap[0] <= start
```

代表：

```text
最早結束的會議室已經空出來
```

可以重複使用。

---

## 💻 LeetCode 435 Code

```python
class Solution:
    def eraseOverlapIntervals(
        self,
        intervals: List[List[int]]
    ) -> int:
        intervals.sort(
            key=lambda interval: interval[1]
        )

        removals = 0
        previous_end = intervals[0][1]

        for i in range(1, len(intervals)):
            current_start = intervals[i][0]
            current_end = intervals[i][1]

            if current_start < previous_end:
                removals += 1
            else:
                previous_end = current_end

        return removals
```

---

## 🧠 LeetCode 435 核心判斷

```python
current_start < previous_end
```

代表：

```text
目前區間開始時，

前一個保留的區間還沒有結束
```

所以兩個區間重疊。

遇到重疊時：

```python
removals += 1
```

代表刪除目前其中一個區間。

因為已經按照結束時間排序，所以前面保留的區間：

```text
結束得比較早
```

通常留下它對後面的區間最有利。

因此重疊時不需要更新：

```python
previous_end
```

---

## 🧪 Example

```python
intervals = [
    [1, 2],
    [2, 3],
    [3, 4],
    [1, 3]
]
```

---

### LeetCode 253 的角度

所有區間都必須保留。

同一時間最多有：

```text
2 個區間重疊
```

所以需要：

```python
2
```

間房間。

---

### LeetCode 435 的角度

可以刪除區間。

只要刪除：

```python
[1, 3]
```

剩下：

```python
[1, 2]
[2, 3]
[3, 4]
```

都不重疊。

所以答案是：

```python
1
```

---

## 🧪 更明顯的差別

```python
intervals = [
    [0, 30],
    [5, 10],
    [15, 20]
]
```

### LeetCode 253

三場會議都必須保留。

安排：

```text
Room 1：[0, 30]

Room 2：[5, 10] → [15, 20]
```

答案：

```python
2
```

---

### LeetCode 435

可以刪除區間。

如果刪除：

```python
[0, 30]
```

剩下：

```python
[5, 10]
[15, 20]
```

完全不重疊。

答案：

```python
1
```

---

## 🔄 排序方式比較

### LeetCode 253

按照開始時間排序：

```python
intervals.sort(
    key=lambda interval: interval[0]
)
```

原因：

```text
依照每場會議開始的時間安排房間
```

---

### LeetCode 435

按照結束時間排序：

```python
intervals.sort(
    key=lambda interval: interval[1]
)
```

原因：

```text
優先保留結束時間最早的區間，

讓後面保留更多選擇空間
```

---

## 📦 資料結構比較

| 題目           | 使用方式                 |
| ------------ | -------------------- |
| LeetCode 253 | Min Heap             |
| LeetCode 435 | 一個 `previous_end` 變數 |

LeetCode 253 要同時管理多間房間，所以需要記錄：

```text
多個結束時間
```

因此使用 Heap。

LeetCode 435 每次只需要記住：

```text
最後一個保留區間的結束時間
```

所以一個變數就夠。

---

## 🔍 相等時算不算重疊？

假設：

```python
[1, 5]
[5, 10]
```

第一個區間在 `5` 結束，第二個區間也在 `5` 開始。

它們不重疊。

---

### LeetCode 253

可以重複使用房間：

```python
previous_end <= current_start
```

也就是：

```python
5 <= 5
```

成立。

---

### LeetCode 435

不需要刪除：

```python
current_start < previous_end
```

也就是：

```python
5 < 5
```

不成立。

---

## 🏆 Cheat Sheet

```text
LeetCode 253

問題：
所有會議都保留，需要幾間房間？

排序：
start

資料結構：
Min Heap

遇到重疊：
增加房間

核心：
earliest_end <= current_start
代表可以重複使用房間
```

```text
LeetCode 435

問題：
最少刪除幾個區間，才能不重疊？

排序：
end

資料結構：
previous_end

遇到重疊：
刪除一個區間

核心：
current_start < previous_end
代表發生重疊
```

---

## 🌟 One Sentence Summary

> LeetCode 253 keeps every interval and uses a min heap to count rooms, while LeetCode 435 removes overlapping intervals and greedily keeps the interval that ends earliest.

> LeetCode 253 必須保留所有會議，因此使用 Min Heap 計算房間數；LeetCode 435 可以刪除區間，因此用 Greedy 優先保留最早結束的區間。
