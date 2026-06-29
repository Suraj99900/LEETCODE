# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
maxDepth= 0
class Solution:
    

    def minDepth(self, root: Optional[TreeNode]) -> int:
        # print(root)
        if root is None:
            return 0

        # Leaf node
        if root.left is None and root.right is None:
            return 1

        # Only right subtree exists
        if root.left is None:
            return 1 + self.minDepth(root.right)

        # Only left subtree exists
        if root.right is None:
            return 1 + self.minDepth(root.left)

        # Both children exist
        return 1 + min(self.minDepth(root.left), self.minDepth(root.right))
        