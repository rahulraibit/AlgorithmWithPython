#URLify: Write a method to replace all spaces in a str1ing with'%20'You may assume that 
#the str1ing has sufficient space at the end to hold the additional characters, 
#and that you are given the "true" length of the str1ing, (Note: if implementing in Java, 
#please use a character array so that you can perform this operation in place.)

#(Page 206). 


def urlify(str1):
    count = 0;
    for c in str1:
        if(c) is ' ':
            count = count + 1;
    
    str1 = list(str1);
    prevLength = len(str1);
    newLenght = len(str1) + count*2;
    for i in range(prevLength -1, newLenght -1):
        str1.append('0');

    for i in range(prevLength-1, 0, -1):
        if str1[i] != ' ':
            str1[newLenght-1] = str1[i]
            newLenght = newLenght - 1;
        else:
            str1[newLenght-1] = '0';
            str1[newLenght-2] = '2';
            str1[newLenght-3] = '%';
            newLenght = newLenght - 3;
    
    return ''.join(str1);





str1= 'tu m mere  ho'

print(urlify(str1))