# dp + offset
class Solution:
  def countBits(self, n: int):
      ans = [0] * (n + 1)
      offset = 1
      for i in range(1, n + 1):
          if i == offset * 2:
              offset *= 2
          ans[i] = ans[i - offset] + 1
      return ans

# brute force 1
class Solution:
    def countBits(self, n: int):
        ans = []
        for i in range(n + 1):
            binary = bin(i)                  # 將數字轉換成二進位字串，如 5 → '0b101'
            ones_count = binary.count('1')  # 計算字串中出現 '1' 的次數
            ans.append(ones_count)
        return ans
    
# brute force 2
class Solution:
    def countBits(self, n: int):
        def count_ones(x: int) -> int:
            cnt = 0
            while x > 0:
                cnt += x & 1
                x >>= 1
            return cnt

        ans = []
        for i in range(n + 1):
            ans.append(count_ones(i))
        return ans

