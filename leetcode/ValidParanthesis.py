#https://leetcode.com/explore/challenge/card/30-day-leetcoding-challenge/530/week-3/3301/
class Solution:
    def checkValidString(self, s: str) -> bool:
        stack = []
        starStack = []
        i = 0
        l = len(s)
        if s == "": 
            return True
        if s[0] == ')' or s[0] == '(' and len(s) == 1:
            return False
        while i < l:
            if s[i] == '(':
                stack.append(i)
            elif s[i] == '*':
                starStack.append(i)
            elif s[i] == ')':
                if len(stack) > 0:
                    stack.pop()
                else:
                    if len(starStack) > 0:
                        starStack.pop()
                    else: 
                        return False
            i = i + 1
        if len(stack) == 0:
             return True
        elif len(stack) <= len(starStack):
            while stack:
                 v1 = stack.pop()
                 v2 = starStack.pop()
                 if v1 > v2:
                        return False;
        else: 
            return False;
        return True
