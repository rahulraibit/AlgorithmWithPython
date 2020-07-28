#1. Is Unique: Implement an algorithm to determine if a str1ing has all unique characters. 
# What if you cannot use additional data str1uctures?


def Isstr1ingCharUnique(str1, str1record):
    if len(str1) > 256:
        return false;
    for c in str1:
        if c in str1record and str1record[c] is True:
            print(c);
            return False;
        else:
            str1record[c] = True;
    return True;

str1 = 'abcdxs8324ikp9-01*lq'
str1record = {}
if Isstr1ingCharUnique(str1, str1record) is True:
    print('charater are unique in the str1ing');
else:
    print('character are not unique in the str1ing');


#without extra space
#O(n^2) - compare using 2 loops
#O(nlogn) - Sorting



