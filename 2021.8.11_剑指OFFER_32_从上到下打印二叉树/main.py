# 从上到下打印出二叉树的每个节点，同一层的节点按照从左到右的顺序打印。
# 例如:
# 给定二叉树: [3,9,20,null,null,15,7],
#
#     3
#    / \
#   9  20
#     /  \
#    15   7
# 返回：
#
# [3,9,20,15,7]
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

#利用队列进行遍历，每一层遍历的时候 单个节点取值，然后将左右子树加入队列中
class Solution:
    def levelOrder(self, root: TreeNode) -> list[int]:
        if root==None:
            return []
        Nodes = [root]
        ReturnList = []
        while Nodes:
            NextLevel = []
            for i in Nodes:
                ReturnList.append(i.val)
                if i.left:
                    NextLevel.append(i.left)
                if i.right:
                    NextLevel.append(i.right)
            Nodes = NextLevel
        return ReturnList