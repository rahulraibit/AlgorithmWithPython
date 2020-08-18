#https://www.youtube.com/watch?v=-qrpJykY2gE
#https://leetcode.com/explore/challenge/card/30-day-leetcoding-challenge/531/week-4/3308/
class Solution:
    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        numberOfshifts = 0;
        while(m != n):
            m = m >> 1;
            n = n >> 1;
            numberOfshifts += 1;
        m = m << numberOfshifts
        return m
            
        
