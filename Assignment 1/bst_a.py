class TreeNode:

  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None


def mergeBSTs(tree1, tree2):
  if tree2 is not None:
    mergeBSTs(tree1, tree2.left)
    tree1 = insert(tree1, tree2.value)
    mergeBSTs(tree1, tree2.right)
  return tree1


def insert(root, value):
  if root is None:
    return TreeNode(value)
  if value < root.value:
    root.left = insert(root.left, value)
  else:
    root.right = insert(root.right, value)
  return root


# Helper function to perform an in-order traversal to verify the merged tree
def inOrderTraversal(root):
  if root is not None:
    inOrderTraversal(root.left)
    print(root.value, end=' ')
    inOrderTraversal(root.right)


# Example usage:
# Create two BSTs
tree1 = TreeNode(4)
tree1.left = TreeNode(2)
tree1.right = TreeNode(6)

tree2 = TreeNode(1)
tree2.left = TreeNode(3)
tree2.right = TreeNode(5)

# Merge the two BSTs
merged_tree = mergeBSTs(tree1, tree2)

# Verify the merged tree using in-order traversal
print("Merged Tree:")
inOrderTraversal(merged_tree)
