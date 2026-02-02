# 第一種寫法：直接計算車隊數量
from typing import List

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # 將車子依照位置由大到小排序（靠近終點先處理）
        cars = sorted(zip(position, speed), reverse=True)

        fleets = 0
        cur_time = 0.0  # 目前前方車隊到終點所需時間（最慢）

        for p, s in cars:
            time = (target - p) / s
            # 若這台車無法追上前方車隊，形成新車隊
            if time > cur_time:
                fleets += 1
                cur_time = time
            # 否則 time <= cur_time，會追上並合併，不增加 fleet

        return fleets

# 第二種寫法：使用 stack 模擬車隊合併過程
from typing import List

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # 1. 依位置由大到小排序（靠近終點先處理）
        cars = sorted(zip(position, speed), reverse=True)

        stack = []  # stack 裡存的是「到終點所需時間」

        for p, s in cars:
            time = (target - p) / s
            stack.append(time)

            # 2. 若後車追得上前車，合併成同一個 fleet
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()  # 後車被前車吸收，移除

        return len(stack)
