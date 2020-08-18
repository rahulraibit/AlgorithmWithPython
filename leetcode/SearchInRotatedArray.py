#https://leetcode.com/explore/challenge/card/30-day-leetcoding-challenge/530/week-3/3304/
class Solution:
    def BST(self, start, end, data, nums):
        if start > end:
            return -1;
        mid = (start + end)//2;
        if nums[mid] == data:
            return mid;
        if nums[start] <= nums[mid]:
            if data >= nums[start] and data <= nums[mid]:
                return self.BST(start, mid-1, data, nums);
            return self.BST(mid+1, end, data, nums);
        elif data >= nums[mid] and data <= nums[end]: 
            return self.BST(mid + 1, end, data, nums);
        else:
            return self.BST(start, mid-1, data, nums);
    def search(self, nums: [int], target: int) -> int:
        l = len(nums);
        return self.BST(0, l-1, target, nums);
