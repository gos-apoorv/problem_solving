"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:

        if not root:
            return 0
        elif not root.children:
            return 1
        else:
            max_depth = 0

            def traverse_tree(tree_node) -> int:
                depth, max_depth = 0, 1

                for node in tree_node:
                    if node.children:
                        depth = traverse_tree(node.children) + 1
                    # print(tree_node, "-->", node.val, "-->", depth)
                    max_depth = max(depth, max_depth)
                return max_depth

            return traverse_tree(root.children) + 1