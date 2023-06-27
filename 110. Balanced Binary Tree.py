class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def height(node):
            if node is None:
                return 0
            return 1 + max(height(node.left), height(node.right))
        def isBalancedHelper(node):
            if node is None:
                return True
            left = height(node.left)
            right = height(node.right)
            if abs(left - right) > 1:
                return False
            return isBalancedHelper(node.left) and isBalancedHelper(node.right)
        return isBalancedHelper(root)
