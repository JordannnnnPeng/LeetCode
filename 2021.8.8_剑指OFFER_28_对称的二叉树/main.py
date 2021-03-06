# 请实现一个函数，用来判断一棵二叉树是不是对称的。如果一棵二叉树和它的镜像一样，那么它是对称的。
# 
# 例如，二叉树 [1,2,2,3,4,4,3] 是对称的。
# 
#     1
#    / \
#   2   2
#  / \ / \
# 3  4 4  3
# 但是下面这个 [1,2,2,null,3,null,3] 则不是镜像对称的:
# 
#     1
#    / \
#   2   2
#    \   \
#    3    3
# 
#  
# 
# 示例 1：
# 
# 输入：root = [1,2,2,3,4,4,3]
# 输出：true
# 示例 2：
# 
# 输入：root = [1,2,2,null,3,null,3]
# 输出：false
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        def recur(L, R):
            if not L and not R: return True
            if not L or not R or L.val != R.val: return False
            return recur(L.left, R.right) and recur(L.right, R.left)

        return recur(root.left, root.right) if root else True
