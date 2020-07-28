
#Rotate Matrix: Given an image represented by an NxN matrix, where each pixel in the image is 4 bytes, 
#write a method to rotate the image by 90 degrees. Can you do this in place?

#(Page 215). 
             #Right Rotate

             #1 2 3       7 4 1              1, 2, 3, 4                        13 9  5 1
             #4 5 6    => 8 5 2              5, 6, 7, 8             =>         14 10 6 2
             #7 8 9       9 6 3              9, 10, 11, 12,                    15 11 7 3
                                            #13, 14, 15, 16                    16 12 8 4

             #left Rotate

             #1 2 3       3 6 9
             #4 5 6    => 2 5 8             
             #7 8 9       1 4 7 


  

def rotateMatrixRight(M):
    for l in range(int((len(M)/2))):
        first = l
        last = len(M) - first - 1
        for i in range(first, last):
            offset = i - first;
            top = M[first][i];
            M[first][i] = M[last-offset][first];
            M[last-offset][first] = M[last][last-offset];
            M[last][last-offset] = M[i][last];
            M[i][last] = top;
    printData(M);

def rotateMatrixLeft(M):
    for l in range(int((len(M)/2))):
        first = l
        last = len(M) - first - 1
        for i in range(first, last):
            offset = i - first;
            top = M[first][i];
            M[first][i] = M[i][last];
            M[i][last] = M[last][last-offset];
            M[last][last-offset] = M[last-offset][first];
            M[last-offset][first] = top;
    printData(M);


def printData(M):
    for i in range(len(M)):
        for j in range(len(M[i])):
                  print(M[i][j]);
    print(" ")


M = [[1,2,3],[4,5,6],[7,8,9]]
M1 = [[1,2,3,4],[5,6,7,8],[9,10,11,12], [13, 14, 15, 16]]
printData(M);
rotateMatrixLeft(M);
