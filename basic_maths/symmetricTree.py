class TreeNode:
    def __init__(self,val=0,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right

class Solution:
    def isSymmetric(self, root:  [TreeNode]) -> bool:
        
        def smr(left,right):
            if not left and not right:
                return True
            if not left or not right:
                return False

            return (left.val == right.val and smr(left.left,right.right) and smr(left.right,right.left))            

        return smr(root.left,root.right) 
    
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(2)
root.left.left = TreeNode(3)
root.left.right = TreeNode(4)
root.right.left = TreeNode(4)
root.right.right = TreeNode(3)

sol = Solution()
    

print(sol.isSymmetric(root))