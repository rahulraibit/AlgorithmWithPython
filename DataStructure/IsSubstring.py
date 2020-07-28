
#1.9 String Rotation; Assume you have a method isSubstring which checks if one word is a substring of another. 
#Given two strings, si and s2, write code to check if s2 is a rotation of s1 using only one call to isSubstring 
#(e.g.,"waterbottle"isa rotation of'erbottlewat").

#(Page 218). 


def IsRotationOfstring(s1, s2):
    s1startingChar = s1[0];
    s2StartingIndex = s2.index(s1startingChar);
    if s2StartingIndex < 0:
        return false;

    s1StartingIndex = 0
    for i in range(0, len(s2)-1):
        x = (i + s2StartingIndex)%len(s2);
        if s1[i] != s2[x]:
            return False;
        s1StartingIndex = s1StartingIndex + 1;
    return True;


def IsRotationOfstring2(s1, s2):
    if len(s1) != len(s2) or s1  == None:
        return False;
    s3 = s1 + s2;
    if ''.join(s3).index(s2) > -1:
        return True;
    return False;

#So, we need to check if there's a way to split si into x and y such that xy = si and 
#yx = s2. Regardless of where the division between x and y is, 
#we can see that yx will always be a substring of xyxy.That is, s 2 
#will always be a substring of si s 1. And this is precisely how we solve the problem; 
#simply do is$ubstring(slsl , s2).

#(Page 219). 

s1 = "rahul3"
s2 = "l3rahu"

print(IsRotationOfstring2(s1, s2));