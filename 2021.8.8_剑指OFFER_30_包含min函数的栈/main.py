# 定义栈的数据结构，请在该类型中实现一个能够得到栈的最小元素的 min 函数在该栈中，调用 min、push 及 pop 的时间复杂度都是 O(1)。
#
#
#
# 示例:
#
# MinStack minStack = new MinStack();
# minStack.push(-2);
# minStack.push(0);
# minStack.push(-3);
# minStack.min();   --> 返回 -3.
# minStack.pop();
# minStack.top();      --> 返回 0.
# minStack.min();   --> 返回 -2.
#
#
# 提示：
#
# 各函数的调用总次数不超过 20000 次
#

class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stackA = []
        self.mini = []

    def push(self, x: int) -> None:
        if len(self.stackA) == 0 or self.mini[-1] >= x:
            self.mini.append(x)
        self.stackA.append(x)

    def pop(self) -> None:
        a = self.stackA.pop()
        if self.mini[-1] == a:
            self.mini.pop()
        return a

    def top(self) -> int:
        if len(self.stackA) == 0:
            return None
        return self.stackA[-1]

    def min(self) -> int:
        if len(self.mini) == 0:
            return None
        return self.mini[-1]

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.min()
