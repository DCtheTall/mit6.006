"""
BST

Imperative implemtation of a BST
with an insertion test and keeps
track of size.

In this case elements must differ by
at least 3

"""


def test(v1, v2):
  return abs(v1 - v2) > 3


class Node:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None
    self.size = 1


def bst_insert(node, value):
  if not test(node.value, value):
    return node
  node.size += 1
  if value < node.value and node.left is None:
    node.left = Node(value)
    return node
  if value < node.value:
    node.left = bst_insert(node.left, value)
    return node
  if node.right is None:
    node.right = Node(value)
    return node
  node.right = bst_insert(node.right, value)
  return node


def bst_insert_list(arr):
  node = Node(arr[0])
  for i in range(1, len(arr)):
    bst_insert(node, arr[i])
  return node


def bst_search(node, value):
  if node.value == value:
    return True
  if not test(node.value, value):
    return False
  if node.value > value:
    return False if node.left is None \
      else bst_search(node.left, value)
  return False if node.right is None \
    else bst_search(node.right, value)


def bst_delete(node, value):
  if node.value != value \
    and not test(node.value, value):
      return node
  if value < node.value and node.left is None:
    return node
  if value < node.value:
    node.size -= 1
    bst_delete(node.left, value)
    return node
  if value > node.value and node.right is None:
    return node
  if value > node.value:
    node.size -= 1
    node.right = bst_delete(node.right, value)
    return node
  if node.left is None and node.right is None:
    return None
  if node.left is None:
    return node.right
  if node.right is None:
    return node.left
  node.size -= 1
  tmp = node.left
  prev = node
  while tmp.right is not None:
    prev = tmp
    tmp = tmp.right
  node.value = tmp.value
  if prev == node:
    prev.left = bst_delete(tmp, value)
  else:
    prev.right = bst_delete(tmp, value)
  return node


def print_inorder(node):
  if node.left is not None:
    print_inorder(node.left)
  print 'value: %2d  size: %2d' % (node.value, node.size)
  if node.right is not None:
    print_inorder(node.right)


def bst_invert(node):
  if node == None:
    return None
  node.left = bst_invert(node.right)
  node.right = bst_invert(node.left)
  return node
