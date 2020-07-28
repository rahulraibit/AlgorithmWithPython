#Check Permutation: Given two strings, write a method to decide if one is a permutation of the other.


#def checkStringPermuation(str1, str2):
#    if len(str1) != len(str2):
#        False;
#    dict1 = {};
#    dict2 = {};
#    for c in str1:
#        if c in dict1:
#            dict1[c] = dict1[c] + 1;
#        else:
#            dict1[c] = 0;

#    for c in str2:
#        if c in dict2:
#            dict2[c] = dict2[c] + 1;
#        else:
#            dict2[c] = 0;

#    for d in dict1:
#        if d in dict1 and d in dict2:
#            if dict1[d] != dict2[d]:
#                return False;
#        else:
#            return False;
#    return True;


#if checkStringPermuation('abc', 'bca') is True:
#    print('Both string are permuation of each other');
#else:
#    print('Both string are not permuation of each other');


#
#Method 2

def checkStringPermuation(str1, str2):
    if sorted(list(str1)) == sorted(list(str2)):
        return True

if checkStringPermuation('abc', 'bcd') is True:
    print('Both string are permuation of each other');
else:
    print('Both string are not permuation of each other');