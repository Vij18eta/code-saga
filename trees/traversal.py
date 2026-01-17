class TreeNode:
def _init_(self,value):
  self.value=value
  self.left=None
  self.right=None

root=TreeNode(1)
root.right=TreeNode(2)
root.left=TreeNode(3)
root.left.right=TreeNode(4)
root.left.left=TreeNode(5)

#inorder traversal
