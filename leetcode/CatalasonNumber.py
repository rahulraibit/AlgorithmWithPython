#Catalan number implementation

#def printCatalenNumber(n):
#    if n == 0 or n == 1:
#        return 1;
#    result = 0;
#    for i in range(n):
#        result = result + printCatalenNumber(i)*printCatalenNumber(n-i-1)
#    return result;

#print(printCatalenNumber(2));

def printCatalenNumberUsingDp(n):
    dp = [ 0 for _ in range(n+1)]
    dp[0] = 1
    dp[1] = 1
    for i in range(2, len(dp)):
        for j in range(i):
            dp[i] = dp[i] + dp[j] * dp[i-j-1]
    return dp[n];
print(printCatalenNumberUsingDp(4));

