#String Compression: Implement a method to perform basic string compression using the counts of repeated characters. 
#For example, the string aabcccccaaa would become a2blc5a3. 
#If the "compressed "string would not become smaller than the original string, your method should return the original string. 
#You can assume the string has only uppercase and lowercase letters (a - z),

#(Page 213). 


def compressedString(str1):
    currentCharCount = 0;
    result= '';
    for i in range(0, len(str1)):
        currentCharCount = currentCharCount + 1;
        if i+1 >= len(str1) or str1[i] != str1[i+1]:
             result = result + str1[i] + str(currentCharCount);
             currentCharCount = 0;
    return str1 if len(str1) < len(result) else result



print(compressedString('aabcccccaaa'))
print(compressedString('aaa'))
print(compressedString('abc'))
print(compressedString('a'))
print(compressedString('tttlkkkkdsllslapdlplewqepqqweqweqw'))