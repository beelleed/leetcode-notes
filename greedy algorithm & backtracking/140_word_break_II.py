from typing import List

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        word_set = set(wordDict)
        n = len(s)
        memo = {}  # memo[i] = 所有從 s[i:] 能組出的句子 (List[str])

        def dfs(i: int) -> List[str]:
            # 1) 如果這個 i 已經算過，直接回傳記憶的結果
            if i in memo:
                return memo[i]

            # 2) base case：i 走到字串尾端，代表後面沒有字了
            #    回傳 [""] 是為了讓上層做拼接時好處理最後一個字
            if i == n:
                return [""]

            res = []  # 3) 用來收集所有從 s[i:] 開始的句子

            # 4) 嘗試字典中的每個單字 w
            for w in word_set:
                # 5) 如果 s 從位置 i 開始的前綴是 w，代表 w 可以當作下一個單字
                if s.startswith(w, i):
                    # 6) 遞迴：去找剩下的部分 s[i+len(w):] 能組成哪些句子
                    tails = dfs(i + len(w))

                    # 7) 把 w 和每個 tail 句子拼起來
                    for tail in tails:
                        if tail == "":
                            # 8) tail 為空代表 w 已經是最後一個字，不要加空格
                            res.append(w)
                        else:
                            # 9) tail 不空：w + 空格 + tail
                            res.append(w + " " + tail)

            # 10) 記憶化：把 i 的答案存起來
            memo[i] = res
            # 11) 回傳從 s[i:] 開始能形成的所有句子
            return res

        # 12) 題目要從 0 開始的所有句子
        return dfs(0)