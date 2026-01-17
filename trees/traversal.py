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
def inorder(root):
  if root is None:
    return
  inorder(root.left)
  print(root.value,end="")
  inorder(root.right)

#preorder traversal
def preorder(root):
  if root is None:
    return
  print(root.value,end="")
  preorder(root.left)
  preorder(root.right)

#postorder traversal
def postorder(root):
  if root is none
   return
 postorder(root.left)
postorder(root.right)
print(root.value,end="")

