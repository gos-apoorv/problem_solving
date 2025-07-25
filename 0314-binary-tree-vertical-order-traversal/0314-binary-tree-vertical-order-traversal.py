# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import defaultdict

class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        if root is None:
            return []

        column_dict = defaultdict(list)
        queue = deque([(root, 0)])

        while queue:
            node, column = queue.popleft()

            if node is not None:
                column_dict[column].append((node.val))

                queue.append((node.left, column - 1))
                queue.append((node.right, column + 1))

        return [column_dict[x] for x in sorted(column_dict.keys())]

        

        