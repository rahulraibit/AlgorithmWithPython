
#How to determine if a binary tree is height-balanced?


class Node:
     def __init__(self, data):
          self.left = self.right = None;
          self.data = data;

def height(root):
        if root is None:
            return 0;
        return max(height(root.left), height(root.right)) + 1;

def Isheightbalanced(root):
         if root is None:
             return True;

         lh = height(root.left);
         rh = height(root.right);
         
         if(abs(lh-rh) <= 1) and Isheightbalanced(root.left) and Isheightbalanced(root.right):
             return True;
         else:
             return False;

root = Node(1) 
root.left = Node(2) 
root.right = Node(3) 
root.left.left = Node(4) 
root.left.right = Node(5) 
root.left.left.left = Node(8) 

if Isheightbalanced(root): 
    print("Tree is balanced") 
else: 
    print("Tree is not balanced")  

#Complexity of the runtime is O(n^2)

#2nd Algorithm // Incomplete have to understand

#class Node:
#    def __init__(self, data):
#          self.left = self.right = None;
#          self.data = data;
#class height:
#    def __init__(self):
#          self.height = 0;

#def Isheightbalanced(root):
#         if root is None:
#             return True;
#         lh = height();
#         rh = height();
         
#         if(abs(lh-rh) <= 1) and Isheightbalanced(root.left) and Isheightbalanced(root.right):
#             return True;
#         else:
#             return False
