#https://www.youtube.com/watch?v=9ZyLjjk536U
class Solution:
    def findMaxLength(self, nums):
        first_oc = {};
        answer = 0;
        pref = 0;
        n = len(nums);
        for i in range(n):
            pref += (1 if nums[i] == 1 else -1);
            if pref == 0:
                answer = max(answer, i + 1);
            if pref in first_oc:
                answer = max(answer, i - first_oc[pref]);
            else:
                first_oc[pref] = i;
        return answer;


sln = Solution()
print(sln.findMaxLength([1,0]))
