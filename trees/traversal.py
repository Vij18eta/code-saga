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


# Function to print the tree structure
def print_tree(root, prefix="", is_left=True):
    if root is not None:
        print(prefix + ("└── " if is_left else "┌── ") + str(root.value))
        print_tree(root.left, prefix + ("    " if is_left else "│   "), False)
        print_tree(root.right, prefix + ("    " if is_left else "│   "), True)

# Print the tree structure
print("Tree structure:")
print_tree(root)

# Call the traversal functions to print output
print("\nInorder traversal:")
inorder(root)
print("\nPreorder traversal:")
preorder(root)
print("\nPostorder traversal:")
postorder(root)
print()

