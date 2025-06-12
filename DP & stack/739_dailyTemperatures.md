# 🌡️ 739. Daily Temperatures

[LeetCode 題目連結](https://leetcode.com/problems/daily-temperatures/)

---

## 📘 題目描述 | Description

給定一個整數陣列 `temperatures`，表示每天的氣溫，請回傳一個相同長度的陣列 `res`，其中 `res[i]` 表示：從第 `i` 天起需等幾天第一次出現更高氣溫；若不存在更高溫則為 `0`。

---
## 🧠 解題思路說明 | Explanation
- 用 stack 存 index，以便回頭給前面還沒找到更高溫的天數答案

- 遍歷當前溫度：

    - 遇到更高溫，便把所有被 stack 遮住，在天數上等待的 index 一併 pop 出，並計算差值

- 最後 stack 中沒遇到更高溫的 index 自然對應 0

- 時間複雜度為 O(n)，因為每個 index 最多進、出一次 stack

---

## ✅ 解法（單調遞減堆疊）

```python
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []  # 存放“尚未找到更高溫”的天數 index
        res = [0] * len(temperatures)

        for i, temp in enumerate(temperatures):
            # 當 stack 不為空，且當前 temp 高於 stack top 所在天的溫度
            while stack and temp > temperatures[stack[-1]]:
                prev = stack.pop()
                res[prev] = i - prev  # 計算等待天數
            stack.append(i)

        return res
```
## 🧠 每一行的意思
```python
stack = []
res = [0] * len(temperatures)
```
- 初始化：stack 存的是 氣溫還沒變暖的「索引」

- res 是答案陣列，先全部填 

```python
for i, temp in enumerate(temperatures):
```
- 走過每天的溫度 temp，i 是當前天數

```python
while stack and temp > temperatures[stack[-1]]:
```
- 如果現在溫度 temp 比「堆疊最上層（之前的日子）」還高，表示：終於等到一個更熱的日子了！

```python
    prev_index = stack.pop()
    res[prev_index] = i - prev_index
```
- stack.pop() 拿出那個之前沒等到熱天的日子

- i - prev_index 計算「等了幾天」

- 填進 res[prev_index]

```python
stack.append(i)
```
- 把現在的索引記住，因為你還沒找到比今天更熱的日子

## 📊 範例模擬 | Example walkthrough
對 temperatures = [73, 74, 75, 71, 69, 72, 76, 73] 的處理：

    i=0：入 stack → [0]

    i=1：74 > 73 → pop→res[0]=1；stack=[1]

    i=2：75 > 74 → pop→res[1]=1；stack=[2]

    ...

    i=6：76 > 72/69/71/75 → pop 四次，更新 res 對應值

最終得到 [1,1,4,2,1,1,0,0]

##  技巧回顧 | What I Learned
- 單調遞減堆疊：stack 裡的 index 對應的溫度一直保持遞減

- 存的是 index 而非溫度值，用來計算天數差

- 溫度比較時判斷: temp > temperatures[stack[-1]] 是關鍵

- 模板可應用於「下次更大數字」的相關題目，如 Next Greater Element 系列