# 📍 LeetCode 252 — Meeting Rooms

## 📄 題目說明 | Problem Description

### 中文

給定一組會議時間區間：

```python
intervals: List[Interval]
```

每一個 `Interval` 物件包含：

```python
interval.start
interval.end
```

分別代表：

```text
會議開始時間

會議結束時間
```

請判斷一個人是否可以參加所有會議。

如果任何兩場會議的時間重疊，就無法參加全部會議，回傳：

```python
False
```

如果所有會議都不重疊，回傳：

```python
True
```

---

### English

Given a list of meeting intervals, determine whether a person can attend all meetings.

If any two meetings overlap, return `False`.

Otherwise, return `True`.

---

### Example 1

```python
intervals = [(0, 30), (5, 10), (15, 20)]
```

Output：

```python
False
```

因為：

```text
(0, 30)

和

(5, 10)
```

時間重疊。

---

### Example 2

```python
intervals = [(5, 8), (9, 15)]
```

Output：

```python
True
```

因為第一場會議在 `8` 結束，第二場在 `9` 開始，沒有重疊。

---

## 🧠 核心觀念 | Key Insight

這題的核心做法是：

```text
按照開始時間排序

↓

比較相鄰會議是否重疊
```

---

### 為什麼要先排序？

假設原本的會議順序是：

```python
[(9, 15), (0, 5), (5, 8)]
```

如果直接按照原本順序比較，就無法正確判斷時間關係。

按照開始時間排序後：

```python
[(0, 5), (5, 8), (9, 15)]
```

所有會議會依照時間順序排列。

這時只需要比較：

```text
目前會議的開始時間

和

前一場會議的結束時間
```

---

### 為什麼只需要比較相鄰會議？

排序後，假設目前處理：

```python
intervals[i]
```

我們只需要檢查它是否和前一場：

```python
intervals[i - 1]
```

重疊。

因為前一場會議是目前會議之前，開始時間最接近它的會議。

如果目前會議沒有和前一場重疊，就不可能和更早的會議重疊。

例如：

```python
[(1, 3), (4, 6), (7, 9)]
```

處理 `(7, 9)` 時，只需要比較 `(4, 6)`。

因為 `(4, 6)` 都已經在 `7` 前結束，更早的 `(1, 3)` 當然也已經結束。

---

### 如何判斷重疊？

```python
intervals[i].start < intervals[i - 1].end
```

也就是：

```text
目前會議開始時間

小於

前一場會議結束時間
```

代表前一場還沒結束，目前會議就已經開始。

因此兩場會議重疊。

---

### 為什麼是 `<`，不是 `<=`？

假設：

```text
前一場：[1, 5]

目前這場：[5, 10]
```

目前會議開始時間：

```python
5
```

前一場結束時間：

```python
5
```

因為前一場剛好在目前會議開始時結束，所以可以連續參加。

因此：

```python
5 < 5
```

是 `False`，代表不重疊。

如果錯誤使用：

```python
5 <= 5
```

會被判斷為重疊。

所以這題必須使用：

```python
current.start < previous.end
```

---

## 💻 Code

```python
class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key=lambda interval: interval.start)

        for i in range(1, len(intervals)):
            if intervals[i].start < intervals[i - 1].end:
                return False

        return True
```

---

## 🧾 程式碼逐行解釋 | Line-by-line Explanation

```python
class Solution:
```

定義 LeetCode 使用的 `Solution` 類別。

---

```python
def canAttendMeetings(
    self,
    intervals: List[Interval]
) -> bool:
```

定義主要函式。

參數：

```python
intervals
```

是一組 `Interval` 物件。

每個物件包含：

```python
interval.start
interval.end
```

回傳：

```python
True
```

代表可以參加全部會議。

回傳：

```python
False
```

代表至少有兩場會議重疊。

---

```python
intervals.sort(
    key=lambda interval: interval.start
)
```

按照每一場會議的開始時間排序。

其中：

```python
lambda interval: interval.start
```

表示排序時使用：

```python
interval.start
```

作為比較依據。

例如：

```python
[(9, 15), (0, 5), (5, 8)]
```

排序後：

```python
[(0, 5), (5, 8), (9, 15)]
```

---

```python
for i in range(1, len(intervals)):
```

從 index `1` 開始遍歷。

原因是每一次都要比較：

```python
intervals[i]
```

和：

```python
intervals[i - 1]
```

如果從 `i = 0` 開始：

```python
intervals[i - 1]
```

會變成：

```python
intervals[-1]
```

也就是最後一場會議，不是我們想要的結果。

所以必須從：

```python
1
```

開始。

---

```python
if intervals[i].start < intervals[i - 1].end:
```

比較：

```text
目前會議的開始時間

與

前一場會議的結束時間
```

如果目前會議開始得太早，前一場會議還沒有結束，就表示重疊。

---

```python
return False
```

只要找到任何一組重疊的會議，就不可能參加全部會議。

因此可以立刻回傳：

```python
False
```

不需要繼續檢查。

---

```python
return True
```

如果整個迴圈都沒有找到重疊，代表所有會議都可以依序參加。

所以回傳：

```python
True
```

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

排序後：

```text
[0, 30]

[5, 10]

[15, 20]
```

---

### i = 1

目前會議：

```text
[5, 10]
```

前一場：

```text
[0, 30]
```

比較：

```python
5 < 30
```

成立。

代表 `[0, 30]` 還沒有結束時，`[5, 10]` 就開始了。

因此重疊：

```python
return False
```

---

## ⏱ Complexity Analysis

### Time Complexity

排序需要：

```text
O(n log n)
```

遍歷所有會議需要：

```text
O(n)
```

所以整體時間複雜度：

```text
O(n log n)
```

---

### Space Complexity

如果不計算 Python 排序所使用的空間：

```text
O(1)
```

如果考慮排序內部額外空間，可能是：

```text
O(n)
```

---

## 🎯 Interview Takeaways

* 先按照 `start` 排序。
* 排序後只需要比較相鄰會議。
* 重疊條件：

```python
current.start < previous.end
```

* 相等不算重疊：

```text
previous.end == current.start
```

表示可以接著參加下一場。

* 找到任何重疊就直接回傳 `False`。
* 迴圈從 `1` 開始，因為需要使用 `i - 1`。

---

## ✍️ 我學到的東西 | What I Learned

* Interval 題目通常先考慮排序。
* 這題按照開始時間排序。
* 排序後只需要檢查相鄰會議。
* `interval.start` 是開始時間。
* `interval.end` 是結束時間。
* `current.start < previous.end` 代表重疊。
* `current.start == previous.end` 不算重疊。
* 只要有一組重疊，就不能參加所有會議。
* 這題不需要 Heap，因為只要判斷有沒有重疊。

---

## 🏆 Cheat Sheet

```text
按照開始時間排序

↓

從第二場開始

↓

比較：

current.start
<
previous.end

↓

成立：

return False

↓

全部沒有重疊：

return True
```

核心程式：

```python
intervals.sort(
    key=lambda interval: interval.start
)

for i in range(1, len(intervals)):
    if (
        intervals[i].start
        < intervals[i - 1].end
    ):
        return False

return True
```

---

## 🌟 One Sentence Summary

> Sort meetings by start time and return `False` if any meeting starts before the previous meeting ends.

> 將所有會議依開始時間排序，如果任何一場會議在前一場結束前開始，就回傳 `False`。

---

## 📌 如果題目給的是普通 List

有些版本的題目不會提供 `Interval` 物件，而是直接給二維 List：

```python
intervals = [
    [0, 30],
    [5, 10],
    [15, 20]
]
```

每一個 interval 的格式是：

```python
[start, end]
```

所以：

```python
interval[0]
```

代表開始時間 `start`。

```python
interval[1]
```

代表結束時間 `end`。

這時可以寫成：

```python
class Solution:
    def canAttendMeetings(
        self,
        intervals: List[List[int]]
    ) -> bool:
        intervals.sort(
            key=lambda interval: interval[0]
        )

        for i in range(1, len(intervals)):
            if intervals[i][0] < intervals[i - 1][1]:
                return False

        return True
```

---

## 🧠 核心判斷

```python
current_start < previous_end
```

在程式中就是：

```python
intervals[i][0] < intervals[i - 1][1]
```

其中：

```python
intervals[i][0]
```

是目前會議的開始時間。

```python
intervals[i - 1][1]
```

是前一場會議的結束時間。

如果：

```python
current_start < previous_end
```

代表：

```text
前一場會議還沒有結束，

下一場會議就已經開始了。
```

所以兩場會議發生重疊，無法全部參加：

```python
return False
```

---

## 🧪 Example

```python
intervals = [
    [0, 30],
    [5, 10],
    [15, 20]
]
```

按照開始時間排序後：

```python
[
    [0, 30],
    [5, 10],
    [15, 20]
]
```

第一次迴圈：

```python
i = 1
```

目前會議：

```python
intervals[i] = [5, 10]
```

前一場會議：

```python
intervals[i - 1] = [0, 30]
```

取得目前會議的開始時間：

```python
intervals[i][0] = 5
```

取得前一場會議的結束時間：

```python
intervals[i - 1][1] = 30
```

比較：

```python
5 < 30
```

成立。

代表：

```text
前一場會議要到時間 30 才結束，

但是下一場會議在時間 5 就開始了。
```

因此兩場會議重疊：

```python
return False
```

---

## 🧪 沒有重疊的例子

```python
intervals = [
    [0, 5],
    [5, 10],
    [12, 15]
]
```

比較第一組相鄰會議：

```python
5 < 5
```

結果是：

```python
False
```

因為第一場在時間 `5` 結束，第二場也在時間 `5` 開始，可以直接接著參加。

再比較：

```python
12 < 10
```

結果也是：

```python
False
```

所有會議都沒有重疊，所以最後回傳：

```python
True
```

---

## 🔍 為什麼使用 `<`，不是 `<=`？

假設：

```python
previous = [0, 5]
current = [5, 10]
```

前一場會議結束時間：

```python
previous_end = 5
```

目前會議開始時間：

```python
current_start = 5
```

因為：

```python
current_start == previous_end
```

代表前一場剛好結束，下一場才開始，所以不算重疊。

正確判斷：

```python
current_start < previous_end
```

也就是：

```python
5 < 5
```

結果為 `False`，所以可以參加。

如果寫成：

```python
current_start <= previous_end
```

則：

```python
5 <= 5
```

會是 `True`，錯誤地把兩場可以連續參加的會議判斷成重疊。

---

## 🆚 Interval 物件與普通 List

### 題目提供 Interval 物件

```python
interval.start
interval.end
```

程式：

```python
class Solution:
    def canAttendMeetings(
        self,
        intervals: List[Interval]
    ) -> bool:
        intervals.sort(
            key=lambda interval: interval.start
        )

        for i in range(1, len(intervals)):
            if (
                intervals[i].start
                < intervals[i - 1].end
            ):
                return False

        return True
```

---

### 題目提供普通 List

```python
interval[0]
interval[1]
```

程式：

```python
class Solution:
    def canAttendMeetings(
        self,
        intervals: List[List[int]]
    ) -> bool:
        intervals.sort(
            key=lambda interval: interval[0]
        )

        for i in range(1, len(intervals)):
            if (
                intervals[i][0]
                < intervals[i - 1][1]
            ):
                return False

        return True
```

---

### 寫法比較

| 資料格式          | 開始時間             | 結束時間           |
| ------------- | ---------------- | -------------- |
| `Interval` 物件 | `interval.start` | `interval.end` |
| 普通 List       | `interval[0]`    | `interval[1]`  |

兩種寫法的演算法完全相同。

差別只在於：

```text
如何從 interval 中取得開始時間和結束時間
```

核心判斷都是：

```python
current_start < previous_end
```

---

## 🏆 Cheat Sheet

```text
普通 List：

[start, end]

interval[0] = start
interval[1] = end
```

排序：

```python
intervals.sort(
    key=lambda interval: interval[0]
)
```

檢查相鄰會議：

```python
for i in range(1, len(intervals)):
```

重疊條件：

```python
intervals[i][0] < intervals[i - 1][1]
```

意思：

```text
目前會議開始時間
<
前一場會議結束時間
```

成立代表：

```text
前一場還沒結束，

目前會議就開始了。
```

所以：

```python
return False
```

全部檢查完都沒有重疊：

```python
return True
```

---

## 🌟 One Sentence Summary

> Sort the meetings by start time, then check whether any meeting starts before the previous meeting ends.

> 將會議依開始時間排序，如果目前會議在前一場會議結束前就開始，代表時間重疊，回傳 `False`。

