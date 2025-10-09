from typing import List

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []  # Store indices of bars in increasing height order
        max_area = 0
        n = len(heights)
        
        # Add a virtual bar of height 0 to flush out the stack at the end
        for i in range(n + 1):
            current_height = 0 if i == n else heights[i]
            
            # While the current bar is lower than the one at the top of the stack
            while stack and (i == n or heights[stack[-1]] > current_height):
                h = heights[stack.pop()]  # Pop the top and treat it as height
                # Width is from the last lower bar index to current i
                width = i if not stack else (i - stack[-1] - 1)
                max_area = max(max_area, h * width)
            
            stack.append(i)  # Push current index into the stack
        
        return max_area
