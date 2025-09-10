# 🌧 LeetCode 42 – Trapping Rain Water | 接水最多
🔗 題目連結：[https://leetcode.com/problems/trapping-rain-water](https://leetcode.com/problems/trapping-rain-water/)

---

## 📄 題目說明 | Problem Description

- **中文**：給定一個非負整數陣列 `height`，每個元素代表地面高度，問下雨後這些區域能接多少雨水。

- **English**: Given `n` non-negative integers representing an elevation map where the width of each bar is 1, compute how much rain water it can trap after raining.

- **Examples**
    - Example 1:

    ![](../images/42_rainwatertrap.png)

        Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]

        Output: 6

        Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.

- Example 2:

    - Input: height = [4,2,0,3,2,5]
    - Output: 9

---

## 🧠 解題思路 | Solution Approach

我們可以用 **動態規劃（雙向預計算）** 或 **雙指針優化**：

### 動態規劃（DP）版本：
- **中文:** 
    1. 構建兩個陣列 `left_max` 和 `right_max`，分別記錄每個位置左邊（含自身）和右邊（含自身）的最大高度值。  
    2. 雨水高度 = `min(left_max[i], right_max[i]) - height[i]`。  
    3. 把每個位置能儲水的量加總起來即可得答案。

- **English:**  
    1. Create two arrays `left_max` and `right_max` that store the max height to the left (inclusive) and right (inclusive) for each position.  
    2. The water trapped at the `i`th index is `min(left_max[i], right_max[i]) - height[i]`.  
    3. Sum it up for all `i` to get the total trapped rainwater.

### 雙指針優化版本：

從左右兩端往中間進行收縮，追蹤左／右最大高度並累計可託水量，效率更高（O(n)、O(1) 空間）。

---

## 💻 程式碼 | DP 實作範本

```python
from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        if n <= 2:
            return 0

        left_max = [0] * n
        right_max = [0] * n
        left_max[0] = height[0]
        right_max[-1] = height[-1]

        for i in range(1, n):
            left_max[i] = max(left_max[i-1], height[i])
        for i in range(n-2, -1, -1):
            right_max[i] = max(right_max[i+1], height[i])

        total_water = 0
        for i in range(n):
            total_water += min(left_max[i], right_max[i]) - height[i]

        return total_water
```
```python
n = len(height)
if n <= 2:
    return 0
```
- 如果 height 的長度小於等於 2，就不可能形成「凹槽」來儲水，直接回傳 0。
```python
left_max = [0] * n
right_max = [0] * n
```
- 初始化兩個長度為 n 的陣列：

    - left_max[i]: 表示從左到第 i 根柱子為止的最高高度。
    - right_max[i]: 表示從右到第 i 根柱子為止的最高高度。
```python
left_max[0] = height[0]
right_max[-1] = height[-1]
```
- 初始化最邊界的最大值：第一個位置的左邊最大值就是它自己；最後一個位置的右邊最大值也是它自己。
```python
for i in range(1,n):
    left_max[i] = max(left_max[i - 1], height[i])
```
- 從左向右走，更新每個位置的左邊最大值（含自己）。例如：

    - left_max[i] = 左邊最高的柱子高度 vs 自己高度的最大值。
```python
for i in range(n - 2, -1, -1):
    right_max[i] = max(right_max[i + 1], height[i])
```
- 從右向左走，更新每個位置的右邊最大值（含自己）。
```python
total_water = 0
for i in range(n):
    total_water += min(left_max[i], right_max[i] - height[i])
```
- 計算每個位置可以接住多少水：

    - 「可接水高度」 = 左右最大值中的較小者 - 自己的高度。

    - 若結果為負，則代表此處無法接水（因為柱子已經比左右高）。

    - 將所有位置的儲水量加總得出 total_water。
```python
return total_water
```
- 回傳總共能接住的雨水量

### 範例
假設 height = [3, 0, 2, 0, 4]：
```makefile
left_max:  [3, 3, 3, 3, 4]
right_max: [4, 4, 4, 4, 4]
```
儲水計算如下：
| index (i) | height\[i] | min(left\_max, right\_max) | trapped water |
| --------- | ---------- | -------------------------- | ------------- |
| 0         | 3          | min(3, 4) = 3              | 0             |
| 1         | 0          | min(3, 4) = 3              | 3             |
| 2         | 2          | min(3, 4) = 3              | 1             |
| 3         | 0          | min(3, 4) = 3              | 3             |
| 4         | 4          | min(4, 4) = 4              | 0             |
| **Total** |            |                            | **7**         |

---

## ⏱ 複雜度分析 | Complexity Analysis
| 類型    | 複雜度                  |
| ----- | -------------------- |
| 時間複雜度 | O(n) — 遍歷常數次         |
| 空間複雜度 | O(n) — 使用三個長度為 n 的陣列 |

---

## 我學到了什麼 | What I Learned

- 用雙向預計算 (left_max, right_max) 是解這類柱狀模型題型的經典方法。

- 精準找出每個位置可儲水的高度 = min(左右最大值) - 本身高度。

- 時間和空間都能保持在線性級別。