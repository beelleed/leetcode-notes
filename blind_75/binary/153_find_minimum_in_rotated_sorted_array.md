# 🔎 LeetCode 153 - Find Minimum in Rotated Sorted Array
[題目連結](https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/)

---

## 📘 題目說明 | Problem Description

### 中文：
給你一個升序排列但經過旋轉的整數陣列 `nums`（元素不重複），請找出其中的最小值。  
**必須在 O(log n) 時間內完成。**

### English:
Given a rotated sorted array `nums` of unique elements, return the minimum element.  
You must solve it in O(log n) time.

---

## 💡 解法思路 | Solution Idea

### ✅ 使用 Binary Search 找轉折點：

1. 利用 `mid` 和 `right` 的值比較，判斷最小值在哪一半。
2. 如果 `nums[mid] > nums[right]`，代表最小值在右半邊（排除了左半含 mid）。
3. 如果 `nums[mid] < nums[right]`，代表最小值在左半邊（包含 mid）。
4. 最終 `left == right` 時，該位置就是最小值。

---

## 🧾 程式碼 | Python Code

```python
class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1

        while left < right:
            mid = (left + right) // 2
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid  # 包含 mid 的左邊可能有最小值

        return nums[left]
```

```python
left, right = 0, len(nums) - 1
```
初始化指標：

- left：左邊界（從頭開始）

- right：右邊界（從尾巴開始）
```python
while left < right:
```
只要搜尋區間還有超過一個元素，就持續執行二分搜尋。
```python
mid = (left + right) // 2
```
每次找出「中間點」mid 的 index。
```python
if nums[mid] > nums[right]:
    left = mid + 1
```
- 若中間值比右邊大，表示最小值一定在右半邊：

    - 因為右半邊才會包含轉折點（小數字）

- 所以排除掉 mid 本身，往右邊搜尋。

### 如果寫 if nums[left] < nums[mid]:
- 這只能判斷：左半邊是不是升序並不能保證 最小值在右邊
- ex: nums = [3,4,5,1,2]
    
    - 第一次：
    ```python
    left=0 right=4
    mid=2
    nums[left]=3
    nums[mid]=5
    ```
    - 判斷：
    ```python
    3 < 5 → True
    left = 3
    ```
    - 現在：
    ```python
    left=3 right=4
    ```
    - mid=3
    ```python
    nums[left]=1
    nums[mid]=1
    ```
    - 條件：
    ```python
    1 < 1 → False
    right = mid
    ```
    - 這時邏輯開始變得不穩定，很多 case 會錯。
```python
else:
    right = mid
```
- 若 nums[mid] <= nums[right]：

    - 表示右半邊是有序的，最小值可能在左邊包含 mid。

- 所以保留 mid，繼續往左半邊找。
```python
return nums[left]
```
- 最後當 left == right，區間只剩一個元素，就是最小值。

- 直接回傳 nums[left]。

---

## 🔁 範例流程 | Example
```python
Input: nums = [4,5,6,7,0,1,2]
Output: 0
```
| left | right | mid | nums\[mid] | nums\[right] | 行為                 |
| ---- | ----- | --- | ---------- | ------------ | ------------------ |
| 0    | 6     | 3   | 7          | 2            | mid > right → 去右邊  |
| 4    | 6     | 5   | 1          | 2            | mid <= right → 去左邊 |
| 4    | 5     | 4   | 0          | 1            | mid <= right → 去左邊 |
| 4    | 4     |     |            |              | 只剩一個 → 回傳 0        |

✅ 小結
| 重點                         | 解釋                  |
| -------------------------- | ------------------- |
| 二分搜尋找轉折點                   | 每次看中間值與右邊值，判斷哪邊有最小值 |
| `nums[mid] > nums[right]`  | 最小值在右邊（排除 mid）      |
| `nums[mid] <= nums[right]` | 最小值在左邊（保留 mid）      |
| 回傳 `nums[left]`            | 最後只剩一個元素時，就是最小值     |

---

## ⏱ 複雜度分析 | Time & Space Complexity
| 項目    | 複雜度        |
| ----- | ---------- |
| 時間複雜度 | `O(log n)` |
| 空間複雜度 | `O(1)`     |

---

## 📚 我學到了什麼 | What I Learned

- 即使陣列被旋轉，只要有部分是有序的，就可以用二分搜尋。

- 關鍵在於觀察 nums[mid] 與 nums[right] 的關係。

- 題目要求 O(log n) 時間，就要想到 Binary Search。