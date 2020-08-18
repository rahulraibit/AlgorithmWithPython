# Definition for a binary tree node.
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
class Solution:
    result = 0
    def maxPathSumUtil(self, node):
        if node == None:
            return -10;
        left = self.maxPathSumUtil(node.left);
        right = self.maxPathSumUtil(node.right);
        xx = max(max(left, right) + node.val, node.val) 
        yy = max(xx, left + right + node.val);
        self.result = max(self.result, yy);
        return xx
    def maxPathSum(self, root: TreeNode) -> int:
        self.maxPathSumUtil(root);
        print(self.result);

root = TreeNode(-1);
#root.left = TreeNode(2);
#root.right = TreeNode(3);
#root.left.left = TreeNode(4);
#root.left.right = TreeNode(5);
sln = Solution();
sln.maxPathSum(root);