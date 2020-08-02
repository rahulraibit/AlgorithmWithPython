#Write a function to connect all the adjacent nodes at the same level in a binary tree. 
#Structure of the given Binary Tree node is like following.


class Node:
    def __init__(self, data):
         self.left = self.right = self.nextRight = None;
         self.data = data;

def connect(root):
    queue = [];
    queue.append(root);
    temp = None;
    while queue:
        n = len(queue);
        for i in range(n):
            prev = temp;
            temp = queue.pop(0);
            if i > 0:
                prev.nextRight = temp;
            if temp.left:
                queue.append(temp.left);
            if temp.right:
                queue.append(temp.right);
    temp.nextRight = None;


root = Node(10); 
root.left = Node(8); 
root.right = Node(2); 
root.left.left = Node(3); 

connect(root); 

print("Following are populated nextRight pointers in "
                        + "the tree"
                        + "(-1 is printed if there is no nextRight)"); 


print("nextRight of", root.data, "is ", end = "") 
if root.nextRight: 
      print(root.nextRight.data) 
else: 
     print(-1) 
print("nextRight of", root.left.data, "is ", end = "")  
if root.left.nextRight: 
    print(root.left.nextRight.data) 
else: 
    print(-1) 
print("nextRight of", root.right.data, "is ", end = "")  
if root.right.nextRight: 
    print(root.right.nextRight.data) 
else: 
    print(-1) 
print("nextRight of", root.left.left.data, "is ", end = "")  
if root.left.left.nextRight: 
    print(root.left.left.nextRight.data) 
else: 
   print(-1) 
