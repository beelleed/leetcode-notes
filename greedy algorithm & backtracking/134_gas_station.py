from typing import List

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        total_tank = 0
        current_tank = 0
        start_station = 0

        for i in range(len(gas)):
            net_gain = gas[i] - cost[i]
            total_tank += net_gain
            current_tank += net_gain

            if current_tank < 0:
                start_station = i + 1
                current_tank = 0

        return start_station if total_tank >= 0 else -1
