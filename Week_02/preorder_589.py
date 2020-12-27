"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        def dfs(node):
            if not node: return
            res.append(node.val)

            if not node.children: return

            for child in node.children:
                dfs(child)

        res = []
        dfs(root)
        return res
