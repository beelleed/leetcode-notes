# 🍌 LeetCode 875 — Koko Eating Bananas

🔗 [題目連結](https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/)

---

## 📄 題目說明 | Problem Description

- **中文**：有若干堆香蕉，每堆有不同數量 `piles[i]`。Koko 有 `h` 小時去吃香蕉。她每小時可以吃 `k` 根香蕉（若剩餘少於 `k` 根則吃完那堆就停），她可以選哪一堆吃。問最小的速度 `k`，使她可以在 `h` 小時內吃完所有香蕉。

- **English**: There are several piles of bananas, `piles[i]` bananas in pile i. Koko has `h` hours to eat all bananas. Each hour, she chooses one pile and eats up to `k` bananas from it (if less than `k`, she eats all). Find the minimum integer `k` such that she can eat all bananas within `h` hours.

### Examples

- Example 1:

    - Input: piles = [3,6,7,11], h = 8
    - Output: 4

- Example 2:

    - Input: piles = [30,11,23,4,20], h = 5
    - Output: 30

- Example 3:

    - Input: piles = [30,11,23,4,20], h = 6
    - Output: 23

---

## 🧠 解題思路 | Solution Idea

這題的關鍵在於 **速度 `k` 的單調性**：

- 如果速度 `k` 可以讓 Koko 在 `h` 小時內吃完所有香蕉，那麼任何比它更快的速度也一定可以。
- 若速度太慢，無法在 `h` 小時內完成。

因此，我們可以對速度做 **二分搜尋（Binary Search on answer）**。

### 步驟：

1. 定義一個輔助函式 `can_finish(k)`，判斷速度為 `k` 時是否能在 `h` 小時內吃完所有香蕉。
2. `can_finish(k)` 做法是對每一堆香蕉 `x = piles[i]`，加入時間 `(x + k - 1) // k`（向上除法）累加，看總時間是否 ≤ `h`。
3. 設定速度範圍：`left = 1`，`right = max(piles)`。
4. 用二分法在這個範圍內找最小合法速度 `k`：
   - mid = (left + right) // 2
   - 如果 `can_finish(mid)` 為真 → 更新答案，並把右界縮小 `right = mid - 1`
   - 否則速度太慢 → `left = mid + 1`
5. 最後答案存在 `left` 或 `ans` 中。

---

## 💻 程式碼實作 | Code (Python)

```python
from typing import List

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def can_finish(k: int) -> bool:
            total = 0
            for x in piles:
                # 吃這一堆 x 根香蕉所需小時 = 向上除法
                total += (x + k - 1) // k
            return total <= h

        left, right = 1, max(piles)
        ans = right

        while left <= right:
            mid = (left + right) // 2
            if can_finish(mid):
                ans = mid
                right = mid - 1
            else:
                left = mid + 1

        return ans
```
```python
def can_finish(k: int) -> bool:
```
### 🧩 判斷是否能以速度 k 吃完香蕉

這是內部函式，用來幫我們檢查當吃香蕉速度是 k 時，能不能在 h 小時內吃完全部。

```python
total = 0
for x in piles:
    total += (x + k - 1) // k
return total <= h
```
- return total <= h: 如果總時間小於等於 h，就回傳 True，否則 False

### 🔢 模擬吃香蕉所需的時間

- (x + k - 1) // k 是「向上除法」，保證即使剩一點點香蕉也算 1 小時

- 把每一堆香蕉吃完需要的時間加總

- 最後比對總時間是否 ≤ h

#### 📘 為什麼不是直接用 x // k？

- 因為 x // k 是「向下取整」，但我們希望「即使只剩 1 根香蕉也得花 1 小時」，所以要用 向上取整。

##### ✅ 舉例說明

假設 k = 3，也就是每小時最多吃 3 根香蕉：

| x（香蕉數） | `x // k`（向下） | `(x + k - 1) // k`（向上） |
| ------ | ------------ | ---------------------- |
| 6      | 2            | 2                      |
| 7      | 2            | 3 ✅                    |
| 8      | 2            | 3 ✅                    |
| 9      | 3            | 3                      |


```python
left, right = 1, max(piles)
ans = right
```
### 🎯 初始化二分搜尋範圍

- left = 1：最小速度（每小時至少吃 1 根）

- right = max(piles)：最大速度（吃最快的情況下，1 小時吃掉整堆最大香蕉）

- ans = right：初始化答案為最大值（保守估計）
```python
while left <= right:
    mid = (left + right) // 2
```
### 🔁 執行二分搜尋迴圈

- 每次嘗試中間速度 mid 看是否可以完成
```python
if can_finish(mid):
    ans = mid
    right = mid - 1
```
- 為什麼可以直接寫 if can_finish(mid)? 因為 can_finish(mid) 本身就是 True 或 False 

- 這其實等價於： if can_finish(mid) == True:

### ✅ 如果這個速度可行，就試更慢

- 嘗試更小速度，看有沒有更小的 k 也能完成

- 所以更新答案，並繼續搜尋左半邊

### 🧠 重點：二分搜尋的對象不是 piles，而是 k（吃香蕉的速度）

```python
else:
    left = mid + 1
```
### ❌ 如果速度不夠快，就往右找

- 提高速度，搜尋右半邊
```python
return ans
```
### 🔚 回傳最小可行速度

- 找出讓 Koko 能吃完香蕉的 最小速度

---

## 🧪 範例 | Example

```python
piles = [3, 6, 7, 11]
h = 8
```

### 初始狀態

- left = 1

- right = max(piles) = 11

- ans = 11

### 第一次迴圈

- mid = (1 + 11) // 2 = 6

- 呼叫 can_finish(6)：

    - 對每堆香蕉計算時間：

        - 3 → (3+6−1)//6 = 1 小時

        - 6 → (6+6−1)//6 = 1 小時

        - 7 → (7+6−1)//6 = 2 小時

        - 11 → (11+6−1)//6 = 2 小時

    - 總時間 = 1+1+2+2 = 6 ≤ 8 → 可以完成

- 因為可以完成 → ans = 6，right = mid - 1 = 5

### 第二次迴圈

- 更新後：left = 1, right = 5

- mid = (1 + 5) // 2 = 3

- 呼叫 can_finish(3)：

    - 各堆時間：

        - 3 → 1

        - 6 → 2

        - 7 → 3

        - 11 → 4

    - 總時間 = 1+2+3+4 = 10 > 8 → 太慢

- 因為無法完成 → left = mid + 1 = 4

### 第三次迴圈

- 現狀：left = 4, right = 5

- mid = (4 + 5) // 2 = 4

- can_finish(4)：

    - 各堆時間：

        - 3 → 1

        - 6 → 2

        - 7 → 2

        - 11 → 3

    - 總時間 = 1+2+2+3 = 8 ≤ 8 → 剛好可以

- 可完成 → ans = 4，right = mid - 1 = 3

- 此時 left = 4, right = 3，跳出迴圈。回傳 ans = 4。

- 最小速度是 4 根／小時。

---

## ⏱ 複雜度分析 | Complexity Analysis

- 時間複雜度：O(n · log M)
    - n = len(piles)，M = max(piles)
    - 因為我們在速度空間範圍做二分，每次檢查 can_finish 要掃一次所有堆 --> O(n)，共 log M 次

- 空間複雜度：O(1)（不使用與輸入長度 n 成比例的額外空間）

---

## ✍️ 我學到了什麼 | What I Learned

- 當答案本身有單調性，可以對答案進行二分搜尋（Binary Search on the result）

- 向上整數除法 (x + k - 1) // k 是處理「每堆香蕉需多少小時」的常用技巧

- 二分搜尋範圍的設定要小心：最低速度不能是 0，最高速度可以取 max(piles)

- 在面試中講這題時，要清楚講出為什麼速度符合單調性、為什麼 can_finish 方法正確、還有怎麼用二分定位最小速度