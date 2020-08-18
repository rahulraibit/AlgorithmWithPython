#https://leetcode.com/explore/challenge/card/30-day-leetcoding-challenge/530/week-3/3302/
class Solution:
    def visitAll(self, grid, i, j):
        if i < len(grid) and i >=0 and j < len(grid[i]) and j >= 0:
            if grid[i][j] == "0":
                return;
            if grid[i][j] == "1":
                grid[i][j] = "0"
            self.visitAll(grid, i+1, j);   
            self.visitAll(grid, i, j+1); 
            self.visitAll(grid, i-1, j);   
            self.visitAll(grid, i, j-1); 
            
    def numIslands(self, grid: [[str]]) -> int:
        numOfIslands = 0;
        
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == "1":
                     self.visitAll(grid, i, j);
                     numOfIslands += 1;
        
        return numOfIslands;    
sln = Solution();

print(sln.numIslands([["1","0","1","1","0","1","1"]]))