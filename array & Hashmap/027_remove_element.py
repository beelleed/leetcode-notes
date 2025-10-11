### 方法 A — 交換法
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        left = 0
        for right in range(len(nums)):
            if nums[right] != val:
                # 將合法元素換到左邊的 left 位置
                nums[right], nums[left] = nums[left], nums[right]
                left += 1
        return left
    
### 方法 B — 從兩端逼迫法
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            if nums[left] == val:
                # 用末端的值覆蓋這個位置
                nums[left] = nums[right]
                right -= 1
            else:
                left += 1
        return left
