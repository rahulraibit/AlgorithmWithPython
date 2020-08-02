#A program to check if a binary tree is BST or not


class Node:
    def __init__(self, data):
        self.left = self.right = None;
        self.data = data;
    
def IsBST(root, l, r):
        if root is None:
            return True;
        if(l is not None and root.data < l.data):
            return False;
        if(r is not None and r.data < root.data):
            return False;
        return IsBST(root.left, l, root) and IsBST(root.right, root, r);

	
root = Node(4) 
root.left = Node(2) 
root.right = Node(5) 
root.left.left = Node(1) 
root.left.right = Node(3) 
	#root.right.left.left = newNode(40) 
if (IsBST(root,None,None)): 
   print("Is BST") 
else: 
   print("Not a BST") 