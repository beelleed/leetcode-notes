class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # 長度不同直接 false
        if len(s) != len(t):
            return False

        # 建頻率表
        freq = {}
        for ch in s:
            freq[ch] = freq.get(ch, 0) + 1

        # 減去 t 中字符
        for ch in t:
            if ch not in freq:
                return False
            freq[ch] -= 1
            if freq[ch] < 0:
                return False

        return True