#You are implementing a binary tree class from scratch which, in addition to 
#insert , find , and delete , has a method getRandomNode() which returns a random node 
#from the tree. All nodes should be equally likely to be chosen. Design and implement an algorithm 
#for getRandomNode, and explain how you would implement the rest of the methods

class Node:
    def __init__(self, data):
        self.left = self.right = None;
        self.data = data;

    def insert(self, data):
        if self.data < data:
            if self.right is None:
                self.right = Node(data);
            else:
                self.right.insert(data);
        elif self.data > data:
            if self.left is None:
                self.left = Node(data);
            else:
                self.left.insert(data);
    def printData(self):
        if self.left:
            self.left.printData();
        print(self.data);
        if self.right:
            self.right.printData();


def delete(root, data):
    if root.data is None:
       return None;
    if data < root.data:
       root.left.delete(data);
    elif data > self.data:
       root.right.delete(data);
    else:
        if root.left is None:
            temp = root.right;
            root = 

root = Node(10);
root.insert(6);
root.insert(15);
root.insert(2);
root.insert(3);
root.insert(12);
root.insert(16);
root.insert(7);

root.printData();