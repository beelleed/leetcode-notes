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

- 使用者一定要看到自己的推文

- 合併 followees + 自己

#### 初始化 heap
```python
heapq.heappush(heap, (-t, tid, u, idx))
```

- heap 中每個元素代表：
```text
(-time, tweetId, 哪個使用者, 在該使用者推文列表中的 index)
```

- 用 -time 模擬 max-heap（最新的先出）

#### 為什麼需要 index？

- 當某個使用者的最新推文被取走

- 我們要能「往前拿他更舊的一則」

#### 從 heap 取出最新推文
```python
_, tid, u, idx = heapq.heappop(heap)
res.append(tid)
```

- 每次 pop 都是「目前全體中最新的一則」

#### 推入下一則舊推文
```python
idx -= 1
if idx >= 0:
    heapq.heappush(heap, ...)
```

- 同一個 user 的推文本身是排序好的

- 像 merge sorted lists 一樣往前推

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