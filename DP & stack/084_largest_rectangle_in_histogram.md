# LeetCode 84：Largest Rectangle in Histogram
[LeetCode 題目連結](https://leetcode.com/problems/largest-rectangle-in-histogram/)

## 📄 題目說明 | Problem

給你一個整數陣列 heights，代表直條圖中每根柱子的高度，且每根柱子的寬度為 1。請你找出，在這個柱狀圖中可以形成的最大矩形面積。

- 中文：在這些相鄰的柱子中選一個區段選擇高度最低的柱子作為矩形的高度，寬度是選擇的柱子數量，求最大的矩形面積。

- English: Given an array heights where each bar has width = 1, find the area of the largest rectangle that can be formed in the histogram.

## Examples
- Example 1:

    ![](../images/84_histogram1.jpg)

    Input: heights = [2,1,5,6,2,3]
    
    Output: 10
    
    Explanation: The above is a histogram where width of each bar is 1. The largest rectangle is shown in the red area, which has an area = 10 units.

- Example 2:

    ![](../images/84_histogram2.jpg)

    Input: heights = [2,4]

    Output: 4

---

## 🧠 解題思路 | Solution Idea

- 直接的暴力法是對每根柱子往左右延伸，找出能延伸到的最大寬度，再乘以該柱子的高度。但這樣的做法是 O(n²)，對大輸入會超時。

- 最常見、高效的方法是使用 單調堆疊（Monotonic Stack）：
    - 我們想為每根柱子 i 找到它作為高度所能延伸的最左邊界和最右邊界（即離它最近的小於它高度的柱子）。

    - 用堆疊維持一個「高度遞增的柱子索引堆疊」。當遇到一根高度比堆疊頂還低的柱子時，就代表堆疊頂那根柱子的右邊界找到了：當前 i 是第一個比它低的柱子。

    - 當我們 pop 出一些索引時，就可以計算它們形成的矩形的寬度與面積。

    - 有時會在 heights 結尾加一個 0 或在迴圈中做額外步驟，以確保把堆疊中剩下的柱子都處理完。

- 這種做法可以做到 O(n) 時間，因為每個索引只會被 push 和 pop 一次。

---

## 💻 程式碼實作 | Python 範例
```python
from typing import List

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []  # Store indices of bars in increasing height order
        max_area = 0
        n = len(heights)
        
        # Add a virtual bar of height 0 to flush out the stack at the end
        for i in range(n + 1):
            current_height = 0 if i == n else heights[i]
            
            # While the current bar is lower than the one at the top of the stack
            while stack and (i == n or heights[stack[-1]] > current_height):
                h = heights[stack.pop()]  # Pop the top and treat it as height
                # Width is from the last lower bar index to current i
                width = i if not stack else (i - stack[-1] - 1)
                max_area = max(max_area, h * width)
            
            stack.append(i)  # Push current index into the stack
        
        return max_area
```
### 🔸 1. 初始化
```python
stack = []
max_area = 0
n = len(heights)
```
- stack：用來記錄柱子的索引，並保持高度遞增

- max_area：用來記錄目前為止最大矩形面積

- n：柱子的數量

### 🔸 2. 主迴圈 + 虛擬柱子處理
```python
for i in range(n + 1):
    current_height = 0 if i == n else heights[i]
```
- 透過 i == n 時加入一個虛擬高度為 0 的柱子，確保 stack 最後會清空

- current_height 是目前這一根柱子的高度

### 🔸 3. 處理「比當前柱子高」的 stack 元素
```python
while stack and (i == n or heights[stack[-1]] > current_height):
```
- 如果目前柱子比較矮，就說明 stack 頂端的柱子該結束了，可以開始計算面積
```python
h = heights[stack.pop()]
width = i if not stack else (i - stack[-1] - 1)
max_area = max(max_area, h * width)
```
- h 是要結束計算的那根柱子的高度

- width 是這根柱子所能延伸的左右寬度（左邊界是 stack 中前一個柱子的 index）

- 更新最大面積

### 🔸 4. 推入當前柱子的索引
```python
stack.append(i)
```
- 把目前這一根柱子的索引推進 stack，等待日後遇到「更矮的柱子」再來處理

### 🔸 5. 回傳結果
```python
return max_area
```

---

## 🧪 範例流程 | Example

以 heights = [2, 1, 5, 6, 2, 3] 為例來說明：

- 當 i = 0，stack 空 → push 0

- i = 1，heights[1] = 1 < heights[0] = 2 → pop 0，計算面積 h=2, width = 1 → area = 2 → 更新 max_area 然後 push 1

- 接下來 i = 2,3 推入 2, 3（因為高度遞增）

- 當 i = 4，heights[4] = 2，遇到比 6 更低、高於 5 也低 → pop 3, 2 分別計算

- 最後當 i = n（這裡 i = 6），取 current_height = 0，pop 出所有剩餘元素，分別計算面積

- 最終得到最大面積 10（由高度 5 或 6 那些柱子組成的區間）

---

## ⏱ 複雜度分析 | Complexity

- 時間複雜度：O(n)，每根柱子被 push 和 pop 最多一次。

- 空間複雜度：O(n)，堆疊最多存儲 n 個索引。

---

## ✍️ 我學到了什麼

- 單調堆疊是處理這類「向左右延伸 + 限制高度」問題的經典技巧。

- 加上額外的一根高度 0（或在迴圈裡模擬）是為了確保最後能把堆疊清空，計算所有可能的矩形。

- 面試時講這題，要能講出為什麼 pop 時可以確定右邊界、為什麼可以算寬度、為什麼那樣設 width = i - stack[-1] - 1。

- 小心處理堆疊為空的情況（那時寬度 = i，而不是差值減一）。