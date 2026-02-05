# 📍 LeetCode 496 — Next Greater Element I | 下一個更大的元素

🔗 [題目連結] https://leetcode.com/problems/next-greater-element-i/

---

## 📄 題目說明 | Problem Description
### 中文

- 給你兩個陣列 nums1、nums2

- nums1 是 nums2 的子集合

- 對 nums1 中的每個元素，找出它在 nums2 中 右邊第一個比它大的數

- 如果不存在，回傳 -1

### English

For each element in nums1, find the next greater element to its right in nums2.
If it does not exist, return -1.

### Examples
- Example 1:

    - Input: nums1 = [4,1,2], nums2 = [1,3,4,2]
    - Output: [-1,3,-1]
    - Explanation: The next greater element for each value of nums1 is as follows:
        - 4 is underlined in nums2 = [1,3,4,2]. There is no next greater element, so the answer is -1.
        - 1 is underlined in nums2 = [1,3,4,2]. The next greater element is 3.
        - 2 is underlined in nums2 = [1,3,4,2]. There is no next greater element, so the answer is -1.
- Example 2:

    - Input: nums1 = [2,4], nums2 = [1,2,3,4]
    - Output: [3,-1]
    - Explanation: The next greater element for each value of nums1 is as follows:
        - 2 is underlined in nums2 = [1,2,3,4]. The next greater element is 3.
        - 4 is underlined in nums2 = [1,2,3,4]. There is no next greater element, so the answer is -1.
 
---

## 🧠 解題思路 | Solution Idea

- 這題我一開始真正想到、也一定寫得出來的流程是：
```css
外層：for 每個 nums1 的元素 x
內層：在 nums2 找到 x 的位置 j
第三步：從 j 的右邊開始，找第一個 > x 的數
```

- 👉 這個想法 100% 正確
- 👉 卡住通常是因為「第三步不知道怎麼翻成 for / if」

- 為什麼這題要用 stack？

    - 如果你對 nums1 的每個元素都：

        - 去 nums2 找位置

        - 再往右掃

- 時間會是 O(n^2)，而且流程容易寫亂。

---

## 🧩 關鍵轉換：把「人話」變成「電腦能跑的話」

1. 從 j + 1 開始

2. 一個一個看（for k）

3. 只要第一次 nums2[k] > x 就停（break）

4. 如果整圈沒找到，用 -1

---

## 💻 程式碼實作 | Code（穩定、好寫版本）
```python
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = []

        for x in nums1:                      # 外層：處理 nums1 的每個元素
            for j in range(len(nums2)):      # 內層：在 nums2 找位置
                if nums2[j] == x:
                    nxt = -1                 # 預設找不到
                    for k in range(j + 1, len(nums2)):  # 第三步：往右找
                        if nums2[k] > x:
                            nxt = nums2[k]
                            break            # 找到第一個就停
                    ans.append(nxt)           # 存結果
                    break                    # 這個 x 處理完了

        return ans
```
### 🔍 程式碼逐段說明 | Line-by-line Explanation
### 1️⃣ 外層 loop：我現在在處理哪一個元素
```python
for x in nums1:
```

- x 是現在要找 next greater 的目標

### 2️⃣ 第二層 loop：在 nums2 找到 x 的位置
```python
for j in range(len(nums2)):
    if nums2[j] == x:
```

- j 是 x 在 nums2 中的位置

- 這一層只負責「找位置」，不負責找答案

### 3️⃣ 第三層 loop：從右邊找第一個更大的
```python
nxt = -1
for k in range(j + 1, len(nums2)):
    if nums2[k] > x:
        nxt = nums2[k]
        break
```

- nxt = -1：先假設「找不到」

- k 從 j+1 開始，代表「右邊」

- 一旦找到第一個 > x：

    - 存起來

    - 立刻 break（因為只要第一個）

### 4️⃣ 存答案，但不要 return
```python
ans.append(nxt)
break
```

- append：存這個 x 的答案

- break：結束 nums2 的搜尋，換下一個 x

- ⚠️ 這裡不能 return，因為題目要的是 list

---

## 🧪 範例流程 | Example Walkthrough
Input
nums1 = [4,1,2]
nums2 = [1,3,4,2]

### x = 4

- 在 nums2 找到 4 在 j = 2

- 往右找：只有 2

- 2 > 4 ❌ → nxt 保持 -1

- append：ans = [-1]

### x = 1

- 找到 1 在 j = 0

- 往右找：3, 4, 2

- 第一個 > 1 是 3 → nxt = 3，break

- append：ans = [-1, 3]

### x = 2

- 找到 2 在 j = 3

- 右邊沒有元素 → for k 不會跑

- nxt 保持 -1

- append：ans = [-1, 3, -1]

### Output
```text
[-1, 3, -1]
```

---

## ⏱ 複雜度分析 | Complexity Analysis

- 時間複雜度：O(m * n)

    - m = len(nums1)

    - n = len(nums2)

    - 最差情況每個 x 都要掃完整個 nums2，還要再往右掃一次

- 空間複雜度：O(1)（不含輸出 ans）

---

## ✍️ 我學到的東西 | What I Learned

- 「找右邊第一個符合條件」的題目，基本套路就是：

    - 找到位置

    - 從位置右邊線性掃描

    - 找到第一個就 break

- 只要題目要回傳 list：

    - 不要在 loop 裡 return

    - 用 append + break 才能把所有答案收集完

---

## 🧠 一句話總結（面試時也能講）

For each element in nums1, I locate its position in nums2, then scan to the right to find the first greater element; if none exists, I return -1.

---

## Monotonic Stack
```python
class Solution:
    def nextGreaterElement(self, nums1, nums2):
        stack = []
        nxt = {}

        for num in nums2:
            while stack and num > stack[-1]:
                nxt[stack.pop()] = num
            stack.append(num)

        return [nxt.get(x, -1) for x in nums1]
```

### 🔍 程式碼逐段說明 | Line-by-line Explanation
### 1️⃣ 初始化 stack 與對照表
```python
stack = []
nxt = {}
```

- stack：存「還沒找到 next greater 的數字」

- nxt：

    - key：某個數字

    - value：它的 next greater element

### 2️⃣ 掃描 nums2（關鍵主流程）
```python
for num in nums2:
```

我們只掃 一次 nums2，答案就在這裡全部算好。

### 3️⃣ while：用現在的 num 解決 stack 裡的人
```python
while stack and num > stack[-1]:
    smaller = stack.pop()
    nxt[smaller] = num
```
- 這個 while 在幹嘛？

    - 意思是：只要現在的 num 比 stack 最上面的人大 👉 那我就是它的 next greater

- stack[-1]：最右邊、最近的、還在等答案的人

- pop 出來，立刻配對答案

### 4️⃣ 為什麼是 while，不是 if？

- 因為一個大的數，可能一次解掉好幾個人

- 例如：
    ```text
    stack = [5, 3, 1]
    num = 6
    ```

- 6 會：

    - 解 1

    - 再解 3

    - 再解 5

### 5️⃣ 把現在這個 num 放進 stack
```python
stack.append(num)
```

- 意思是：「我現在也還不知道我的 next greater，
先進 stack 等未來的人幫我」

### 6️⃣ 最後組答案（nums1）
```python
return [nxt.get(x, -1) for x in nums1]
```
- 對 nums1 裡的每一個 x，去字典 nxt 查 x 對應的值，查不到就用 -1，最後把結果組成一個 list 回傳。

- nxt.get(key, default)
    - 如果 key 在字典裡 → 回傳對應的 value

    - 如果 key 不在字典裡 → 回傳 default

- 如果 x 有在 nxt：

    - 回傳對應值

- 否則：

    - 代表右邊沒有更大的 → -1

---

## 🧪 範例流程 | Example Walkthrough
### Input
```text
nums1 = [4,1,2]
nums2 = [1,3,4,2]
```
### Step-by-step 跑 nums2
#### num = 1
```text
stack = []
→ push 1
stack = [1]
```
#### num = 3
```text
3 > 1 → pop 1
nxt[1] = 3
push 3
stack = [3]
```
#### num = 4
```text
4 > 3 → pop 3
nxt[3] = 4
push 4
stack = [4]
```
#### num = 2
```text
2 > 4 ❌
push 2
stack = [4, 2]
```
#### 結果對照表
```text
nxt = {
  1: 3,
  3: 4
}
```
#### 組 nums1 的答案
```text
4 → not in map → -1
1 → 3
2 → not in map → -1
```
#### Output
```text
[-1, 3, -1]
```

---

## ⏱ 複雜度分析 | Complexity Analysis

- 時間複雜度：O(n)

    - 每個元素最多進 stack 一次、出 stack 一次

- 空間複雜度：O(n)

    - stack + hashmap

---

## ✍️ 我學到的東西 | What I Learned

- monotonic stack 的本質不是「現在解題」

- 而是：把問題延後，交給未來更大的元素來解

- 記住三句話就夠：

    1. stack 裡是「還沒找到答案的人」

    2. 新來的如果比較大，就幫前面的人解答

    3. 解完再把自己放進 stack

---

## 🧠 一句話總結

I use a monotonic decreasing stack to process nums2 in one pass, where each element waits in the stack until a greater element appears to its right and resolves it.