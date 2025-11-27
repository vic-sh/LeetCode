# while len(s > 0):
# go throug all elements 
# find first open and closed brackets
# remove open and closed brackets
# if there is no closed brackets
# return false
# find next open and closed brackets
# remove open and closed brackets
# ...
# retiun true


class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) < 2:
            return False
        else:
            stack_list = []
            for i in range(len(s)):
                if s[i] in "([{":
                    stack_list.append(s[i])
                elif s[i] in ")]}" and len(stack_list) > 0: # s[i] in ")]}"
                    if s[i] == ")" and stack_list[-1] == "(":
                        stack_list.pop()
                    elif s[i] == "]" and stack_list[-1] == "[":
                        stack_list.pop()
                    elif s[i] == "}" and stack_list[-1] == "{":
                        stack_list.pop()
                    else:
                        return False
                else:
                    return False
            if len(stack_list) != 0:
                return False
            else:
                return True
 
a = Solution()
print(a.isValid("()"))
print(a.isValid("(){}[]"))
print(a.isValid("()"))
print(a.isValid("(]"))
print(a.isValid("([)]"))
print(a.isValid("([])"))
print(a.isValid("]"))
print(a.isValid("){"))
print(a.isValid(")(){}"))
