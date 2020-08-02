class Solution:
    def groupAnagrams(self, strs: [str]) -> [[str]]:
        dic = {};
        result = [];
        for i in range(len(strs)):
            if ''.join(sorted(strs[i])) not in dic:
                 dic[''.join(sorted(strs[i]))] = [strs[i]];
            else:
                dic[''.join(sorted(strs[i]))].append(strs[i]);
        
        for key in dic:
            result.append(dic[key]);
        print(result)
        return result;

sln =  Solution();
sln.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]);

