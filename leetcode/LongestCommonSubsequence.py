#https://www.youtube.com/watch?v=NnD96abizww
#https://leetcode.com/explore/challenge/card/30-day-leetcoding-challenge/531/week-4/3311/
def LCS(X, Y):
    m = len(X);
    n = len(Y);
    L = [[None for _ in range(n+1)]for _ in range(m+1)]

    for i in range(m+1):
        for j in range(n+1):
            if i == 0 or j == 0:
                 L[i][j] = 0;
            elif X[i-1] == Y[j-1]:
                 L[i][j] = L[i-1][j-1] + 1
            else:
                 L[i][j] = max(L[i-1][j], L[i][j-1])

    #return L[m][n];
    i = m
    j = n
    result = []
    while i > 0 and j > 0:
        if X[i-1] == Y[j-1]:
            result.append(X[i-1]);
            i -= 1;
            j -= 1;
        elif L[i-1][j] > L[i][j-1]:
            i -= 1;
        else:
            j -= 1;
    result = "".join(result)[::-1]
    print(result)


print(LCS("abcdef", "acf"))
