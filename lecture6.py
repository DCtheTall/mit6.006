"""
Imperative AVL Tree

Self balancing binary search tree
that builds off the work I did
on BSTs for lecture 5
"""

from lecture5 import Node, bst_insert, bst_delete, print_inorder


def height(node):
  if node is None:
    return 0
  if not node.left and not node.right:
    return 1
  return 1 + max(height(node.left), height(node.right))


get_size = lambda node: 0 if node is None else node.size


def rotate_left(node):
  tmp = node.right
  node.right = tmp.left
  tmp.left = node
  node.size = 1 + get_size(node.right) + get_size(node.left)
  tmp.size = 1 + get_size(tmp.left) + get_size(tmp.right)
  return tmp


def rotate_right(node):
  tmp = node.left
  node.left = tmp.right
  tmp.right = node
  node.size = 1 + get_size(node.right) + get_size(node.left)
  tmp.size = 1 + get_size(tmp.left) + get_size(tmp.right)
  return tmp


def avl_test(node):
  return abs(height(node.left) - height(node.right)) <= 1


def avl_balance(node):
  if not node:
    return None
  node.left = avl_balance(node.left)
  node.right = avl_balance(node.right)
  if avl_test(node):
    return node
  if height(node.left) > height(node.right):
    return rotate_right(node)
  return rotate_left(node)


def avl_insert(node, value):
  node = bst_insert(node, value)
  node = avl_balance(node)
  return node


def avl_delete(node, value):
  node = bst_delete(node, value)
  node = avl_balance(node)
  return node


def avl_insert_list(arr):
  node = Node(arr[0])
  for i in range(1, len(arr)):
    node = avl_insert(node, arr[i])
  return node
