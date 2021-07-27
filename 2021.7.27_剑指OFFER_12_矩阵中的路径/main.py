# 给定一个 m x n 二维字符网格 board 和一个字符串单词 word 。如果 word 存在于网格中，返回 true ；否则，返回 false 。
#
# 单词必须按照字母顺序，通过相邻的单元格内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。同一个单元格内的字母不允许被重复使用。
#
# 示例 1：
#
# 输入：board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
# 输出：true
# 示例 2：
#
# 输入：board = [["a","b"],["c","d"]], word = "abcd"
# 输出：false
#  
#
# 提示：
#
# 1 <= board.length <= 200
# 1 <= board[i].length <= 200
# board 和 word 仅由大小写英文字母组成
#

def Search(board: list[list[str]],used_board:list[list[int]], word: str,x,y)-> bool:
    used_board[y][x] = 1

    if x!=0:#check the left cell
        if board[y][x-1]==word[0] and used_board[y][x-1]==0:
            if len(word)==1:
                return True
            a=x-1  #do not use x=x-1 and pass x to the following Search function:deep copy and copy
            b=y
            if Search(board,used_board,word[1:],a,b)==True:
                return True
    if x!=len(board[0])-1:#check the right cell
        if board[y][x+1]==word[0]and used_board[y][x+1]==0:
            if(len(word))==1:
                return True
            a = x + 1  # do not use x=x-1 and pass x to the following Search function:deep copy and copy
            b = y
            if Search(board, used_board, word[1:], a, b) == True:
                return True
    if y!=0:#check the up cell
        if board[y-1][x]==word[0]and used_board[y-1][x]==0:
            if(len(word))==1:
                return True
            a=x
            b=y-1
            if Search(board,used_board,word[1:],a,b)==True:
                return True
    if y!=len(board)-1:#check the down cell
        if board[y+1][x]==word[0]and used_board[y+1][x]==0:
            if(len(word))==1:
                return True
            a=x
            b=y+1
            if Search(board,used_board,word[1:],a,b)==True:
                return True
    used_board[y][x]=0
    return False



class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        height=len(board)
        if height!=0:
            width=len(board[0])
            if width!=0:
                if height*width>=len(word):


                    for x in range(width):
                        for y in range(height):
                            if board[y][x]==word[0]:

                                if len(word)==1:
                                    return True
                                used_board = [[0] * width for i in range(height)]  # how to create a matrix full of 0
                                used_board[y][x]=1
                                if Search(board,used_board,word[1:],x,y)==True:
                                    return True


        return False

a=Solution()
print(a.exist([["A","B","C","E"],["S","F","E","S"],["A","D","E","E"]],"ABCESEEEFS"))