# 实现pow(x,n)，即计算 x 的 n 次幂函数（即，xn）。不得使用库函数，同时不需要考虑大数问题。
#
#
#
# 示例 1：
#
# 输入：x = 2.00000, n = 10
# 输出：1024.00000
# 示例 2：
#
# 输入：x = 2.10000, n = 3
# 输出：9.26100
# 示例 3：
#
# 输入：x = 2.00000, n = -2
# 输出：0.25000
# 解释：2^-2 = 1/2^2 = 1/4 = 0.25
#
#
# 提示：
#
# -100.0 <x< 100.0
# -231<= n <=231-1
# -104<= x^n<= 104
#
class Solution:
    def myPow(self, x: float, n: int) -> float:
        a = 1
        if abs(n) < 100000:
            if n > 0:
                for i in range(n):
                    a = a * x
            elif n == 0:
                return 1
            elif n < 0:
                n = -n
                for i in range(n):
                    a = a / x
        else:
            if n < 0:
                x, n = 1 / x, -n
            for i in range(n):
                if n & 1:
                    a *= x
                x *= x
                n //= 2

        return a


a = Solution()
print(a.myPow(0.00001,21))#1.0000000000000019e-105
#浮点数的精度是有限的
print(a.myPow(0.00001,214748))#0.0
