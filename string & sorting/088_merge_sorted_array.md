# LeetCode 88: Merge Sorted Array – Solution
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
