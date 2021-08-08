s.strip(' ')不会直接在s的基础上删除左右的空格，需要s=s.strip(' ') 与列表s.pop()之类的不同

因为字符串是定长的，当字符串初始化后就不能修改了，所以s.strip()返回的是一个新的字符串，想要在源地址修改需要重新赋值

我的思路：

如何判断是整数：去掉第一个正负号后，应该全部都是数字

如何判断是小数：去掉第一个正负号后，应该符合comma_num==1 and digit_num>=1 and digit_num+comma_num==len(s)

将e或者E的左右两边提取出来，左边应该是整数或者一个小数，右边应该是一个整数

[面试题20. 表示数值的字符串（有限状态自动机，清晰图解） - 表示数值的字符串 - 力扣（LeetCode） (leetcode-cn.com)](https://leetcode-cn.com/problems/biao-shi-shu-zhi-de-zi-fu-chuan-lcof/solution/mian-shi-ti-20-biao-shi-shu-zhi-de-zi-fu-chuan-y-2/)

编译原理：有限状态机来处理，如何将简单有限状态机用python实现？

