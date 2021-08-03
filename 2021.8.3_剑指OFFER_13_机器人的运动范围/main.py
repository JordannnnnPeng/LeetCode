# 地上有一个m行n列的方格，从坐标 [0,0] 到坐标 [m-1,n-1] 。一个机器人从坐标 [0, 0] 的格子开始移动，它每次可以向左、右、上、下移动一格（不能移动到方格外），也不能进入行坐标和列坐标的数位之和大于k的格子。例如，当k为18时，
# 机器人能够进入方格 [35, 37] ，因为3+5+3+7=18。但它不能进入方格 [35, 38]，因为3+5+3+8=19。请问该机器人能够到达多少个格子？
#
#
#
# 示例 1：
#
# 输入：m = 2, n = 3, k = 1
# 输出：3
# 示例 2：
#
# 输入：m = 3, n = 1, k = 0
# 输出：1
# 提示：
#
# 1 <= n,m <= 100
# 0 <= k <= 20
class Solution:
    def movingCount(self, m: int, n: int, k: int) -> int:

        board = [[1] * n for i in range(m)]
        for y in range(m):
            for x in range(n):
                sum = int(y / 10) + int(x / 10) + (y - int(y / 10) * 10) + (x - int(x / 10) * 10)
                if sum > k:
                    board[y][x] = 0
        stack_x = [0]
        stack_y = [0]
        count = 1
        while len(stack_y) != 0 and len(stack_x) != 0:
            x = stack_x.pop(0)
            y = stack_y.pop(0)

            if y+1<m:
                if board[y + 1][x] == 1:
                    count += 1
                    board[y + 1][x] = -1
                    stack_x.append(x)
                    stack_y.append(y+1)
            if x+1<n:
                if board[y][x + 1] == 1:
                    count += 1
                    board[y][x + 1] = -1
                    stack_x.append(x+1)
                    stack_y.append(y)
        return count
