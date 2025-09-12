class MinStack:
    def __init__(self):
        self.stack = []       # 主 stack：儲存所有值
        self.min_stack = []   # 輔助 stack：儲存對應最小值

    def push(self, val: int) -> None:
        self.stack.append(val)
        # 如果 min_stack 是空的，就直接放；否則放當前 val 和上個最小值中較小者
        if not self.min_stack:
            self.min_stack.append(val)
        else:
            self.min_stack.append(min(val, self.min_stack[-1]))

    def pop(self) -> None:
        self.stack.pop()
        self.min_stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]
