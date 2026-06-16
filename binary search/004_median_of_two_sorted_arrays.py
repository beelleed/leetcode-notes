class Solution:
    def findMedianSortedArrays(self, nums1, nums2):

        A, B = nums1, nums2

        if len(A) > len(B):
            A, B = B, A

        m, n = len(A), len(B)

        total = m + n
        half = (total + 1) // 2

        left, right = 0, m

        while left <= right:

            i = (left + right) // 2
            j = half - i

            Aleft = A[i - 1] if i > 0 else float('-inf')
            Aright = A[i] if i < m else float('inf')

            Bleft = B[j - 1] if j > 0 else float('-inf')
            Bright = B[j] if j < n else float('inf')

            if Aleft <= Bright and Bleft <= Aright:

                if total % 2 == 1:
                    return max(Aleft, Bleft)

                return (max(Aleft, Bleft) + min(Aright, Bright)) / 2

            elif Aleft > Bright:
                right = i - 1

            else:
                left = i + 1