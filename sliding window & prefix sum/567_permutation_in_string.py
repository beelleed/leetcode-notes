from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        len1, len2 = len(s1), len(s2)
        if len1 > len2:
            return False

        need = Counter(s1)
        window = Counter(s2[:len1])

        if window == need:
            return True

        for i in range(len1, len2):
            # 加入右邊字元
            window[s2[i]] += 1
            # 移除左邊字元
            left_char = s2[i - len1]
            window[left_char] -= 1
            if window[left_char] == 0:
                del window[left_char]

            # 檢查是否符合
            if window == need:
                return True

        return False
