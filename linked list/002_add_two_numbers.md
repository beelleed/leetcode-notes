# 🔢 LeetCode 2 - 兩數相加 | Add Two Numbers

🔗 題目連結：[https://leetcode.com/problems/add-two-numbers/](https://leetcode.com/problems/add-two-numbers/)

---

## 📘 題目說明 | Problem Description

### 中文：
給你兩個非空的 linked list，表示兩個非負整數。數字按**位數倒序儲存**，每個節點只儲存一個數字。請你將兩數相加，並以相同形式回傳結果的 linked list。

### English:
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in **reverse order**, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

---

## 🧠 解題思路 | Solution Idea

### 中文邏輯：
1. 使用 dummy 節點簡化操作。
2. 設定 carry（進位）初始為 0。
3. 同時遍歷 l1 和 l2，每次計算：val1 + val2 + carry。
4. 建立新節點儲存 result 的個位數，carry 更新為十位數。
5. 若最後 carry > 0，要再補一個節點。

### English logic:
1. Use a dummy node to build the result list.
2. Maintain a `carry` to handle sums >= 10.
3. Traverse both lists; for each node, compute `val1 + val2 + carry`.
4. Add a new node with the result's ones place.
5. At the end, if `carry > 0`, add one more node.

---

## 🧾 程式碼與逐行註解 | Code with Explanation

```python
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)      # 建立虛擬節點
        curr = dummy             # 指向結果串列的當前節點
        carry = 0                # 初始化進位為 0

        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0   # 取出 l1 的值，若為 None 則為 0
            val2 = l2.val if l2 else 0   # 同上

            total = val1 + val2 + carry  # 計算總和
            carry = total // 10          # 更新進位（只留下十位數，例如 14 → 1）
            curr.next = ListNode(total % 10)  # 把個位數做成節點加進結果串列（14 → 建立值為 4 的節點
            curr = curr.next                   # 將 curr 移動到新節點上，準備接下一個數字

            #  如果 l1 還沒到底，就往下走一步（走訪下一個節點）
            if l1: 
                l1 = l1.next 

            # 如果 l2 還沒到底，就往下走一步（走訪下一個節點 ）
            if l2: 
                l2 = l2.next

        return dummy.next  # 最後返回 dummy.next，就是結果串列的起點（略過 dummy 自己）
```

✅ 範例：輸入 l1 = [2, 4, 3]、l2 = [5, 6, 4]

代表：

- l1 = 342

- l2 = 465

加總結果：807 → 應該輸出 [7, 0, 8]

執行流程：
| val1 | val2 | carry | total | node 值 | carry 新值 |
| ---- | ---- | ----- | ----- | ------ | -------- |
| 2    | 5    | 0     | 7     | 7      | 0        |
| 4    | 6    | 0     | 10    | 0      | 1        |
| 3    | 4    | 1     | 8     | 8      | 0        |

### 🧠 小結：
- dummy 是虛擬起點，讓你不用特別處理第一個節點

- carry 是進位控制變數，每輪更新

- while l1 or l2 or carry 是保險寫法，保證所有狀況都處理

---

## ⏱️ 時間與空間複雜度 | Time & Space Complexity
| 類型 | 複雜度          | 說明                  |
| -- | ------------ | ------------------- |
| 時間 | O(max(n, m)) | 需走訪兩個 list 的所有節點    |
| 空間 | O(1)         | 不計輸出串列所需的空間，操作是原地進行 |

---

## 📌 學到的技巧 | Key Takeaways
- dummy node 簡化 list 建構過程。

- carry 是處理進位不可少的變數。

- l1.val if l1 else 0 是遍歷兩 list 的安全寫法。

- while l1 or l2 or carry: 是這類題的通用條件。

## 📚 延伸題目 | Related Problems
- LeetCode 445 - Add Two Numbers II（正序版本）

- LeetCode 415 - Add Strings（字串版加法）

- LeetCode 2 是 linked list + 進位處理的經典題