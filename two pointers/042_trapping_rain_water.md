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

🔄 for i in range(n - 2, -1, -1) 是什麼意思？

這一行代表：

- i 從 n - 2 開始（倒數第二個 index）

- 每次遞減 1（因為第三個參數是 -1）

- 到 0 結束（含 0）

也就是說：從右往左走整個陣列

🤔 為什麼要從倒數第二個 index 開始？
- 因為最右邊那個 right_max[n-1]，沒有右邊了！

- 所以它自己的「右邊最大值」就是自己 ➜ right_max[n-1] = height[n-1]

---

💡 右邊一格一格往左更新，為什麼用 i + 1？

- 是因為雖然我們從右往左走（i = n-2 → 0），但我們在用 i + 1 拿「右邊一格」的資訊來幫助計算目前 i 的最大值。

### 🧱 假設 height 是這樣：
```python
height = [2, 1, 5, 3]
```
➡️ 我們要建立 right_max，從右往左算：

初始：
```python
right_max = [0, 0, 0, 3]  # 最右邊就是 height[3] = 3
```
接下來從 i = 2 開始：
```python
right_max[2] = max(right_max[3], height[2]) = max(3, 5) = 5
```
再來 i = 1：
```python
right_max[1] = max(right_max[2], height[1]) = max(5, 1) = 5
```
再來 i = 0：
```python
right_max[0] = max(right_max[1], height[0]) = max(5, 2) = 5
```
✅ 結果：
```python
right_max = [5, 5, 5, 3]
```

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

### 範例 1
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

### 範例二
### 🧾 Step 1：初始化
```python
n = 12
left_max = [0] * n
right_max = [0] * n
left_max[0] = height[0] = 0
right_max[-1] = height[-1] = 1
```
### ⬅️ Step 2：建立 left_max
```python
for i in range(1, n):
    left_max[i] = max(left_max[i - 1], height[i])
```
| i  | height\[i] | left\_max\[i-1] | left\_max\[i] |
| -- | ---------- | --------------- | ------------- |
| 1  | 1          | 0               | 1             |
| 2  | 0          | 1               | 1             |
| 3  | 2          | 1               | 2             |
| 4  | 1          | 2               | 2             |
| 5  | 0          | 2               | 2             |
| 6  | 1          | 2               | 2             |
| 7  | 3          | 2               | 3             |
| 8  | 2          | 3               | 3             |
| 9  | 1          | 3               | 3             |
| 10 | 2          | 3               | 3             |
| 11 | 1          | 3               | 3             |

🔹 最後 left_max = [0,1,1,2,2,2,2,3,3,3,3,3]
### ➡️ Step 3：建立 right_max
```python
for i in range(n - 2, -1, -1):
    right_max[i] = max(right_max[i + 1], height[i])
```
| i  | height\[i] | right\_max\[i+1] | right\_max\[i] |
| -- | ---------- | ---------------- | -------------- |
| 10 | 2          | 1                | 2              |
| 9  | 1          | 2                | 2              |
| 8  | 2          | 2                | 2              |
| 7  | 3          | 2                | 3              |
| 6  | 1          | 3                | 3              |
| 5  | 0          | 3                | 3              |
| 4  | 1          | 3                | 3              |
| 3  | 2          | 3                | 3              |
| 2  | 0          | 3                | 3              |
| 1  | 1          | 3                | 3              |
| 0  | 0          | 3                | 3              |

🔹 最後 right_max = [3,3,3,3,3,3,3,3,2,2,2,1]

### 💧 Step 4：計算總雨水量
```python
total_water = 0
for i in range(n):
    total_water += min(left_max[i], right_max[i]) - height[i]
```
| i  | min(left, right) | height\[i] | water |
| -- | ---------------- | ---------- | ----- |
| 0  | min(0,3)=0       | 0          | 0     |
| 1  | min(1,3)=1       | 1          | 0     |
| 2  | min(1,3)=1       | 0          | 1     |
| 3  | min(2,3)=2       | 2          | 0     |
| 4  | min(2,3)=2       | 1          | 1     |
| 5  | min(2,3)=2       | 0          | 2     |
| 6  | min(2,3)=2       | 1          | 1     |
| 7  | min(3,3)=3       | 3          | 0     |
| 8  | min(3,2)=2       | 2          | 0     |
| 9  | min(3,2)=2       | 1          | 1     |
| 10 | min(3,2)=2       | 2          | 0     |
| 11 | min(3,1)=1       | 1          | 0     |

🔢 總和：1 + 1 + 2 + 1 + 1 = 6

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