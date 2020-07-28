#Palindrome Permutation: Given a string, write a function to check if it is a permutation of a palindrome.
# A palindrome is a word or phrase that is the same forwards and backwards, A permutation is a rearrangement of letters. 
# The palindrome does not need to be limited to just dictionary words.

#(Page 207). 

def IsPalindromPermutaion(str1):
    dic = {};
    for c in str1:
        if c in dic:
            dic[c] = dic[c] + 1;
        else:
            dic[c] = 1;

    numberOfOdds = 0;
    for d in dic:
        if dic[d]%2 > 0:
            numberOfOdds = numberOfOdds +1;

    if numberOfOdds > 1:
        return False;
    else:
        return True;


str1 = 'tactcoapapa';

if IsPalindromPermutaion(str1) is True:
     print('Yes');
else:
    print('No');

#Another Solution

#If you think more deeply about this problem, you might notice that we don't actually need to know the counts. 
#We just need to know if the count is even or odd. Think about flipping a light on/off (that is initially off). 
#If the light winds up in the of f state, we don't know how many times we flipped it, 
#but we do know it was an even count, Given this, we can use a single integer (as a bit vector). When we see a letter, 
#we map it to an integer between 0 and 26 (assuming an English alphabet). 
#Then we toggle the bit at that value. At the end of the iteration, we check that at most one bit in the integer is set to I. 
#We can easily check that no bits in the integer are 1: just compare the integer to 0. 
#There is actually a very elegant way to check that an integer has exactly one bit set to 1. Picture an integer like 00010000. 
#We could of course shift the integer repeatedly to check that there's only a single 1. Alternatively, if we subtract 1 from the number, 
#we'll get 00001111. What's notable about this

#(Page 209). 