#2.2 Return Kth to Last: implement an algorithm to find the kth to last 
#element of a singly linked list. pg

#(Page 221). 


class Node:
    def __init__(self, data):
        self.data = data;
        self.next = None;

class LinkedList:
    def __init__(self):
        self.head = None;
        self.nextNode = None;
        self.data =None;
    def add(self, data):
        if self.head is None:
            self.head = Node(data);
            self.nextNode = self.head;
        else:
            self.nextNode.next = Node(data);
            self.nextNode = self.nextNode.next;
    
    def KthFromLastWithRecursion(self, temp, k):
        #base case
        if temp is None:
            return 0;
        jth = self.KthFromLastWithRecursion(temp.next, k) + 1
        if jth == k:
            self.data = temp.data;
        return jth;
  
    def KthFromLastWithLength(self, k):
        totalLength = 0;
        self.temp = self.head;
        while(self.temp is not None):
            totalLength = totalLength + 1;
            self.temp = self.temp.next;
        jth = totalLength - k + 1;
        self.temp = self.head;
        i = 1;
        while(i != jth):
            self.temp = self.temp.next;
            i = i + 1;
        return self.temp






#Method 3
#A more optimal, but less straightforward, solution is to implement this iteratively. 
#We can use two pointers, p1 and p2. We place them k nodes apart in the linked list by 
#putting p2 at the beginning and moving pi k nodes into the list. Then, when we move them at 
#the same pace, p1 will hit the end of the linked list after LENGTH - k steps. At that point,
#p2 will be LENGTH - k nodes into the list, or k nodes from the end.

#(Page 223). 

    
def printLinkList(head): 
     while(head is not None):
         print(str(head.data),end='=>');
         head = head.next;


# Code execution starts here
if __name__ == '__main__': 
  
    # Start with the empty list
    llist = LinkedList() 
    llist.add(14)
    llist.add(4)
    llist.add(5)
    llist.add(1)
    llist.add(6)
    llist.add(3)
    llist.add(9)
    llist.add(13)
    llist.add(0)
    llist.add(7)
    llist.add(10)

printLinkList(llist.head);
result = llist.KthFromLastWithLength(3);
print(" ")
print(result.data);
llist.KthFromLastWithRecursion(llist.head, 3);
print(" ")
print(llist.data)

#1 => 2 => 3 => 4=> 5



    