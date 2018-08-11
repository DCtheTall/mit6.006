"""
Red-Black Tree
--------------

"""


class Node(object):
  """
  Binary search tree Node class

  """
  def __init__(self, value, color=True):
    self.value = value
    self.color = color
    self.left = None
    self.right = None
    self.parent = None

  def grandparent(self):
    """
    Get grandparent of node

    """
    if self.parent is None:
      return None
    return self.parent.parent

  def sibling(self):
    """
    Get the node's sibling

    """
    if self.parent is None:
      return None
    if self == self.parent.left:
      return self.parent.right
    return self.parent.left

  def uncle(self):
    """
    Get uncle of node

    """
    if self.parent is None:
      return None
    return self.parent.sibling()

  def inorder(self):
    """
    Get tree as an inorder list

    """
    lst = []
    if self.left is not None:
      lst = self.left.inorder()
    lst.append(self.value)
    if self.right is not None:
      lst.extend(self.right.inorder())
    return lst


def bst_insert(parent, child):
  """
  Insert into a binary search tree

  """
  if child.value == parent.value:
    return
  if child.value < parent.value:
    if parent.left is None:
      parent.left = child
      child.parent = parent
    else:
      bst_insert(parent.left, child)
  elif parent.right is None:
    parent.right = child
    child.parent = parent
  else:
    bst_insert(parent.right, child)


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


def rotate_if_inner_child(node):
  grandparent = node.grandparent()
  if grandparent.left.right == node:
    rotate_left(node.parent)
    return True
  if grandparent.right.left == node:
    rotate_right(node.parent)
    return True
  return False


def red_black_insert_repair(node):
  """
  Restores the balancing properites of a
  red-black tree after insert

  node: Node painted red
  """
  if node.parent is None:
    node.color = False
  if not node.parent.color: # if parent is black, tree is balanced
    return
  uncle = node.uncle()
  if uncle and uncle.color:
    # if the parent and uncle are black, change their color to black
    node.parent.color = False
    uncle.color = False
    grandparent = node.grandparent()
    grandparent.color = True # also paint the grandparent red
    red_black_insert_repair(grandparent) # and rebalance at grandparent (root test)
  else:
    if rotate_if_inner_child(node):
      node = node.parent
    grandparent = node.grandparent()
    # if the parent is red, node must have grandparent
    if node == grandparent.left.left:
      rotate_right(grandparent)
    else:
      rotate_left(grandparent)
    grandparent.color = True
    node.parent.color = False



def red_black_insert(parent, child):
  """
  Insert a node into an existing red-black
  tree

  """
  child.parent = parent
  bst_insert(parent, child)
  red_black_insert_repair(child)


# def replace_node(node, child):
#   """
#   Replace a node with one of its children

#   """
#   child.parent = node.parent
#   if node.parent is None:
#     return
#   elif node == node.parent.left:
#     node.parent.left = child
#   else:
#     node.parent.right = child


# def delete_case1(node):
#   """
#   If the node is not the root,
#   continue to case 2

#   """
#   if node.parent is None: # if the node is the root, we're done
#     return
#   delete_case2(node)


# def delete_case2(node):
#   """
#   If the node's sibling is red,
#   repaint the parent red and
#   repaint the sibling black

#   Then rotate the tree so that
#   the sibling is now the root
#   of the subtree to rebalance it

#   """
#   sibling = node.get_sibling()
#   if sibling.color: # if the sibling is red
#     node.parent.color = True # repaint the parent red
#     sibling.color = False # repaint the sibling black
#   if node == node.parent.left:
#     rotate_left(node.parent)
#   else:
#     rotate_right(node.parent)
#   delete_case3(node)


# def delete_case3(node):
#   """
#   If the newly replaced node, its parent,
#   the sibling and the sibling's children
#   are all black, this means that the deleted
#   node was also black

#   So in this calse, we recolor the sibling
#   red to correct the imbalance of black
#   heights, then since all paths going through
#   the parent now have 1 less black node,
#   we rebalance the tree at the parent node

#   """
#   sibling = node.get_sibling()
#   if node.color \
#     or sibling.color \
#     or sibling.left.color \
#     or sibling.right.color:
#       delete_case4(node)
#   else:
#     sibling.color = True
#     delete_case1(node.parent)


# def delete_case4(node):
#   """
#   If the node's parent is red,
#   and the sibling and its children
#   are black, repaint the sibling red
#   and the new node's parent black

#   """
#   sibling = node.get_sibling()
#   if node.parent.color \
#     and not sibling.color \
#     and not sibling.left.color \
#     and not sibling.right.color:
#       sibling.color = True
#       node.parent.color = False
#   return delete_case5(node)


# def delete_case5(node):
#   """
#   Review later

#   """
#   sibling = node.get_sibling()
#   if not sibling.color:
#     if node == node.parent.left \
#       and not sibling.right.color \
#       and sibling.left.color:
#         sibling.color = False
#         sibling.left.color = True
#         rotate_right(sibling)
#     elif node == node.parent.right \
#       and not sibling.left.color \
#       and sibling.right.color:
#         sibling.color = False
#         sibling.right.color = True
#         rotate_left(sibling)
#   delete_case6(node)


# def delete_case6(node):
#   """
#   Review later

#   """
#   sibling = node.get_sibling()
#   sibling.color = node.parent.color
#   node.parent.color = False
#   if node == node.parent.left:
#     sibling.right.color = False
#     rotate_left(node.parent)
#   else:
#     sibling.left.color = False
#     rotate_right(node.parent)


# def delete_node_with_one_child(node):
#   """
#   Delete a node with at most 1 child

#   """
#   child = node.left if node.right is None else node.right
#   if child is None: # leaf node case
#     delete_case1(node)
#   replace_node(node, child) # replace the node with its child
#   if not node.color: # if the node was red (True), we are done
#     # the child must be red or else the tree was imbalanced
#     child.color = False  # so repaint it black


# def red_black_delete(node, v):
#   """
#   Delete from a Red-Black tree

#   """
#   if v < node.value:
#     red_black_delete(node.left, v)
#   elif v > node.value:
#     red_black_delete(node.right, v)
#   else:
#     if node.left and node.right:
#       tmp = node.left
#       while tmp.right is not None:
#         tmp = tmp.right
#       node.value = tmp.value
#       delete_node_with_one_child(tmp)
#     else:
#       delete_node_with_one_child(node)
