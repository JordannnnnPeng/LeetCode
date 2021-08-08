# 输入一个矩阵，按照从外向里以顺时针的顺序依次打印出每一个数字。
#
#
#
# 示例 1：
#
# 输入：matrix = [[1,2,3],[4,5,6],[7,8,9]]
# 输出：[1,2,3,6,9,8,7,4,5]
# 示例 2：
#
# 输入：matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
# 输出：[1,2,3,4,8,12,11,10,9,5,6,7]
#
#
# 限制：
#
# 0 <= matrix.length <= 100
# 0 <= matrix[i].length <= 100


class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        a = []
        if len(matrix) == 0:
            return a
        elif len(matrix[0]) == 0:
            return a

        left = 0
        right = len(matrix[0]) - 1
        top = 0
        bottom = len(matrix) - 1

        while left <= right and top <= bottom:
            for i in range(left, right + 1):
                a.append(matrix[top][i])
            top += 1
            if top > bottom:
                break
            for i in range(top, bottom + 1):
                a.append(matrix[i][right])
            right -= 1
            if left > right:
                break
            for i in range(right, left - 1, -1):
                a.append(matrix[bottom][i])
            bottom -= 1
            if top > bottom:
                break
            for i in range(bottom, top - 1, -1):
                a.append(matrix[i][left])
            left += 1
            if left > right:
                break
        return a
