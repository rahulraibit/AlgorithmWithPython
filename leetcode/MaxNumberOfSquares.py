#https://leetcode.com/explore/challenge/card/30-day-leetcoding-challenge/531/week-4/3312/
#https://www.youtube.com/watch?v=_Lf1looyJMU
class Solution:
    def maximalSquare(self, matrix: [[str]]) -> int:
        m = len(matrix);
        if m == 0:
            return 0
        n = len(matrix[0]);
        L = [[None for _ in range(n+1)]for _ in range(m+1)]
        for i in range(m+1):
            for j in range(n+1):
                if i == 0 or j == 0:
                    L[i][j] = 0;
                elif int(matrix[i-1][j-1]) == 0:
                    L[i][j] = 0;
                else:
                    L[i][j] = min(int(L[i-1][j]),int(L[i][j-1]),int(L[i-1][j-1])) + int(matrix[i-1][j-1])
        maxNumber = 0
        for i in range(m+1):
            for j in range(n+1): 
                if L[i][j] > maxNumber:
                    maxNumber= L[i][j];
                    
        return maxNumber*maxNumber;
