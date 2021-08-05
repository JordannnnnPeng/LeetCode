# 请实现一个函数用来匹配包含'. '和'*'的正则表达式。模式中的字符'.'表示任意一个字符，而'*'表示它前面的字符可以出现任意次（含0次）。
# 在本题中，匹配是指字符串的所有字符匹配整个模式。例如，字符串"aaa"与模式"a.a"和"ab*ac*a"匹配，但与"aa.a"和"ab*a"均不匹配。
#
# 示例 1:
#
# 输入:
# s = "aa"
# p = "a"
# 输出: false
# 解释: "a" 无法匹配 "aa" 整个字符串。
# 示例 2:
#
# 输入:
# s = "aa"
# p = "a*"
# 输出: true
# 解释:因为 '*' 代表可以匹配零个或多个前面的那一个元素, 在这里前面的元素就是 'a'。因此，字符串 "aa" 可被视为 'a' 重复了一次。
# 示例3:
#
# 输入:
# s = "ab"
# p = ".*"
# 输出: true
# 解释:".*" 表示可匹配零个或多个（'*'）任意字符（'.'）。
# 示例 4:
#
# 输入:
# s = "aab"
# p = "c*a*b"
# 输出: true
# 解释:因为 '*' 表示零个或多个，这里 'c' 为 0 个, 'a' 被重复一次。因此可以匹配字符串 "aab"。
# 示例 5:
#
# 输入:
# s = "mississippi"
# p = "mis*is*p*."
# 输出: false
# s可能为空，且只包含从a-z的小写字母。
# p可能为空，且只包含从a-z的小写字母以及字符.和*，无连续的 '*'。
#
class Solution:
    def isMatch(self, s: str, p: str) -> bool:


        s_list=[]
        p_list=[]
        for i in s:
            s_list.append(i)
        for i in p:
            p_list.append(i)

        while True:

            if len(s_list) == 0:
                if len(p_list) == 0:
                    return True
                while p_list[-1] == '*':   #空串——a*b*c*
                    p_list = p_list[:-2]
                    if len(p_list) == 0:
                        return True
                return False

            if len(p_list) == 0:
                if len(s_list) == 0:
                    return True
                else:
                    return False

            if len(p_list)==1:
                if p_list[0]=='.' and len(s_list)==1:
                    return True

            if s_list[0]==p_list[0] and len(p_list)==1:
                s_list.pop(0)
                p_list.pop(0)
            elif s_list[0]==p_list[0] and p_list[1]!='*':
                s_list.pop(0)
                p_list.pop(0)
            elif p_list[0]=='.' and p_list[1]!='*':
                s_list.pop(0)
                p_list.pop(0)

            elif p_list[1]=='*' and p_list[0]=='.':
                p_list.pop(0)
                p_list.pop(0)
                test = s_list.copy()
                test.insert(0, s_list[0])
                for i in range(len(s_list)+1):
                    test.pop(0)
                    test_string=''.join([str(item) for item in test])#converting list to string
                    new_p_strin=''.join([str(item) for item in p_list])#converting list to string
                    if Solution().isMatch(test_string, new_p_strin):
                        return True
            elif p_list[1]=='*' and p_list[0]!='.':
                charac=p_list[0]
                p_list.pop(0)
                p_list.pop(0)
                test = s_list.copy()
                test.insert(0, s_list[0])
                while s_list[0]==charac:
                    test.pop(0)
                    test_string = ''.join([str(item) for item in test])  # converting list to string
                    new_p_strin = ''.join([str(item) for item in p_list])  # converting list to string
                    if Solution().isMatch(test_string, new_p_strin):
                        return True
            elif s_list[0]!=p_list[0]:
                if len(s_list)>1 and len(p_list)>1:
                    if p_list[1]!=s_list[1]:
                        return False
                return False


print(Solution().isMatch("aab","c*a*b"))


#Not Passed