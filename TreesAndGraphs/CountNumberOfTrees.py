#BST Sequences: A binary search tree was created by traversing through an array from left to right 
#and inserting each element. Given a binary search tree with distinct elements, print all possible 
#arrays that could have led to this tree -- Have to see the solution

def countNumberOfTress(n):
    T = [0]*(n+1);
    T[0] = 1;
    T[1] = 1;
    for i in range(2, n + 1):
        for j in range(0, i):
            T[i] = T[i] + T[j]*T[i-j-1];
    return T[n];

print(countNumberOfTress(3));