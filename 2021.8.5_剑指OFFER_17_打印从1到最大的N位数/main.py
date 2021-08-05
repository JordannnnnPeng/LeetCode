# 输入数字 n，按顺序打印出从 1 到最大的 n 位十进制数。比如输入 3，则打印出 1、2、3 一直到最大的 3 位数 999。
#
# 示例 1:
#
# 输入: n = 1
# 输出: [1,2,3,4,5,6,7,8,9]
class Solution:
    def printNumbers(self, n: int) -> list[int]:
        a=[]
        for i in range(1,10**n):
            a.append(i)
        return a