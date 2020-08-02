#Input: 19
#Output: true
#Explanation: 
#12 + 92 = 82
#82 + 22 = 68
#62 + 82 = 100
#12 + 02 + 02 = 1

#class Solution:
#    def isHappy(self, n: int) -> bool:
#        dic = {};
#        while(1):
#            result = self.Srt(n);
#            if result == 1:
#                return true;
#            elif dic[result] == True:
#                return False;
#            else:
#                 n = result;
#                 dic[result] = True;
    
#    def Srt(self, number) -> int:
#        result = 0;
#        while(number):
#           srtsum = (number%10)*(number%10);
#           number = number/ 10;
#           result = result + setsum;
            
#        return result;

#data = Solution();
#print(data.isHappy(19));
          
class Solution:
    def isHappy(self, n: int) -> bool:
        dic = {};
        while(1):
            if n == 1:
                return True;
            if n in dic:
                return False;
            else:
                result = 0;
                dic[n] = True;
                while n:
                    remender = n % 10;
                    n = int(n/ 10);
                    result = result + remender * remender;
                n = result;



data = Solution();
print(data.isHappy(19));          
        