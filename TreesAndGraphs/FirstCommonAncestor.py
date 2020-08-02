#First Common Ancestor: Design an algorithm and write code to find the first
#common ancestor
#of two nodes in a binary tree.  Avoid storing additional nodes in a data
#structure.  NOTE: This is not
#necessarily a binary search tree
class Node:
    def __init__(self, data):
        self.left = self.right = None
        self.data = data


def findCommonAncestor(root, n1, n2):
    if root is None:
        return None

    if root.data == n1 or root.data == n2:
        return root
    
    left = findCommonAncestor(root.left, n1, n2)
    right = findCommonAncestor(root.right, n1, n2)
    
    if left is None and right is None:
        return None
    if left and right:
        return root
    if left is None:
        return right
    else: return left

root = Node(1) 
root.left = Node(2) 
root.right = Node(3) 
root.left.left = Node(4) 
root.left.right = Node(5) 
root.right.left = Node(6) 
root.right.right = Node(7) 
  
print("LCA(4, 5) = %d" %(findCommonAncestor(root, 4, 5)).data) 
print("LCA(4, 6) = %d" %(findCommonAncestor(root, 4, 6)).data)
print("LCA(3, 4) = %d" %(findCommonAncestor(root,3,4)).data) 
print("LCA(2, 4) = %d" %(findCommonAncestor(root,2, 4)).data); 