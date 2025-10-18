# 🌲 LeetCode 124 — Binary Tree Maximum Path Sum
🔗 題目連結：[https://leetcode.com/problems/binary-tree-maximum-path-sum/](https://leetcode.com/problems/binary-tree-maximum-path-sum/)

---

## 📄 題目說明 | Problem Description

### **中文**：

給你一棵二元樹（binary tree），找出其中任意一條路徑（path）的最大和。這條路徑可以從任意節點開始，也可以在任意節點結束，但每個節點只能用一次，且節點之間要有父子邊相連。 

### **English**: 
Given a binary tree, find the maximum path sum of any path. The path can start and end at any node in the tree, but you can only traverse parent-child connections and can’t reuse nodes.

### Examples
- Example 1:

![](../images/124_exx1.jpg)

    Input: root = [1,2,3]
    
    Output: 6
    
    Explanation: The optimal path is 2 -> 1 -> 3 with a path sum of 2 + 1 + 3 = 6.

- Example 2:

![](../images/124_exx2.jpg)

    Input: root = [-10,9,20,null,null,15,7]

    Output: 42

    Explanation: The optimal path is 15 -> 20 -> 7 with a path sum of 15 + 20 + 7 = 42.

---

## 🧠 解題思路 | Solution Idea

關鍵: **從每個節點作為「最高點（peak）」或者「轉折點」** 計算可能的最大路徑，同時又要考慮當節點向上貢獻路徑給父節點時只能選擇其左右子樹的一邊。

1. 用 DFS 遞迴（post‑order：先算左子樹、右子樹，再算自己）遍歷整顆樹。  
2. 對於任一節點 node，先從左子樹和右子樹取得貢獻值（即從那邊往下能得到的最大正路徑值），記為 `left_gain`、`right_gain`。  
   - 如果某邊的貢獻為負數，ignore（把負數當作 0 用），因為加上負數只會讓總和變小。  
3. 計算「從左 + node + 右」的組合，這是以 node 為最高點、穿過 node 的最大的路徑和，更新全局最大值。  
4. 回傳給父節點能用的最大「單側子樹 + node」的值（不能左右都加給父節點，因為父節點往上只能走一條分支）。

---

## 💻 程式碼實作 | Code (Python)

```python
from typing import Optional

class TreeNode:
    def __init__(self, val: int = 0, left: Optional['TreeNode'] = None, right: Optional['TreeNode'] = None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.max_sum = float('-inf')

        def dfs(node: Optional[TreeNode]) -> int:
            if not node:
                return 0

            # 計算左子樹對這條路徑能提供的最大正貢獻
            left_gain = max(dfs(node.left), 0)
            # 同理右子樹
            right_gain = max(dfs(node.right), 0)

            # 計算經過這個節點，把左右貢獻都加上的路徑總和
            current_max_path = node.val + left_gain + right_gain

            # 更新全局最大路徑和
            self.max_sum = max(self.max_sum, current_max_path)

            # 回傳給父節點的最大「單側貢獻」，父節點只能選擇 left 或 right
            return node.val + max(left_gain, right_gain)

        dfs(root)
        return self.max_sum
```
| 區段                                                                            | 功能                                            | 為什麼這樣寫                              |
| ----------------------------------------------------------------------------- | --------------------------------------------- | ----------------------------------- |
| `self.max_sum = float('-inf')`                                                | 初始化一個全域變數來追蹤目前見過的最大路徑和                        | 因為節點值可以是負的，如果初始化為 0 的話可能錯過全負的最大路徑場景 |
| 定義 `dfs(node)` 函式                                                             | 做遞迴，自底向上計算每個節點對上一層的「貢獻」 + 更新最大路徑              | 要探訪所有節點，且子節點先算，父節點再用子節點結果           |
| `if not node: return 0`                                                       | 基本情況：空節點對路徑和的貢獻為 0                            | 空節點不能貢獻，避免遞迴 None 帶來錯誤              |
| `left_gain = max(dfs(node.left), 0)` 和 `right_gain = max(dfs(node.right), 0)` | 算左右子樹對這條路徑可以加的最大正貢獻；如果貢獻是負的，就不要用（取 0）         | 否則如果子樹值是負值，加上會降低總和，最好忽略該方向          |
| `current_max_path = node.val + left_gain + right_gain`                        | 計算如果這個節點作為「頂點」(peak)，同時接受左右的貢獻，經過 node 的最大路徑和 | 因為路徑可以通過這個節點，上下左右連接左右兩邊             |
| `self.max_sum = max(self.max_sum, current_max_path)`                          | 更新整棵樹中見過的最大路徑和                                | 確保考慮所有節點做為中間節點的情況                   |
| `return node.val + max(left_gain, right_gain)`                                | 回傳給父節點的最大「單一路徑貢獻」，父節點不能同時往左和往右繼續，只能選一邊        | 父節點如果要連接這子樹的話，只能選左右中比較大的一條來延伸       |

---

## 🧪 範例流程

假設樹是：
```markdown
       -10
       /  \
      9    20
          /  \
        15    7
```
初始 self.max_sum = -∞

遞迴流程（post‑order）：

1. dfs(9)

    - 左子、右子都是 None → left_gain = 0, right_gain = 0

    - current_max_path = 9 + 0 + 0 = 9

    - 更新 self.max_sum = max(-∞, 9) = 9

    - 返回 9 + max(0, 0) = 9

2. dfs(15) → 類似，得 15，更新 self.max_sum → 15

3. dfs(7) → 得 7，self.max_sum 保持 15

4. dfs(20)

    - 左子 dfs(15) 給 15, 右子 dfs(7) 給 7

    - left_gain = max(15,0) = 15, right_gain = max(7,0) = 7

    - current_max_path = 20 + 15 + 7 = 42

    - 更新 self.max_sum = max(15,42) = 42

    - 返回給父：20 + max(15,7) = 35

5. dfs(-10)

    - 左子給 9，右子給 35

    - left_gain = max(9,0) = 9, right_gain = max(35,0) = 35

    - current_max_path = -10 + 9 + 35 = 34

    - self.max_sum = max(42,34) = 42

    - 返回 (不重要給父，因為這是 root)

6. 最後回傳 self.max_sum = 42

---

## ⏱ 複雜度分析 | Time & Space Complexity
| 分類          | 複雜度                                                                 |
| ----------- | ------------------------------------------------------------------- |
| 時間複雜度 Time  | **O(n)**，每個節點恰好被 DFS 遍歷一次，且每個節點做 O(1) 的操作（計算左右貢獻 + 更新全局最大 + 回傳單側最大） |
| 空間複雜度 Space | **O(h)**，h 是樹的高度，因為 DFS 遞迴堆疊深度最多是樹高；最壞情況（樹是一條鏈）是 O(n)               |

---

## ✍️ 我學到了什麼 | What I Learned

- 當路徑可以從任意節點開始與結束時，需要考慮“經過節點的路徑 + 往上能傳給父節點的那條路徑”這兩種不同的值。

- 負數子樹的貢獻要做處理（當作 0 忽略），非常重要，否則路徑會被拖垮。

- DFS(post-order) 很適合這種「從子節點回傳值 + 更新全局最大」的題型。

- 在面試講這題時，說明為什麼要兩種貢獻（through node + 單側貢獻給父節點）是面試官會留意的部分。