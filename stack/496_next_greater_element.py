# brute force
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = []

        for x in nums1:                      # 外層：處理 nums1 的每個元素
            for j in range(len(nums2)):      # 內層：在 nums2 找位置
                if nums2[j] == x:
                    nxt = -1                 # 預設找不到
                    for k in range(j + 1, len(nums2)):  # 第三步：往右找
                        if nums2[k] > x:
                            nxt = nums2[k]
                            break            # 找到第一個就停
                    ans.append(nxt)           # 存結果
                    break                    # 這個 x 處理完了

        return ans
    
# Monotonic Stack
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        next_greater = {}

        for num in nums2:
            while stack and num > stack[-1]:
                smaller = stack.pop()
                next_greater[smaller] = num
            stack.append(num)

        return [next_greater.get(x, -1) for x in nums1]
