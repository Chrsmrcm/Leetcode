'''
Given the root of a binary tree, return its maximum depth.
A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the 
farthest leaf node.
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def maxDepth(self, root: Optional[TreeNode], depth: Optional[int]=1) -> int:

    #edge case
    if not root:
        return 0
    
    #I added the optional depth parameter so that it could travel through the recursion
    #this way each recursion can return the max depth it reaches from each branch
    left,right = -1,-1
    if root.left:
        left = self.maxDepth(root.left,depth+1)

    if root.right:
        right = self.maxDepth(root.right,depth+1)
    
    return max(depth,left,right)