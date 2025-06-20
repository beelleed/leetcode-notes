class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        p1 = m - 1  # nums1 的最後一個有效元素
        p2 = n - 1  # nums2 的最後一個元素
        p = m + n - 1  # 合併後 nums1 的最後一個位置

        while p1 >= 0 and p2 >= 0:
            if nums1[p1] > nums2[p2]:
                nums1[p] = nums1[p1]
                p1 -= 1
            else:
                nums1[p] = nums2[p2]
                p2 -= 1
            p -= 1

        # 把 nums2 剩下的補進 nums1 前面
        while p2 >= 0:
            nums1[p] = nums2[p2]
            p2 -= 1
            p -= 1