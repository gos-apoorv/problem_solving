# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        def tree_traversal(node:Optional[TreeNode]) -> List[int]:
            result = []
            if node.left:
                result.extend(tree_traversal(node.left))
            
            result.append(node.val)

            if node.right:
                result.extend(tree_traversal(node.right))
            
            return result
        
        if root == None:
            return []
        ans = tree_traversal(root)  
        return ans

        