from collections import defaultdict, deque
from typing import List

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # 建圖與計算入度
        graph = defaultdict(list)
        indegree = [0] * numCourses
        for course, pre in prerequisites:
            graph[pre].append(course)
            indegree[course] += 1

        # 初始化 queue，所有入度為 0 的課程
        queue = deque([i for i in range(numCourses) if indegree[i] == 0])
        order = []

        # 拓撲排序
        while queue:
            curr = queue.popleft()
            order.append(curr)
            for next_course in graph[curr]:
                indegree[next_course] -= 1
                if indegree[next_course] == 0:
                    queue.append(next_course)

        # 檢查是否所有課程都能排進順序中
        if len(order) == numCourses:
            return order
        else:
            return []