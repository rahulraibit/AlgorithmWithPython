#Given two strings S and T, return if they are equal when both are 
#typed into empty text editors. # means a backspace character.

#Note that after backspacing an empty text, the text will continue empty.

#Input: S = "ab#c", T = "ad#c"
#Output: true
#Explanation: Both S and T become "ac".

class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        if self.backspaceUtility(S) == self.backspaceUtility(T):
            return True;
        else:
            return False;
        
    def backspaceUtility(self, data):
        ans = [];
        for c in data:
            if c != '#':
                ans.append(c);
            else:
                if len(ans) > 0:
                    ans.pop();
        return "".join(ans);