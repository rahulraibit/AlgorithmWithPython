#min swap for sorting the array

def minswap(arr):
    arrPos = [*enumerate(arr)]
    arrPos = sorted(arrPos, key = lambda k : k[1])
    vis = {k : False for k in range(len(arr))}
    ans = 0;
    for i in range(len(arrPos)):
        if vis[i] or arrPos[i][0] == i:
            continue;
        j = i
        cycleSize = 0;
        while not vis[j]:
            vis[j] = True;
            cycleSize += 1;
            j = arrPos[j][0]
        if cycleSize > 0:
            ans = ans + cycleSize - 1;
    return ans;
print(minswap([4, 3, 1, 2]))
