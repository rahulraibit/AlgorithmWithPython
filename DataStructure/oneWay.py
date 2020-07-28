#One Away: There are three types of edits that can be performed on strings: insert a character, remove a character, 
#or replace a character. Given two strings, write a function to check if they are one edit (or zero edits) away.
#EXAMPLE pale , pa e - > tru e pales , pal e - > tru e pale , bal e - > tru e pale , bae - > fals e

#(Page 211). 


def IsOneWay(str1, str2):
    if abs(len(str1) - len(str2)) >  1:
        return false;
    if abs(len(str1) - len(str2)) > 0:
        strlist1 = sorted(list(str1));
        strlist2 = sorted(list(str2));
        if len(str1) > len(str2):
            if ''.join(strlist1).find(''.join(strlist2)) > -1:
               return True;
            else: 
               return False;
        else:
            if ''.join(strlist2).find(''.join(strlist1)) > -1:
               return True;
            else: 
               return False;
    else:
         strlist1 = sorted(list(str1));
         strlist2 = sorted(list(str2));
         dic = {};
         for c in strlist1:
             if c in dic:
                 dic[c] = dic[c] + 1;
             else:
                 dic[c] = 1;

         for c in  strlist2:
             if c in dic:
                 dic[c] = dic[c] - 1;
         count = 0;
         for d in  dic:
             count = count  + dic[d];
         if count > 1:
            return False;
         else:
            return True;


print(IsOneWay('pale', 'ple'));
print(IsOneWay('pales', 'pale'));
print(IsOneWay('pale', 'bale'));
print(IsOneWay('pale', 'bae'));

