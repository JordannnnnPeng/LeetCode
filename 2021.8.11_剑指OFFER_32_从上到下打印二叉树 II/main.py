# 从上到下按层打印二叉树，同一层的节点按从左到右的顺序打印，每一层打印到一行。
# 
#  
# 
# 例如:
# 给定二叉树: [3,9,20,null,null,15,7],
# 
#     3
#    / \
#   9  20
#     /  \
#    15   7
# 返回其层次遍历结果：
# 
# [
#   [3],
#   [9,20],
#   [15,7]
# ]
#  
# 
# 提示：
# 
# 节点总数 <= 1000
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
            ReturnList.append(ThisLevel)
        return ReturnList