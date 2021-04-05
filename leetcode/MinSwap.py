#min swap for sorting the array

def minswap(arr):
    arrPos = [(i, n ) for i,n in enumerate(arr)]
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

#Must visit
#Point to next higher value node in a linked list with an arbitrary pointer
#https://www.geeksforgeeks.org/point-to-next-higher-value-node-in-a-linked-list-with-an-arbitrary-pointer/

#find-distance-between-two-nodes-of-a-binary-tree
#https://www.geeksforgeeks.org/find-distance-between-two-nodes-of-a-binary-tree/

#Get the local maxima or minima in array
#https://www.geeksforgeeks.org/amazon-interview-experience-set-326-sde-ii/
#https://www.geeksforgeeks.org/fix-two-swapped-nodes-of-bst/
#https://amortizedminds.wordpress.com/2016/06/28/design-questions/
#https://www.youtube.com/watch?v=ontAs5VfCwo
#https://github.com/donnemartin/system-design-primer
#https://www.geeksforgeeks.org/puzzle-cut-blue-painted-cube/
#https://www.geeksforgeeks.org/nuts-bolts-problem-lock-key-problem/.
#https://www.geeksforgeeks.org/edit-distance-dp-5/
#LCS of 2 strings

#https://www.geeksforgeeks.org/evaluation-prefix-expressions/ => read from the end and use stack
#https://practice.geeksforgeeks.org/problems/evaluation-of-postfix-expression1735/1 =  Read from the left and use stack
#https://www.geeksforgeeks.org/write-a-c-program-to-print-all-permutations-of-a-given-string/
#https://www.geeksforgeeks.org/trapping-rain-water/
#https://www.geeksforgeeks.org/print-right-view-binary-tree-2/
#https://practice.geeksforgeeks.org/problems/clone-a-linked-list-with-next-and-random-pointer/1
#Given a result of a competition among all the students of a class, write a program to make students stand in a order such that every student must have lost to the student 
#in his/her immediate left and won against the student to his/her immediate right
#https://www.geeksforgeeks.org/check-if-a-binary-tree-is-subtree-of-another-binary-tree/
#https://www.geeksforgeeks.org/kth-smallest-element-in-a-row-wise-and-column-wise-sorted-2d-array-set-1/
#https://www.geeksforgeeks.org/largest-rectangle-under-histogram/

#What they do for force update in the mobile app
#Implementation of Queue but with certain kind of constraints. Basically looking for knowledge of design patterns
#Implementation of Queue but with certain kind of constraints. Basically looking for knowledge of design patterns
#https://www.geeksforgeeks.org/maximum-sum-path-across-two-arrays/
#https://www.geeksforgeeks.org/find-maximum-number-possible-by-doing-at-most-k-swaps/
#round robin load balancer, hash-map based load balancer, two layer caching, nosql db, design patterns, 
#solid principles, ACID property, CAP theorem
#https://www.geeksforgeeks.org/given-sorted-dictionary-find-precedence-characters/
#esign a geographically partitioned multi-player card game
#https://www.geeksforgeeks.org/generate-palindromic-numbers-less-n/
#https://www.geeksforgeeks.org/design-a-data-structure-that-supports-insert-delete-search-and-getrandom-in-constant-time/
#https://www.geeksforgeeks.org/minimum-steps-reach-target-knight/
#Design a scalable meeting room booking system
#https://www.geeksforgeeks.org/minimum-no-of-operations-required-to-make-all-array-elements-zero/
#https://www.geeksforgeeks.org/longest-possible-chunked-palindrome/
#https://www.geeksforgeeks.org/print-left-view-binary-tree/
#https://practice.geeksforgeeks.org/problems/minimum-platforms-1587115620/1
#https://www.geeksforgeeks.org/print-nodes-distance-k-given-node-binary-tree/
#https://www.geeksforgeeks.org/triplet-with-a-given-sum-in-bst-set-2/
#https://www.geeksforgeeks.org/partition-a-set-into-two-subsets-such-that-the-difference-of-subset-sums-is-minimum/
#https://www.geeksforgeeks.org/find-the-row-with-maximum-number-1s/
#https://www.geeksforgeeks.org/minimum-number-of-additons-to-make-the-string-balanced/
#https://www.geeksforgeeks.org/find-first-non-repeating-character-stream-characters/
#https://www.geeksforgeeks.org/maximum-number-formed-from-array-with-k-number-of-adjacent-swaps-allowed/
#https://www.geeksforgeeks.org/find-next-greater-number-set-digits/
#https://www.geeksforgeeks.org/length-longest-consecutive-1s-binary-representation/
#https://www.geeksforgeeks.org/count-number-binary-strings-without-consecutive-1s/
#int t=a[n-1] + b[n-1];//total no of string with non consecutive ones
#return pow(2,n)-t;//no of string with consecutive ones