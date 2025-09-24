from collections import Counter

class Solution:
  def characterReplacement(self, s: str, k: int) -> int:
      count = Counter()
      l = 0
      max_count = 0
      ans = 0

      for r, ch in enumerate(s):
          count[ch] += 1
          # 更新窗口內最頻繁字母的次數
          max_count = max(max_count, count[ch])

          # 若當前窗口需要替換的字符數超過 k，縮左邊界
          # window_len = r - l + 1
          if (r - l + 1) - max_count > k:
              count[s[l]] -= 1
              l += 1

          # 更新答案：當前窗口長度
          ans = max(ans, r - l + 1)

      return ans
    