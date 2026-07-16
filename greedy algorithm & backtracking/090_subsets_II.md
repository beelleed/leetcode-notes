# 📍 LeetCode 90 — Subsets II

🔗 https://leetcode.com/problems/subsets-ii/

---

## 📄 題目說明 | Problem Description

### 中文

* 給定一個可能包含重複元素的整數陣列 `nums`。
* 回傳所有可能的子集合（Subsets）。
* **不能有重複的子集合。**

### English

* Given an integer array `nums` that may contain duplicates.
* Return all possible subsets.
* The solution set must not contain duplicate subsets.

### Examples

#### Example 1

Input

```python
nums = [1,2,2]
```

Output

```text
[
 [],
 [1],
 [2],
 [1,2],
 [2,2],
 [1,2,2]
]
```

不能出現：

```text
[
 [1,2],
 [1,2]
]
```

因為：

```text
Duplicate Subsets
```

---

#### Example 2

Input

```python
nums = [0]
```

Output

```text
[
 [],
 [0]
]
```

---

## 🧠 核心觀念 | Key Insight

### 這題和 LeetCode 78 的差別

* LeetCode 78 的 `nums` 沒有重複元素。
* LeetCode 90 的 `nums` 可能有重複元素。
* 因此除了產生所有 Subsets 之外，還要避免產生重複答案。

---

### 第一步一定要排序

```python
nums.sort()
```

例如：

```python
nums = [2,1,2]
```

排序後：

```python
[1,2,2]
```

排序的目的：

```text
把相同元素放在一起
```

這樣才能判斷：

```python
nums[i] == nums[i-1]
```

並跳過重複元素。

---

### Backtracking 的想法

每一次遞迴代表：

```text
目前已經選好了一部分數字
```

例如：

```text
[]

↓

[1]

↓

[1,2]

↓

[1,2,2]
```

每一層都可以：

```text
選下一個數字
```

並繼續往下搜尋。

---

### path 是什麼？

在你的寫法中：

```python
def backtrack(start, path):
```

* `start`：下一個可以開始選的位置。
* `path`：目前已經選好的 Subset。

例如：

```text
path = []
```

代表：

```text
目前還沒有選任何數字
```

下一步：

```python
path.append(1)
```

變成：

```text
path = [1]
```

再下一步：

```python
path.append(2)
```

變成：

```text
path = [1,2]
```

因此：

```text
path 永遠代表目前正在建立的答案
```

---

### 為什麼每一層都不用建立新的 path？

很多人會以為：

```python
backtrack(i + 1, path)
```

代表：

```text
建立新的 path
```

其實不是。

它只是把：

```text
同一個 path
```

傳給下一層。

例如：

```text
[]

↓

append(1)

↓

[1]

↓

append(2)

↓

[1,2]
```

下一層看到的仍然是：

```text
同一個 list
```

因此回來時一定要：

```python
path.pop()
```

把剛剛加入的數字移除。

這就是：

```text
Backtracking（回溯）
```

---

## 💻 Code

```python
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:

        nums.sort()

        res = []

        def backtrack(start, path):

            res.append(path[:])

            for i in range(start, len(nums)):

                if i > start and nums[i] == nums[i - 1]:
                    continue

                path.append(nums[i])

                backtrack(i + 1, path)

                path.pop()

        backtrack(0, [])

        return res
```

## 🧾 程式碼逐行解釋 | Line-by-line Explanation

```python
nums.sort()
```

* 先將陣列排序。
* 排序後，相同的數字會排在一起。
* 這樣後面才能判斷：

```python
nums[i] == nums[i - 1]
```

例如：

排序前：

```python
[2,1,2]
```

排序後：

```python
[1,2,2]
```

---

```python
res = []
```

* 用來存放所有答案。

例如：

```text
[
 [],
 [1],
 [1,2]
]
```

最後都會存在：

```python
res
```

裡面。

---

```python
def backtrack(start, path):
```

* 建立 Backtracking 函式。
* `start`：下一個可以開始選的位置。
* `path`：目前已經選好的 Subset。

例如：

```text
nums = [1,2,2]
```

可能某一次：

```python
start = 2

path = [1]
```

代表：

```text
目前已經選了 1

接下來只能從 index = 2 開始選
```

---

```python
res.append(path[:])
```

* 每到一個新的遞迴，就代表找到一個新的 Subset。
* 所以先把目前的 `path` 加入答案。

注意：

一定要：

```python
path[:]
```

不能直接：

```python
res.append(path)
```

因為：

```text
path 是同一個 list
```

後面：

```python
path.append(...)
```

或：

```python
path.pop()
```

都會修改它。

所以：

```python
path[:]
```

會建立一份新的 copy。

例如：

目前：

```python
path = [1,2]
```

加入：

```python
res.append(path[:])
```

得到：

```text
[
 [1,2]
]
```

之後：

```python
path.pop()
```

變成：

```python
path = [1]
```

但是：

```text
res

仍然是

[
 [1,2]
]
```

不會被影響。

---

```python
for i in range(start, len(nums)):
```

* 從 `start` 開始選下一個數字。
* 不能回頭選前面的數字。

例如：

```python
nums = [1,2,3]
```

如果：

```python
start = 1
```

代表：

只能選：

```text
2

3
```

不能再選：

```text
1
```

---

```python
if i > start and nums[i] == nums[i - 1]:
    continue
```

* 本題最重要的一行。
* 用來避免產生重複的 Subset。

如果：

```python
nums[i]
```

和：

```python
nums[i-1]
```

相同。

而且：

```python
i > start
```

代表：

```text
同一層

前面已經選過相同數字了
```

因此：

```python
continue
```

直接跳過。

---

例如：

```python
nums = [1,2,2]
```

第一層：

```text
選第一個 2
```

會得到：

```text
[2]
```

如果：

又選第二個 2。

也會得到：

```text
[2]
```

完全重複。

因此：

```text
第二個 2

跳過
```

---

為什麼一定是：

```python
i > start
```

而不是：

```python
i > 0
```

因為：

```text
只跳過

同一層

重複元素
```

不是：

```text
所有重複元素
```

例如：

```python
nums = [2,2]
```

答案應該包含：

```text
[]

[2]

[2,2]
```

所以：

第二層的：

```text
第二個 2
```

不能跳。

---

```python
path.append(nums[i])
```

* 把目前選擇的數字加入 Subset。

例如：

原本：

```python
path = [1]
```

加入：

```python
2
```

變成：

```python
path = [1,2]
```

---

```python
backtrack(i + 1, path)
```

* 繼續往下一層搜尋。
* 下一層只能從：

```python
i + 1
```

開始。

因為：

每個數字只能選一次。

注意：

```python
backtrack(i + 1, path)
```

不是建立新的 `path`。

而是：

```text
把同一個 path

傳給下一層
```

例如：

第一層：

```python
path = [1]
```

第二層收到的也是：

```python
path = [1]
```

不是新的 list。

---

```python
path.pop()
```

* Backtracking 最重要的一步。
* 把剛剛加入的數字移除。
* 恢復到遞迴前的狀態。

例如：

加入前：

```python
path = [1]
```

加入：

```python
path.append(2)
```

變成：

```python
path = [1,2]
```

遞迴結束後：

```python
path.pop()
```

恢復：

```python
path = [1]
```

這樣才能繼續嘗試：

```text
其他選擇
```

例如：

```text
[1]

↓

[1,2]

↓

回復

↓

[1]

↓

[1,3]
```

這就是：

```text
Backtracking（回溯）
```

---

```python
backtrack(0, [])
```

* 開始遞迴。
* 一開始：

```python
start = 0

path = []
```

代表：

```text
還沒有選任何數字
```

從第一個數字開始搜尋。

---

```python
return res
```

* 回傳所有 Subsets。

例如：

```text
[
 [],
 [1],
 [2],
 [1,2],
 [2,2],
 [1,2,2]
]
```
---

## 🧪 Example Walkthrough

### Example 1

Input

```python
nums = [1,2,2]
```

---

### Step 1：排序

```python
nums.sort()
```

排序後：

```python
[1,2,2]
```

目前：

```text
res = []

path = []

start = 0
```

開始：

```python
backtrack(0, [])
```

---

### Step 2：第一層（start = 0）

目前：

```text
path = []
```

先加入答案：

```python
res.append(path[:])
```

得到：

```text
res = [
    []
]
```

開始迴圈：

```python
for i in range(0,3)
```

也就是：

```text
i = 0

i = 1

i = 2
```

---

### Step 3：選 nums[0] = 1

加入：

```python
path.append(1)
```

變成：

```text
path = [1]
```

呼叫：

```python
backtrack(1, [1])
```

---

### Step 4：第二層（start = 1）

目前：

```text
path = [1]
```

加入答案：

```text
res

[
 [],
 [1]
]
```

開始：

```python
for i in range(1,3)
```

也就是：

```text
i = 1

i = 2
```

---

### Step 5：選 nums[1] = 2

加入：

```python
path.append(2)
```

目前：

```text
path = [1,2]
```

呼叫：

```python
backtrack(2, [1,2])
```

---

### Step 6：第三層（start = 2）

加入答案：

```text
res

[
 [],
 [1],
 [1,2]
]
```

開始：

```python
for i in range(2,3)
```

只有：

```text
i = 2
```

---

### Step 7：選 nums[2] = 2

加入：

```python
path.append(2)
```

目前：

```text
path = [1,2,2]
```

呼叫：

```python
backtrack(3, [1,2,2])
```

---

### Step 8：第四層

加入答案：

```text
res

[
 [],
 [1],
 [1,2],
 [1,2,2]
]
```

現在：

```python
start = 3
```

因此：

```python
range(3,3)
```

沒有任何數字可以選。

回上一層。

---

### Step 9：開始 Backtracking

回來後：

```python
path.pop()
```

原本：

```text
path = [1,2,2]
```

變成：

```text
path = [1,2]
```

第三層結束。

再回上一層。

再次：

```python
path.pop()
```

變成：

```text
path = [1]
```

---

### Step 10：第二層繼續

現在：

```text
path = [1]
```

下一個：

```text
i = 2
```

判斷：

```python
if i > start and nums[i] == nums[i-1]
```

也就是：

```python
2 > 1

True
```

而且：

```python
nums[2] == nums[1]

2 == 2
```

成立。

因此：

```python
continue
```

跳過。

---

### 為什麼這裡要跳？

因為：

如果選：

第一個：

```text
2
```

得到：

```text
[1,2]
```

如果又選：

第二個：

```text
2
```

得到：

```text
[1,2]
```

答案完全一樣。

所以：

```text
第二個 2

不用再試一次
```

---

### Step 11：回第一層

回來：

```python
path.pop()
```

變成：

```text
path = []
```

目前：

```text
res

[
 [],
 [1],
 [1,2],
 [1,2,2]
]
```

第一層繼續。

---

### Step 12：第一層選 nums[1] = 2

加入：

```python
path.append(2)
```

變成：

```text
path = [2]
```

呼叫：

```python
backtrack(2, [2])
```

加入答案：

```text
[
 [],
 [1],
 [1,2],
 [1,2,2],
 [2]
]
```

---

### Step 13：下一層

現在：

```text
start = 2
```

只有：

```text
i = 2
```

加入：

```python
path.append(2)
```

變成：

```text
path = [2,2]
```

加入答案：

```text
[
 [],
 [1],
 [1,2],
 [1,2,2],
 [2],
 [2,2]
]
```

---

### Step 14：Backtracking

一路：

```python
path.pop()
```

回到：

```text
path = []
```

---

### Step 15：第一層最後一次

現在：

```text
i = 2
```

判斷：

```python
i > start

2 > 0
```

成立。

而且：

```python
nums[2] == nums[1]
```

成立。

因此：

```python
continue
```

直接跳過。

---

### 最終答案

```text
[
 [],
 [1],
 [1,2],
 [1,2,2],
 [2],
 [2,2]
]
```

---

### 遞迴樹（Recursion Tree）

```text
                         []
                    /        \
                  1           2
                 /             \
              [1]             [2]
              |                |
              2                2
              |                |
           [1,2]           [2,2]
              |
              2
              |
         [1,2,2]
```

注意：

```text
第一層

第二個 2

×

跳過
```

以及：

```text
第二層

第二個 2

×

跳過
```

因為：

```text
同一層

不能重複選相同數字當起點
```

但是：

```text
下一層

可以繼續選
```

所以：

```text
[2,2]

是合法答案
```

---

## ⏱ Complexity Analysis

### Time Complexity

* 最多會產生：

```text
2^n
```

個 subsets。

每個 subset 最長：

```text
n
```

因此：

```text
O(n × 2^n)
```

---

### Space Complexity

* 遞迴深度：

```text
O(n)
```

* 儲存答案：

```text
O(n × 2^n)
```

---

## 🎯 Interview Takeaways

* 看到：

```text
Subsets
```

想到：

```text
Backtracking
```

---

* 如果：

```text
有 Duplicate
```

第一步一定：

```python
nums.sort()
```

---

* 去重模板一定記：

```python
if i > start and nums[i] == nums[i - 1]:
    continue
```

---

* `path` 永遠代表：

```text
目前正在建立的 Subset
```

---

* Backtracking 標準模板：

```text
append

↓

recursive

↓

pop
```

---

## ✍️ 我學到的東西 | What I Learned

* LeetCode 90 和 78 的差別只有：

  * 多了排序。
  * 多了去重。

* `path` 不會一直建立新的 list。

* 每層遞迴都共用同一個 `path`。

* `path.pop()` 是恢復現場（Backtracking）。

* `i > start` 的意思是：

```text
只跳過

同一層

重複元素
```

不是跳過所有重複元素。

---

## 🏆 Cheat Sheet

```text
LeetCode 90

Subsets II

Sort

↓

Backtracking

↓

res.append(path[:])

↓

for i in range(start,n)

↓

Duplicate?

i > start

and

nums[i]==nums[i-1]

↓

continue

↓

append

↓

backtrack(i+1)

↓

pop
```

---

## 🌟 One Sentence Summary

> Sort the array first, then use backtracking to generate all subsets while skipping duplicate numbers at the same recursion level.

> 先排序，再利用 Backtracking 產生所有 Subsets，並在**同一層遞迴**跳過重複元素，以避免產生重複答案。

