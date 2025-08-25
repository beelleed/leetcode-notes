# 001. Two Sum

[題目連結](https://leetcode.com/problems/two-sum/)

---

## ✅ English Summary

**Problem:** Given an array of integers `nums` and a target value, return indices of the two numbers such that they add up to the target.  
**Approach:**  
- Iterate through `nums`, and for each element, calculate `target - num`
- Check if the complement exists in a hash map
- If yes, return the index of the complement and the current index
- Otherwise, store the current number with its index in the hash map

**Time Complexity:** O(n)  
**Space Complexity:** O(n)

---

## 題目描述

給定一個整數陣列 `nums` 和一個整數目標值 `target`，請回傳陣列中「兩個不同元素的索引」，使得這兩個元素的和等於 `target`。每個輸入只會有一組解答。

---

## 嘗試錯誤一：比較的是索引而不是數值

```python
for i in range(len(nums)):
    for j in range(len(nums)):
        if i + j == target:  # 錯誤：這裡是 index 相加
            return [i, j]
```

錯誤點：

題目要求是「nums[i] + nums[j] == target」，不是索引相加。

因為 i 和 j 是位置，我誤以為題目要我找「兩個位置加總 = target」，這其實很常見但危險的直覺錯誤。

---

## 嘗試錯誤二：index 相同會出錯

```python
for i in range(len(nums)):
    for j in range(len(nums)):
        if nums[i] + nums[j] == target:  # 會有 i == j 的情況
            return [i, j]
```

錯誤點：

當 i == j 時，相當於用自己加自己，不符合「兩個不同元素」的條件。

範例中若 target = 6，而 nums[3] = 3，程式會回傳 (3, 3)，這是錯誤解。

---

## 修正後的解法（正確）

```python
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):  # 從 i+1 開始，避免 i == j
                if nums[i] + nums[j] == target:
                    return [i, j]
```
時間複雜度：O(n²)
雙層迴圈，對每一個元素都檢查其後面所有元素。

空間複雜度：O(1)
沒有使用額外空間，只用兩個變數。

---

## 優化解法：Hash Map（線性解）

```python
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}  # key: number, value: index
        for i, num in enumerate(nums):
            complement = target - num
            if complement in hashmap:
                return [hashmap[complement], i]
            hashmap[num] = i
```

解法說明（逐行解析）
hashmap = {}
建立一個空的字典來儲存「我們已經看過的數字」和它對應的 index。

for i, num in enumerate(nums):
同時取得每個元素的 index（i）和數值（num）。

complement = target - num
想要找的另一個數字（配對數）是 target - num。

if complement in hashmap:
如果配對數在 hashmap 裡，代表之前出現過，那麼你就找到答案了！

return [hashmap[complement], i]
回傳先前那個數字的 index 和現在這個的 index。

hashmap[num] = i
如果還沒找到，就把目前的數字和它的 index 記進 hashmap，讓下一輪用得到。

時間複雜度：O(n)
每個元素只看一次，用 hashmap 加速查找。

空間複雜度：O(n)
用一個 dict 儲存數字與索引對應關係。

學習心得

Hash Map 是解這種「查找配對」類題目的利器。

*if target - num in hashmap:* 幾乎是模板。

---

## 範例
- 假設：nums = [2, 7, 11, 15], target = 9
- 步驟：
    1. i = 0, num = 2

       complete = 9 - 2 = 7

       hashmap = {} → 補數 7 不在 hashmap

       存入 hashmap → {2: 0}

    2. i = 1, num = 7

       complete = 9 - 7 = 2
       
       hashmap = {2: 0} → 補數 2 已存在
       
       ✅ 回傳 [0, 1]

---

## 解題心得與學習筆記

- 這題是 LeetCode 刷題的經典入門題，幫助我練習：

- 如何正確理解題目敘述

- 寫出暴力解、再優化成更快的方法

- HashMap 是解題的利器（記得 target - num 的技巧）

- 我也學到要非常小心 index 與值的差異，還有 index 是否會重複的問題。