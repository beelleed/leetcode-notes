#1.answer
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = { "(":")" , "{":"}" , "[":"]"}
        for i in s:
            if i in mapping:  # 左括號 → 放進 stack
                stack.append(i)
            elif i in mapping.values():  # 右括號 → 要配對檢查
                if not stack or mapping[stack.pop()] != i:
                    return False
        return not stack
# Time complexity: O(n)
# Space complexity: O(n)

#2. answer
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = { ")":"(" , "}":"{" , "]":"["}
        for i in s:
            if i in mapping.values():
                stack.append(i)
            elif i in mapping:
                if not stack or stack[-1] != mapping[i]:
                    return False
                else:
                    stack.pop()
        return not stack

---------------------------------------------------------------
#wrong answer
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = { "(":")" , "{":"}" , "[":"]"}
        for i in s:
            if i in mapping.values():
                stack.append(i)
            elif i in mapping:
                if not stack or stack[-1] != mapping[i]:
                    return False
                else:
                    stack.pop()
        return not stack
