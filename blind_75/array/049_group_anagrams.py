from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)  # 建立一個自動初始化 list 的 dict

        for s in strs:
            key = ''.join(sorted(s))  # 排序字串當作 key，例如 eat → aet
            anagrams[key].append(s)   # 加入對應的群組

        return list(anagrams.values())  # 回傳所有異位詞群組
