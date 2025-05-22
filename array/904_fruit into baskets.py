class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        count,i = {} , 0
        max_len = 0
        for j,v in enumerate(fruits):
            count[v] = count.get(v,0) + 1
            while len(count) > 2:
                count[fruits[i]] -= 1
                if count[fruits[i]] == 0:
                    del count[fruits[i]]
                i += 1
            max_len = max(max_len, j - i +1)
        return max_len
        