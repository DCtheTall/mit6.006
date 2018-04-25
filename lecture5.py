"""
Functional Binary Search Tree
Implementation

A bst structure using only lambda statements
by representing it a a series of nested linked
lists
"""

select_first = lambda x, y: x

select_second = lambda x, y: y

nil = lambda s: s(None, None)

head = lambda L: L(select_first)

tail = lambda L: L(select_second)

def append(e, L):
  return lambda s: s(e, L)

node = lambda v: append(v, append(nil, append(nil, nil)))

valueof = lambda node: head(node)

left_child = lambda node: head(tail(node))

right_child = lambda node: head(tail(tail(node)))

insert_left = lambda parent, child: \
  append(valueof(parent), append(child, append(right_child(parent), nil)))

insert_right = lambda parent, child: \
  append(valueof(parent), append(left_child(parent), append(child, nil)))

def fn_bst_insert(parent, child):
  if valueof(parent) > valueof(child) and left_child(parent) == nil:
    return insert_left(parent, child)
  if valueof(parent) > valueof(child):
    return insert_left(parent, fn_bst_insert(left_child(parent), child))
  if right_child(parent) == nil:
    return insert_right(parent, child)
  return insert_right(parent, fn_bst_insert(right_child(parent), child))

def fn_bst_search(node, value):
  if valueof(node) == value:
    return True
  if left_child(node) != nil and value < valueof(node):
    return fn_bst_search(left_child(node), value)
  if right_child(node) != nil:
    return fn_bst_search(right_child(node), value)
  return False

# TODO functional BST delete

"""
Imperative BST

Imperative implemtation of a BST
with an insertion test

In this case elements must differ by
at least 3
"""

def test(v1, v2):
  return abs(v1 - v2) >= 3

class Node:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

def bst_insert(node, value):
  if not test(node.value, value):
    return False
  if value < node.value and node.left is None:
    node.left = Node(value)
    return True
  if value < node.value:
    return bst_insert(node.left, value)
  if node.right is None:
    node.right = Node(value)
    return True
  return bst_insert(node.right, value)

# TODO delete with tree rotation
