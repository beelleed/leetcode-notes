class Solution:
    def getSum(self, a: int, b: int) -> int:
        # 為了模擬 32-bit 整數的行為，用 mask 限制
        mask = 0xFFFFFFFF
        # 最大的正數 32-bit
        MAX_INT = 0x7FFFFFFF
        
        a &= mask
        b &= mask
        
        while b != 0:
            # sum 不考慮進位
            sum_no_carry = (a ^ b) & mask
            # 進位部分
            carry = ((a & b) << 1) & mask
            
            a = sum_no_carry
            b = carry
        
        # 如果 a 在 32-bit 範圍內是正數，就直接回傳
        if a <= MAX_INT:
            return a
        else:
            # 否則是負數，轉回 Python 的負值表示
            return ~((a ^ mask))
