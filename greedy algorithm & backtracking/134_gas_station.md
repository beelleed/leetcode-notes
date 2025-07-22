# ⛽ LeetCode 134 - Gas Station
🔗 [題目連結](https://leetcode.com/problems/gas-station/)

## 📝 題目說明 | Problem Description
### 中文：
有一個環形路線，共有 n 個加油站。每個加油站 i 有 gas[i] 單位的汽油。從加油站 i 到下一個加油站 (i + 1) % n 需要消耗 cost[i] 單位的汽油。你有一輛油箱容量無限的車，初始時油箱為空。請找出一個起始加油站的索引，使得你可以繞行一圈回到起點，否則返回 -1。

### English:
There are n gas stations along a circular route, where the amount of gas at the ith station is gas[i]. You have a car with an unlimited gas tank and it costs cost[i] of gas to travel from the ith station to its next (i + 1)th station. You begin the journey with an empty tank at one of the gas stations. Return the starting gas station's index if you can travel around the circuit once in the clockwise direction, otherwise return -1.

### 🔍 範例 | Examples
- Example 1:

    - Input: gas = [1,2,3,4,5], cost = [3,4,5,1,2]
    - Output: 3
    - Explanation:
        - Start at station 3 (index 3) and fill up with 4 unit of gas. Your tank = 0 + 4 = 4
        - Travel to station 4. Your tank = 4 - 1 + 5 = 8
        - Travel to station 0. Your tank = 8 - 2 + 1 = 7
        - Travel to station 1. Your tank = 7 - 3 + 2 = 6
        - Travel to station 2. Your tank = 6 - 4 + 3 = 5
        - Travel to station 3. The cost is 5. Your gas is just enough to travel back to station 3.
        - Therefore, return 3 as the starting index.
- Example 2:

    - Input: gas = [2,3,4], cost = [3,4,3]
    - Output: -1
    - Explanation:
        - You can't start at station 0 or 1, as there is not enough gas to travel to the next station.
        - Let's start at station 2 and fill up with 4 unit of gas. Your tank = 0 + 4 = 4
        - Travel to station 0. Your tank = 4 - 3 + 2 = 3
        - Travel to station 1. Your tank = 3 - 3 + 3 = 3
        - You cannot travel back to station 2, as it requires 4 unit of gas but you only have 3.
        - Therefore, you can't travel around the circuit once no matter where you start.

---

## 🧠 解題思路 | Solution Strategy
✅ 核心想法：
- 如果總油量小於總消耗，則無法完成一圈，返回 -1。

- 使用貪婪策略，從第 0 個加油站開始，累計油量差 tank += gas[i] - cost[i]。

    - 如果 tank 變為負數，表示無法從當前起點到達加油站 i + 1，因此將起點設為 i + 1，並重置 tank 為 0。

- 如果總油量差 total_tank >= 0，則返回起點索引；否則返回 -1。

---

## 💻 程式碼 | Python Code
```python
from typing import List

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        total_tank = 0
        current_tank = 0
        start_station = 0

        for i in range(len(gas)):
            net_gain = gas[i] - cost[i]
            total_tank += net_gain
            current_tank += net_gain

            if current_tank < 0:
                start_station = i + 1
                current_tank = 0

        return start_station if total_tank >= 0 else -1
```
### 🧾 程式碼解釋 | Code Explanation
```python
total_tank = 0
current_tank = 0
start_station = 0
```
- total_tank: 整體油量是否足夠跑完一圈（gas.sum() >= cost.sum()）。

- current_tank: 嘗試從某個起點出發，過程中剩餘的油量。

- start_station: 嘗試作為起點的站點編號。

#### 🔁 for 迴圈解釋
```python
for i in range(len(gas)):
    net_gain = gas[i] - cost[i]
```
- 表示每個站點的盈餘油量。例如：gas[i] = 3, cost[i] = 2，則多出 1 單位油可供繼續使用。
```python
total_tank += net_gain
current_tank += net_gain
```
- 加總所有盈餘油量，total_tank 用來判斷最終是否可行。

- current_tank 則用來看從目前的 start_station 出發能否成功跑下去。

#### ❌ 油不夠的情況
```python
if current_tank < 0:
    start_station = i + 1
    current_tank = 0
```
- 一旦從當前起點走到第 i 站時油量變負，說明從這個起點走不下去。

- 所以我們把起點換到 i + 1，並把 current_tank 重置為 0。

#### ✅ 最後判斷
```python
return start_station if total_tank >= 0 else -1
```
- 如果總油量夠跑完全程，回傳 start_station。

- 否則回傳 -1，表示哪裡都無法當起點完成一圈。

---

## ⏱ 時間與空間複雜度 | Time & Space Complexity
- 時間複雜度 Time Complexity: O(n)

- 空間複雜度 Space Complexity: O(1)

---

## 📈 圖解流程 | Visual Explanation
以下是 gas = [1,2,3,4,5]，cost = [3,4,5,1,2] 的圖解流程：

```plaintext
加油站索引:    0   1   2   3   4
gas:          1   2   3   4   5
cost:         3   4   5   1   2
net_gain:    -2  -2  -2  +3  +3
```
從加油站 3 開始：

- current_tank = 0

- 加油站 3：current_tank += 4 - 1 = 3

- 加油站 4：current_tank += 5 - 2 = 6

- 加油站 0：current_tank += 1 - 3 = 4

- 加油站 1：current_tank += 2 - 4 = 2

- 加油站 2：current_tank += 3 - 5 = 0

成功回到起點，返回起點索引 3。

---

## 📌 學習重點 | What I Learned
- 這題展示了貪婪策略在解決最小跳躍問題中的應用。

- 透過追蹤當前跳躍範圍內能到達的最遠位置，確保每次跳躍都能覆蓋更多的範圍，從而達到最少的跳躍次數。


