def isPowerOfFour(n):
    # using bit opeartors
    # for any multiple of there will be only 1 set in the binary.
    #    3.  A number n is a power of 4 if following conditions are met.
    #a) There is only one bit set in the binary representation of n (or n is a
    #power of 2)
    #b) The count of zero bits before the (only) set bit is even.
    # To find if only 1 bit is there - n and n & (n-1) 4- 100 & 011 = 000, 100
    # & 111 => 000
    # to prevent n == 0 extra and is required
     count = 0
     if n and not(n & (n - 1)):
         while n > 1:
             n = n >> 1
             count = count + 1
         if count % 2 == 0:
             return True
         return False
     return False
print(isPowerOfFour(5))

    #class Solution:
    #def isPowerOfFour(self, num: int) -> bool:
    #    factors = 0
    #    if num <= 0:
    #        return False;
    #    while num > 1:
    #        if num%4 == 0:
    #            factors += 1;
    #            num = num/4;
    #        else:
    #            return False;
    #    if factors%2 == 0 or factors%2 == 1:
    #        return True;
    #    return False;
            
            
             
        
        
        
        
        
