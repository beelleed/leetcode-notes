# 📍 LeetCode 25 — Reverse Nodes in k-Group

🔗 https://leetcode.com/problems/reverse-nodes-in-k-group/

---

# 📄 題目說明 | Problem Description

## 中文

給定一個 Linked List：

```python
head
```

以及一個整數：

```python
k
```

每 k 個節點為一組進行反轉。

如果最後剩下的節點數量不足 k 個：

```text
不要反轉
直接保留原樣
```

---

## English

Given the head of a linked list, reverse the nodes of the list k at a time and return the modified list.

If the number of nodes remaining is less than k, leave them as-is.

---

## 🧪 Example 1

```text
Input:

1 → 2 → 3 → 4 → 5

k = 2
```

Output:

```text
2 → 1 → 4 → 3 → 5
```

---

## 🧪 Example 2

```text
Input:

1 → 2 → 3 → 4 → 5

k = 3
```

Output:

```text
3 → 2 → 1 → 4 → 5
```

---

# 🧠 核心觀念 | Key Insight

這題本質其實是：

```text
Reverse Linked List
+
分組處理
```

---

不是一次反轉整條鏈結串列。

而是：

```text
每 k 個節點
反轉一次
```

---

例如：

```text
1 → 2 → 3 → 4 → 5 → 6

k = 3
```

分組：

```text
(1 2 3) (4 5 6)
```

反轉：

```text
3 2 1 6 5 4
```

---

# 🎯 解題流程

每輪做四件事：

### ① 找到 k 個節點

```text
groupPrev
      ↓
dummy → 1 → 2 → 3 → 4 → 5
```

找到：

```text
kth
```

---

### ② 確認有沒有 k 個

如果：

```python
kth == None
```

代表：

```text
剩餘不足 k 個
```

直接結束。

---

### ③ 反轉這一組

例如：

```text
1 → 2 → 3
```

變：

```text
3 → 2 → 1
```

---

### ④ 接回原本鏈表

反轉前：

```text
dummy → 1 → 2 → 3 → 4
```

反轉後：

```text
dummy → 3 → 2 → 1 → 4
```

---

# 🔑 Dummy Node

建立：

```python
dummy = ListNode(0)
dummy.next = head
```

---

作用：

方便處理：

```text
第一組反轉
```

否則：

```text
head 可能改變
```

會很麻煩。

---

# 💻 Code

```python
class Solution:
    def reverseKGroup(self, head, k):

        dummy = ListNode(0)
        dummy.next = head

        groupPrev = dummy

        while True:

            kth = groupPrev

            for _ in range(k):
                kth = kth.next

                if not kth:
                    return dummy.next

            groupNext = kth.next

            prev = groupNext
            curr = groupPrev.next

            while curr != groupNext:

                temp = curr.next

                curr.next = prev

                prev = curr

                curr = temp

            temp = groupPrev.next

            groupPrev.next = kth

            groupPrev = temp
```

---

# 🧠 變數解釋

---

## dummy

```python
dummy = ListNode(0)
```

用途：

```text
永遠指向整條 linked list 開頭
```

---

## groupPrev

指向：

```text
每組開始前一個節點
```

例如：

```text
dummy → 1 → 2 → 3 → 4
↑
groupPrev
```

---

## kth

找到：

```text
第 k 個節點
```

---

## groupNext

記錄：

```text
下一組起點
```

例如：

```text
1 → 2 → 3 → 4 → 5

kth = 3

groupNext = 4
```

# 🧾 程式碼逐行解釋 | Line-by-line Explanation

## 建立 Dummy Node

```python
dummy = ListNode(0)
```

建立一個假的頭節點（Dummy Node）。

目的：

```text
避免第一組反轉後 head 改變不好處理
```

例如：

```text
原本：

1 → 2 → 3 → 4

反轉後：

2 → 1 → 4 → 3
```

head 已經從 1 變成 2。

如果沒有 dummy，處理會很麻煩。

---

```python
dummy.next = head
```

讓 dummy 指向原本的 linked list。

變成：

```text
dummy → 1 → 2 → 3 → 4 → 5
```

---

```python
groupPrev = dummy
```

`groupPrev`

代表：

```text
每一組開始前的節點
```

一開始第一組前面只有 dummy。

因此：

```text
groupPrev
    ↓
dummy → 1 → 2 → 3 → 4 → 5
```

---

## 開始處理每一組

```python
while True:
```

不斷重複：

```text
1. 找 kth
2. 確認有沒有 k 個
3. 反轉
4. 接回 linked list
```

直到不足 k 個為止。

---

# Step 1：找到 kth

```python
kth = groupPrev
```

從這組前面的節點開始。

例如：

```text
groupPrev
    ↓
dummy → 1 → 2 → 3 → 4 → 5
```

---

```python
for _ in range(k):
```

往前走 k 步。

目的是找到：

```text
這一組最後一個節點
```

---

```python
kth = kth.next
```

往後移動。

例如：

```text
dummy → 1 → 2 → 3 → 4 → 5
```

k = 2

第一次：

```text
kth = 1
```

第二次：

```text
kth = 2
```

---

```python
if not kth:
    return dummy.next
```

如果找不到 kth。

代表：

```text
剩下不足 k 個節點
```

例如：

```text
5
```

但：

```text
k = 2
```

不符合題目要求。

因此：

```python
return dummy.next
```

直接回傳。

---

# Step 2：記錄下一組位置

```python
groupNext = kth.next
```

記錄下一組的開始位置。

例如：

```text
dummy → 1 → 2 → 3 → 4 → 5
          ↑   ↑
       start kth
```

得到：

```text
groupNext = 3
```

---

之後反轉：

```text
1 ↔ 2
```

也不會找不到後面的：

```text
3 → 4 → 5
```

---

# Step 3：初始化反轉

```python
prev = groupNext
```

這是這題最重要的一行。

一般 Reverse Linked List：

```python
prev = None
```

但這題不能。

---

例如：

```text
1 → 2 → 3 → 4
```

k = 3

反轉區間：

```text
1 → 2 → 3
```

下一組：

```text
4
```

---

所以：

```python
prev = 4
```

反轉完後：

```text
3 → 2 → 1 → 4
```

自動接回去。

---

```python
curr = groupPrev.next
```

找到這一組第一個節點。

例如：

```text
dummy → 1 → 2 → 3 → 4
        ↑
       curr
```

---

# Step 4：反轉這一組

```python
while curr != groupNext:
```

只反轉：

```text
[groupPrev.next ~ kth]
```

不碰：

```text
groupNext
```

---

## Round 1

```python
temp = curr.next
```

先保存下一個節點。

例如：

```text
1 → 2 → 3
```

保存：

```text
temp = 2
```

---

```python
curr.next = prev
```

反轉方向。

原本：

```text
1 → 2
```

變：

```text
1 → 3
```

因為：

```python
prev = groupNext
```

---

```python
prev = curr
```

更新 prev。

變：

```text
prev = 1
```

---

```python
curr = temp
```

繼續處理下一個節點。

變：

```text
curr = 2
```

---

## Round 2

原本：

```text
2 → 3
```

---

保存：

```python
temp = 3
```

---

反轉：

```python
curr.next = prev
```

變：

```text
2 → 1 → 3
```

---

更新：

```python
prev = 2
curr = 3
```

---

停止：

```python
curr == groupNext
```

---

反轉結果：

```text
2 → 1 → 3
```

---

# Step 5：接回 Linked List

此時：

```text
dummy → 1 → 3
```

以及：

```text
2 → 1 → 3
```

是分離的。

---

```python
temp = groupPrev.next
```

保存：

```text
原本這組第一個節點
```

也就是：

```text
1
```

---

因為反轉後：

```text
1
```

會變成：

```text
這組最後一個節點
```

---

```python
groupPrev.next = kth
```

接回新頭。

原本：

```text
dummy → 1 → 2
```

變：

```text
dummy → 2 → 1
```

---

```python
groupPrev = temp
```

更新 groupPrev。

變：

```text
groupPrev = 1
```

因為：

```text
1
```

現在是這組尾巴。

下一輪從：

```text
1 → 3 → 4 → 5
```

繼續處理。

---

# 🔍 完整流程圖

```text
dummy → 1 → 2 → 3 → 4 → 5

找 kth
↓
dummy → 1 → 2

groupNext = 3

反轉
↓
2 → 1 → 3

接回
↓
dummy → 2 → 1 → 3 → 4 → 5

更新 groupPrev
↓
groupPrev = 1

繼續下一組
```

---

# 🧠 核心記憶

這題其實就是：

```text
Reverse Linked List
+
Group Processing
```

每輪固定流程：

```text
① 找 kth

② 檢查有沒有 k 個

③ groupNext = kth.next

④ Reverse

⑤ 接回去

⑥ groupPrev 移到尾巴

⑦ 下一組
```


---

# 🔍 Example Walkthrough

## Input

```text
1 → 2 → 3 → 4 → 5

k = 2
```

---

## 初始化

```text
dummy → 1 → 2 → 3 → 4 → 5

groupPrev = dummy
```

---

# 第一組

---

## 找 kth

```text
groupPrev
↓
dummy → 1 → 2 → 3 → 4 → 5
```

往前走 k 次：

```text
kth = 2
```

---

## groupNext

```text
groupNext = 3
```

---

## 開始反轉

初始化：

```python
prev = 3
curr = 1
```

---

### Round 1

```python
temp = 2

curr.next = prev
```

變：

```text
1 → 3
```

---

更新：

```python
prev = 1
curr = 2
```

---

### Round 2

```python
temp = 3

curr.next = prev
```

變：

```text
2 → 1 → 3
```

---

更新：

```python
prev = 2
curr = 3
```

---

停止：

```python
curr == groupNext
```

---

結果：

```text
2 → 1 → 3
```

---

## 接回去

原本：

```text
dummy → 1 → 2 → 3
```

現在：

```text
dummy → 2 → 1 → 3
```

---

更新：

```python
groupPrev = 1
```

因為：

```text
1
```

變成這組最後一個節點。

---

# 第二組

原本：

```text
2 → 1 → 3 → 4 → 5
```

---

找到：

```text
kth = 4
```

---

反轉：

```text
3 → 4
```

變：

```text
4 → 3
```

---

接回：

```text
2 → 1 → 4 → 3 → 5
```

---

# 第三組

剩下：

```text
5
```

---

不足：

```text
k = 2
```

---

停止：

```python
return dummy.next
```

---

# 🎯 為什麼這樣反轉？

關鍵：

```python
prev = groupNext
```

---

例如：

```text
1 → 2 → 3 → 4

groupNext = 4
```

---

反轉時：

```text
1 ← 2 ← 3
          ↓
          4
```

---

所以：

```text
反轉完直接接回下一組
```

不用額外處理。

---

# ⏱ Complexity Analysis

## Time Complexity

每個節點最多走一次：

```text
O(n)
```

---

## Space Complexity

只用幾個指標：

```text
O(1)
```

---

# 🎯 Interview Takeaways

看到：

```text
Reverse Nodes in k-Group
```

立刻想到：

```text
Dummy Node
+
Reverse Linked List
+
Group Processing
```

---

# ✍️ 我學到的東西

* Dummy 可以簡化 head 改變問題
* Reverse Linked List 是這題核心
* groupPrev 負責接回前一組
* kth 負責確認有沒有 k 個節點
* groupNext 負責記錄下一組開始位置
* 不足 k 個不能反轉

---

# 🏆 Cheat Sheet

```text
25

Dummy

groupPrev

找 kth

找到 groupNext

反轉 [groupPrev.next ~ kth]

接回去

更新 groupPrev

重複
```

---

# 🌟 One Sentence Summary

> Reverse every k nodes using the standard linked list reversal technique and reconnect each reversed group back into the list.

> 使用 Linked List Reverse 技巧，每 k 個節點反轉一次，再接回原本鏈表。
