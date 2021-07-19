#解题思路：
若使用暴力法遍历矩阵 matrix ，则时间复杂度为 O(NM)O(NM) 。暴力法未利用矩阵 “从上到下递增、从左到右递增” 的特点，显然不是最优解法。

如下图所示，我们将矩阵逆时针旋转 45° ，并将其转化为图形式，发现其类似于 二叉搜索树 ，即对于每个元素，其左分支元素更小、右分支元素更大。因此，通过从 “根节点” 开始搜索，遇到比 target 大的元素就向左，反之向右，即可找到目标值 target 。

![Picture1.png](https://pic.leetcode-cn.com/6584ea93812d27112043d203ea90e4b0950117d45e0452d0c630fcb247fbc4af-Picture1.png)

“根节点” 对应的是矩阵的 “左下角” 和 “右上角” 元素，本文称之为 标志数 ，以 matrix 中的 左下角元素 为标志数 flag ，则有:

若 flag > target ，则 target 一定在 flag 所在 行的上方 ，即 flag 所在行可被消去。
若 flag < target ，则 target 一定在 flag 所在 列的右方 ，即 flag 所在列可被消去。
算法流程：
从矩阵 matrix 左下角元素（索引设为 (i, j) ）开始遍历，并与目标值对比：
当 matrix[i][j] > target 时，执行 i-- ，即消去第 i 行元素；
当 matrix[i][j] < target 时，执行 j++ ，即消去第 j 列元素；
当 matrix[i][j] = target 时，返回 truetrue ，代表找到目标值。
若行索引或列索引越界，则代表矩阵中无目标值，返回 falsefalse 。
每轮 i 或 j 移动后，相当于生成了“消去一行（列）的新矩阵”， 索引(i,j) 指向新矩阵的左下角元素（标志数），因此可重复使用以上性质消去行（列）。

复杂度分析：
时间复杂度 O(M+N)O(M+N) ：其中，NN 和 MM 分别为矩阵行数和列数，此算法最多循环 M+NM+N 次。
空间复杂度 O(1)O(1) : i, j 指针使用常数大小额外空间。









#我的问题：

特殊二维数组：[], [[]]

判断边界条件的写法不能这么写:

` while x1<=x and matrix[x1][y]<target:                x1+=1`

这样当x1越界时，还会判断matrix[x1]的值的大小，发生数组越界

在循环中注意使用的参数，不能写成：

` for i in range(x1,x+1):                    for i in range (y1,y+1):                        if matrix[x1][y1] == target:                            return True`

