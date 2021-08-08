#
# 输入两棵二叉树A和B，判断B是不是A的子结构。(约定空树不是任意一个树的子结构)
#
# B是A的子结构， 即 A中有出现和B相同的结构和节点值。
#
# 例如:
# 给定的树 A:
#
#      3
#     / \
#    4   5
#   / \
#  1   2
# 给定的树 B：
#
#    4
#   /
#  1
# 返回 true，因为 B 与 A 的一个子树拥有相同的结构和节点值。
#
# 示例 1：
#
# 输入：A = [1,2,3], B = [3,1]
# 输出：false
# 示例 2：
#
# 输入：A = [3,4,5,1,2], B = [4,1]
# 输出：true
# 限制：
#
# 0 <= 节点个数 <= 10000\


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def getRoot(A: TreeNode, val: int):
    if A == None:
        return None
    if A.val == val:
        return A
    else:
        if getRoot(A.left, val) is not None:
            return getRoot(A.left, val)
        if getRoot(A.right, val) is not None:
            return getRoot(A.right, val)
        return None


def isEqual(A: TreeNode, B: TreeNode) -> bool:
    if B is not None:
        if A is not None:
            if A.val != B.val:
                return False
            if not isEqual(A.left, B.left):
                return False
            if not isEqual(A.right, B.right):
                return False
        else:
            return False


class Solution:
    def isSubStructure(self, A: TreeNode, B: TreeNode) -> bool:
        if B is None:
            return False
        while (start := getRoot(A, B.val)) is not None:
            start = getRoot(A, B.val)
            if not isEqual(start, B):
                start.val = -1.223
            else:
                return True
        return False


A = TreeNode(1)
A.left = TreeNode(0)
A.right = TreeNode(1)
A.left.left = TreeNode(-4)
A.left.right = TreeNode(-3)

B = TreeNode(1)
B.left = TreeNode(-4)

print(Solution().isSubStructure(A, B))
