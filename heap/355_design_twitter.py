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
