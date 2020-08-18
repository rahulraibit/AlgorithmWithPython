import sys
#class Solution:
#    def minPathSumUtil(self, grid, i, j):
#        lrow = len(grid)
#        lcol = len(grid[0])
#        if i > lrow-1 or j > lcol-1:
#            return sys.maxsize;
#        if i == lrow - 1 and  j == lcol-1: 
#            return grid[i][j]
#        return grid[i][j] + min(self.minPathSumUtil(grid, i + 1, j),
#                                           self.minPathSumUtil(grid, i, j + 1))

#    def minPathSum(self, grid: [[int]]) -> int:
#        i = j = 0
#        minsum = sys.maxsize
#        return self.minPathSumUtil(grid, i, j)

class Solution:
    def minPathSum(self, grid: [[int]]) -> int:
        rowl = len(grid);
        if rowl == 0:
            return 0;
        coll = len(grid[0]);
        temp = [[0 for _ in range(coll)] for _ in range(rowl)];
        temp[0][0] = grid[0][0]
        for i in range(1, coll):
            temp[0][i] = temp[0][i-1] + grid[0][i];
        for i in range(1, rowl):
            temp[i][0] = temp[i-1][0] + grid[i][0];
        for i in range(1, rowl):
            for j in range(1, coll):
                temp[i][j] = grid[i][j] + min (temp[i-1][j], temp[i][j-1]);
        return temp[rowl-1][coll-1];

        
            
sln = Solution()
print(sln.minPathSum([[1,2,5],[3,2,1]]))