class Solution:
  def numDecodings(self, s: str) -> int:
    # 若字串空或開頭是 '0'，無法解碼
    if not s or s[0] == '0':
        return 0

    n = len(s)
    # dp[i] 表示前 i 個字元有多少種解碼方式
    dp = [0] * (n + 1)
    dp[0] = 1
    dp[1] = 1  # 前提是 s[0] != '0'

    for i in range(2, n + 1):
        # 單個字元部分：s[i-1]
        if s[i - 1] != '0':
            dp[i] += dp[i - 1]

        # 兩位數部分：s[i-2:i]
        two = int(s[i - 2 : i])
        if 10 <= two <= 26:
            dp[i] += dp[i - 2]
    return dp[n]
