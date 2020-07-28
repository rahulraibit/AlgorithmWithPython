class Solution:
    def isHappy(self, n: int) -> bool:
        dic = {};
        while(1):
            result = self.Srt(n);
            if result == 1:
                return true;
            elif dic[result] == True:
                return False;
            else:
                 n = result;
                 dic[result] = True;
    
    def Srt(self, number) -> int:
        result = 0;
        while(number):
           srtsum = (number%10)*(number%10);
           number = number/ 10;
           result = result + setsum;
            
        return result;

data = Solution();
print(data.isHappy(19));
            