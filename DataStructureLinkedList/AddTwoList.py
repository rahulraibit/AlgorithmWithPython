#Sum Lists: You have two numbers represented by a linked list, where each node contains a single digit. 
#The digits are stored in reverse order, such that the 1's digit is at the head of the iist. Write a function that 
#adds the two numbers and returns the sum as a linked list.

#(Page 226). 



#input; (7- > 1 -> 6) + (S -> 9 -> 2). That is, 617 + 295. Output; 2 -> 1 -> 9.That is, 912.

#(Page 226). 


class Node:
    def __init__(self, data):
        self.data = data;
        self.next = None;

class LinkedList:
    def __init__(self):
        self.head = None;
        self.nextNode = None;
        self.data =None;
    def reverseList(self, head: Node):
        if not head.next or not head:
            return head;
        p = self.reverseList(head.next);
        head.next.next = head
        head.next = None;
        return p;
    #def reverseList(self, head: Node):
    #    prev = None
    #    current = head
    #    next = None
    #    while current:
    #        next = current.next;
    #        current.next = prev
    #        prev = current
    #        current = next
    #    return prev; 
    def add(self, data):
        if self.head is None:
            self.head = Node(data);
            self.nextNode = self.head;
        else:
            self.nextNode.next = Node(data);
            self.nextNode = self.nextNode.next;

    def swapPairs(self, head: Node) -> Node:
        newhead = Node(-1)
        newhead.next = head
        prev = newhead
        while head and head.next:
            firstNode = head;
            secondNode = head.next;
            prev.next =  secondNode
            firstNode.next = secondNode.next
            secondNode.next = firstNode
            
            prev = firstNode
            head = firstNode.next
        return newhead.next


# Code execution starts here
if __name__ == '__main__': 
  
    # Start with the empty list
    llist1 = LinkedList() 
    llist1.add(1)
    llist1.add(2)
    llist1.add(3) 
    llist1.add(4)
    llist1.reverseList(llist1.head)
    #llist1.swapPairs(llist1.head)

result=0
rem = 0;
#if len(llist1) >= len(llist2):
temp1 = llist1.head;
temp2 = llist2.head;
while(llist1!= None):
       result = result + (temp1.data + temp2.data + rem);
       rem = (int)(result/10);
       result = (int)(result%10);
       result = result*10;
       temp1 = temp1.next;
       temp2 = temp2.next;
#else:
while(list2!= null):
       result =  llist1.data + llist2.data + rem;
       rem = result%10;
print(result);