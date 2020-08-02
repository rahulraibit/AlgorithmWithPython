##Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.
#Input: [0,1,0,3,12]
#Output: [1,3,12,0,0]

#class Solution:
#    def moveZeroes(self, nums: [int]) -> None:
#        """
#        Do not return anything, modify nums in-place instead.
#        """
#        count = 0;
#        for i in range(0, len(nums)):
#            j = i;
#            while j < len(nums) and nums[j] == 0:
#                count = count + 1;
#                j = j + 1 ;
#                continue;
#            if count > 0:
#                z = i;
#                while z + count < len(nums):
#                    nums[z] = nums[count + z];
#                    nums[count + z] = 0;
#                    z  = z + 1;
#                count = 0;
#        print(nums);

#sln = Solution();
#sln.moveZeroes([0,0,0,1, 1, 0, 0, 0, 1]);


#easy solution

class Solution:
    def moveZeroes(self, nums: [int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        lastZeroIndex = 0;
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[lastZeroIndex] = nums[i];
                nums[i] = 0;
                lastZeroIndex = lastZeroIndex + 1;
        print(nums);


sln = Solution();
sln.moveZeroes([0,1,0,3,12]);