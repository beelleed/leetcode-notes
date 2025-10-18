class Solution:
    def reverseBits(self, n: int) -> int:
        ans = 0
        for i in range(32):
            # 擷取最右邊那一位
            bit = n & 1
            # 把這位放到反轉位置
            ans |= (bit << (31 - i))
            # 準備處理下一位
            n >>= 1
        return ans
