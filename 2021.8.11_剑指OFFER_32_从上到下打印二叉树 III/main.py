# 请实现一个函数按照之字形顺序打印二叉树，即第一行按照从左到右的顺序打印，第二层按照从右到左的顺序打印，第三行再按照从左到右的顺序打印，其他行以此类推。
#
#
#
# 例如:
# 给定二叉树: [3, 9, 20, null, null, 15, 7],
#
# 3
# / \
#     9
# 20
# / \
#     15
# 7
# 返回其层次遍历结果：
#
# [
#     [3],
#     [20, 9],
#     [15, 7]
# ]
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> list[list[int]]:
        if root==None:
            return []
        Nodes = [root]
        ReturnList = []
        x=0
        while Nodes:
            NextLevel = []
            ThisLevel=[]
            for i in Nodes:
                ThisLevel.append(i.val)
                if i.left:
                    NextLevel.append(i.left)
                if i.right:
                    NextLevel.append(i.right)
            Nodes = NextLevel
            if x&1:
                ThisLevel.reverse()

            ReturnList.append(ThisLevel)
            x+=1


        return ReturnList