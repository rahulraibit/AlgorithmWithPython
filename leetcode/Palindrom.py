#https://leetcode.com/explore/featured/card/august-leetcoding-challenge/549/week-1-august-1st-august-7th/3411/

class Solution:
    def isPalindrome(self, s: str) -> bool:
        i = 0;
        j = len(s)-1;
        while(i <= j):
            if not s[i].isalnum():
                i = i + 1;
                continue;
            if not s[j].isalnum():
                j = j - 1;
                continue;
            if s[i].lower() != s[j].lower():
                return False;
            else:
                i = i + 1;
                j = j-1;
        return True;