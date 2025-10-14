from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        # 數字到字母的映射
        digit_to_letters = {
            '2': "abc",
            '3': "def",
            '4': "ghi",
            '5': "jkl",
            '6': "mno",
            '7': "pqrs",
            '8': "tuv",
            '9': "wxyz"
        }

        results: List[str] = []

        def backtrack(index: int, path: List[str]):
            # 如果已經使用完所有 digits
            if index == len(digits):
                # 將 path（字母列表）組成字串加入結果
                results.append("".join(path))
                return

            # 取出當前 digit 對應的所有可能字母
            letters = digit_to_letters[digits[index]]
            for ch in letters:
                path.append(ch)            # 選擇這個字母
                backtrack(index + 1, path)  # 繼續處理下一個 digit
                path.pop()                  # 回溯，撤銷選擇

        backtrack(0, [])
        return results