## ✅ LeetCode 560 - Subarray Sum Equals K

[題目連結](https://leetcode.com/problems/subarray-sum-equals-k/)

---

## 🧩 題目描述 | Problem Description

- 中文：給定一個整數陣列 nums 和一個整數 k，請你找出陣列中總和等於 k 的連續子陣列的個數。

- English: Given an integer array nums and an integer k, return the total number of continuous subarrays whose sum equals to k.

---

## 🧠 解題思路 | Approach

1.使用一個變數 prefix_sum 來記錄從陣列開始到當前元素的總和。

2.使用一個字典 sum_freq 來記錄每個前綴和出現的次數。

3.對於每個元素，計算當前的 prefix_sum，然後檢查 prefix_sum - k 是否在 sum_freq 中。如果存在，表示從之前某個位置到當前位置的子陣列總和為 k。

3.最後，將當前的 prefix_sum 加入到 sum_freq 中。

---

## 💻 程式碼 | Python Code
answer 1.
```python
from collections import defaultdict

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0                  # ✅ 記錄總共有幾段子陣列加總為 k
        prefix_sum = 0             # ✅ 記錄目前的累積總和
        sum_freq = defaultdict(int)
        sum_freq[0] = 1            # ✅ 初始化：代表從頭開始的情況（前綴和 = k）

        for num in nums:
            prefix_sum += num      # 👉 更新目前的總和
            if prefix_sum - k in sum_freq:
                count += sum_freq[prefix_sum - k]  # ✅ 找到符合條件的子陣列數量
            sum_freq[prefix_sum] += 1              # 👉 紀錄這個總和出現過一次


        return count
```
## 舉例
nums = [2, 3, 5, 6, 4, 10] k = 10
```python
prefix_sum = 0
count = 0
sum_freq = {0: 1}  # 前綴和為 0，出現過一次（處理從開頭開始的情況）
```
步驟逐一分析

第 1 步：num = 2

	- prefix_sum = 2

	- prefix_sum - k = -8 → 不在 sum_freq 中

	- 更新 sum_freq: {0:1, 2:1}

	- count = 0

⸻

第 2 步：num = 3

	- prefix_sum = 5

	- prefix_sum - k = -5 → 不在 sum_freq 中

	- 更新 sum_freq: {0:1, 2:1, 5:1}

	- count = 0

⸻

第 3 步：num = 5

	- prefix_sum = 10

	- prefix_sum - k = 0 → 在 sum_freq 中，出現過 1 次

	- count += 1 → count = 1 ✅

	- 更新 sum_freq: {0:1, 2:1, 5:1, 10:1}

	- 對應子陣列：[2, 3, 5]

⸻

第 4 步：num = 6

	- prefix_sum = 16

	- prefix_sum - k = 6 → 不在 sum_freq 中

	- 更新 sum_freq: {... , 16:1}

	- count = 1

⸻

第 5 步：num = 4

	- prefix_sum = 20

	- prefix_sum - k = 10 → 在 sum_freq 中，出現過 1 次

	- count += 1 → count = 2 ✅

	- 更新 sum_freq: {... , 20:1}

	- 對應子陣列：[6, 4]

⸻

第 6 步：num = 10

	- prefix_sum = 30

	- prefix_sum - k = 20 → 在 sum_freq 中，出現過 1 次

	- count += 1 → count = 3 ✅

	- 更新 sum_freq: {... , 30:1}

	- 對應子陣列：[10]
最終答案：count = 3

符合條件的子陣列：

	1.	[2, 3, 5]

	2.	[6, 4]

	3.	[10]

answer 2.
```python
def subarraySum(nums, k):
    count = 0
    prefix_sum = 0
    prefix_sums = {0: 1}  # 初始化，表示前綴和為0出現過一次

    for num in nums:
        prefix_sum += num
        # 檢查是否存在一個之前的 prefix_sum 使得 prefix_sum - k 存在
        if prefix_sum - k in prefix_sums:
            count += prefix_sums[prefix_sum - k]
        # 更新當前 prefix_sum 出現的次數
        prefix_sums[prefix_sum] = prefix_sums.get(prefix_sum, 0) + 1

    return count
```

sum_freq = defaultdict(int) 並設定 sum_freq[0] = 1
跟 sum_freq = {0: 1}
在初始化結果上是一樣的，但行為上有差別。

⸻

差別說明：

1. defaultdict(int) 的行為：

這是 Python 提供的一種「自動初始化」的字典，當你訪問一個不存在的 key時，它會自動建立該 key，並預設值為 0（因為 int() 預設為 0）。
```python
from collections import defaultdict

d = defaultdict(int)
print(d[100])  # 會輸出 0，不會報錯
```
2. 一般 dict：
```python
d = {0: 1}
print(d[100])  # KeyError，因為 100 不存在
```

所以：

	•	defaultdict(int) 是用來簡化程式邏輯的，讓你可以放心地對不存在的 key 做加法、不用先檢查。
	•	在這題中，它讓這行程式變得簡潔

    •	sum_freq[prefix_sum] += 1  

小結：

| 寫法                                             | 初始效果一樣 | 訪問不存在 key  | 適用情境            |
| ---------------------------------------------- | ------ | ---------- | --------------- |
| `sum_freq = {0: 1}`                            | 是      | 會報錯        | 小範圍內明確 key 的初始化 |
| `sum_freq = defaultdict(int); sum_freq[0] = 1` | 是      | 不會報錯，預設為 0 | 適合用在統計或累加場景     |

可以想成：defaultdict 只是幫你偷懶，自動補上初始值。

## ⏱️ 時間與空間複雜度 | Complexity
類別	複雜度
時間	O(n) → 只掃一次陣列
空間	O(n) → 最多記錄 n 種前綴和

--- 

## 🧠 學到的東西 | What I Learned
1.原來總和為 k 的連續子陣列可以轉換成「前綴和差值為 k」

2.HashMap 可以記錄出現過的累積總和次數，是這題的關鍵技巧

3.sum_freq[0] = 1 是非常重要的初始化，代表從頭開始就是一段解

## 📌 額外筆記建議 | Additional Notes
1.前綴和（Prefix Sum）：prefix_sum[i] 表示從陣列開始到第 i 個元素的總和。

2.差值概念：如果 prefix_sum[j] - prefix_sum[i] = k，則表示從第 i+1 到第 j 個元素的子陣列總和為 k。

3.初始化 sum_freq[0] = 1：這是為了處理從陣列開始的子陣列總和為 k 的情況。

## ✅ 題型歸類
1.Prefix Sum（前綴和）

2.HashMap

3.Sliding Window（邏輯上類似，但範圍不固定）