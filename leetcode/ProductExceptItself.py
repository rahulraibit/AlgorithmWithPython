#https://www.youtube.com/watch?v=gREVHiZjXeQ
class Solution:
    def productExceptSelf(self, nums: [int]) ->[int]:
        l = len(nums);
        resultArray = [1]*l;
        leftArray = [1]*l;
        rightArray = [1]*l;
        leftArray[0] = nums[0];
        rightArray[len(nums)-1] = nums[len(nums)-1] 
        for i in range(len(nums)-2, -1, -1):
            rightArray[i] = nums[i]*rightArray[i+1];
        for i in range(1, len(nums)):
            leftArray[i] = nums[i]*leftArray[i-1];
        for i in range(0, len(nums)):
            if i == 0:
                resultArray[i] = rightArray[i+1];
            elif i == len(nums)-1:
                 resultArray[i] = leftArray[i-1];
            else:
                 resultArray[i] = leftArray[i-1] * rightArray[i + 1];
        return resultArray;

sln = Solution();
sln.productExceptSelf([1,2,3,4]);
