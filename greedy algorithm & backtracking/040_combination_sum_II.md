# 📍 LeetCode 40 — Combination Sum II

🔗 https://leetcode.com/problems/combination-sum-ii/

---

## 📄 題目說明 | Problem Description

### 中文

給定一個整數陣列 `candidates` 和一個整數 `target`。

請找出所有數字總和等於 `target` 的組合。

限制：

* 每個數字**只能使用一次**。
* 陣列中可能有**重複元素**。
* 回傳的答案**不能有重複的組合**。

---

### English

Given a collection of candidate numbers (`candidates`) and a target number (`target`).

Return all unique combinations where the candidate numbers sum to `target`.

Rules:

* Each number may only be used **once**.
* The array may contain **duplicate numbers**.
* The solution set must not contain duplicate combinations.

---

### Examples

#### Example 1

Input

```python
candidates = [10,1,2,7,6,1,5]
target = 8
```

Output

```text
[
 [1,1,6],
 [1,2,5],
 [1,7],
 [2,6]
]
```

---

#### Example 2

Input

```python
candidates = [2,5,2,1,2]
target = 5
```

Output

```text
[
 [1,2,2],
 [5]
]
```

---

## 🧠 核心觀念 | Key Insight

這題可以看成：

```text
LeetCode 39
+
LeetCode 90
```

也就是：

* Combination Sum（找所有符合 target 的組合）
* Subsets II（避免重複答案）

因此需要同時考慮：

1. 如何找到所有可能的組合。
2. 如何避免重複組合。
3. 每個數字只能使用一次。

---

### 第一步一定要排序

```python
candidates.sort()
```

例如：

排序前：

```python
[2,1,2,5]
```

排序後：

```python
[1,2,2,5]
```

排序有兩個目的：

### ① 去除重複答案

因為相同數字會排在一起，所以才能判斷：

```python
if i > start and candidates[i] == candidates[i - 1]:
    continue
```

避免：

```text
[1,2]

又得到

[1,2]
```

---

### ② 提前停止搜尋（Pruning）

排序後：

如果目前：

```text
remaining = 3
```

看到：

```text
5
```

因為：

```text
5 > 3
```

後面只會更大：

```text
6

7

10
```

所以：

```python
break
```

直接停止搜尋。

---

### Backtracking 的想法

每一層遞迴代表：

```text
目前已經選好一些數字
```

例如：

```text
[]

↓

[1]

↓

[1,2]

↓

[1,2,5]
```

每一層都會：

* 選一個新的數字
* 更新剩餘目標值
* 繼續往下搜尋

直到：

```text
remaining == 0
```

表示：

```text
剛好湊出 target
```

就是一組合法答案。

---

### path 是什麼？

你的寫法：

```python
backtrack(start, path, remaining)
```

其中：

* `start`：下一個可以開始選的位置。
* `path`：目前已經選好的組合。
* `remaining`：距離 target 還差多少。

例如：

```text
target = 8

目前：

path = [1,2]

remaining = 5
```

代表：

```text
目前已經選了

1 + 2 = 3

還需要 5
```

---

### remaining 比 total 更直覺

有兩種常見寫法。

第一種：

```python
backtrack(start, path, total)
```

代表：

```text
目前已經加到多少
```

第二種（本題）：

```python
backtrack(start, path, remaining)
```

代表：

```text
還差多少
```

例如：

```text
target = 8
```

加入：

```text
1
```

變成：

```text
remaining = 7
```

再加入：

```text
2
```

變成：

```text
remaining = 5
```

因此：

```text
remaining

一直往 0 靠近
```

通常閱讀起來會比 `total` 更容易理解。

---

### 每個數字只能使用一次

加入目前數字後：

下一層一定是：

```python
backtrack(i + 1, path, ...)
```

而不是：

```python
backtrack(i, path, ...)
```

原因：

```text
每個 index

只能使用一次
```

例如：

```python
[1,2,5]
```

如果已經用了：

```text
2
```

下一層只能從：

```text
5
```

開始。

不能再回來使用同一個：

```text
2
```

---

### 去除重複答案

本題最重要的一行：

```python
if i > start and candidates[i] == candidates[i - 1]:
    continue
```

意思：

```text
同一層

如果前一個數字已經選過

後面的相同數字就跳過
```

例如：

```python
[1,2,2]
```

第一層：

如果：

第一個：

```text
2
```

已經當起點。

第二個：

```text
2
```

就不用再當起點。

否則：

會得到完全一樣的答案。

注意：

```text
只跳過

同一層
```

不是：

```text
所有重複元素
```

因此：

```text
[2,2]
```

仍然是合法答案。

---

### Pruning（剪枝）

本題使用：

```python
if candidates[i] > remaining:
    break
```

不是：

```python
if remaining < 0:
    return
```

兩者最大的差別是：

---

#### 方法一（本題）

```python
if candidates[i] > remaining:
    break
```

代表：

```text
還沒進 DFS

就知道不可能成功
```

例如：

```text
remaining = 3

目前看到：

5
```

因為：

```text
5 > 3
```

又因為：

```text
已經排序
```

所以：

```text
後面的數字只會更大
```

因此：

```python
break
```

完全不用遞迴。

---

#### 方法二

```python
if remaining < 0:
    return
```

流程則是：

```text
先選

↓

進 DFS

↓

remaining 變負

↓

return
```

例如：

```text
remaining = 3

↓

選 5

↓

remaining = -2

↓

return
```

因此：

已經：

```text
多跑了一層 DFS
```

效率比較差。

---

### 為什麼可以使用 break？

因為：

```python
candidates.sort()
```

例如：

```text
remaining = 4

目前：

5

6

8

10
```

既然：

```text
5 都太大
```

那：

```text
6

8

10
```

一定更大。

因此：

```python
break
```

完全安全。

如果：

沒有排序。

例如：

```text
7

2

5

1
```

看到：

```text
7 > remaining
```

就不能：

```python
break
```

因為：

後面：

```text
2

1
```

仍然有可能成功。

所以：

> **`break` 能成立的前提，就是一定先排序。**

---

## 💻 Code

```python
class Solution:
    def combinationSum2(
        self, candidates: List[int], target: int
    ) -> List[List[int]]:

        candidates.sort()

        res = []

        def backtrack(start, path, remaining):

            if remaining == 0:
                res.append(path[:])
                return

            for i in range(start, len(candidates)):

                if i > start and candidates[i] == candidates[i - 1]:
                    continue

                if candidates[i] > remaining:
                    break

                path.append(candidates[i])

                backtrack(i + 1, path, remaining - candidates[i]
                )

                path.pop()

        backtrack(0, [], target)

        return res
```

## 🧾 程式碼逐行解釋 | Line-by-line Explanation

```python
class Solution:
```

* 定義 LeetCode 的 `Solution` 類別。
* LeetCode 會建立這個類別，並呼叫裡面的 `combinationSum2` 方法。

```python
def combinationSum2(
    self, candidates: List[int], target: int
) -> List[List[int]]:
```

* 定義主要函式 `combinationSum2`。
* `candidates` 是可以選擇的數字陣列。
* `target` 是希望組合加總後達到的目標值。
* 回傳型態：

```python
List[List[int]]
```

代表：

```text
由很多個整數陣列組成的答案
```

例如：

```python
[
    [1, 1, 6],
    [1, 2, 5],
    [1, 7],
    [2, 6]
]
```

```python
candidates.sort()
```

* 先將 `candidates` 由小到大排序。

例如：

```python
[10, 1, 2, 7, 6, 1, 5]
```

排序後：

```python
[1, 1, 2, 5, 6, 7, 10]
```

排序有兩個非常重要的用途：

* 讓相同的數字排在一起，方便去除重複答案。
* 當目前數字大於 `remaining` 時，可以直接 `break`。

如果沒有排序，就不能安全使用：

```python
if candidates[i] > remaining:
    break
```

因為後面可能還有比較小的數字。

```python
res = []
```

* 建立答案陣列。
* 所有合法的組合都會存進 `res`。

例如：

```python
res = [
    [1, 1, 6],
    [1, 2, 5]
]
```

```python
def backtrack(start, path, remaining):
```

* 建立 Backtracking 遞迴函式。

三個參數分別代表：

```text
start
```

* 下一個可以開始選擇的 index。

```text
path
```

* 目前已經選擇的數字組合。

```text
remaining
```

* 距離 `target` 還差多少。

例如：

```python
target = 8
path = [1, 2]
remaining = 5
```

代表：

```text
目前已經選了 1 + 2 = 3

距離 8 還差 5
```

```python
if remaining == 0:
```

* 如果 `remaining` 剛好等於 `0`，表示目前的組合總和剛好等於 `target`。

例如：

```python
target = 8
path = [1, 2, 5]
remaining = 0
```

因為：

```text
1 + 2 + 5 = 8
```

所以找到一組合法答案。


```python
res.append(path[:])
```

* 將目前的 `path` 複製一份後加入答案。

一定要使用：

```python
path[:]
```

不能直接使用：

```python
res.append(path)
```

原因是所有遞迴層共用同一個 `path` list。

後面會一直執行：

```python
path.append(...)
path.pop()
```

如果直接把 `path` 放進 `res`，答案中的內容會一起被修改。

例如：

```python
path = [1, 2, 5]
```

執行：

```python
res.append(path[:])
```

會建立一個新的 list：

```python
[1, 2, 5]
```

即使之後：

```python
path.pop()
```

讓 `path` 變成：

```python
[1, 2]
```

`res` 裡的：

```python
[1, 2, 5]
```

仍然不會改變。

```python
return
```

* 找到一組答案後，直接結束目前這一層遞迴。

因為題目中的數字都是正整數。

當：

```python
remaining == 0
```

時，不需要再繼續加入其他數字。

如果繼續加入正數，總和一定會超過 `target`。

```python
for i in range(start, len(candidates)):
```

* 從 `start` 開始，依序嘗試每一個候選數字。
* `i` 代表目前想選擇的 index。

例如：

```python
candidates = [1, 1, 2, 5]
start = 2
```

這一層可以選擇：

```text
index 2 的 2
index 3 的 5
```

不能再選：

```text
index 0 的 1
index 1 的 1
```

因為那些位置已經屬於前面的選擇範圍。

```python
if i > start and candidates[i] == candidates[i - 1]:
    continue
```

* 這一行用來避免產生重複組合。
* 只跳過「同一層」中的重複數字。

判斷分成兩部分。

第一部分：

```python
i > start
```

表示：

```text
目前不是這一層第一次選擇的數字
```

第二部分：

```python
candidates[i] == candidates[i - 1]
```

表示：

```text
目前數字和前一個數字相同
```

兩者同時成立，就代表：

```text
同一層中，前面已經用相同數字當過起點
```

所以直接：

```python
continue
```

跳過目前這個數字。

### 為什麼一定要有 `i > start`？

假設：

```python
candidates = [1, 1, 6]
```

目標：

```python
target = 8
```

合法答案包含：

```python
[1, 1, 6]
```

第一層選擇第一個 `1` 後：

```python
path = [1]
start = 1
```

進入下一層時：

```python
i = 1
start = 1
```

此時：

```python
i > start
```

是：

```text
1 > 1

False
```

所以第二個 `1` 不會被跳過。

因此可以形成：

```python
[1, 1, 6]
```

這表示：

```text
不同遞迴層可以選擇相同數字
```

只要它們來自不同 index。

### 同一層為什麼要跳過？

排序後：

```python
[1, 1, 2]
```

在最外層：

```python
start = 0
```

第一次：

```python
i = 0
```

選第一個 `1`，可以找到所有以 `1` 開頭的答案。

當：

```python
i = 1
```

又想選第二個 `1` 當起點時，會重新產生一模一樣的搜尋結果。

因此第二個 `1` 必須跳過。


```python
if candidates[i] > remaining:
    break
```

* 如果目前數字已經大於 `remaining`，就停止這一層的整個迴圈。
* 這是一個剪枝條件。

例如：

```python
remaining = 4
candidates = [1, 2, 5, 6, 7]
```

當走到：

```python
candidates[i] = 5
```

因為：

```text
5 > 4
```

代表選擇 `5` 一定會超過目標。

又因為陣列已經排序，所以後面的：

```text
6
7
```

只會更大。

因此不需要繼續檢查，直接：

```python
break
```

離開目前這一層的 `for` 迴圈。

### 為什麼是 `break`，不是 `continue`？

如果使用：

```python
continue
```

只會跳過目前的數字，然後繼續檢查後面的數字。

但因為陣列已經排序：

```text
目前數字都太大了

後面的數字一定更大
```

所以後面全部不可能成功。

因此應該使用：

```python
break
```

直接停止整個迴圈。


```python
path.append(candidates[i])
```

* 將目前選擇的數字加入 `path`。

例如：

```python
path = [1, 2]
candidates[i] = 5
```

加入後：

```python
path = [1, 2, 5]
```

這代表：

```text
做出目前這個選擇
```


```python
backtrack(
    i + 1,
    path,
    remaining - candidates[i]
)
```

* 帶著目前的選擇進入下一層遞迴。

下一層的三個參數分別是：

```python
i + 1
```

* 下一個只能從目前 index 的下一個位置開始。
* 確保同一個 index 不會被重複使用。

```python
path
```

* 將目前的組合傳給下一層。
* 傳入的是同一個 list，不是新的 list。

```python
remaining - candidates[i]
```

* 扣除目前選擇的數字。
* 更新還差多少才能達到 `target`。

例如：

```python
remaining = 7
candidates[i] = 2
```

下一層會變成：

```python
remaining = 5
```

### 為什麼是 `i + 1`？

因為本題規定：

```text
每個 index 只能使用一次
```

如果寫成：

```python
backtrack(i, path, ...)
```

下一層仍然可以再次選擇同一個位置。

那就會變成 LeetCode 39 的寫法。

本題必須寫：

```python
backtrack(i + 1, path, ...)
```

代表：

```text
目前這個 index 已經使用過

下一層必須往後選
```

```python
path.pop()
```

* 下一層遞迴結束後，移除剛剛加入的數字。
* 恢復到做選擇之前的狀態。

例如：

遞迴前：

```python
path = [1, 2]
```

做選擇：

```python
path.append(5)
```

變成：

```python
path = [1, 2, 5]
```

探索完所有以 `[1, 2, 5]` 開頭的可能後：

```python
path.pop()
```

恢復成：

```python
path = [1, 2]
```

接著就能嘗試其他數字。

這就是 Backtracking 的核心：

```text
做選擇

↓

遞迴探索

↓

撤銷選擇
```

```python
backtrack(0, [], target)
```

* 從初始狀態開始執行 Backtracking。

初始參數：

```python
start = 0
```

代表從第一個 index 開始選。

```python
path = []
```

代表還沒有選任何數字。

```python
remaining = target
```

代表一開始還差完整的 `target`。

例如：

```python
target = 8
```

初始狀態：

```python
backtrack(0, [], 8)
```

```python
return res
```

* 回傳所有合法且不重複的組合。

---

## 🌿 `break` 與 `remaining < 0` 的差別

這題也可以寫成：

```python
def backtrack(start, path, remaining):
    if remaining == 0:
        res.append(path[:])
        return

    if remaining < 0:
        return

    for i in range(start, len(candidates)):
        path.append(candidates[i])

        backtrack(
            i + 1,
            path,
            remaining - candidates[i]
        )

        path.pop()
```

但這個版本的效率通常比：

```python
if candidates[i] > remaining:
    break
```

差一些。


### 寫法一：DFS 前剪枝

```python
if candidates[i] > remaining:
    break
```

例如：

```python
remaining = 3
candidates[i] = 5
```

程式在加入 `5` 之前就知道：

```text
5 已經太大

一定不可能成功
```

所以直接停止。

流程：

```text
檢查 5 > 3

↓

成立

↓

break

↓

不會 append

↓

不會進入下一層 DFS
```

---

### 寫法二：DFS 後才發現失敗

```python
if remaining < 0:
    return
```

例如：

```python
remaining = 3
```

先選擇：

```python
5
```

接著呼叫：

```python
backtrack(..., remaining = -2)
```

下一層才發現：

```python
remaining < 0
```

然後返回。

流程：

```text
append 5

↓

進入下一層 DFS

↓

remaining = -2

↓

return

↓

pop 5
```

這個版本多做了：

* 一次 `append`
* 一次遞迴呼叫
* 一次負數判斷
* 一次 `pop`

---

### 兩種寫法都能得到正確答案嗎？

可以。

只要其他邏輯正確，兩種寫法都能得到正確答案。

差別主要在於：

```text
什麼時候發現這條路不可能成功
```

`candidates[i] > remaining`：

```text
進入 DFS 前就發現
```

`remaining < 0`：

```text
進入 DFS 後才發現
```

因此第一種剪枝更早。

---

### 為什麼 `remaining` 可能是 8？

第一次呼叫：

```python
backtrack(0, [], target)
```

如果：

```python
target = 8
```

那一開始：

```python
remaining = 8
```

這是正常的。

`remaining` 不是固定小於某一個候選數字。

它代表：

```text
目前還差多少
```

隨著選擇數字，它會逐漸減少。

例如：

```text
remaining = 8

選 1

remaining = 7

選 2

remaining = 5

選 5

remaining = 0
```

---

### `if remaining < 0` 為什麼不能取代所有剪枝？

它可以作為安全檢查，但它無法利用排序帶來的資訊。

假設：

```python
remaining = 4
candidates = [5, 6, 7, 10]
```

使用：

```python
if remaining < 0:
    return
```

會依序嘗試：

```text
選 5 → -1 → return
選 6 → -2 → return
選 7 → -3 → return
選 10 → -6 → return
```

但使用：

```python
if candidates[i] > remaining:
    break
```

看到第一個 `5` 時就知道：

```text
5 已經太大

後面全部更大
```

因此一次 `break` 就全部停止。

---

### 比較表

| 寫法                                    | 判斷位置 | 是否進入無效 DFS | 是否依賴排序 | 能否停止後面所有候選 |
| ------------------------------------- | ---- | ---------: | -----: | ---------: |
| `if candidates[i] > remaining: break` | 選擇前  |         不會 |      會 |         可以 |
| `if remaining < 0: return`            | 選擇後  |          會 |    不一定 | 不行，只返回目前分支 |

---

### 最推薦的寫法

本題因為已經排序，所以推薦：

```python
if candidates[i] > remaining:
    break
```

理由：

* 更早發現不可能的分支。
* 不會多進一層遞迴。
* 可以一次停止後面全部更大的數字。
* 程式邏輯更清楚。

---

## 🧪 Example Walkthrough

### Example 1

Input：

```python
candidates = [10, 1, 2, 7, 6, 1, 5]
target = 8
```

排序後：

```python
candidates = [1, 1, 2, 5, 6, 7, 10]
```

初始呼叫：

```python
backtrack(0, [], 8)
```

目前：

```text
start = 0
path = []
remaining = 8
```

---

### 第一層：`path = []`

先從：

```python
i = 0
```

開始。

目前數字：

```python
candidates[0] = 1
```

檢查重複：

```python
i > start
```

也就是：

```text
0 > 0

False
```

不跳過。

檢查剪枝：

```python
1 > 8
```

是 `False`。

所以選擇 `1`：

```python
path = [1]
```

下一層：

```python
backtrack(1, [1], 7)
```

---

### 第二層：`path = [1]`

目前：

```text
start = 1
remaining = 7
```

從：

```python
i = 1
```

開始。

目前數字：

```python
candidates[1] = 1
```

雖然它和前一個數字相同，但：

```python
i > start
```

也就是：

```text
1 > 1

False
```

所以不能跳過。

這是不同遞迴層的第二個 `1`，可以使用。

選擇後：

```python
path = [1, 1]
remaining = 6
```

下一層：

```python
backtrack(2, [1, 1], 6)
```

---

### 第三層：`path = [1, 1]`

目前：

```text
start = 2
remaining = 6
```

先嘗試：

```python
candidates[2] = 2
```

選擇後：

```python
path = [1, 1, 2]
remaining = 4
```

進入下一層。

---

### 第四層：`path = [1, 1, 2]`

目前：

```text
remaining = 4
start = 3
```

目前第一個候選數字是：

```python
candidates[3] = 5
```

判斷：

```python
5 > 4
```

成立。

所以：

```python
break
```

不會選擇 `5`。

這條分支結束。

回上一層並執行：

```python
path.pop()
```

`path` 從：

```python
[1, 1, 2]
```

恢復成：

```python
[1, 1]
```

---

### `path = [1, 1]` 繼續嘗試

下一個候選數字：

```python
candidates[3] = 5
```

判斷：

```python
5 > 6
```

不成立。

選擇 `5`：

```python
path = [1, 1, 5]
remaining = 1
```

下一層中，第一個可選數字是：

```python
6
```

因為：

```python
6 > 1
```

直接 `break`。

所以 `[1,1,5]` 不能形成答案。

---

回到：

```python
path = [1, 1]
remaining = 6
```

下一個候選數字：

```python
6
```

因為：

```python
6 <= 6
```

可以選。

選擇後：

```python
path = [1, 1, 6]
remaining = 0
```

進入下一層：

```python
backtrack(5, [1, 1, 6], 0)
```

因為：

```python
remaining == 0
```

加入答案：

```python
res = [
    [1, 1, 6]
]
```

然後 `return`。

---

### 回到第一個 `[1]`

探索完第二個 `1` 開頭的分支後，回到：

```python
path = [1]
remaining = 7
start = 1
```

接著：

```python
i = 2
```

選擇：

```python
2
```

得到：

```python
path = [1, 2]
remaining = 5
```

下一層從 index `3` 開始。

第一個可選數字：

```python
5
```

因為：

```python
5 <= 5
```

選擇後：

```python
path = [1, 2, 5]
remaining = 0
```

加入答案：

```python
res = [
    [1, 1, 6],
    [1, 2, 5]
]
```

---

回到：

```python
path = [1]
remaining = 7
```

之後選擇：

```python
7
```

得到：

```python
path = [1, 7]
remaining = 0
```

加入答案：

```python
res = [
    [1, 1, 6],
    [1, 2, 5],
    [1, 7]
]
```

---

### 回到最外層

探索完第一個 `1` 的所有分支後：

```python
path = []
start = 0
```

接著：

```python
i = 1
```

目前數字也是：

```python
1
```

判斷：

```python
i > start
```

也就是：

```text
1 > 0

True
```

而且：

```python
candidates[1] == candidates[0]
```

也就是：

```text
1 == 1

True
```

所以：

```python
continue
```

跳過第二個 `1`。

原因是第一個 `1` 已經在同一層當過起點。

如果再次用第二個 `1` 當起點，會產生重複答案。

---

### 最外層選擇 `2`

接著：

```python
i = 2
```

選擇：

```python
2
```

得到：

```python
path = [2]
remaining = 6
```

下一層從 index `3` 開始。

依序嘗試：

```text
5
6
7
10
```

選擇 `5`：

```python
path = [2, 5]
remaining = 1
```

下一個候選數字是 `6`：

```python
6 > 1
```

所以停止。

回到：

```python
path = [2]
remaining = 6
```

選擇 `6`：

```python
path = [2, 6]
remaining = 0
```

加入答案：

```python
res = [
    [1, 1, 6],
    [1, 2, 5],
    [1, 7],
    [2, 6]
]
```

---

### 剩下候選數字

最外層接著會嘗試：

```text
5
6
7
```

但都無法湊成新的合法組合。

當走到：

```python
10
```

因為：

```python
10 > 8
```

直接：

```python
break
```

搜尋結束。

---

### 最終答案

```python
[
    [1, 1, 6],
    [1, 2, 5],
    [1, 7],
    [2, 6]
]
```

---

### 搜尋樹重點

```text
[]
├── [1]
│   ├── [1,1]
│   │   ├── [1,1,2]
│   │   ├── [1,1,5]
│   │   └── [1,1,6] ✓
│   ├── [1,2]
│   │   └── [1,2,5] ✓
│   ├── [1,5]
│   ├── [1,6]
│   └── [1,7] ✓
├── 第二個 1 × 同層重複
├── [2]
│   ├── [2,5]
│   └── [2,6] ✓
├── [5]
├── [6]
├── [7]
└── 10 > 8，break
```

---

## ⏱ Complexity Analysis

### Time Complexity

最壞情況下，每個數字都有：

```text
選

或

不選
```

兩種可能。

因此搜尋樹最多有：

```text
2^n
```

個狀態。

每找到一個答案時，需要複製：

```python
path[:]
```

一個組合最長可能有 `n` 個元素。

因此整體時間複雜度通常寫成：

```text
O(n × 2^n)
```

另外排序需要：

```text
O(n log n)
```

所以完整表示可以寫成：

```text
O(n log n + n × 2^n)
```

通常由：

```text
O(n × 2^n)
```

主導。

### Space Complexity

不包含答案儲存空間時：

* 遞迴深度最多為 `n`
* `path` 最多存放 `n` 個數字

因此額外空間：

```text
O(n)
```

如果包含輸出答案：

```text
O(n × 2^n)
```

---

## 🎯 Interview Takeaways

* 看到「找所有組合」通常先想到 Backtracking。
* 看到陣列中有重複數字，先排序。
* 去除同層重複的模板：

```python
if i > start and candidates[i] == candidates[i - 1]:
    continue
```

* 每個數字只能使用一次，所以遞迴傳入：

```python
i + 1
```

* 如果數字可以重複使用，才會傳：

```python
i
```

* 使用 `remaining` 時：

```python
remaining == 0
```

代表找到答案。

* 排序後可以使用：

```python
if candidates[i] > remaining:
    break
```

提前停止搜尋。

* `break` 是停止目前這一層後面的所有候選數字。
* `return` 是結束目前這一次函式呼叫。
* `continue` 只跳過目前這一個候選數字。

---

## ✍️ 我學到的東西 | What I Learned

* `remaining` 代表距離 `target` 還差多少。
* 每次選擇數字後，都要執行：

```python
remaining - candidates[i]
```

* `path` 在所有遞迴層中是同一個 list。
* 因此標準 Backtracking 流程是：

```text
append

↓

recursive call

↓

pop
```

* `path[:]` 是複製答案，避免之後的 `pop()` 修改已儲存的結果。
* `i > start` 是用來判斷目前是否位於同一層的後續位置。
* 相同數字在同一層只能當一次起點。
* 相同數字在不同層仍然可以使用，因此 `[1,1,6]` 是合法的。
* `if candidates[i] > remaining: break` 比 `if remaining < 0: return` 更早剪枝。
* `break` 可以成立，是因為陣列已經排序。
* LeetCode 40 使用 `i + 1`，因為每個 index 只能使用一次。

---

## 🏆 Cheat Sheet

```text
LeetCode 40 — Combination Sum II

先排序

candidates.sort()

↓

Backtracking 狀態

start
path
remaining

↓

找到答案

if remaining == 0:
    res.append(path[:])
    return

↓

同層去重

if i > start and candidates[i] == candidates[i - 1]:
    continue

↓

排序後剪枝

if candidates[i] > remaining:
    break

↓

做選擇

path.append(candidates[i])

↓

每個 index 只能使用一次

backtrack(
    i + 1,
    path,
    remaining - candidates[i]
)

↓

撤銷選擇

path.pop()
```

### LeetCode 39 vs LeetCode 40

| 題目          | 每個數字能否重複使用 | 下一層 start | 是否需要同層去重 |
| ----------- | ---------- | --------- | -------- |
| LeetCode 39 | 可以         | `i`       | 通常不需要    |
| LeetCode 40 | 不可以        | `i + 1`   | 需要       |

### `break` vs `remaining < 0`

```text
if candidates[i] > remaining:
    break
```

* 遞迴前剪枝。
* 不會進入無效 DFS。
* 依賴排序。
* 可以停止後面全部數字。

```text
if remaining < 0:
    return
```

* 遞迴後才發現超過。
* 會多進一層 DFS。
* 不一定依賴排序。
* 只能返回目前分支。

---

## 🌟 One Sentence Summary

> Sort the candidates, use backtracking with `i + 1` so each index is used once, skip duplicates at the same recursion level, and stop early when the current candidate exceeds the remaining target.

> 先排序，再使用 Backtracking；透過 `i + 1` 確保每個 index 只使用一次，利用 `i > start` 跳過同層重複數字，並在目前數字大於 `remaining` 時直接 `break` 提前剪枝。
