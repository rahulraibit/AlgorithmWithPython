#Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.
#Input: [-2,1,-3,4,-1,2,1,-5,4],
#Output: 6
#Explanation: [4,-1,2,1] has the largest sum = 6.

#from collections import List
class Solution:
    def maxSubArray(self, nums: [int]) -> int:
        maxsumSoFor = nums[0];
        currentSum = nums[0];
        startingindex = 0;
        endingindex = 0
        for i in range(1, len(nums)):
            if nums[i] > currentSum + nums[i]:
                startingindex = i;
                currentSum = nums[i];
            else:
                currentSum = currentSum + nums[i];
            if currentSum > maxsumSoFor:
                maxsumSoFor = currentSum;
                endingindex = i;
            else:
                maxsumSoFor = maxsumSoFor;
        #print(startingindex, endingindex)
        #print()
        return maxsumSoFor;

sln = Solution()
result = sln.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]);
print(result);