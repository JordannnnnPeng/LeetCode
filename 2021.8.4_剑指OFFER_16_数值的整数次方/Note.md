快速判断奇偶性：n & 1

浮点数的精度是有限的，0.00001^21可以表示出来，但是0.00001^214748会直接输出0，计算机会舍弃掉一定位数后面的小数

[面试题16. 数值的整数次方（快速幂，清晰图解） - 数值的整数次方 - 力扣（LeetCode） (leetcode-cn.com)](https://leetcode-cn.com/problems/shu-zhi-de-zheng-shu-ci-fang-lcof/solution/mian-shi-ti-16-shu-zhi-de-zheng-shu-ci-fang-kuai-s/)

快速幂法可以降低时间复杂度