# Method 1: Expand Around Center
class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        count = 0

        def expand(l: int, r: int) -> int:
            res = 0
            while l >= 0 and r < n and s[l] == s[r]:
                res += 1
                l -= 1
                r += 1
            return res

        for i in range(n):
            # odd-length 回文，以 s[i] 為中心
            count += expand(i, i)
            # even-length 回文，以 s[i] 和 s[i+1] 為中心
            count += expand(i, i + 1)

        return count

# Method 2: Dynamic Programming
class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        # dp[i][j] 表示 s[i..j] 是否為回文
        dp = [[False] * n for _ in range(n)]
        count = 0

        # 填長度為 1 和 2 的基本情況
        for i in range(n):
            dp[i][i] = True
            count += 1

        for i in range(n - 1):
            if s[i] == s[i + 1]:
                dp[i][i + 1] = True
                count += 1

        # 處理長度 ≥ 3
        # len_sub 是子字串長度
        for length in range(3, n + 1):  # 從 3 到 n
            for i in range(0, n - length + 1):
                j = i + length - 1
                if s[i] == s[j] and dp[i + 1][j - 1]:
                    dp[i][j] = True
                    count += 1

        return count