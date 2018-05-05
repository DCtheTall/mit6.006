"""
Functional AVL Tree

Self balancing functional
binary search tree
"""

from lecture5 import (
  nil,
  node,
  valueof,
  left_child,
  right_child,
  set_left_child,
  set_right_child,
  fn_bst_insert,
  fn_bst_delete,
  fn_print_inorder,
)


height = lambda node: \
  0 if node == nil \
    else 1 + max(
        height(left_child(node)),
        height(right_child(node)))


fn_rotate_left = lambda node: \
  set_left_child(
    right_child(node),
    set_right_child(
      node,
      left_child(right_child(node))))


fn_rotate_right = lambda node: \
  set_right_child(
    left_child(node),
    set_left_child(
      node,
      right_child(left_child(node))))


fn_avl_test = lambda node: 1 >= abs(height(left_child(node)) - height(right_child(node)))


apply_to_children = lambda f, node: \
  set_left_child(
    set_right_child(
      node,
      f(right_child(node))),
    f(left_child(node)))


def fn_avl_balance(node):
  if node == nil:
    return node
  if fn_avl_test(node):
    return apply_to_children(fn_avl_balance, node)
  if height(left_child(node)) > height(right_child(node)):
    return fn_rotate_right(apply_to_children(fn_avl_balance, node))
  return fn_rotate_left(apply_to_children(fn_avl_balance, node))


fn_avl_insert = lambda parent, value: fn_avl_balance(fn_bst_insert(parent, value))


fn_avl_delete = lambda node, value: fn_avl_balance(fn_bst_delete(node, value))


"""
Imperative AVL Tree

Self balancing binary search tree
that builds off the work I did
on BSTs for lecture 5
"""


from lecture5 import Node, bst_insert, bst_delete, print_inorder


def get_node_height(node):
  if node is None:
    return 0
  if not node.left and not node.right:
    return 1
  return 1 + max(get_node_height(node.left), get_node_height(node.right))


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
  return abs(get_node_height(node.left) - get_node_height(node.right)) <= 1


def avl_balance(node):
  if not node:
    return None
  node.left = avl_balance(node.left)
  node.right = avl_balance(node.right)
  if avl_test(node):
    return node
  if get_node_height(node.left) > get_node_height(node.right):
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
