# 输入一棵二叉树和一个整数，打印出二叉树中节点值的和为输入整数的所有路径。从树的根节点开始往下一直到叶节点所经过的节点形成一条路径。
#
#  
#
# 示例:
# 给定如下二叉树，以及目标和 target = 22，
#
#               5
#              / \
#             4   8
#            /   / \
#           11  13  4
#          /  \    / \
#         7    2  5   1
# 返回:
#
# [
#    [5,4,11,2],
#    [5,8,4,5]
# ]
#  
#
# 提示：
#
# 节点总数 <= 10000
#
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def pathSum(self, root: TreeNode, target: int) -> list[list[int]]:
        answer=[]
        list=[]
        sum=0
        def dig(root,list,sum):

            if root is None :#不能用>符号去排除：正负数会影响
                return None
            if (sum+root.val)==target and root.left is None and root.right is None:
                list.append(root.val)
                answer.append(list[:])
                #在递归中使用list[:]而非list
                #结果应该为[[5, 4, 11, 2], [5, 8, 4, 5]]
                #用list的结果为[[5,4,11,2,8,4,5,1],[5,4,11,2,8,4,5,1]]    #深复制，浅复制
            else:
                list.append(root.val)
                sum+=root.val
                dig(root.left,list[:],sum)
                dig(root.right,list[:],sum)
        dig(root,list,sum)
        return answer

a=TreeNode(5,TreeNode(4,TreeNode(11,TreeNode(7,None,None),TreeNode(2,None,None)),None),TreeNode(8,TreeNode(13,None,None),TreeNode(4,TreeNode(5,None,None),TreeNode(1,None,None))))
target=22
b=TreeNode(-2,None,TreeNode(-3,None,None))
print(Solution().pathSum(b,-5))


