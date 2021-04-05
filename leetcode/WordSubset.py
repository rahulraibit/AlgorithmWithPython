import collections 
from collections import Counter
class Solution:
    def wordSubsets(self, A: [str], B: [str]) -> [str]:
        count = collections.Counter()
        res = []
        for b in B:
            count = count | collections.Counter(b)
        for a in A:
            if Counter(a) & count == count:
                res.append(a)
        return res
                    
        
sln = Solution()
sln.wordSubsets(["amazon","apple","facebook","google","leetcode"],
["e","o"])