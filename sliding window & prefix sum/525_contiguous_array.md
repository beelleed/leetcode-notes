# 525. Contiguous Array – 最長連續子陣列，0 和 1 數量相等
🔗 [題目連結](https://leetcode.com/problems/contiguous-array/)

---

## 📘 題目描述 | Problem Description

- **中文**：給定一個只包含 0 和 1 的二元陣列 `nums`，返回其中包含 **相等數量的 0 和 1** 的 **最長連續子陣列** 的長度。
- **English**: Given a binary array `nums`, return the maximum length of a **contiguous subarray** with an **equal number of 0s and 1s**.
### Examples
- Example 1:

    - Input: nums = [0,1]
    - Output: 2
    - Explanation: [0, 1] is the longest contiguous subarray with an equal number of 0 and 1.
- Example 2:

    - Input: nums = [0,1,0]
    - Output: 2
    - Explanation: [0, 1] (or [1, 0]) is a longest contiguous subarray with equal number of 0 and 1.
- Example 3:

    - Input: nums = [0,1,1,1,1,1,0,0,0]
    - Output: 6
    - Explanation: [1,1,1,0,0,0] is the longest contiguous subarray with equal number of 0 and 1.

---

## 💡 解題思路 | Solution Idea
### 中文
透過「前綴和 + 哈希表」的技巧，以 O(n) 的時間複雜度解題：

- 將 `0` 視為 `-1`，`1` 視為 `+1`。這樣累加後，**出現相同累計和**表示 0 和 1 在那段區間是平衡的。
- 使用一個字典 `mp` 存儲每個 `sum`（累加值）第一次出現的索引。
- 若該 `sum` 再次出現，即代表該區段 0 和 1 數量相等，可以利用當前索引減去第一次出現的索引得到子陣列長度。

### English
By using the technique of prefix sum + hash map, we can solve this problem in O(n) time complexity:

- Treat each 0 as -1 and each 1 as +1. With this transformation, when the same prefix sum appears more than once, it indicates that the number of 0s and 1s are balanced in that subarray.

- Use a dictionary mp to store the first occurrence index of each prefix sum.

- When the same sum appears again, it means that the subarray between the previous index and the current index is balanced. The length can be calculated as current_index - first_occurrence.

---

## 🧾 Python 程式碼

```python
class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        mp = {0: -1}         # 初始前綴和 0 在 -1 處先出現
        sum = 0              # running sum，以 +1 為 1，-1 為 0
        max_len = 0

        for i, num in enumerate(nums):
            if num == 1:
                sum += 1
            else:
                sum -= 1

            if sum in mp:  # 曾出現過 same sum
                max_len = max(max_len, i - mp[sum])
            else:
                mp[sum] = i  # 第一次出現 sum

        return max_len
```
```python
mp = {{0: -1}}
```
- 初始化：讓「sum = 0」出現在 index = -1 的位置。

為什麼這樣做？為了讓從 index 0 開始的區間也能被正確計算。

```python
sum = 0
max_len = 0
```
- sum: 累積和（遇到 1 +1，遇到 0 -1）

- max_len: 紀錄目前為止找到的最長平衡子陣列長度
```python
for i, num in enumerate(nums):
```
- 遍歷 nums 每一個元素，i 是索引，num 是值（0 或 1）
```python
if num == 1:
    sum += 1
else:
    sum -= 1
```
- 把 0 當成 -1、1 當成 +1

- 這樣當某段區間總和為 0，就代表 0 和 1 數量相同

```python
if sum in mp:
    max_len = max(max_len, i - mp[sum])
```
- 如果這個累積和 sum 已經出現過（mp[sum] 有記錄）

- 代表從 mp[sum] + 1 到現在的 i，是一段平衡子陣列

- 計算長度 i - mp[sum]，並更新最大值
```python
else:
    mp[sum] = i
```
- 如果這是第一次出現這個 sum，就把當前索引記下來

- 不可以覆蓋，因為我們只關心「最早」出現的 sum（這樣區間會最長）

## 🧪 範例模擬：nums = [0,1,0,1,1]
每一步紀錄：

| i | num | sum | mp           | 是否更新 max\_len | max\_len |
| - | --- | --- | ------------ | ------------- | -------- |
| 0 | 0   | -1  | {0:-1, -1:0} | 否             | 0        |
| 1 | 1   | 0   | 已出現：0\@-1    | ✅ 1-(-1)=2    | 2        |
| 2 | 0   | -1  | 已出現：-1\@0    | ✅ 2-0=2       | 2        |
| 3 | 1   | 0   | 已出現：0\@-1    | ✅ 3-(-1)=4    | 4        |
| 4 | 1   | 1   | 首次出現         | 否             | 4        |
✅ 最終結果：
- 回傳 max_len = 4，即子陣列 [0,1,0,1] 是最長的平衡區段。

---

## ⏱ 時間與空間複雜度分析
### 🕒 時間複雜度（Time Complexity）：O(n)
- 每個元素只遍歷一次（for loop）

- 每次查詢與更新哈希表都是 O(1)

- 所以總體是 O(n)

### 🧠 空間複雜度（Space Complexity）：O(n)
- 最壞情況下 sum 每次都不同，需要存進 map

- 哈希表最多儲存 n+1 個鍵值對（包含 sum = 0 的初始情況）

---

## 📚 我學到了什麼 | What I Learned
- 將 0 視為 -1，這種「轉換技巧」常用於二元陣列處理平衡問題

- 使用 prefix sum + 哈希表快速記錄平衡點的位置

- 只記錄 第一次出現該 sum 的位置，是為了讓子陣列最長

- 題目本身是「平衡區間」問題的變形，在很多變體中都有應用