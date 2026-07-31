# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        res = []

        def dfs(curr):
            if not curr:
                res.append('x')
                return

            res.append(str(curr.val))
            dfs(curr.left)
            dfs(curr.right)

        dfs(root)
        return ",".join(res)

        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        self.i = 0
        data = data.split(",")
        def dfs():
            if self.i >= len(data):
                return None

            if data[self.i] == "x":
                self.i += 1
                return None

            node = TreeNode(data[self.i])
            self.i += 1
            node.left = dfs()
            node.right = dfs()

            return node

        return dfs()
