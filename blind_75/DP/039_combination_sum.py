from typing import List
class Solution:
    def combinationSum(self, candidates:List[int], target: int):
        res = []
        def backtrack(start: int, path: List[int], remaining: int):
            if remaining == 0:
                res.append(path[:])
                return
            elif remaining < 0:
                return
            for i in range(start, len(candidates)):
                path.append(candidates[i])
                backtrack(i, path, remaining - candidates[i])
                path.pop()
        backtrack(0, [], target)
        return res