# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # base case. not a node
        if not root:
            return 0
        # base case. no children
        if not root.left and not root.right:
            return 1
        depth1, depth2 = 1, 1
        if root.left:
            depth1 += self.maxDepth(root.left)
        if root.right:
            depth2 += self.maxDepth(root.right)
        if depth1 >= depth2:
            return depth1
        else:
            return depth2
        