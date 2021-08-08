# 请实现一个函数用来判断字符串是否表示数值（包括整数和小数）。
#
# 数值（按顺序）可以分成以下几个部分：
#
# 若干空格
# 一个小数或者整数
# （可选）一个'e'或'E'，后面跟着一个整数
# 若干空格
# 小数（按顺序）可以分成以下几个部分：
#
# （可选）一个符号字符（'+' 或 '-'）
# 下述格式之一：
# 至少一位数字，后面跟着一个点 '.'
# 至少一位数字，后面跟着一个点 '.' ，后面再跟着至少一位数字
# 一个点 '.' ，后面跟着至少一位数字
# 整数（按顺序）可以分成以下几个部分：
#
# （可选）一个符号字符（'+' 或 '-'）
# 至少一位数字
# 部分数值列举如下：
#
# ["+100", "5e2", "-123", "3.1416", "-1E-16", "0123"]
# 部分非数值列举如下：
#
# ["12e", "1a3.14", "1.2.3", "+-5", "12e+5.4"]
#
#
# 示例 1：
#
# 输入：s = "0"
# 输出：true
# 示例 2：
#
# 输入：s = "e"
# 输出：false
# 示例 3：
#
# 输入：s = "."
# 输出：false
# 示例 4：
#
# 输入：s = "   .1"
# 输出：true
#  
#
# 提示：
#
# 1 <= s.length <= 20
# s 仅含英文字母（大写和小写），数字（0-9），加号 '+' ，减号 '-' ，空格 ' ' 或者点 '.' 。
#



#先提取E出来，然后将数字分为左右两边，如果合格的话，两边应该都是数字

def integer(s:list):
    if len(s)>=1:
        if s[0]=='+' or s[0]=='-':
            s.pop(0)
            if len(s)==0:
                return False
        for i in s:
            if not i.isdigit():
                return False
        return True
    return False



def decimal(s:list):
    if len(s)>=1:
        if s[0]=='+' or s[0]=='-':
            s.pop(0)
            if len(s)==0:
                return False
        digit_num=0
        comma_num=0
        for i in s:
            if i.isdigit():
                digit_num+=1
            elif i=='.':
                comma_num+=1
        if comma_num==1 and digit_num>=1 and digit_num+comma_num==len(s):
            return True
        else:
            return False
    return False





class Solution:
    def isNumber(self, s: str) -> bool:
        s=s.strip(' ')
        e_index=s.find('e')
        E_index=s.find('E')
        s_list=[]
        for i in s:
            s_list.append(i)

        if e_index==-1 and E_index==-1:
            if decimal(s_list) or integer(s_list):
                return True
            else:
                return False

        elif e_index!=-1 :
            left=s_list[:e_index]
            right=s_list[e_index:]
            right.pop(0)
            if (integer(left) or decimal(left)) and integer(right):
                return True
            else:
                return False
        elif E_index!=-1:
            left=s_list[:E_index]
            right=s_list[E_index:]
            right.pop(0)
            if (integer(left) or decimal(left)) and integer(right):
                return True
            else:
                return False




Solution().isNumber("1 ")

s="  1  "
print(s.strip(' '))
print(s)














