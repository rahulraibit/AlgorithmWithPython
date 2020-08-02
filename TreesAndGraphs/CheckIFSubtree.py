#T1 and T2 are two very large binary trees, with T1 much bigger than T2. Create an 
#algorithm to determine if 12 is a subtree ofTl . 
#AtreeT2 is a subtree of T1 if there exists a node n in T1 such that the subtree of n is identical to 12, 
#That is, if you cut off the tree at node n, the two trees would be identical.

class Node:
    def __init__(self, data):
        self.data = data;
        self.left = self.right = None;

def IsTreeisSubTree(root1, root2):
    if root2 is None:
        return True;
    if root1 is None:
        return False;
    if IsIdentical(root1, root2):
        return True;
    return IsTreeisSubTree(root1.left, root2) or IsTreeisSubTree(root1.right, root2);
    
def IsIdentical(root1, root2):
    if root1 is None and root2 is None:
        return True;
    if root1 is None or root2 is None:
        return False;
    return root1.data == root2.data and IsIdentical(root1.left, root2.left) and IsIdentical(root1.right, root2.right)

root1 = Node(10);
root1.left = Node(6);
root1.right = Node(15);
root1.right.left = Node(12);
root1.right.right = Node(16);
root1.left.left = Node(2);
root1.left.right = Node(3);

root2 = Node(15);
root2.left = Node(12);
root2.right = Node(16);


if IsTreeisSubTree(root1, root2):
    print ("T1 and T2 are identical tree");
else: print("T1 and T2 are not the identical tree");