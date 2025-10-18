# 🌊 11. Container With Most Water | 盛最多水的容器
🔗 題目連結：[https://leetcode.com/problems/container-with-most-water/](https://leetcode.com/problems/container-with-most-water/)

---

## 📄 題意說明 | Problem Description

- **中文：**  
  給定整數陣列 `height`，表示在 x 軸上每個位置的柱子高度，請找出兩條柱子與 x 軸形成的容器能盛最多的水量。

- **English:**  
  You are given an array `height` where `height[i]` is the height of a vertical line at position `i`. Find two lines that, together with the x‑axis, form a container that holds the maximum amount of water. Return the maximum water area.

### Examples
- Example 1:

![](../images/11.jpg)

    Input: height = [1,8,6,2,5,4,8,3,7]

    Output: 49

    Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.

- Example 2:

    - Input: height = [1,1]
    - Output: 1

---

## 🧠 解題思維 | Solution Idea
### 中文
#### Brute-force 方法（O(n²)）
- 檢查所有可能的兩根柱子組合，計算面積：`(j − i) × min(height[i], height[j])`。雖正確但效率過低。

#### Two‑Pointer 優化策略 – O(n) 時間，O(1) 空間
- 初始化兩指針：`left = 0`（最左），`right = n − 1`（最右）。
- 算出當前容器面積。
- 為了可能提升面積（寬度只會縮小），我們 **移動指向較矮那邊的指針**：
  - 如果 `height[left] < height[right]` → 左指針右移（希望找到更高的柱子）
  - 否則右指針左移。
- 重複以上過程直到兩指針相遇。

### English
#### Brute-force Method (O(n²))

- Check all possible pairs of lines and calculate the area:
(j − i) × min(height[i], height[j]). This method is correct but inefficient due to its high time complexity.

#### Two‑Pointer Optimization – O(n) Time, O(1) Space

- Initialize two pointers: left = 0 (start of the array), right = n − 1 (end of the array).

- Compute the current container area.

- To possibly increase the area (as the width is decreasing), move the pointer pointing to the shorter height:

    - If height[left] < height[right] → move the left pointer to the right (hoping to find a taller line).

    - Otherwise, move the right pointer to the left.

- Repeat the process until the two pointers meet.

---

## 💻 Python 程式碼實作

```python
from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        max_area = 0

        while left < right:
            width = right - left
            h = min(height[left], height[right])
            max_area = max(max_area, width * h)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_area
```
```python
left, right = 0, len(height) - 1
max_area = 0
```
- 兩個指針：一個從左邊開始 (left)，一個從右邊開始 (right)。

- max_area 記錄目前找到的最大水量。

### 🔁 迴圈：直到兩指針相遇為止
```python
while left < right:
```
- 只要還沒碰頭，就不斷嘗試更好的解。

### 🧮 計算面積
```python
width = right - left
h = min(height[left], height[right])
max_area = max(max_area, width * h)
```
- 寬度為兩指針距離。

-  高度為左右兩邊中較矮的柱子。

-  面積 = 高 × 寬。

- 更新 max_area

### 🔄 移動指針策略
```python
if height[left] < height[right]:
    left += 1
else:
    right -= 1
```
- 由於高度被矮的一邊限制，我們只移動矮的那邊，試圖找到更高的柱子。

- 不能同時移動兩邊，否則可能會錯過最大值。

### ✅ 回傳答案
```python
return max_area
```
- 回傳整個過程中找到的最大值。

---

## 🧪 範例說明
- height = [1,8,6,2,5,4,8,3,7]
### 📌 初始設定
```python
left = 0           # 指向 index 0 → height = 1
right = 8          # 指向 index 8 → height = 7
max_area = 0
```
### 🔁 迴圈第 1 次：
```python
width = 8 - 0 = 8
h = min(1, 7) = 1
area = 8 × 1 = 8
max_area = 8
```
因為 height[left] < height[right]，所以 left += 1 → left = 1

### 🔁 迴圈第 2 次：
```python
left = 1 (height = 8), right = 8 (height = 7)
width = 7
h = min(8, 7) = 7
area = 7 × 7 = 49
max_area = 49 ✅
```
height[right] < height[left]，所以 right -= 1 → right = 7
### 🔁 第 3 次：
```python
left = 1 (height = 8), right = 7 (height = 3)
width = 6
h = min(8, 3) = 3
area = 6 × 3 = 18
max_area = 49 ❌（沒更新）
```
right -= 1 → right = 6
### 🔁 第 4 次：
```python
left = 1 (height = 8), right = 6 (height = 8)
width = 5
h = min(8, 8) = 8
area = 5 × 8 = 40
max_area = 49 ❌
```
right -= 1 → right = 5
### 🔁 第 5 次：
```python
left = 1 (height = 8), right = 5 (height = 4)
width = 4
h = 4
area = 16
max_area = 49 ❌
```
right -= 1 → right = 4
### 🔁 第 6 次：
```python
left = 1 (height = 8), right = 4 (height = 5)
width = 3
h = 5
area = 15
max_area = 49 ❌
```
right -= 1 → right = 3
### 🔁 第 7 次：
```python
left = 1 (height = 8), right = 3 (height = 2)
width = 2
h = 2
area = 4
max_area = 49 ❌
```
right -= 1 → right = 2
### 🔁 第 8 次：
```python
left = 1 (height = 8), right = 2 (height = 6)
width = 1
h = 6
area = 6
max_area = 49 ❌
```
right -= 1 → right = 1
### 🛑 迴圈結束（left == right）
### ✅ 最終結果：
```python
return max_area = 49
```

---

## ⏱ 複雜度分析 | Complexity Analysis

- 時間複雜度 Time: O(n)，因為 left／right 總共只移動 n 次左右。

- 空間複雜度 Space: O(1)，只使用固定數量變數，不依賴額外空間大小。

---

## 學到了什麼 | What I Learned

- 兩指針法可將 O(n²) 的暴力解優化至 O(n)

- 每次移動較矮指針有助於快速收斂至最優解

- 面積受限於較矮柱子的高度，理解這一點是解法精妙之處