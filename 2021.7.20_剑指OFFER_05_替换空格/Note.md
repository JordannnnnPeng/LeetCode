方法二：原地修改
在 C++ 语言中， string 被设计成「可变」的类型（参考资料），因此可以在不新建字符串的情况下实现原地修改。

由于需要将空格替换为 "%20" ，字符串的总字符数增加，因此需要扩展原字符串 s 的长度，计算公式为：新字符串长度 = 原字符串长度 + 2 * 空格个数 ，示例如下图所示。

![Picture6.png](https://pic.leetcode-cn.com/1599931882-pPgkor-Picture6.png)

算法流程：
初始化：空格数量 count ，字符串 s 的长度 len ；
统计空格数量：遍历 s ，遇空格则 count++ ；
修改 s 长度：添加完 "%20" 后的字符串长度应为 len + 2 * count ；
倒序遍历修改：i 指向原字符串尾部元素， j 指向新字符串尾部元素；当 i = j 时跳出（代表左方已没有空格，无需继续遍历）；
当 s[i] 不为空格时：执行 s[j] = s[i] ；
当 s[i] 为空格时：将字符串闭区间 [j-2, j] 的元素修改为 "%20" ；由于修改了 3 个元素，因此需要 j -= 2 ；
返回值：已修改的字符串 s ；

复杂度分析：
时间复杂度 O(N)O(N) ： 遍历统计、遍历修改皆使用 O(N)O(N) 时间。
空间复杂度 O(1)O(1) ： 由于是原地扩展 s 长度，因此使用 O(1)O(1) 额外空间。

C++

`class Solution {
public:
    string replaceSpace(string s) {
        int count = 0, len = s.size();
        // 统计空格数量
        for (char c : s) {
            if (c == ' ') count++;
        }
        // 修改 s 长度
        s.resize(len + 2 * count);
        // 倒序遍历修改
        for(int i = len - 1, j = s.size() - 1; i < j; i--, j--) {
            if (s[i] != ' ')
                s[j] = s[i];
            else {
                s[j - 2] = '%';
                s[j - 1] = '2';
                s[j] = '0';
                j -= 2;
            }
        }
        return s;
    }
};`

