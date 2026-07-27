# 📍 LeetCode 1851 - Minimum Interval to Include Each Query

**Difficulty:** Hard

**Topics**

- Sorting
- Heap (Priority Queue)
- Sweep Line
- Offline Query

---

# 📄 題目說明 | Problem Description

## 中文

給定一個二維陣列 `intervals`，其中：

```python
intervals[i] = [lefti, righti]
```

表示一個閉區間：

```
[left, right]
```

以及一個陣列

```python
queries
```

對於每一個 query，

找出：

> 所有包含這個 query 的 interval 中，
>
> **長度最短的那一個。**

如果沒有任何 interval 包含 query，

答案就是

```
-1
```

---

### Interval 長度

例如

```
[2,5]
```

不是

```
5-2=3
```

而是

```
5-2+1=4
```

因為包含：

```
2
3
4
5
```

共有四個數。

---

## English

You are given a list of intervals and a list of queries.

For every query,

find the size of the smallest interval that contains it.

If no interval contains the query,

return

```
-1
```

---

# 📚 Example 1

```python
intervals = [[1,4],[2,4],[3,6],[4,4]]

queries = [2,3,4,5]
```

Output

```python
[3,3,1,4]
```

---

### Query = 2

包含它的區間：

```
[1,4]
size=4

[2,4]
size=3
```

最短：

```
3
```

---

### Query = 3

```
[1,4]
size=4

[2,4]
size=3

[3,6]
size=4
```

答案：

```
3
```

---

### Query = 4

```
[1,4]
size=4

[2,4]
size=3

[3,6]
size=4

[4,4]
size=1
```

答案：

```
1
```

---

### Query = 5

只有：

```
[3,6]
```

答案：

```
4
```

---

# 📚 Example 2

```python
intervals=[[2,3],[2,5],[1,8],[20,25]]

queries=[2,19,5,22]
```

Output

```python
[2,-1,4,6]
```

---

# 💻 Code

```python
import heapq

class Solution:

    def minInterval(
        self,
        intervals: List[List[int]],
        queries: List[int]
    ) -> List[int]:

        intervals.sort()

        sorted_queries = sorted(
            (query,index)
            for index,query in enumerate(queries)
        )

        answer = [-1] * len(queries)

        min_heap = []

        i = 0

        for query,index in sorted_queries:

            while (
                i < len(intervals)
                and intervals[i][0] <= query
            ):

                left,right = intervals[i]

                size = right-left+1

                heapq.heappush(
                    min_heap,
                    (size,right)
                )

                i += 1

            while (
                min_heap
                and min_heap[0][1] < query
            ):

                heapq.heappop(min_heap)

            if min_heap:

                answer[index] = min_heap[0][0]

        return answer
```

---

# 🧠 第一眼怎麼想到？

這題第一次看到，

很多人第一個想到的是：

```
每個 Query

↓

掃所有 Interval

↓

看看有沒有包含

↓

找最短
```

例如：

```
queries

2
3
4
5
```

每一個都重新掃：

```
[1,4]

[2,4]

[3,6]

[4,4]
```

假設

```
N = interval數量

M = query數量
```

時間：

```
O(N × M)
```

LeetCode 最大：

```
100000
```

所以：

```
100000 × 100000

=

10^10
```

完全不可能。

因此一定需要：

> **不要一直重複掃 Interval。**

---

# 🧠 第二個想法

如果 Query 是：

```
2

↓

3

↓

4

↓

5
```

你會發現：

Query 是一路變大的。

那麼：

```
已經看過的 Interval

是不是不用再重新掃？
```

例如：

```
interval

[1,4]
```

Query=2

加入。

下一個 Query=3

還是會用到。

下一個 Query=4

還是會用到。

所以：

```
不用重新掃。
```

---

因此：

想到：

```
Interval

只掃一次。
```

這就是：

```
Sweep Line
```

思想。

---

# 🧠 Offline Query

可是：

Query 原本可能是：

```python
[5,2,100,7]
```

沒有順序。

因此：

不能 Sweep。

所以：

第一步：

```
先排序 Query。
```

例如：

原本：

```
5

2

100

7
```

排序：

```
2

5

7

100
```

是不是就可以一路往右走？

所以：

```
Interval

排序

+

Query

排序
```

就是 Offline Query。

---

# 🧠 為什麼要保留 Index？

例如：

```python
queries

[5,2,100]
```

排序後：

```
2

5

100
```

最後得到：

```
3

4

8
```

可是題目要：

```
原本順序
```

所以：

需要知道：

```
2

原本在哪？
```

因此：

排序的是：

```python
(query,index)
```

例如：

```
[(2,1),

(5,0),

(100,2)]
```

最後：

```
answer[index]

=

答案放回原位置
```

---

# 🧠 Heap 要放什麼？

很多人第一個想到：

```
Heap

放：

right
```

錯。

因為題目不是找：

```
最早結束
```

而是：

```
最短 Interval
```

因此：

Priority 必須是：

```
size
```

所以：

Heap 第一個元素：

```
size
```

但是：

還需要知道：

```
這個 Interval

是不是已經不能用了？
```

所以：

還要存：

```
right
```

因此：

Heap 放：

```python
(size,right)
```

例如：

```
[2,5]

↓

size=4

↓

(4,5)
```

不是：

```
(left,right)
```

也不是：

```
(right,size)
```

因為 Python Heap：

永遠比較：

Tuple 第一個元素。

因此：

第一個一定要是：

```
size
```

才能保證：

Heap Top

永遠都是：

```
最短區間。
```
## 🧾 程式碼逐行解釋 | Line-by-line Explanation

### 1. 匯入 Heap

```python
import heapq
```

Python 的 Min Heap 使用：

```python
heapq
```

常用操作：

```python
heapq.heappush(heap, value)
```

將元素加入 Heap。

```python
heapq.heappop(heap)
```

移除並回傳 Heap 中最小的元素。

```python
heap[0]
```

查看 Heap 中最小的元素，但不移除。

---

### 2. 建立 Solution Class

```python
class Solution:
```

LeetCode 固定要求使用：

```python
class Solution
```

並且在裡面定義題目指定的方法。

---

### 3. 定義函式

```python
def minInterval(
    self,
    intervals: List[List[int]],
    queries: List[int]
) -> List[int]:
```

輸入：

```python
intervals
```

每一個元素是一個區間：

```python
[left, right]
```

例如：

```python
[[1,4],[2,4],[3,6]]
```

另一個輸入：

```python
queries
```

例如：

```python
[2,3,4,5]
```

回傳：

```python
List[int]
```

也就是每個 query 對應的最短區間長度。

---

### 4. 排序 Intervals

```python
intervals.sort()
```

Python 對二維陣列排序時，會先比較第一個元素。

例如：

```python
intervals = [
    [3,6],
    [1,4],
    [4,4],
    [2,4]
]
```

排序後：

```python
[
    [1,4],
    [2,4],
    [3,6],
    [4,4]
]
```

也就是依照：

```python
left
```

由小到大排序。

---

### 為什麼要按照 Left 排序？

因為處理某個 query 時，我們需要加入所有：

```python
left <= query
```

的區間。

如果 interval 已經依照 `left` 排序，就可以使用一個 pointer：

```python
i
```

一路往右移。

例如：

```text
intervals:

[1,4]
[2,4]
[3,6]
[4,4]
```

處理：

```text
query = 2
```

可以加入：

```text
[1,4]
[2,4]
```

下一個：

```text
query = 3
```

不需要從頭重新掃。

只要從：

```text
[3,6]
```

繼續。

這樣每個 interval 只會被查看一次。

---

### 5. 排序 Queries 並保留原始 Index

```python
sorted_queries = sorted(
    (query, index)
    for index, query in enumerate(queries)
)
```

這一段可以拆成兩步理解。

---

#### enumerate(queries)

假設：

```python
queries = [5,2,4]
```

執行：

```python
enumerate(queries)
```

會產生：

```text
index = 0, query = 5
index = 1, query = 2
index = 2, query = 4
```

---

#### 建立 Tuple

```python
(query, index)
```

所以會變成：

```python
[
    (5,0),
    (2,1),
    (4,2)
]
```

---

#### 再進行排序

```python
sorted(...)
```

排序後：

```python
[
    (2,1),
    (4,2),
    (5,0)
]
```

---

### 為什麼 Tuple 是 `(query, index)`？

因為 Python 排序 Tuple 時，會先比較第一個值。

我們想依照：

```python
query
```

排序。

所以 `query` 必須放第一個。

如果寫成：

```python
(index, query)
```

排序就會按照 index，而不是 query。

那就沒有意義。

---

### 為什麼不能直接寫？

```python
queries.sort()
```

因為這樣會失去原本順序。

例如：

```python
queries = [5,2,4]
```

排序後：

```python
[2,4,5]
```

假設答案是：

```python
[3,1,4]
```

這是按照排序後 query 的答案。

但題目要求回傳原本：

```python
[5,2,4]
```

的順序。

所以必須記住：

```python
原始 index
```

---

### 6. 建立 Answer Array

```python
answer = [-1] * len(queries)
```

假設：

```python
queries = [2,3,4,5]
```

長度是：

```python
4
```

因此：

```python
answer = [-1,-1,-1,-1]
```

---

### 為什麼預設放 `-1`？

因為題目規定：

如果沒有任何 interval 包含 query，

答案就是：

```python
-1
```

所以先將所有位置設成：

```python
-1
```

找到答案時再覆蓋。

這樣就不需要額外處理：

```python
else:
    answer[index] = -1
```

---

### 7. 建立 Min Heap

```python
min_heap = []
```

Python 的 Heap 本質上使用 List。

一開始沒有任何候選 interval，所以：

```python
min_heap = []
```

Heap 裡面會放：

```python
(size, right)
```

例如：

```python
interval = [2,5]
```

長度：

```python
5 - 2 + 1 = 4
```

加入 Heap：

```python
(4,5)
```

---

## 8. 建立 Interval Pointer

```python
i = 0
```

`i` 表示：

> 下一個還沒有加入 Heap 的 interval。

例如：

```python
intervals = [
    [1,4],
    [2,4],
    [3,6],
    [4,4]
]
```

一開始：

```python
i = 0
```

指向：

```python
[1,4]
```

當 `[1,4]` 加入 Heap 後：

```python
i += 1
```

接著指向：

```python
[2,4]
```

---

### 為什麼不需要把 i 歸零？

因為 queries 已經排序。

Query 只會越來越大。

一個 interval 一旦滿足：

```python
left <= query
```

並被加入 Heap，

它就不需要再次加入。

因此 pointer 永遠只會向右移。

---

### 9. 依序處理排序後的 Query

```python
for query, index in sorted_queries:
```

例如：

```python
sorted_queries = [
    (2,1),
    (4,2),
    (5,0)
]
```

每一次迴圈會得到：

```text
query = 2
index = 1
```

接著：

```text
query = 4
index = 2
```

最後：

```text
query = 5
index = 0
```

---

### 10. 加入所有已經開始的 Interval

```python
while (
    i < len(intervals)
    and intervals[i][0] <= query
):
```

這個 `while` 有兩個條件。

---

#### 條件一

```python
i < len(intervals)
```

確保 pointer 沒有超出陣列範圍。

假設：

```python
len(intervals) = 4
```

合法 index：

```python
0
1
2
3
```

當：

```python
i = 4
```

就不能再執行：

```python
intervals[i]
```

否則會出現：

```text
IndexError
```

---

#### 條件二

```python
intervals[i][0] <= query
```

`intervals[i][0]` 是：

```python
left
```

這個條件表示：

```python
left <= query
```

也就是這個 interval 已經有可能包含 query。

例如：

```python
interval = [2,6]
query = 4
```

因為：

```python
2 <= 4
```

所以有可能包含。

---

### 為什麼只是「有可能」？

因為還要檢查：

```python
right >= query
```

例如：

```python
interval = [1,2]
query = 4
```

雖然：

```python
left <= query
```

但：

```python
right < query
```

所以已經失效。

這一部分會在後面的 pop 階段處理。

---

### 為什麼用 `while`，不是 `if`？

因為同一個 query 可能同時讓很多 intervals 成為候選。

例如：

```python
intervals = [
    [1,10],
    [2,8],
    [3,7]
]
```

現在：

```python
query = 5
```

三個 interval 都滿足：

```python
left <= 5
```

如果使用：

```python
if
```

只會加入一個 interval。

但正確答案可能是後面的：

```python
[3,7]
```

所以必須使用：

```python
while
```

把所有符合：

```python
left <= query
```

的 interval 全部加入。

---

### 11. 取出 Left 和 Right

```python
left, right = intervals[i]
```

例如：

```python
intervals[i] = [2,5]
```

執行後：

```python
left = 2
right = 5
```

這叫做：

```text
Unpacking
```

比起：

```python
left = intervals[i][0]
right = intervals[i][1]
```

更加簡潔。

---

### 12. 計算 Interval Size

```python
size = right - left + 1
```

例如：

```python
left = 2
right = 5
```

計算：

```python
5 - 2 + 1 = 4
```

因為閉區間 `[2,5]` 包含：

```text
2
3
4
5
```

總共四個值。

---

### 為什麼一定要 `+1`？

如果寫成：

```python
right - left
```

那 `[4,4]` 的長度會是：

```python
4 - 4 = 0
```

但實際上：

```python
[4,4]
```

包含一個數字：

```python
4
```

所以長度應該是：

```python
1
```

---

### 13. 將 Interval 加入 Heap

```python
heapq.heappush(
    min_heap,
    (size, right)
)
```

加入：

```python
(size, right)
```

例如：

```python
interval = [2,5]
```

放入：

```python
(4,5)
```

---

### 為什麼 Heap 放 `(size, right)`？

這兩個值分別有不同用途。

```python
size
```

用途：

```text
決定誰是最短 interval
```

```python
right
```

用途：

```text
判斷 interval 是否過期
```

---

### Python Tuple 在 Heap 中如何比較？

Python 會先比較第一個元素。

例如：

```python
(3,10)
(5,6)
(4,100)
```

Heap Top 是：

```python
(3,10)
```

因為第一個值：

```python
3
```

最小。

因此將 `size` 放第一個，就能讓最短 interval 位於 Heap Top。

---

### 如果 Size 一樣呢？

例如：

```python
(4,5)
(4,8)
```

第一個值相同時，Python 會比較第二個值。

所以：

```python
(4,5)
```

會排在：

```python
(4,8)
```

之前。

但這不影響答案。

因為兩個 interval 長度都是：

```python
4
```

題目只要求回傳長度。

---

### 為什麼不用存 Left？

因為 interval 加入 Heap 前，已經確認：

```python
left <= query
```

而且 query 只會越來越大。

一旦某個 interval 的 left 已經小於等於目前 query，

對後面的 query 也一定是：

```python
left <= query
```

所以之後不需要再看 left。

只需要判斷：

```python
right
```

是否還能覆蓋目前 query。

---

### 14. Pointer 往右移

```python
i += 1
```

表示：

這個 interval 已經加入 Heap。

下一次檢查下一個 interval。

---

### 為什麼 i 在 Push 後才加一？

因為必須先處理目前的 interval。

流程是：

```text
讀取 interval
↓
計算 size
↓
加入 Heap
↓
pointer 往右
```

如果一開始就：

```python
i += 1
```

就可能跳過目前 interval。

---

### 15. 移除已失效的 Interval

```python
while (
    min_heap
    and min_heap[0][1] < query
):
```

這個 while 同樣有兩個條件。

---

#### 條件一

```python
min_heap
```

確認 Heap 不是空的。

空 List 在 Python 中會被視為：

```python
False
```

如果 Heap 是空的，不能存取：

```python
min_heap[0]
```

否則會出現：

```text
IndexError
```

---

#### 條件二

```python
min_heap[0][1] < query
```

`min_heap[0]` 是 Heap Top。

假設：

```python
min_heap[0] = (3,4)
```

則：

```python
min_heap[0][1]
```

就是：

```python
right = 4
```

如果目前：

```python
query = 5
```

因為：

```python
4 < 5
```

所以該 interval 已經無法包含 query。

必須移除。

---

## 為什麼是 `< query`，不是 `<= query`？

因為 interval 是閉區間。

例如：

```python
interval = [1,4]
query = 4
```

這個 interval 仍然包含：

```python
4
```

所以不能在：

```python
right == query
```

時移除。

只有：

```python
right < query
```

才表示完全過期。

---

## 為什麼又是 `while`，不是 `if`？

因為可能有多個失效 interval。

例如目前 Heap：

```python
[
    (1,2),
    (2,3),
    (4,4),
    (10,20)
]
```

目前：

```python
query = 5
```

前三個都過期。

如果只使用：

```python
if
```

只會移除一個。

新的 Heap Top 可能仍然是失效的 interval。

因此必須持續 pop，直到：

```text
Heap 空了
```

或：

```text
Heap Top 仍然有效
```

---

## 16. 移除 Heap Top

```python
heapq.heappop(min_heap)
```

每次移除目前 Heap 中：

```python
size 最小
```

的 interval。

---

## 為什麼只檢查 Heap Top？

這是這題最容易困惑的地方。

Heap 中可能有其他已經過期的 interval。

例如：

```python
[
    (2,10),
    (5,3),
    (6,4)
]
```

目前：

```python
query = 5
```

其中：

```python
(5,3)
(6,4)
```

都已經過期。

但是 Heap Top 是：

```python
(2,10)
```

仍然有效。

這時不需要立刻刪除其他過期 interval。

因為答案只會從 Heap Top 取得。

只要 Heap Top 有效，它就是目前最短的有效 interval。

那些藏在下面的失效元素，等它們未來成為 Heap Top 時再刪除即可。

這種作法叫做：

```text
Lazy Deletion
```

中文可以理解為：

```text
延遲刪除
```

---

## Lazy Deletion 的核心

不是一發現元素失效就立即找出並刪除。

而是：

```text
只有當失效元素影響答案時，才刪除它。
```

Heap 不支援有效率地刪除任意位置元素。

如果每次都掃整個 Heap 找失效 interval：

```python
O(n)
```

就會變慢。

因此只清理 Heap Top。

---

## 17. 判斷是否存在有效 Interval

```python
if min_heap:
```

經過前面的移除後：

如果 Heap 仍然不空，

代表至少存在一個有效 interval。

因為：

* 所有 `left <= query` 的 interval 都已加入
* Heap Top 中 `right < query` 的都已移除

所以留下來的 Heap Top 一定包含 query。

---

## 18. 記錄答案

```python
answer[index] = min_heap[0][0]
```

`min_heap[0]` 是 Heap Top。

例如：

```python
min_heap[0] = (3,4)
```

其中：

```python
min_heap[0][0]
```

就是：

```python
size = 3
```

因此將最短 interval 的長度放回原始 query 的位置。

---

## 為什麼使用 `index`？

例如：

```python
queries = [5,2,4]
```

排序後先處理：

```python
query = 2
index = 1
```

假設答案是：

```python
3
```

就要寫入：

```python
answer[1] = 3
```

而不是直接 append。

否則答案會變成排序後 query 的順序。

---

## 19. 回傳 Answer

```python
return answer
```

所有 query 處理完畢後，

`answer` 已經按照原始 queries 順序排列。

---

## 🧪 Example Walkthrough

使用：

```python
intervals = [[1,4],[2,4],[3,6],[4,4]]

queries = [2,3,4,5]
```

---

### Step 0：排序

Intervals 排序後：

```python
[
    [1,4],
    [2,4],
    [3,6],
    [4,4]
]
```

Queries 加上 index：

```python
[
    (2,0),
    (3,1),
    (4,2),
    (5,3)
]
```

初始狀態：

```text
i = 0

heap = []

answer = [-1,-1,-1,-1]
```

---

## Query = 2

```text
query = 2
index = 0
```

---

### 加入 `[1,4]`

判斷：

```python
left = 1
```

因為：

```python
1 <= 2
```

所以加入。

區間長度：

```python
4 - 1 + 1 = 4
```

Heap Push：

```python
(4,4)
```

狀態：

```text
heap = [(4,4)]

i = 1
```

---

### 加入 `[2,4]`

判斷：

```python
2 <= 2
```

成立。

長度：

```python
4 - 2 + 1 = 3
```

Push：

```python
(3,4)
```

Heap 概念上：

```text
[(3,4), (4,4)]
```

狀態：

```text
i = 2
```

---

### 是否加入 `[3,6]`？

判斷：

```python
3 <= 2
```

不成立。

停止加入。

---

### 移除過期 Interval

Heap Top：

```python
(3,4)
```

right：

```python
4
```

判斷：

```python
4 < 2
```

不成立。

因此不需要移除。

---

### 取得答案

Heap Top：

```python
(3,4)
```

最短長度：

```python
3
```

放到：

```python
answer[0]
```

目前：

```python
answer = [3,-1,-1,-1]
```

---

## Query = 3

```text
query = 3
index = 1
```

目前：

```text
i = 2

heap = [(3,4),(4,4)]
```

---

### 加入 `[3,6]`

判斷：

```python
3 <= 3
```

成立。

長度：

```python
6 - 3 + 1 = 4
```

Push：

```python
(4,6)
```

Heap：

```text
[(3,4),(4,4),(4,6)]
```

Pointer：

```python
i = 3
```

---

### 是否加入 `[4,4]`？

判斷：

```python
4 <= 3
```

不成立。

停止。

---

### 清理過期 Interval

Heap Top：

```python
(3,4)
```

判斷：

```python
4 < 3
```

不成立。

---

### 取得答案

最短有效 interval：

```python
(3,4)
```

答案：

```python
3
```

寫入：

```python
answer[1] = 3
```

現在：

```python
answer = [3,3,-1,-1]
```

---

## Query = 4

```text
query = 4
index = 2
```

---

### 加入 `[4,4]`

判斷：

```python
4 <= 4
```

成立。

長度：

```python
4 - 4 + 1 = 1
```

Push：

```python
(1,4)
```

Heap 概念上：

```text
[
    (1,4),
    (3,4),
    (4,6),
    (4,4)
]
```

Pointer：

```python
i = 4
```

目前所有 intervals 都已經加入過。

---

### 清理過期 Interval

Heap Top：

```python
(1,4)
```

判斷：

```python
4 < 4
```

不成立。

注意：

```python
right == query
```

仍然有效。

---

### 取得答案

Heap Top size：

```python
1
```

寫入：

```python
answer[2] = 1
```

目前：

```python
answer = [3,3,1,-1]
```

---

## Query = 5

```text
query = 5
index = 3
```

此時：

```python
i = 4
```

沒有更多 interval 可加入。

Heap：

```text
[
    (1,4),
    (3,4),
    (4,6),
    (4,4)
]
```

---

## 第一次 Pop

Heap Top：

```python
(1,4)
```

判斷：

```python
4 < 5
```

成立。

移除：

```python
heapq.heappop(min_heap)
```

---

## 第二次檢查

新的 Heap Top 可能是：

```python
(3,4)
```

判斷：

```python
4 < 5
```

成立。

再次移除。

---

## 第三次檢查

Heap Top 可能是：

```python
(4,4)
```

判斷：

```python
4 < 5
```

成立。

再次移除。

---

## 第四次檢查

Heap Top：

```python
(4,6)
```

判斷：

```python
6 < 5
```

不成立。

停止移除。

---

## 取得答案

Heap Top：

```python
(4,6)
```

表示：

```text
size = 4
right = 6
```

答案：

```python
4
```

寫入：

```python
answer[3] = 4
```

最終：

```python
answer = [3,3,1,4]
```

---

# 📊 Heap 狀態總整理

| Query | 加入 Heap          | 移除 Heap                   | Heap Top | Answer |
| ----- | ---------------- | ------------------------- | -------- | -----: |
| 2     | `(4,4)`, `(3,4)` | 無                         | `(3,4)`  |      3 |
| 3     | `(4,6)`          | 無                         | `(3,4)`  |      3 |
| 4     | `(1,4)`          | 無                         | `(1,4)`  |      1 |
| 5     | 無                | `(1,4)`, `(3,4)`, `(4,4)` | `(4,6)`  |      4 |

---

# 📊 Pointer 變化

初始：

```text
i = 0
```

處理 query `2`：

```text
加入 [1,4]
i = 1

加入 [2,4]
i = 2
```

處理 query `3`：

```text
加入 [3,6]
i = 3
```

處理 query `4`：

```text
加入 [4,4]
i = 4
```

處理 query `5`：

```text
沒有新的 interval
i 仍然是 4
```

每個 interval 只被加入一次。

---

# 🤔 為什麼 Push 在 Pop 前面？

程式順序：

```python
while left <= query:
    push

while right < query:
    pop
```

先加入，再刪除。

---

## 原因

處理 query 時，必須先把所有：

```python
left <= query
```

的 interval 放入候選集合。

其中有些 interval 可能一加入就已經過期。

例如：

```python
interval = [1,2]
query = 5
```

它符合：

```python
left <= query
```

因此會加入。

但馬上發現：

```python
right < query
```

所以又被移除。

雖然看起來有點多餘，但整體仍然正確。

而且每個 interval 最多：

```text
Push 一次
Pop 一次
```

時間仍然是：

```python
O(n log n)
```

---

## 能不能先 Pop 再 Push？

理論上也可以設計其他流程。

但目前這種寫法最直觀：

```text
先收集所有已經開始的 interval
↓
再清理已經結束的 interval
↓
Heap Top 就是答案
```

---

# 🤔 為什麼 Heap 中可以留下過期元素？

因為 Heap 只保證：

```text
最小元素在最上面
```

不保證整個陣列完全排序。

我們只需要答案：

```python
min_heap[0]
```

所以只要保證 Heap Top 有效即可。

如果失效元素藏在下面：

```text
它目前不可能成為答案
```

不需要立刻處理。

未來它浮到 Heap Top 時，再移除。

---

# 🤔 為什麼 Query 必須排序？

如果不排序，例如：

```python
queries = [10,2]
```

先處理：

```python
query = 10
```

pointer 可能已經把所有：

```python
left <= 10
```

的 interval 加入。

接著處理：

```python
query = 2
```

但 pointer 不能倒退。

而且一些在 query `10` 時被判定過期、移除的 interval，

可能其實可以包含 query `2`。

所以 Sweep Line 必須保證：

```text
Query 單調遞增
```

因此一定要排序。

---

# 🤔 為什麼不能只排序 Intervals？

只排序 intervals 不夠。

如果每個 query 仍然按照原順序處理：

```python
[100,2,50,4]
```

pointer 和 Heap 狀態就無法單向維護。

所以：

```text
Intervals 排序
+
Queries 排序
```

兩者缺一不可。

---

# 🤔 為什麼不能用普通 Queue？

普通 Queue 的順序是：

```text
First In, First Out
```

但這題需要的不是最早加入的 interval。

而是：

```text
長度最小的 interval
```

所以需要：

```text
Priority Queue
```

也就是 Min Heap。

---

# 🤔 為什麼不能只用 Sort？

可以把符合 query 的 intervals 全部排序，

但每個 query 都重新排序會太慢。

Heap 的優勢：

```text
每次加入 O(log n)
每次移除 O(log n)
查看最小值 O(1)
```

很適合動態維護：

```text
目前候選區間中的最短區間
```

---

# 🧠 整體流程再整理一次

```text
1. Intervals 按照 Left 排序

2. Queries 排序並保留原始 Index

3. 使用 Pointer 掃描 Intervals

4. 對每個 Query：

   把所有 left <= query 的 interval 加入 Heap

5. Heap 存：

   (size, right)

6. 移除所有 Heap Top 中：

   right < query

7. 如果 Heap 不空：

   Heap Top 的 size 就是答案

8. 使用原始 Index 將答案放回正確位置
```
