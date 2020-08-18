#https://leetcode.com/explore/challenge/card/may-leetcoding-challenge/534/week-1-may-1st-may-7th/3322/
#https://www.geeksforgeeks.org/check-two-nodes-cousins-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        if level(root, x, 1) == level(root, y, 1) and not IsSibling(root, x, y):
            return True;
        return False;
        
def IsSibling(root, key1, key2):
    if root is None:
        return 0;
    return ((root.left and root.left.val == key1 and root.right and root.right.val == key2) or 
              (root.left and root.left.val == key2 and root.right and root.right.val == key1) or
              IsSibling(root.left, key1, key2) or IsSibling(root.right, key1, key2))

def level(root, key, lvl):
    if root is None:
        return 0;
    if root.val == key:
        return lvl;
    l = level(root.left, key, lvl+1);
    if l != 0:
        return l
    return level(root.right, key, lvl + 1);

        