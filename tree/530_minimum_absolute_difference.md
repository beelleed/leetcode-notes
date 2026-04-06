# 📍 LeetCode 530 — Minimum Absolute Difference in BST

🔗 [題目連結](https://leetcode.com/problems/minimum-absolute-difference-in-bst/)

---

## 🧠 題目核心

👉 給一棵 BST
👉 找任意兩個節點之間的最小差值

---

## 🎯 關鍵觀察

👉 BST 的 inorder traversal = sorted array

👉 如果是排序好的：

👉 最小差值一定發生在「相鄰元素」之間

---

## 🔥 關鍵結論

❗不用比較所有 pair
❗只要比較「當前 node 和前一個 node」

---

## 🧩 解法思路（一步一步）

1. 用 inorder traversal（左 → 中 → 右）
2. 用 prev 記錄上一個值
3. 每次 visit：
```python
node.val - prev
```
4. 更新最小值

---

## 🧠 Template（核心骨架）
```python
dfs(node.left)

if prev exists:
    計算差值

更新 prev

dfs(node.right)
```

---

## ✍️ Code
```python
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        self.min = float('inf')
        self.prev = None

        def dfs(node):
            if not node:
                return
            
            dfs(node.left)

            if self.prev is not None:
                self.min = min(self.min, node.val - self.prev)

            self.prev = node.val

            dfs(node.right)

        dfs(root)
        return self.min
```

---

## ⚠️ 常見錯誤
### ❌ 忘記 base case
```python
if not node:
    return
```
### ❌ 沒檢查 prev
```python
node.val - None  ❌
```
### ❌ 更新順序錯

👉 一定要：先算差值 → 再更新 prev

### ❌ 想用兩層 loop（錯誤方向）

👉 不需要 O(n²)

👉 inorder 已經幫你排序好了

---

## 🧠 複雜度
- Time: O(n)
- Space: O(h)

---

## 🔁 和其他題的關聯（幫你建立連結）
| 題目  | 中間做什麼 |
| --- | ----- |
| 230 | count |
| 98  | 檢查遞增  |
| 530 | 計算差值  |

👉 ❗同一個 inorder 模板

---

## 🎯 一句話記憶

👉 inorder 會排序 → 最小差值只會出現在相鄰節點
