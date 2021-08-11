# 输入一个整数数组，判断该数组是不是某二叉搜索树的后序遍历结果。如果是则返回
# true，否则返回
# false。假设输入的数组的任意两个数字都互不相同。

# 参考以下这颗二叉搜索树：
#
# 5
# / \
#     2
# 6
# / \
#     1
# 3
# 示例
# 1：
#
# 输入: [1, 6, 3, 2, 5]
# 输出: false
# 示例
# 2：
#
# 输入: [1, 3, 2, 6, 5]
# 输出: true

#二叉查找树 （Binary Search Tree），（又：二叉搜索树，二叉排序树）它或者是一棵空树，或者是具有下列性质的 二叉树 ：
# 若它的左子树不空，则左子树上所有结点的值均小于它的 根结点 的值； 若它的右子树不空，则右子树上所有结点的值均大于它的根结点的值；
# 它的左、右子树也分别为 二叉排序树 。

class Solution:
    def verifyPostorder(self, postorder: [int]) -> bool:
        def recur(i, j):
            if i >= j: return True
            p = i
            while postorder[p] < postorder[j]: p += 1
            m = p
            while postorder[p] > postorder[j]: p += 1
            return p == j and recur(i, m - 1) and recur(m, j - 1)

        return recur(0, len(postorder) - 1)
