class Solution:
    def countNodes(self, root: TreeNode) -> int:
        
        if root:
            return self.util(root)
        return 0
    
    def util(self, root):
        
        if not root:
            return 0
     
        return 1 + self.util(root.left) + self.util(root.right)