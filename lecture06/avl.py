"""
Lecture 6: AVL Tree
-------------------
Self balancing binary search tree
that builds off the work I did
on BSTs for lecture 5

"""


from bst import Node, bst_insert, bst_delete, print_inorder


def get_node_height(node):
  """
  Get the height of a node.

  """
  if node is None:
    return 0
  if not node.left and not node.right:
    return 1
  return 1 + max(
      get_node_height(node.left),
      get_node_height(node.right))


def rotate_left(node):
  """
  Rotate a tree to the left

  """
  tmp = node.right
  tmp.left, node.right = node, tmp.left
  tmp.parent = node.parent
  node.parent = tmp
  if node.right:
    node.right.parent = node
  return tmp


def rotate_right(node):
  """
  Rotate the tree to the right

  """
  tmp = node.left
  tmp.right, node.left = node, tmp.right
  tmp.parent = node.parent
  node.parent = tmp
  if node.left:
    node.left.parent = node
  return tmp


def avl_test(node):
  """
  Test the AVL invariant of the tree,
  no node's subtrees' heights can differ
  by more than 1.

  """
  return 1 >= \
    abs(get_node_height(node.left) \
      - get_node_height(node.right))


def avl_balance(node):
  """
  Balance an AVL tree using tree
  rotation.

  """
  if not node:
    return None
  avl_balance(node.left)
  avl_balance(node.right)
  if avl_test(node):
    return
  if get_node_height(node.left) > get_node_height(node.right):
    rotate_right(node)
  rotate_left(node)


def avl_insert(node, value):
  """
  Insert into an AVL tree.

  """
  bst_insert(node, value)
  avl_balance(node)
  return node


def avl_delete(node, value):
  """
  Delete from an AVL tree.

  """
  bst_delete(node, value)
  avl_balance(node)
  return node


def avl_insert_list(arr):
  """
  Convert a list into a balanced binary
  search tree.

  """
  node = Node(arr[0])
  for i in range(1, len(arr)):
    node = avl_insert(node, arr[i])
  return node
