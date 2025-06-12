class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []  # 存放“尚未找到更高溫”的天數 index
        res = [0] * len(temperatures)

        for i, temp in enumerate(temperatures):
            # 當 stack 不為空，且當前 temp 高於 stack top 所在天的溫度
            while stack and temp > temperatures[stack[-1]]:
                prev = stack.pop()
                res[prev] = i - prev  # 計算等待天數
            stack.append(i)

        return res