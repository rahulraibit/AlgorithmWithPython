#We have a collection of stones, each stone has a positive integer weight.

#Each turn, we choose the two heaviest stones and smash them together.  Suppose the stones have weights x and y with x <= y.  The result of this smash is:

#If x == y, both stones are totally destroyed;
#If x != y, the stone of weight x is totally destroyed, and the stone of weight y has new weight y-x.
#At the end, there is at most 1 stone left.  Return the weight of this stone (or 0 if there are no stones left.)

#Input: [2,7,4,1,8,1]
#Output: 1
#Explanation: 
#We combine 7 and 8 to get 1 so the array converts to [2,4,1,1,1] then,
#we combine 2 and 4 to get 2 so the array converts to [2,1,1,1] then,
#we combine 2 and 1 to get 1 so the array converts to [1,1,1] then,
#we combine 1 and 1 to get 0 so the array converts to [1] then that's the value of last stone.


from heapq import heappop, heappush, heapify

#heap = [];
#heapify(heap);

#heappush(heap, -1 * 10) 
#heappush(heap, -1 * 30) 
#heappush(heap, -1 * 20) 
#heappush(heap, -1 * 400) 
  
## printing the value of maximum element 
#print("Head value of heap : "+str(-1 * heap[0])) 
  
## printing the elements of the heap 
#print("The heap elements : ") 
#for i in heap: 
#    print(-1 * i, end = ' ') 
#print("\n") 
  
#element = heappop(heap) 
  
## printing the elements of the heap 
#print("The heap elements : ") 
#for i in heap: 
#    print(-1 * i, end = ' ') 

class Solution:
    def lastStoneWeight(self, stones):
        heap = [];
        heapify(heap);
        for s in stones:
            heappush(heap, -1*s);
        while len(heap) > 1:
            firstStone =  heappop(heap);
            secondStone =  heappop(heap);
            if firstStone != secondStone:
               remaining =  -(firstStone-secondStone);
               heappush(heap, -1*remaining);
        return -heappop(heap);

sln = Solution();
print(sln.lastStoneWeight([2,7,4,1,8,1]));