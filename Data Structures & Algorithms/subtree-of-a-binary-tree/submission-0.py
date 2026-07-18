# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        curr = root
        stack = []
        while curr:
            if curr.val == subRoot.val:
                if self.isSameTree(curr, subRoot):
                    return True
            if curr.right:
                stack.append(curr.right)
            if curr.left:
                curr = curr.left
            elif stack:
                curr = stack.pop()
            else:
                curr = None

        return False

    def isSameTree(self, t1, t2) -> bool:
        if t1 is None and t2 is None:
            return True
        if not t1 or not t2:
            return False
        if t1.val == t2.val:
            return self.isSameTree(t1.left, t2.left) and self.isSameTree(t1.right, t2.right)