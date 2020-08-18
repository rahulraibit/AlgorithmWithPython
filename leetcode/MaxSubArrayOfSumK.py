#https://leetcode.com/explore/challenge/card/30-day-leetcoding-challenge/531/week-4/3307/

class Solution:
    def subarraySum(self, nums: [int], k: int) -> int:
        maxsubArray = 0;
        l = len(nums);
        sum = 0
        map = {0:1};
        for i in range(l):
            sum = sum + nums[i];
            if sum-k in map:
                maxsubArray += map[sum-k];
            if sum in map:
                map[sum] = map[sum] + 1;
            else:
                map[sum] = 1
        return maxsubArray;
