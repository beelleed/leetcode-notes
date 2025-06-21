# LeetCode 88: Merge Sorted Array
## 🔗 題目連結 / Problem Link  
[LeetCode #88 - Merge Sorted Array](https://leetcode.com/problems/merge-sorted-array/)

---

## 📖 題目描述 | Problem Description

**English**

You are given two integer arrays `nums1` and `nums2`, sorted in **non-decreasing order**, and two integers `m` and `n`, representing the number of elements in `nums1` and `nums2` respectively.

**Merge `nums2` into `nums1` as one sorted array.**

The final sorted array should not be returned by the function, but instead be stored inside the array `nums1`. To accommodate this, `nums1` has a length of `m + n`, with the last `n` elements set to `0`, and should be ignored.

**中文**

給你兩個排序好的數字陣列 `nums1`和 `nums2`，及數字 `m` 和 `n`，表示屬於 `nums1`和 `nums2`的有效元素數。

**請使用 in-place 方式，將 `nums2` 合併至 `nums1`中，並保持升序排列。**

`nums1` 有 `m + n` 個位置，其中後 `n` 個元素為 0，用於容納 `nums2`。

#### 🧪 Example 範例：

```python
Input: nums1 = [1,2,3,0,0,0], m = 3
       nums2 = [2,5,6], n = 3
Output: nums1 = [1,2,2,3,5,6]
```

---

## 🤔 解題策略 | Solution Strategy

### 方法一：從後往前合併 Two Pointers from the Back

- 利用 nums1 後面的空位，從後往前放較大的數字。
- 指針 `p1` 指向 `nums1` 的最後有效元素，`p2` 指向 `nums2` 的尾端，`p` 指向合併後的尾端。
- 比較 `nums1[p1]` 與 `nums2[p2]`，較大的填入 `nums1[p]`，然後移動對應指標。
- 如果 `nums2` 還有剩下的數字，最後補進 `nums1` 開頭。

#### 詳細程式碼解析
```python
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        p1 = m - 1  # nums1 的最後一個有效元素
        p2 = n - 1  # nums2 的最後一個元素
        p = m + n - 1  # 合併後 nums1 的最後一個位置

        while p1 >= 0 and p2 >= 0:
            if nums1[p1] > nums2[p2]:
                nums1[p] = nums1[p1]
                p1 -= 1
            else:
                nums1[p] = nums2[p2]
                p2 -= 1
            p -= 1

        # 把 nums2 剩下的補進 nums1 前面
        while p2 >= 0:
            nums1[p] = nums2[p2]
            p2 -= 1
            p -= 1
```
#### 📌 初始指標
p1 = 2 (指向 3)

p2 = 2 (指向 6)

p = 5 (合併填入位置)

#### 🔁 合併過程
| 比較     | 操作         | nums1 更新      | p1 | p2 | p |
| ------ | ---------- | ------------- | -- | -- | - |
| 3 vs 6 | nums2 wins | nums1\[5] = 6 | 2  | 1  | 4 |
| 3 vs 5 | nums2 wins | nums1\[4] = 5 | 2  | 0  | 3 |
| 3 vs 2 | nums1 wins | nums1\[3] = 3 | 1  | 0  | 2 |
| 2 vs 2 | nums2 wins | nums1\[2] = 2 | 1  | -1 | 1 |

#### ✅ 進入第二段 while：while p2 >= 0
- 現在 p2 = -1，已經不需要補 nums2

- 所以第二段 while 雖存在，但 在這個例子中不會執行

#### ✅ 最終結果：
nums1 = [1,2,2,3,5,6]

---

#### 🔍 延伸說明
若改成：
```python 
nums1 = [0,0,0,0,0,0]
m = 0
nums2 = [1,2,3,4,5,6]
n = 6
```
那麼這個情況下：

p1 = m - 1 = -1

p2 = n - 1 = 5

p = m + n - 1 = 5

就會直接執行：
```python
while p2 >= 0:
    nums1[p] = nums2[p2]
```
#### 🔁 合併過程：

| p2 | nums2\[p2] | nums1\[p] 被設為 | nums1 更新後           |
| -- | ---------- | ------------- | ------------------- |
| 5  | 6          | 6             | \[0, 0, 0, 0, 0, 6] |
| 4  | 5          | 5             | \[0, 0, 0, 0, 5, 6] |
| 3  | 4          | 4             | \[0, 0, 0, 4, 5, 6] |
| 2  | 3          | 3             | \[0, 0, 3, 4, 5, 6] |
| 1  | 2          | 2             | \[0, 2, 3, 4, 5, 6] |
| 0  | 1          | 1             | \[1, 2, 3, 4, 5, 6] |

#### ✅ 最終結果：

nums1 = [1, 2, 3, 4, 5, 6]

---

#### ✅ 為什麼不用管 p2 < 0？
1. 兩個陣列中，只會有一邊有剩：

    - 第一個 while p1 >= 0 and p2 >= 0 的迴圈結束時：

        - 要嘛 p1 < 0（nums1 用完）

        - 要嘛 p2 < 0（nums2 用完）

        - 或者兩邊同時用完

2. 我們只需要處理「nums2 還有剩」的情況：

    - 如果是 p1 < 0、p2 >= 0 → 就要補 nums2 的剩下元素

    - 如果是 p2 < 0，那就已經完成合併了，不需要再動任何東西

3. 沒有必要補 nums1：

    - 因為 nums1 的資料本來就在正確的位置，剩下未覆蓋的 nums1 直接保留即可

4. 總結一句話：
    「當 p2 < 0，代表 nums2 的元素都已經合併完畢，因此不需要特別處理這種情況。」

---

### 方法二：簡單排序合併（非 in-place）
- 先把 nums1 有效部分和 nums2 合併成一個新列表，再排序。
- 最後更新回 nums1。

#### 程式碼與解釋
```python
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        nums1[m:] = nums2  # 將 nums2 接到 nums1 後面
        nums1.sort()       # 排序整個 nums1
```
- `nums1[m:] = nums2`：將 nums2 直接放進 nums1 的預留位置
- `nums1.sort()`：直接使用 Python 內建排序，時間複雜度 O((m+n)log(m+n))

---

## ⏱️ 時間與空間複雜度 |Time & Space Complexity 

### 方法一
- **Time Complexity:** O(m + n)
- **Space Complexity:** O(1) – 原地修改（in-place）

### 方法二
- **Time Complexity:** O((m + n)log(m + n))
- **Space Complexity:** O(1)，但會使用 Python sort 函式的內部空間

---

## 📌 重點總結 | Key Takeaways
- ✅ 倒序合併技巧是經典 in-place 操作技巧
- ✅ 先比較再移動指標，確保不覆蓋原始有效資料
- ✅ 方法二適合用於練習排序合併概念，但不符合 in-place 要求
