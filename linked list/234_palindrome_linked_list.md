# 🧠 LeetCode 234 - 回文連結串列 | Palindrome Linked List

🔗 題目連結 | Problem Link: [https://leetcode.com/problems/palindrome-linked-list/](https://leetcode.com/problems/palindrome-linked-list/)

---

## 📘 題目說明 | Problem Description

### 中文：
給定一個單向連結串列的頭節點 `head`，判斷該連結串列是否為回文串列（即正著讀與反著讀相同）。

### English:
Given the head of a singly linked list, return `true` if it is a palindrome or `false` otherwise.

### Examples
- Example 1:

![](../images/234_pal1linked-list1.jpg)

    Input: head = [1,2,2,1]

    Output: true

- Example 2:

![](../images/234_pal2linked-list2.jpg)

    Input: head = [1,2]
    
    Output: false

---

## 🧠 解題思路 | Solution Idea

### 中文：
1. 使用快慢指標（`fast` 和 `slow`）找到連結串列的中間節點。
2. 反轉連結串列的後半部分。
3. 比較前半部分和反轉後的後半部分的節點值。
4. 如果所有對應節點的值都相同，則為回文串列。

### English:
1. Use two pointers (`fast` and `slow`) to find the middle of the linked list.
2. Reverse the second half of the linked list.
3. Compare the first half and the reversed second half node by node.
4. If all corresponding nodes have equal values, the list is a palindrome.

---

## 🧾 程式碼與註解 | Code with Explanation

```python
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # Step 1: 使用快慢指標找到中間節點
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Step 2: 反轉後半部分的連結串列
        prev = None
        curr = slow
        while curr:
            next_temp = curr.next
            curr.next = prev
            prev = curr
            curr = next_temp

        # Step 3: 比較前半部分和反轉後的後半部分
        left = head
        right = prev
        while right:
            if left.val != right.val:
                return False
            left = left.next
            right = right.next

        return True
```

✅ 第一步：使用快慢指標找出中點
```python
slow = head
fast = head
while fast and fast.next:
```
我們要保證：

- fast != None

- fast.next != None

✅ 所以才寫： while fast and fast.next

### ❌ 為什麼不能只寫一個？

1️⃣ while fast:
- 問題：fast.next 可能是 None

- 然後你下一步會寫 fast = fast.next.next → Boom 💥 錯誤

2️⃣ while fast.next:
- 問題：當 fast 是 None 時，根本不能 fast.next

- 這樣會直接出錯（存取 None 的屬性） → 也 Boom 💥

### 🧠 小口訣記憶法：
    「快兩步，檢查兩層」
    → 你要讓快指標走兩步，就要檢查 fast 和 fast.next 都不是 None

```python
    slow = slow.next
    fast = fast.next.next
```
| 變數     | 說明                          |
| ------ | --------------------------- |
| `slow` | 每次走一步，用來找到中點。走完後會停在中點。      |
| `fast` | 每次走兩步，當它走到尾巴時，`slow` 剛好在中點。 |

- 舉例
```scss
1 → 2 → 3 → 2 → 1
s    f
    s      f
        s      f(X)
```
- 迴圈退出時，slow 會在「後半段起點」的位置。

✅ 第二步：反轉後半段 linked list
```python 
prev = None
curr = slow
while curr:
    next_temp = curr.next
    curr.next = prev
    prev = curr
    curr = next_temp
```
- 這是一段「反轉 linked list」的經典邏輯。

- 每次把 curr 的 next 指向 prev，然後整體往後推進。

- 初始值：
```ini
curr = slow (中間開始)
prev = None
```
反轉後：
```markdown
原本：2 → 1
變成：1 → 2
        ↑
       prev（新的頭）
```

✅ 第三步：從兩端開始比對值
```python
left = head
right = prev
while right:
    if left.val != right.val:
        return False
    left = left.next
    right = right.next
```
| 變數      | 說明              |
| ------- | --------------- |
| `left`  | 從原 list 的開頭走    |
| `right` | 從反轉後的尾巴（現在是新頭）走 |

- 每次比對 left.val 和 right.val，若不同就不是回文，提早返回 False。

- 為什麼只走 right 的長度？

    - 因為原串列長度可能是奇數，反轉後 right 範圍是後半，不需要比中間那個。

✅ 第四步：都比完沒問題，回傳 True
```python 
return True
```
- 比對都通過，代表原 linked list 是回文。

### 🔚 補充小技巧
- 這個解法不使用額外空間，只改動了後半段指標，空間複雜度是 O(1)

- 若要求不能破壞原始 list，可在結束後再反轉一次復原


---

## ⏱️ 時間與空間複雜度 | Time and Space Complexity
| 項目 | 複雜度  | 說明                            |
| -- | ---- | ----------------------------- |
| 時間 | O(n) | 需要遍歷連結串列找到中間節點，反轉後半部分，並比較兩半部分 |
| 空間 | O(1) | 使用常數空間進行操作，沒有使用額外的資料結構        |

---

## 📌 學到的重點 | Key Takeaways
- 快慢指標：用於找到連結串列的中間節點，是處理連結串列問題的常用技巧。

- 反轉連結串列：掌握如何反轉連結串列的部分區段，對於處理各種連結串列問題非常重要。

- 比較兩個連結串列：理解如何逐節點比較兩個連結串列的值，以判斷其是否相同。

---

## 📚 延伸閱讀 | Further Reading
- LeetCode 206 - 反轉連結串列（Reverse Linked List）

- LeetCode 21 - 合併兩個有序連結串列（Merge Two Sorted Lists）

- LeetCode 143 - 重排連結串列（Reorder List）
