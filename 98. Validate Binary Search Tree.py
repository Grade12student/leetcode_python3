class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def inorder(node, lower=float('-inf'), upper=float('inf')):
            if not node:
                return True

            val = node.val
            if val <= lower or val >= upper:
                return False
            if not inorder(node.left, lower, val):
                return False
            if not inorder(node.right, val, upper):
                return False
            return True
        return inorder(root)
