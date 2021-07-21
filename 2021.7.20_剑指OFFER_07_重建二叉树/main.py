# 输入某二叉树的前序遍历和中序遍历的结果，请构建该二叉树并返回其根节点。
# 假设输入的前序遍历和中序遍历的结果中都不含重复的数字。
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def buildTree(self, preorder: list[int], inorder: list[int]) -> TreeNode:

        return treeNode(preorder,inorder)


def treeNode(preorder,inorder):
    if len(preorder) == 0 or len(inorder) == 0:
        return None
    root = 0
    in_sub = -1
    for i in range(len(inorder)):
        if inorder[i] == preorder[root]:
            in_sub = i
            break
    if in_sub==-1:
        return None
    root_node = TreeNode(preorder[root])
    preorder.pop(0)
    root_node.left = treeNode(preorder, inorder[:in_sub])
    root_node.right = treeNode(preorder, inorder[in_sub:])
    return root_node

a=Solution()
a.buildTree([3,9,20,15,7],[9,3,15,20,7])
print(a)
