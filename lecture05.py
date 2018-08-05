"""
BST

Imperative implemtation of a BST
with an insertion test and keeps
track of size.

In this case elements must differ by
at least 3

"""


class Node:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None
    self.parent = None


def bst_insert(node, value):
  if node.value == value:
    return
  if value < node.value:
    if node.left:
      bst_insert(node.left, value)
    else:
      node.left = Node(value)
      node.left.parent = node
  if node.right is None:
    node.right = Node(value)
    node.right.parent = node
  bst_insert(node.right, value)


def bst_insert_list(arr):
  node = Node(arr[0])
  for i in range(1, len(arr)):
    bst_insert(node, arr[i])
  return node


def bst_search(node, value):
  if node.value == value:
    return True
  if node.value > value:
    return False if node.left is None \
      else bst_search(node.left, value)
  return False if node.right is None \
    else bst_search(node.right, value)


def bst_delete(node, value):
  if value < node.value and node.left is not None:
    bst_delete(node.left, value)
  elif value > node.value and node.right is not None:
    bst_delete(node.right, value)
  elif value == node.value:
    if node.left is None \
      and node.right is None \
      and node.parent is not None:
        if node == node.parent.left:
          node.parent.left = None
        else:
          node.parent.right = None
    elif node.left is None and node.parent:
      if node == node.parent.left:
        node.parent.left = node.right
      else:
        node.parent.right = node.right
    elif node.right is None and node.parent:
      if node == node.parent.left:
        node.parent.left = node.left
      else:
        node.parent.right = node.left
    else:
      tmp = node.left
      while tmp.right is not None:
        tmp = tmp.right
      node.value = tmp.value
      bst_delete(tmp, tmp.value)


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
