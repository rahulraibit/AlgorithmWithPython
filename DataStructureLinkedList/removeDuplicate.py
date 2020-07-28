#Remove Dups: Write code to remove duplicates from an unsorted linked list.
#FOLLOW UP How would you solve this problem if a temporary buffer is not
#allowed?

#(Page 220).
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkList:
    def __init__(self):
        self.head = None
        self.nextNode = None
    def add(self, data):
        if self.head is None:
            self.head = Node(data)
            self.nextNode = self.head
        else:
            self.nextNode.next = Node(data)
            self.nextNode = self.nextNode.next
    
    def removeDuplicate(self):
        dic = {};
        self.temp = self.head;
        self.previous = None;
        while(self.temp is not None):
            if self.temp.data in dic:
                self.previous.next = self.temp.next;
            else:
                dic[self.temp.data] = True;
                self.previous = self.temp;
            self.temp = self.temp.next;
       
          
def printLinkList(head): 
     while(head is not None):
         print(str(head.data),end='=>');
         head = head.next;

#3 -> 4 ->5 -> 6 ->3 ->4 ->5 ->8 ==> 3 -> 4 -> 5 ->6 ->8

# Code execution starts here
if __name__ == '__main__': 
  
    # Start with the empty list
    llist = LinkList() 
    llist.add(3)
    llist.add(4)
    llist.add(5)
    llist.add(1)
    llist.add(6)
    llist.add(3)
    llist.add(4)
    llist.add(5)
    llist.add(8)
    llist.add(8)
    llist.add(8)

printLinkList(llist.head);
llist.removeDuplicate();
print(" ")
printLinkList(llist.head);





