#Write an algorithm to find the "next" node (i.e., in-order successor) of a given node in a 
#binary search tree.

#Input: node, root // node is the node whose Inorder successor is needed.
#Output: succ // succ is Inorder successor of node.

#If right subtree of node is not NULL, then succ lies in right subtree. Do the following.
#Go to right subtree and return the node with minimum key value in the right subtree.
#If right sbtree of node is NULL, then succ is one of the ancestors. Do the following.
#Travel up using the parent pointer until you see a node which is left child of its parent. The parent of such a node is the succ.

class Node:
    def __init__(self, data):
        self.data = data;
        self.left = self.right = None;

def inOrderSuccessor(root, node):
    successor = None;
    if node.right:
        return findMin(node.right);
    while node is not None:
        if node.data < root.data:
            successor = root;
            root = root.left;
        elif node.data > root.data:
            root = root.right;
        else:
            break;
    return successor;


def findMin(node):
    temp = node;
    while temp is not None:
        if temp.left is not None:
            temp = temp.left;
        else: break;
        return temp;

root = Node(20) 
root.left = Node(8);                     
root.right = Node(22); 
root.left.left = Node(4); 
root.left.right = Node(12); 
root.left.right.left = Node(10);   
root.left.right.right = Node(14);     
temp = root.right 


        #        20
        #    8        22
        #4      12
        #     10   14

  
succ = inOrderSuccessor( root, temp) 
if succ is not None: 
    print ("\nInorder Successor of % d is % d " %(temp.data, succ.data)) 
else: 
    print ("\nInorder Successor doesn't exist")
  