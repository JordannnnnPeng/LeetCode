# 在一个 n * m 的二维数组中，每一行都按照从左到右递增的顺序排序，每一列都按照从上到下递增的顺序排序。请完成一个高效的函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。
#
#  
#
# 示例:
#
# 现有矩阵 matrix 如下：
#
# [
#   [1,   4,  7, 11, 15],
#   [2,   5,  8, 12, 19],
#   [3,   6,  9, 16, 22],
#   [10, 13, 14, 17, 24],
#   [18, 21, 23, 26, 30]
# ]
# 给定 target=5，返回true。
#
# 给定target=20，返回false。
#
#  
#
# 限制：
#
# 0 <= n <= 1000
#
# 0 <= m <= 1000
#
#  
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/er-wei-shu-zu-zhong-de-cha-zhao-lcof
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
class Solution:
    def findNumberIn2DArray(self, matrix: list[list[int]], target: int) -> bool:
        y=len(matrix)
        if y>0:
            x = len(matrix[0])
            if x>0:
                x-=1   #turn x and y into subscripts
                y-=1
                x1=-1
                y1=-1
                while x1<=x:
                    x1+=1
                    if matrix[x1][y]>target:
                        break
                while y1<=y :
                    y1+=1
                    if matrix[x][y1]>target:
                        break

                for i in range(x1,x+1):
                    for j in range (y1,y+1):
                        if matrix[i][j] == target:
                            return True
        return False


#####   Not Passed