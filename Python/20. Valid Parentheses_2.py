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
            for i in s:
                if i in ['[', '(', '{']:
                    stack_list.append(i)
                elif i in [']', ')', '}'] and len(stack_list) > 0:
                    if i == ')' and stack_list[-1] == '(':
                        stack_list.pop()
                    elif i == ']' and stack_list[-1] == '[':
                        stack_list.pop()
                    elif i == '}' and stack_list[-1] == '{':
                        stack_list.pop()
                    else: return False
                else: return False
            if len(stack_list) == 0: return True
            else: return False
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
