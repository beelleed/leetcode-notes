## 方法一 : Hashmap

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        hashmap = {}
        for i, num in enumerate(numbers):
            complement = target - num
            if complement in hashmap:
                return [hashmap[complement] + 1, i + 1]  # ✅ 索引從 1 開始
            hashmap[num] = i

---
## 方法二 : Two Pointers
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers) - 1
        while left < right:
            total = numbers[left] + numbers[right]
            if total == target:
                return [left + 1, right + 1]  # ✅ 索引 +1
            elif total < target:
                left += 1
            else:
                right -= 1
