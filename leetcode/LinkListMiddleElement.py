import math;

class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        count = 0
        temp  = head;
        while temp != None:
            count =  count + 1;
            temp = temp.next;
        mid = math.ceil((count + 1)/2);
        print(mid);
        i = 0;
        while i != mid:
            head = head.next;
            i = i + 1;
        return head;

sln = Solution();
head = ListNode(1);
head.next = ListNode(2);
head.next.next = ListNode(3);
head.next.next.next = ListNode(4);
head.next.next.next.next = ListNode(5);
sln.middleNode(head);