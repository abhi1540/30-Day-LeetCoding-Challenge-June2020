class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        
        if root:

            self.util(root)        
        
        return root
        
        
    def util(self, root):
        
        if not root:
            return 
        if root:
            temp = None

            temp = root.left
            root.left = root.right
            root.right = temp
              
            self.util(root.left)
            self.util(root.right)
            return root