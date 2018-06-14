"""
Functional Binary Search Tree
Implementation

A bst structure using only lambda statements
by representing it a a series of nested linked
lists

"""

nil = lambda s: s(None, None)


def head(L): return L(lambda x, y: x)


def tail(L): return L(lambda x, y: y)


def append(e, L):
  return lambda s: s(e, L)


node = lambda v: append(v, append(nil, append(nil, nil)))


valueof = lambda node: head(node)


left_child = lambda node: head(tail(node))


right_child = lambda node: head(tail(tail(node)))


set_value = lambda node, value: \
  append(value, append(left_child(node), append(right_child(node), nil)))


set_left_child = lambda parent, child: \
  append(valueof(parent), append(child, append(right_child(parent), nil)))


set_right_child = lambda parent, child: \
  append(valueof(parent), append(left_child(parent), append(child, nil)))


def fn_bst_insert(parent, value):
  if valueof(parent) > value \
    and left_child(parent) == nil:
      return set_left_child(parent, node(value))
  if valueof(parent) > value:
    return set_left_child(parent, fn_bst_insert(left_child(parent), node(value)))
  if right_child(parent) == nil:
    return set_right_child(parent, node(value))
  return set_right_child(parent, fn_bst_insert(right_child(parent), node(value)))


def fn_bst_search(node, value):
  if valueof(node) == value:
    return True
  if left_child(node) != nil and value < valueof(node):
    return fn_bst_search(left_child(node), value)
  if right_child(node) != nil:
    return fn_bst_search(right_child(node), value)
  return False


def fn_bst_delete(node, value):
  if valueof(node) < value:
    return set_left_child(node, fn_bst_delete(left_child(node), value))
  if valueof(node) > value:
    return set_right_child(node, fn_bst_delete(right_child(node), value))
  if left_child(node) == nil and right_child(node) == nil:
    return nil
  if left_child(node) == nil:
    return right_child(node)
  if right_child(node) == nil:
    return left_child(node)
  return set_left_child(
    set_value(node, valueof(left_child(node))),
    fn_bst_delete(set_value(left_child(node), value), value))


def fn_print_inorder(node):
  if node == nil:
    return
  fn_print_inorder(left_child(node))
  print valueof(node)
  fn_print_inorder(right_child(node))


def fn_bst_invert(node):
  if node == nil:
    return nil
  return set_left_child(
    set_right_child(
      node,
      fn_bst_invert(left_child(node))),
    fn_bst_invert(right_child(node)))


"""
Imperative BST

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
    node.left = bst_delete(node.left, value)
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
  node.value = node.left.value
  node.left.value = value
  node.size -= 1
  node.left = bst_delete(node.left, value)
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
