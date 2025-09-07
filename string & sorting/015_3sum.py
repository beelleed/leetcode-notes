from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()  # 先對 nums 排序，方便雙指標操作與去除重複
        result = []  # 存放所有合法的不重複三元組
        n = len(nums)

        for i in range(n - 2):  # 最多只需要迴圈到倒數第 3 個數字
            if nums[i] > 0:
                break  # 提前結束：因為排序後的數字全為正，無法再湊成 0

            if i > 0 and nums[i] == nums[i - 1]:
                continue  # 跳過重複元素，避免重複解答

            l, r = i + 1, n - 1  # 設定雙指標：左邊從 i+1 開始，右邊從陣列尾端

            while l < r:
                total = nums[i] + nums[l] + nums[r]  # 計算三數之和

                if total < 0:
                    l += 1  # 如果總和小於 0，就往右移動左指標（增加總和）
                elif total > 0:
                    r -= 1  # 如果總和大於 0，就往左移動右指標（減少總和）
                else:
                    result.append([nums[i], nums[l], nums[r]])  # 三數和為 0，加入結果
                    l += 1
                    r -= 1

                    # 移動後的 l、r 可能仍是相同的數字 → 跳過重複
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                    while l < r and nums[r] == nums[r + 1]:
                        r -= 1

        return result
