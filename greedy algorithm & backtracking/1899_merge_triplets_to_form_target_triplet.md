# 📍 LeetCode 1899 - Merge Triplets to Form Target Triplet

**Difficulty:** Medium

**Topics:**

* Greedy
* Array
* Set
* Component-wise Maximum

---

# 📄 題目說明 | Problem Description

## 中文

給定一個二維陣列：

```python
triplets
```

其中每一個元素都是包含三個整數的三元組：

```python
triplets[i] = [ai, bi, ci]
```

另外給定目標三元組：

```python
target = [x, y, z]
```

我們可以選擇兩個 triplet：

```python
[a1, b1, c1]
[a2, b2, c2]
```

將它們合併成：

```python
[
    max(a1, a2),
    max(b1, b2),
    max(c1, c2)
]
```

也就是：

> 每一個位置都選擇兩個 triplet 中較大的值。

這個操作可以重複任意次。

題目要判斷：

> 能不能透過合併若干個 triplets，最後得到完全相同的 target？

---

## English

You are given a list of triplets and a target triplet.

You may merge two triplets by taking the maximum value at each corresponding position.

For example:

```python
[2,5,3]
[1,7,5]
```

合併後得到：

```python
[
    max(2,1),
    max(5,7),
    max(3,5)
]
```

結果：

```python
[2,7,5]
```

Return `True` if it is possible to obtain `target` by repeatedly merging triplets.

Otherwise, return `False`.

---

# 📚 Example 1

```python
triplets = [
    [2,5,3],
    [1,8,4],
    [1,7,5]
]

target = [2,7,5]
```

輸出：

```python
True
```

---

## 分析

第一個 triplet：

```python
[2,5,3]
```

能提供 target 的第一個位置：

```text
2 == target[0]
```

第三個 triplet：

```python
[1,7,5]
```

能提供：

```text
7 == target[1]
5 == target[2]
```

合併：

```python
[2,5,3]
[1,7,5]
```

得到：

```python
[
    max(2,1),
    max(5,7),
    max(3,5)
]
```

結果：

```python
[2,7,5]
```

等於 target。

因此回傳：

```python
True
```

---

# 📚 Example 2

```python
triplets = [
    [3,4,5],
    [4,5,6]
]

target = [3,2,5]
```

輸出：

```python
False
```

---

## 分析

第一個 triplet：

```python
[3,4,5]
```

第二個位置是：

```python
4
```

但 target 第二個位置只有：

```python
2
```

因為合併操作只能取最大值，所以一旦選擇這個 triplet：

```text
第二個位置至少會是 4
```

不可能再降低成 `2`。

第二個 triplet 也超過 target。

因此沒有任何可用的 triplet 可以組成 target。

---

# 📚 Example 3

```python
triplets = [
    [2,5,3],
    [2,3,4],
    [1,2,5],
    [5,2,3]
]

target = [2,5,5]
```

輸出：

```python
True
```

可使用：

```python
[2,5,3]
[1,2,5]
```

合併：

```python
[
    max(2,1),
    max(5,2),
    max(3,5)
]
```

得到：

```python
[2,5,5]
```

---

# 💻 Code

```python
class Solution:
    def mergeTriplets(
        self,
        triplets: List[List[int]],
        target: List[int]
    ) -> bool:

        good = set()

        for t in triplets:

            if (
                t[0] > target[0]
                or t[1] > target[1]
                or t[2] > target[2]
            ):
                continue

            for i, v in enumerate(t):

                if v == target[i]:
                    good.add(i)

        return len(good) == 3
```

---

# 🧠 核心觀念 | Key Insight

這題最重要的觀察是：

> 合併操作只會讓每一個位置的數值變大，永遠不會變小。

因為每次合併使用：

```python
max(...)
```

例如：

```python
max(3,5) = 5
```

結果只可能：

```text
維持原值或增加
```

不可能從：

```text
5 變回 3
```

---

# 🧠 哪些 Triplet 不能使用？

假設：

```python
target = [2,7,5]
```

有一個 triplet：

```python
[3,4,5]
```

它的第一個位置：

```python
3 > target[0]
```

也就是：

```python
3 > 2
```

如果使用這個 triplet，第一個位置至少會變成 `3`。

但是 target 第一個位置只需要 `2`。

因為合併只能使用最大值，之後不可能把 `3` 降回 `2`。

所以這個 triplet 一定不能選。

---

## 無效 Triplet 的條件

只要任一位置超過 target：

```python
t[0] > target[0]
```

或：

```python
t[1] > target[1]
```

或：

```python
t[2] > target[2]
```

這個 triplet 就不能使用。

因此直接：

```python
continue
```

跳過。

---

# 🧠 哪些 Triplet 可以使用？

如果某個 triplet 的三個位置全部都沒有超過 target：

```python
t[0] <= target[0]
t[1] <= target[1]
t[2] <= target[2]
```

那麼這個 triplet 是安全的。

例如：

```python
target = [2,7,5]
t = [2,5,3]
```

三個位置：

```text
2 <= 2
5 <= 7
3 <= 5
```

所以可以選擇。

它不會讓任何位置超過 target。

---

# 🧠 為什麼只需要找每個 Target 位置？

Target 有三個位置：

```text
index 0
index 1
index 2
```

例如：

```python
target = [2,7,5]
```

我們只需要確認：

```text
有沒有安全的 triplet 可以提供第一個位置的 2？

有沒有安全的 triplet 可以提供第二個位置的 7？

有沒有安全的 triplet 可以提供第三個位置的 5？
```

只要三個位置都能被某些安全 triplets 提供，就可以把它們全部合併。

---

## 為什麼可以來自不同 Triplet？

例如：

```python
target = [2,7,5]
```

有：

```python
[2,5,3]
[1,7,4]
[1,3,5]
```

第一個位置由：

```python
[2,5,3]
```

提供。

第二個位置由：

```python
[1,7,4]
```

提供。

第三個位置由：

```python
[1,3,5]
```

提供。

將三者合併：

```python
[
    max(2,1,1),
    max(5,7,3),
    max(3,4,5)
]
```

得到：

```python
[2,7,5]
```

因此不需要某一個 triplet 完全等於 target。

只需要不同 triplets 合作提供三個位置。

---

# 🧠 Set `good` 存什麼？

```python
good = set()
```

`good` 記錄：

> target 的哪些位置已經可以被安全的 triplet 提供。

可能加入的值只有：

```python
0
1
2
```

例如：

```python
good = {0, 2}
```

表示：

```text
target[0] 已經找到
target[2] 已經找到
target[1] 尚未找到
```

當：

```python
good = {0,1,2}
```

代表 target 的三個位置都已找到。

因此可以回傳：

```python
True
```

---

# 🧠 為什麼使用 Set？

因為同一個位置可能被很多 triplets 重複提供。

例如：

```python
target = [2,7,5]
```

以下 triplets 都有第一個位置 `2`：

```python
[2,1,1]
[2,3,4]
[2,7,2]
```

每次都會執行：

```python
good.add(0)
```

但是 Set 不會保存重複值。

最後仍然只是：

```python
good = {0}
```

這正是我們需要的結果。

我們只在意：

```text
這個位置有沒有被找到
```

不在意找到幾次。

---

# 🧾 程式碼逐行解釋 | Line-by-line Explanation

---

## 建立 Solution Class

```python
class Solution:
```

LeetCode 固定要求將解法放在：

```python
class Solution
```

裡面。

---

## 定義函式

```python
def mergeTriplets(
    self,
    triplets: List[List[int]],
    target: List[int]
) -> bool:
```

輸入：

```python
triplets
```

是一組三元組。

例如：

```python
[
    [2,5,3],
    [1,8,4],
    [1,7,5]
]
```

輸入：

```python
target
```

是想要形成的目標三元組。

例如：

```python
[2,7,5]
```

函式最後回傳：

```python
True
```

或：

```python
False
```

---

# 建立 Good Set

```python
good = set()
```

建立一個空 Set。

一開始：

```python
good = set()
```

代表 target 的三個位置都尚未找到。

---

## Good 中可能保存哪些值？

因為每個 triplet 只有三個位置，所以 index 只有：

```python
0
1
2
```

因此 `good` 可能是：

```python
set()
```

或：

```python
{0}
```

或：

```python
{0,2}
```

或：

```python
{0,1,2}
```

---

# 逐一檢查每個 Triplet

```python
for t in triplets:
```

例如：

```python
triplets = [
    [2,5,3],
    [1,8,4],
    [1,7,5]
]
```

迴圈會依序取得：

```python
t = [2,5,3]
```

接著：

```python
t = [1,8,4]
```

最後：

```python
t = [1,7,5]
```

---

# 判斷 Triplet 是否超過 Target

```python
if (
    t[0] > target[0]
    or t[1] > target[1]
    or t[2] > target[2]
):
```

這個判斷檢查：

> 是否有任何一個位置超過 target。

---

## 第一個條件

```python
t[0] > target[0]
```

檢查 triplet 的第一個位置是否過大。

例如：

```python
t = [3,4,2]
target = [2,7,5]
```

因為：

```python
3 > 2
```

所以這個 triplet 不能使用。

---

## 第二個條件

```python
t[1] > target[1]
```

檢查第二個位置是否過大。

例如：

```python
t = [1,8,4]
target = [2,7,5]
```

因為：

```python
8 > 7
```

所以不能使用。

---

## 第三個條件

```python
t[2] > target[2]
```

檢查第三個位置是否過大。

例如：

```python
t = [1,4,6]
target = [2,7,5]
```

因為：

```python
6 > 5
```

所以不能使用。

---

## 為什麼使用 `or`？

只要其中任何一個位置超過 target，整個 triplet 就不能使用。

因此使用：

```python
or
```

例如：

```python
False or True or False
```

整體結果是：

```python
True
```

代表至少有一個位置不合法。

---

## 為什麼不是 `and`？

如果寫成：

```python
t[0] > target[0]
and t[1] > target[1]
and t[2] > target[2]
```

就會要求三個位置都超過 target 才跳過。

這是錯的。

例如：

```python
t = [2,100,5]
target = [2,7,5]
```

只有第二個位置超過 target。

但只要選擇它，第二個位置就會變成 `100`，不可能回到 `7`。

所以只要一個位置超過就必須跳過。

---

# 跳過不合法的 Triplet

```python
continue
```

`continue` 表示：

> 停止目前這一次迴圈，直接處理下一個 triplet。

例如：

```python
t = [1,8,4]
target = [2,7,5]
```

因為：

```python
8 > 7
```

執行：

```python
continue
```

不會再檢查這個 triplet 是否有任何位置等於 target。

---

## 為什麼不能只忽略超過的那個位置？

例如：

```python
t = [2,100,5]
target = [2,7,5]
```

這個 triplet 的第一個位置等於 target：

```python
2 == 2
```

第三個位置也等於 target：

```python
5 == 5
```

但不能因此把 index `0` 和 `2` 加入 good。

因為只要選擇這個 triplet：

```text
第二個位置就會變成 100
```

整體永遠無法等於 target。

所以整個 triplet 必須完全跳過。

---

# 檢查安全 Triplet 的每個位置

```python
for i, v in enumerate(t):
```

`enumerate(t)` 同時提供：

```text
index
value
```

例如：

```python
t = [2,5,3]
```

會依序得到：

```text
i = 0, v = 2
i = 1, v = 5
i = 2, v = 3
```

---

## 為什麼需要 Index？

因為需要比較相同位置：

```python
v == target[i]
```

例如：

```text
t[0] 和 target[0] 比較
t[1] 和 target[1] 比較
t[2] 和 target[2] 比較
```

---

## 如果不使用 enumerate

可以寫成：

```python
for i in range(3):
    if t[i] == target[i]:
        good.add(i)
```

兩種方式都可以。

這份程式使用：

```python
enumerate(t)
```

可以同時取得位置與數值。

---

# 判斷是否能提供 Target 位置

```python
if v == target[i]:
```

如果目前 triplet 在第 `i` 個位置的值，剛好等於 target 同一位置：

```python
v == target[i]
```

就代表這個 triplet 可以提供 target 的第 `i` 個位置。

---

## Example

```python
t = [2,5,3]
target = [2,7,5]
```

---

### Index 0

```python
v = 2
target[0] = 2
```

因為：

```python
2 == 2
```

所以 index `0` 可以被提供。

---

### Index 1

```python
v = 5
target[1] = 7
```

因為：

```python
5 != 7
```

所以不能提供 index `1`。

---

### Index 2

```python
v = 3
target[2] = 5
```

因為：

```python
3 != 5
```

所以不能提供 index `2`。

---

# 將位置加入 Good

```python
good.add(i)
```

假設：

```python
i = 0
```

則：

```python
good.add(0)
```

如果原本：

```python
good = set()
```

現在變成：

```python
good = {0}
```

---

## 如果重複加入呢？

例如另一個 triplet 也可以提供 index `0`：

```python
good.add(0)
```

Set 不會出現重複值。

仍然是：

```python
good = {0}
```

---

# 判斷三個位置是否都找到

```python
return len(good) == 3
```

如果：

```python
good = {0,1,2}
```

則：

```python
len(good) = 3
```

所以：

```python
len(good) == 3
```

結果為：

```python
True
```

---

如果：

```python
good = {0,2}
```

則：

```python
len(good) = 2
```

結果：

```python
False
```

代表第二個位置無法被任何安全 triplet 提供。

---

## 為什麼只檢查長度就可以？

因為 `good` 中只可能加入：

```python
0
1
2
```

不可能出現其他 index。

所以當長度等於 `3` 時，必定是：

```python
{0,1,2}
```

---

# 🧪 Example Walkthrough

使用：

```python
triplets = [
    [2,5,3],
    [1,8,4],
    [1,7,5]
]

target = [2,7,5]
```

---

## 初始狀態

```python
good = set()
```

---

# 第一個 Triplet

```python
t = [2,5,3]
```

---

## 是否有位置超過 Target？

比較：

```text
2 > 2？False
5 > 7？False
3 > 5？False
```

沒有任何位置超過 target。

所以這個 triplet 是安全的。

---

## 檢查每個位置

### Index 0

```python
2 == target[0]
```

也就是：

```python
2 == 2
```

成立。

加入：

```python
good.add(0)
```

現在：

```python
good = {0}
```

---

### Index 1

```python
5 == target[1]
```

也就是：

```python
5 == 7
```

不成立。

---

### Index 2

```python
3 == target[2]
```

也就是：

```python
3 == 5
```

不成立。

---

# 第二個 Triplet

```python
t = [1,8,4]
```

---

## 是否有位置超過 Target？

比較：

```text
1 > 2？False
8 > 7？True
4 > 5？False
```

第二個位置超過 target。

所以：

```python
continue
```

整個 triplet 被跳過。

即使它的其他位置可能有用，也不能選。

`good` 不變：

```python
good = {0}
```

---

# 第三個 Triplet

```python
t = [1,7,5]
```

---

## 是否有位置超過 Target？

比較：

```text
1 > 2？False
7 > 7？False
5 > 5？False
```

安全。

---

## 檢查每個位置

### Index 0

```python
1 == 2
```

不成立。

---

### Index 1

```python
7 == 7
```

成立。

加入：

```python
good.add(1)
```

目前：

```python
good = {0,1}
```

---

### Index 2

```python
5 == 5
```

成立。

加入：

```python
good.add(2)
```

目前：

```python
good = {0,1,2}
```

---

# 最後判斷

```python
len(good) == 3
```

因為：

```python
len({0,1,2}) = 3
```

回傳：

```python
True
```

---

# 📊 Good Set 變化

| Triplet   | 是否安全      | 提供的 Target 位置 | Good      |
| --------- | --------- | ------------- | --------- |
| `[2,5,3]` | 是         | `0`           | `{0}`     |
| `[1,8,4]` | 否，`8 > 7` | 無             | `{0}`     |
| `[1,7,5]` | 是         | `1,2`         | `{0,1,2}` |

最終：

```python
len(good) == 3
```

所以答案為：

```python
True
```

---

# 🧪 Failure Walkthrough

```python
triplets = [
    [2,3,4],
    [1,5,4],
    [2,4,3]
]

target = [2,5,5]
```

---

## 第一個 Triplet

```python
[2,3,4]
```

安全。

可以提供：

```text
index 0
```

所以：

```python
good = {0}
```

---

## 第二個 Triplet

```python
[1,5,4]
```

安全。

可以提供：

```text
index 1
```

所以：

```python
good = {0,1}
```

---

## 第三個 Triplet

```python
[2,4,3]
```

安全。

只能再次提供：

```text
index 0
```

Set 不變：

```python
good = {0,1}
```

---

## 最終

沒有任何安全 triplet 的第三個位置等於：

```python
target[2] = 5
```

因此：

```python
len(good) = 2
```

回傳：

```python
False
```

---

# 🤔 為什麼這是 Greedy？

這題的 Greedy 選擇是：

> 所有不超過 target 的 triplets 都可以安全地選擇。

我們不需要真的決定要選哪些 triplets。

只要確認：

```text
每個 target 位置是否至少有一個安全 triplet 能提供
```

即可。

因為所有安全 triplets 合併後，每個位置都不會超過 target。

而只要每一個位置至少有一個值等於 target，最終每個位置的最大值就會剛好等於 target。

---

# 🧠 正確性的推導

假設 target：

```python
[x, y, z]
```

所有選擇的 triplets 都必須滿足：

```text
第一個值 <= x
第二個值 <= y
第三個值 <= z
```

所以合併後：

```text
第一個位置不可能超過 x
第二個位置不可能超過 y
第三個位置不可能超過 z
```

接著，如果存在安全 triplet 提供：

```text
第一個位置 = x
```

那麼合併後第一個位置的最大值就是：

```text
x
```

同理，如果第二、第三個位置也分別有人提供：

```text
y 和 z
```

最終結果就是：

```python
[x,y,z]
```

---

# 🤔 為什麼不需要真的執行 Merge？

最直覺的方式可能是建立：

```python
current = [0,0,0]
```

然後將安全的 triplets 全部合併：

```python
current[0] = max(current[0], t[0])
current[1] = max(current[1], t[1])
current[2] = max(current[2], t[2])
```

最後比較：

```python
current == target
```

這種寫法也正確。

但是這份程式使用 Set：

```python
good
```

只記錄哪些位置已經達到 target。

因為我們不需要知道中間具體最大值，只需要知道：

```text
三個位置是否都能達到目標值
```

---

# 🆚 Set 解法 vs Merge Array 解法

## Set 解法

```python
good = set()

for t in triplets:
    if any value exceeds target:
        continue

    for i, v in enumerate(t):
        if v == target[i]:
            good.add(i)

return len(good) == 3
```

優點：

```text
直接記錄哪些位置已完成
```

---

## Merge Array 解法

```python
merged = [0,0,0]

for t in triplets:
    if t[0] > target[0] or t[1] > target[1] or t[2] > target[2]:
        continue

    for i in range(3):
        merged[i] = max(merged[i], t[i])

return merged == target
```

優點：

```text
更直接模擬題目中的 merge 操作
```

兩種方法的核心觀念相同。

---

# 🤔 為什麼不能只找某個 Triplet 等於 Target？

錯誤想法：

```python
if target in triplets:
    return True
```

題目允許合併多個 triplets。

例如：

```python
triplets = [
    [2,5,3],
    [1,7,5]
]

target = [2,7,5]
```

沒有任何單一 triplet 等於：

```python
[2,7,5]
```

但合併後可以得到 target。

因此不能只找完全相同的 triplet。

---

# 🤔 為什麼不能使用超過 Target 的 Triplet？

例如：

```python
target = [2,7,5]
t = [2,8,5]
```

看起來它可以提供第一和第三個位置。

但一旦合併：

```text
第二個位置至少是 8
```

而 target 第二個位置只有 `7`。

因為 max 操作不可逆，所以不能使用。

---

# 🤔 為什麼小於 Target 的值沒關係？

例如：

```python
target = [2,7,5]
t = [2,3,1]
```

第二和第三個位置小於 target。

這沒有問題。

因為其他 triplet 可以提供更大的合法值：

```python
[1,7,5]
```

合併後：

```python
[
    max(2,1),
    max(3,7),
    max(1,5)
]
```

結果：

```python
[2,7,5]
```

所以小於 target 是安全的。

只有大於 target 才是不可接受的。

---

# 🤔 為什麼 Good 記 Index，不記 Value？

可以保存：

```python
good.add(target[i])
```

但如果 target 中有重複數字，就會有問題。

例如：

```python
target = [2,2,2]
```

如果保存 value：

```python
good = {2}
```

Set 長度只有 `1`。

無法知道三個不同位置都已完成。

因此必須保存：

```python
index
```

也就是：

```python
0
1
2
```

---

# ⚠️ 常見錯誤 | Common Mistakes

---

## 錯誤一：沒有過濾超過 Target 的 Triplet

錯誤：

```python
for t in triplets:
    for i, v in enumerate(t):
        if v == target[i]:
            good.add(i)
```

例如：

```python
t = [2,100,5]
target = [2,7,5]
```

這段會加入：

```python
0
2
```

但這個 triplet 根本不能使用，因為第二個位置會超過 target。

所以一定要先完整檢查 triplet 是否安全。

---

## 錯誤二：使用 `and` 判斷超過 Target

錯誤：

```python
if (
    t[0] > target[0]
    and t[1] > target[1]
    and t[2] > target[2]
):
    continue
```

這只會排除三個位置都超過的 triplet。

正確是：

```python
or
```

只要一個位置超過，就不能選。

---

## 錯誤三：Good 保存 Target Value

錯誤：

```python
good.add(v)
```

若 target 有重複值，就無法區分位置。

正確：

```python
good.add(i)
```

---

## 錯誤四：要求同一個 Triplet 提供三個位置

題目允許合併不同 triplets。

所以不需要找到：

```python
t == target
```

只需不同安全 triplets 一起提供三個位置。

---

## 錯誤五：看到小於 Target 就跳過

小於 target 是合法的。

例如：

```python
t = [1,7,3]
target = [2,7,5]
```

它仍然可以提供 index `1`。

所以只有：

```python
>
```

才是非法。

不是：

```python
<
```

---

## 錯誤六：使用 `>=` 過濾

錯誤：

```python
if t[0] >= target[0]:
    continue
```

如果：

```python
t[0] == target[0]
```

這正是我們需要的值。

所以不能跳過。

正確只檢查：

```python
t[0] > target[0]
```

---

# ⏱ Complexity Analysis

假設：

```text
n = triplets 的數量
```

每個 triplet 固定只有三個值。

---

## 外層迴圈

```python
for t in triplets:
```

總共處理 `n` 個 triplets。

時間：

```text
O(n)
```

---

## 內層迴圈

```python
for i, v in enumerate(t):
```

每個 triplet 固定只有三個元素。

因此每次：

```text
O(3)
```

常數可以忽略。

---

## 總時間複雜度

```text
O(n)
```

---

# 💾 Space Complexity

`good` 最多保存：

```python
{0,1,2}
```

只有三個元素。

因此額外空間：

```text
O(1)
```

---

# 🆚 1899 vs 56 Merge Intervals

雖然題目名稱都有：

```text
Merge
```

但兩題完全不同。

---

## LeetCode 56

合併重疊區間：

```python
[1,3]
[2,6]
```

變成：

```python
[1,6]
```

核心：

```text
Sorting + Interval Overlap
```

---

## LeetCode 1899

合併三元組時，每個位置各自取最大值：

```python
[2,5,3]
[1,7,5]
```

變成：

```python
[2,7,5]
```

核心：

```text
Greedy + Component-wise Maximum
```

---

# 🆚 1899 vs 846 Hand of Straights

## 846

需要：

```text
Count + Min Heap + Greedy
```

因為要反覆取得目前最小牌並建立連續群組。

---

## 1899

不需要 Heap，也不需要排序。

只要線性掃描所有 triplets：

```text
排除不安全 triplets
+
記錄能提供哪些 target positions
```

---

# 🎯 Interview Takeaways

看到以下關鍵字：

```text
操作是逐位置取 Max
+
目標值不能被超過
+
可以選擇多個元素合併
```

要想到：

```text
先排除任何位置超過 Target 的候選
```

接著確認：

```text
每一個 Target 位置是否有人能剛好提供
```

---

## 面試時可以這樣說

```text
The merge operation only increases each coordinate because it takes a component-wise maximum.

Therefore, any triplet containing a value greater than the corresponding target value can never be used.

For every valid triplet, I check which coordinates exactly match the target and record those coordinate indices in a set.

If all three coordinates can be supplied by valid triplets, merging those triplets will produce exactly the target.
```

---

# 🗣 Interview English Version

```text
The key observation is that the merge operation is irreversible because each coordinate can only stay the same or increase.

Therefore, I discard any triplet that exceeds the target in at least one coordinate.

For every remaining triplet, I record the coordinates where its value equals the target value.

If I can cover all three coordinate indices, then merging those valid triplets produces the target exactly.
```

---

# ✍️ What I Learned

## 1. Max 操作是不可逆的

一旦某個位置超過 target，就無法降低。

因此任何位置超過 target 的 triplet 都不能使用。

---

## 2. 不需要真的模擬所有 Merge

只需要確認 target 的三個位置是否都能由安全 triplet 提供。

---

## 3. 不同位置可以來自不同 Triplets

不用找到單一 triplet 完全等於 target。

---

## 4. Set 很適合記錄完成狀態

只需要記錄：

```text
index 0 是否完成
index 1 是否完成
index 2 是否完成
```

Set 可以自動避免重複。

---

## 5. 必須記 Index，而不是 Value

Target 可能有重複值。

Index 才能代表不同位置。

---

# 🏆 Cheat Sheet

## 初始化

```python
good = set()
```

記錄已經能達成的 target 位置。

---

## 掃描 Triplets

```python
for t in triplets:
```

---

## 排除不合法 Triplet

```python
if (
    t[0] > target[0]
    or t[1] > target[1]
    or t[2] > target[2]
):
    continue
```

任何位置超過 target，整個 triplet 都不能使用。

---

## 找出能提供的 Target 位置

```python
for i, v in enumerate(t):
    if v == target[i]:
        good.add(i)
```

---

## 判斷是否三個位置都完成

```python
return len(good) == 3
```

---

# 🧭 解題流程圖

```text
建立 good Set
      |
      v
逐一檢查每個 Triplet
      |
      v
是否有任一位置 > Target？
      |
   +--+--+
   |     |
  是     否
   |     |
跳過     v
      檢查三個位置
            |
            v
      t[i] == target[i]？
          /        \
        否          是
        |           |
      繼續      good.add(i)
                    |
                    v
             所有 Triplets 結束
                    |
                    v
             len(good) == 3？
                /        \
              否          是
              |           |
           False        True
```

---

# 🔑 Pattern Recognition

看到：

```text
每個位置獨立做 Max
```

先想：

```text
有沒有候選值超過 Target？
```

如果有：

```text
該候選永久不能使用
```

再想：

```text
每個 Target 位置是否都能被某個合法候選達成？
```

完整 Pattern：

```text
Filter Invalid Candidates
+
Track Target Coordinates
+
Greedy
```

---

# 🌟 One Sentence Summary

## English

> Ignore every triplet that exceeds the target in any coordinate, then check whether the remaining triplets can collectively match all three target coordinates.

## 中文

> 排除任何位置超過 target 的 triplet，再確認剩餘的安全 triplets 是否能共同提供 target 的三個位置。

---

# ✅ Final Takeaway

這題最重要的核心觀念是：

```text
Max 只能增加，不能減少。
```

所以解題流程是：

```text
1. 排除任何位置超過 Target 的 Triplet

2. 對安全的 Triplet，找出哪些位置剛好等於 Target

3. 用 Set 記錄已經找到的位置

4. 三個位置都找到就回傳 True
```

最精簡記法：

```text
不能超過 Target

+

每一格都要有人達到 Target
```
