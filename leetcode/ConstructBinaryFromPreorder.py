# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructTree(self, root, data):
        if data < root.val:
            if root.left == None:
                root.left = TreeNode(data);
            else:
                root.left = self.constructTree(root.left, data);
        elif data > root.val:
            if root.right == None:
                root.right = TreeNode(data);
            else:
                root.right = self.constructTree(root.right, data);
        return root
    
    def bstFromPreorder(self, preorder: [int]) -> TreeNode:
        l = len(preorder);
        if l == 0:
            return TreeNode();
        root = TreeNode(preorder[0]);
        for i in range(1, l):
            root  = self.constructTree(root, preorder[i]);
        return root;
        
sln = Solution();
sln.bstFromPreorder([8,5,1,7,10,12])            
