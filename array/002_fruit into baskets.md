## 904. Total Fruit
LeetCode 題目連結: https://leetcode.com/problems/fruit-into-baskets/

🧩 題目描述（中文）
你有一排樹，每棵樹上長著一種水果，用整數表示。你只能拿兩個籃子，每個籃子只能裝一種水果。你要從某棵樹開始，往右連續採水果，直到你不能再裝進這兩個籃子為止。請找出你最多可以採多少個水果。

🧩 Problem Description (English)
You have a row of trees, each bearing one type of fruit represented by an integer. You may carry only two baskets, and each basket can hold only one type of fruit. Starting from any tree, you must collect fruit moving continuously to the right until you can no longer carry fruit. Find the maximum number of fruits you can collect.

💡 解法說明 | Solution Explanation
我們使用「滑動視窗」（sliding window）技巧，維護一個視窗內最多兩種水果。每當加入第三種水果，就從左邊開始縮小視窗，直到回到只有兩種為止。這樣就能在 O(n) 時間內找出所有合法視窗的最大長度。

We use the sliding window technique to maintain a window with at most two types of fruits. Each time a third type is encountered, we shrink the window from the left until only two remain. This allows us to find the maximum valid subarray in O(n) time.

from typing import List

---

## ✅ 正確解法（滑動視窗 + HashMap）
```python
class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        count, i = {}, 0               # 🇨🇳 初始化計數字典與左指標 i（滑動視窗的起點）
                                       # 🇺🇸 Initialize count map and left pointer i (start of sliding window)

        max_len = 0                    # 🇨🇳 記錄目前為止最大視窗長度
                                       # 🇺🇸 Track the maximum window size found

        for j, v in enumerate(fruits): # 🇨🇳 使用 j 為右指標，v 為當前水果類型
                                       # 🇺🇸 j is the right pointer, v is the fruit type at position j

            count[v] = count.get(v, 0) + 1
            # 🇨🇳 把當前水果加入計數字典中，如果之前沒看過則從 0 開始加
            # 🇺🇸 Increment the count of current fruit type; start from 0 if unseen

            while len(count) > 2:
                # 🇨🇳 如果視窗中水果種類超過 2 種，開始縮小左邊界
                # 🇺🇸 If more than 2 types in window, shrink the window from the left

                count[fruits[i]] -= 1
                # 🇨🇳 減少左邊水果的數量
                # 🇺🇸 Decrease count of the leftmost fruit

                if count[fruits[i]] == 0:
                    del count[fruits[i]]
                    # 🇨🇳 如果某水果數量歸 0，從字典中移除
                    # 🇺🇸 Remove the fruit from the map if its count drops to 0

                i += 1
                # 🇨🇳 左指標右移一格
                # 🇺🇸 Move the left pointer one step to the right

            max_len = max(max_len, j - i + 1)
            # 🇨🇳 更新目前為止最大視窗長度（j - i + 1 為當前視窗長度）
            # 🇺🇸 Update max length if current window is longer

        return max_len
        # 🇨🇳 回傳結果：最大視窗長度
        # 🇺🇸 Return the maximum window length

```
⏱️ 時間與空間複雜度（Time & Space Complexity）
時間：O(n)，每個元素最多被訪問兩次

空間：O(1)，最多儲存兩種水果的 count

---
## 📝 學習筆記整理（Learning Notes）
✅ 視窗設計與條件收縮：

1.左指標 i 不斷移動以排除多餘水果
2.視窗內永遠只會有 兩種水果或更少

✅ 知識點補充：
dict.get(k, 0)：取出 key 值，如果不存在則回傳 0

j - i + 1：表示當前視窗長度（從 i 到 j）

📌 額外筆記建議（Extra Notes）
✅ 雙指標定義說明：
i: 左指標 → 視窗的起始位置（window left boundary）

j: 右指標 → 每次向右擴展一格，代表視窗的尾端（window right boundary）

✅ 為什麼滑動視窗是「右擴左縮」？
每次我們嘗試「擴大視窗」（j += 1）來找更長的合法區間。

但一旦發現 超出條件（超過 2 種水果），就從左邊開始縮小（i += 1）。

這種結構確保我們可以「每次找出合法最大區段」，同時不漏解也不多算。

✅ 為什麼要移動 left？
題目要求最多只能裝兩種水果，所以：

當我們遇到第 3 種水果時，就必須把最左邊那種慢慢移除掉。

不這麼做會讓 count 字典超過兩種 → 違反題意。

