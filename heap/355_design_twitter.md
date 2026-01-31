# 📍 LeetCode 355 — Design Twitter / 設計推特

🔗 [題目連結](https://leetcode.com/problems/design-twitter/)

---

## 📄 題目說明 | Problem Description
### 中文：

- 設計一個簡化版的 Twitter，需支援以下功能：

    1. postTweet(userId, tweetId) 
        - 使用者發送一則推文

    2. getNewsFeed(userId) 
        - 回傳使用者自己 以及他 follow 的人 的最新 10 則推文
        - 推文需依「新 → 舊」排序

    3. follow(followerId, followeeId)
        - follower 開始追蹤 followee

    4. unfollow(followerId, followeeId)
        - follower 取消追蹤 followee（不能取消追蹤自己）

### English:

Design a simplified Twitter where users can post tweets, follow/unfollow others, and retrieve the 10 most recent tweets from themselves and people they follow.

### Examples
- Example 1:

    - Input
        ["Twitter", "postTweet", "getNewsFeed", "follow", "postTweet", "getNewsFeed", "unfollow", "getNewsFeed"]

        [[], [1, 5], [1], [1, 2], [2, 6], [1], [1, 2], [1]]
    - Output
        [null, null, [5], null, null, [6, 5], null, [5]]

    - Explanation
        - Twitter twitter = new Twitter();
        - twitter.postTweet(1, 5); // User 1 posts a new tweet (id = 5).
        - twitter.getNewsFeed(1);  // User 1's news feed should return a list with 1 tweet id -> [5]. return [5]
        - twitter.follow(1, 2);    // User 1 follows user 2.
        - twitter.postTweet(2, 6); // User 2 posts a new tweet (id = 6).
        - twitter.getNewsFeed(1);  // User 1's news feed should return a list with 2 tweet ids -> [6, 5]. Tweet id 6 should precede tweet id 5 because it is posted after tweet id 5.
        - twitter.unfollow(1, 2);  // User 1 unfollows user 2.
        - twitter.getNewsFeed(1);  // User 1's news feed should return a list with 1 tweet id -> [5], since user 1 is no longer following user 2.

---

## 🧠 解題思路 | Solution Idea
- 核心觀察

    - 每個使用者的推文本身是 時間排序

    - getNewsFeed 本質是：

        - 合併多個「已排序串列」，取最新的前 10 筆

- 👉 這是一個典型的：

    - K-way merge

    - Top K from multiple sorted lists

- 👉 最適合的資料結構：Heap（優先佇列）

---

## 🧠 核心設計 | Key Design
- 為什麼需要 timestamp？

    - tweetId 本身沒有時間順序保證

    - 用全域遞增的 time 來表示新舊

---

## 🧩 資料結構設計 | Data Structures
### 1️⃣ Tweets
```text
tweets[userId] = [(time, tweetId), ...]
```

- 每個 user 自己的一個推文列表

- 依照時間遞增 append（最新在最後）

### 2️⃣ Following
```text
following[userId] = {followeeId1, followeeId2, ...}
```

- 使用 set，避免重複

- unfollow 操作是 O(1)

### 3️⃣ Time
```text
time = 1, 2, 3, ...
```

- 每次 postTweet 全域 +1

- 數字越大 → 越新

---

## 💻 程式碼實作 | Code (Python)
```python
from typing import List
from collections import defaultdict
import heapq

class Twitter:

    def __init__(self):
        self.time = 0
        self.tweets = defaultdict(list)     # userId -> [(time, tweetId)]
        self.following = defaultdict(set)   # userId -> set of followees

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.time += 1
        self.tweets[userId].append((self.time, tweetId))

    def getNewsFeed(self, userId: int) -> List[int]:
        users = set(self.following[userId])
        users.add(userId)   # user should see own tweets

        heap = []
        # heap item: (-time, tweetId, ownerUser, index_in_owner_tweets)
        for u in users:
            if self.tweets[u]:
                idx = len(self.tweets[u]) - 1
                t, tid = self.tweets[u][idx]
                heapq.heappush(heap, (-t, tid, u, idx))

        res = []
        while heap and len(res) < 10:
            _, tid, u, idx = heapq.heappop(heap)
            res.append(tid)

            idx -= 1
            if idx >= 0:
                t, tid2 = self.tweets[u][idx]
                heapq.heappush(heap, (-t, tid2, u, idx))

        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId == followeeId:
            return
        self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId == followeeId:
            return
        self.following[followerId].discard(followeeId)
```
### 🔍 程式碼逐段說明 | Line-by-line Explanation
#### 初始化
```python
self.time = 0
self.tweets = defaultdict(list)
self.following = defaultdict(set)
```

- time：全域時間戳

- tweets：每個 user 的推文列表

- following：追蹤關係

#### postTweet
```python
self.time += 1
self.tweets[userId].append((self.time, tweetId))
```

- 每發一篇推文，時間 +1

- append 到該 user 的推文列表

#### getNewsFeed — 使用者集合
```python
users = set(self.following[userId])
users.add(userId)
```
#### 1️⃣ 為什麼要用 set？

- following[userId] 可能本來就是 set

- 即使不是，用 set 可以保證：

    - 不重複

    - 後面 iterate 時乾淨

#### 2️⃣ 為什麼一定要 add(userId)？

- 因為題目規定：使用者 一定能看到自己的推文

- 即使他沒有 follow 任何人。

#### 初始化 heap
```python
heap = []
# heap item: (-time, tweetId, ownerUser, index_in_owner_tweets)
```
- 這行 comment 非常重要，它定義了 heap 裡「每一個元素代表什麼」。

- heap 裡每一個 item 代表的是：某一個使用者「目前還沒處理過的最新一則推文」

- 而不是：

    - 這個使用者的全部推文

    - 或全體推文一次丟進去

- 👉 這是效率的關鍵。

```python
if self.tweets[u]:
    idx = len(self.tweets[u]) - 1
    t, tid = self.tweets[u][idx]
    heapq.heappush(heap, (-t, tid, u, idx))
```
#### if self.tweets[u]:

- 如果這個 user 完全沒發過推文

- 那他對 news feed 完全沒貢獻

- 直接跳過

#### idx = len(self.tweets[u]) - 1

- 這行非常關鍵。

- 為什麼是 -1？

- 因為你的設計是：
```python
self.tweets[user] = [(time1, tweet1), (time2, tweet2), ...]
```

- 推文是 依時間遞增 append

- 所以：

    - index 最後一個 = 最新的推文

- 👉 idx 代表：這個 user「目前要考慮的那一則推文的位置」

#### t, tid = self.tweets[u][idx]

- t：這則推文的時間戳

- tid：tweetId

#### 為什麼 push 這 4 個東西？
```python
heapq.heappush(heap, (-t, tid, u, idx))
```
- 每個欄位的意義

| 欄位    | 意義                        |
| ----- | ------------------------- |
| `-t`  | 讓 heap 變成「最新優先」（max heap） |
| `tid` | 真正要回傳的推文 ID               |
| `u`   | 這則推文屬於哪個 user             |
| `idx` | 這則推文在該 user 推文列表的位置       |

- 👉 這 4 個缺一不可少任何一個，後面都會壞。

#### 為什麼需要 index？

- 當某個使用者的最新推文被取走

- 我們要能「往前拿他更舊的一則」

```python
res = []
while heap and len(res) < 10:
```
- 條件一：heap

    - heap 空了 → 沒推文了 → 結束

- 條件二：len(res) < 10

    - 題目只要最新 10 則

    - 不需要更多

- 👉 這兩個條件完美對齊題目需求。

```python
_, tid, u, idx = heapq.heappop(heap)
res.append(tid)
```
- 這一行代表 目前「所有 user 的候選推文」中，最新的一則
- 因為 heap 是用 -time 排序。


#### 為什麼要 idx -= 1？
```python
idx -= 1
```
因為你剛剛已經把：
```text
tweets[u][idx]
```

- 這一則用掉了。

- 👉 下一步你要做的是：嘗試拿「同一個 user 的下一則舊推文」

#### 為什麼要把「同一個 user 的舊推文」再丟回 heap？
if idx >= 0:
    t, tid2 = self.tweets[u][idx]
    heapq.heappush(heap, (-t, tid2, u, idx))

- 這一段在做的事是： 「補上一個新的候選者」

- 因為 heap 的 invariant 是：

    - heap 裡永遠存著：
    - 每個 user『目前尚未被處理的最新一則』

- 剛剛 pop 掉的是：

    - user u 的最新一則

- 所以要：

    - 把 u 的「下一則舊推文」補回 heap

    - 讓它繼續跟其他 user 的推文競爭

#### 整段邏輯用一句話串起來

這段 getNewsFeed 本質是在做：每個 user 的推文列表本身已排序，heap 永遠只保留每個 user 的當前最新候選推文，每次取出最新的一則後，再補回該 user 的下一則舊推文，直到收集到 10 則或沒有推文為止。

---

## 🧪 範例流程 | Example Walkthrough

操作序列
```text
postTweet(1, 5)
postTweet(1, 3)
postTweet(2, 6)
follow(1, 2)
getNewsFeed(1)
```
### 🔹 Step 0：初始化狀態
```text
time = 0
tweets = {}
following = {}
```
### 🔹 Step 1：postTweet(1, 5)
```python
self.time += 1        # time = 1
self.tweets[1].append((1, 5))
```

狀態：
```text
tweets = {
  1: [(1, 5)]
}
```
### 🔹 Step 2：postTweet(1, 3)
```python
self.time += 1        # time = 2
self.tweets[1].append((2, 3))
```

狀態：
```text
tweets = {
  1: [(1, 5), (2, 3)]
}
```
### 🔹 Step 3：postTweet(2, 6)
```python
self.time += 1        # time = 3
self.tweets[2].append((3, 6))
```

狀態：
```text
tweets = {
  1: [(1, 5), (2, 3)],
  2: [(3, 6)]
}
```
### 🔹 Step 4：follow(1, 2)
```python
self.following[1].add(2)
```

狀態：
```text
following = {
  1: {2}
}
```
### 🔹 Step 5：getNewsFeed(1)
#### 5.1 建立使用者集合
```python
users = set(self.following[1])  # {2}
users.add(1)                    # {1, 2}
```
#### 5.2 初始化 heap（只放「每個人最新的一則」）
User 1
```python
idx = len(tweets[1]) - 1 = 1
(t, tid) = (2, 3)
heap.push((-2, 3, 1, 1))
```
User 2
```python
idx = len(tweets[2]) - 1 = 0
(t, tid) = (3, 6)
heap.push((-3, 6, 2, 0))
```

此時 heap（邏輯上）：
```text
(-3, 6, 2, 0)   # 最新
(-2, 3, 1, 1)
```
### 🔹 Step 6：開始從 heap 取推文（while heap and len(res) < 10）
#### ➤ 第一次 pop
```python
(-3, 6, 2, 0) = heapq.heappop(heap)
res.append(6)
```

結果：
```text
res = [6]
```

嘗試推回 User 2 的「更舊推文」：
```python
idx = 0 - 1 = -1   # < 0 → 沒有更舊的
```

heap 剩下：
```text
(-2, 3, 1, 1)
```
#### ➤ 第二次 pop
```python
(-2, 3, 1, 1) = heapq.heappop(heap)
res.append(3)
```

結果：
```text
res = [6, 3]
```

推回 User 1 的更舊推文：
```python
idx = 1 - 1 = 0
(t, tid) = (1, 5)
heap.push((-1, 5, 1, 0))
```

heap：
```text
(-1, 5, 1, 0)
```
#### ➤ 第三次 pop
```python
(-1, 5, 1, 0) = heapq.heappop(heap)
res.append(5)
```

結果：
```text
res = [6, 3, 5]
```
```python
idx = 0 - 1 = -1   # 無更舊推文
```

- heap 為空，while 結束。

#### ✅ 最終回傳結果
```python
return [6, 3, 5]
```

- 依照「最新 → 最舊」

- 完全符合題目與程式碼行為

---

## 🔑 範例重點

- heap 永遠只放每個 user「目前最可能成為答案的一則」

- idx 負責往「更舊推文」移動

- 行為等價於 merge k sorted lists

- 沒有任何一步是多餘的排序

---

## ⏱ 複雜度分析 | Complexity Analysis

- postTweet: O(1)

- follow / unfollow: O(1)

- getNewsFeed:

    - heap size ≤ follow 人數 + 1

    - pop 最多 10 次

    - 👉 O((F + 1) + 10 log(F + 1))

---

## ✍️ 我學到的東西 | What I Learned

- 這題本質是 merge 多個排序串列

- 不需要把所有推文混在一起排序

- heap 裡只放「每個人目前最有可能成為答案的那一則」

- 這是非常典型的系統設計 + heap 題

---

## 🧠 一句話總結

I use a max heap to merge the most recent tweets from the user and their followees, retrieving the top 10 tweets efficiently.