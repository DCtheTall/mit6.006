class Node:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None
    self.parent = None


def bst_insert(root, value):
  if root.value == value:
    return
  if value < root.value:
    if root.left:
      bst_insert(root.left, value)
    else:
      root.left = Node(value)
      root.left.parent = root
  if root.right is None:
    root.right = Node(value)
    root.right.parent = root
  bst_insert(root.right, value)


def bst_insert_list(arr):
  node = Node(arr[0])
  for i in range(1, len(arr)):
    bst_insert(node, arr[i])
  return node


def bst_search(root, value):
  if root.value == value:
    return True
  if root.value > value:
    return False if root.left is None \
        else bst_search(root.left, value)
  return False if root.right is None \
      else bst_search(root.right, value)


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
    elif node.parent:
      tmp = node.left
      while tmp.right is not None:
        tmp = tmp.right
      node.value = tmp.value
      bst_delete(tmp, tmp.value)


def print_inorder(root):
  if root.left is not None:
    print_inorder(root.left)
  print 'value: %2d ' % root.value
  if root.right is not None:
    print_inorder(root.right)


def bst_invert(node):
  if node == None:
    return None
  node.left = bst_invert(node.right)
  node.right = bst_invert(node.left)
  return node
