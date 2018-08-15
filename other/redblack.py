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
  """
  Rotate the tree at node.parent
  if node is the right child of a
  left child or the left child of a right child

  """
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

  node: newly inserted Node painted red

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


def rebalance_tree_after_delete(node):
  """
  Handles deleting a black node with only leaf
  children from a red-black tree

  The argument is the node that was deleted,
  its parents subtree needs rebalancing

  """
  if node.parent is None:
    # Root node case
    return
  parent = node.parent # label this P
  sibling = node.sibling() # label this S
  if sibling.color:
    # In the case that the S is red,
    # repaint S black and P red
    # then rotate the tree so that
    # S is where the P used to be
    sibling.color = False
    parent.color = True
    if sibling == parent.left:
      rotate_right(parent)
    else:
      rotate_left(parent)
    sibling = node.sibling() # relabel the node's new sibling as S
  if not parent.color \
    and (sibling.left is None or not sibling.left.color) \
    and (sibling.right is None or not sibling.right.color):
      # The case when the P, S (red case for S above), and S's children are black
      sibling.color = True
      rebalance_tree_after_delete(parent)
      # After this, both of the P's subtrees have
      # 1 less black node, and the tree needs to be rebalanced
      # at the parent node
  elif (sibling.left is None or not sibling.left.color) \
    and (sibling.right is None or not sibling.right.color):
      # The case when P is red, but S and its children are black (red case for S above)
      sibling.color = True
      parent.color = False
      return
  # TODO delete cases 5-6



def replace_node(node, child):
  """
  Replace a node with one of its children

  """
  child.parent = node.parent
  if node.parent is None:
    return
  elif node == node.parent.left:
    node.parent.left = child
  else:
    node.parent.right = child


def delete_node_with_at_most_one_child(node):
  """
  Delete a node with at most 1 child

  """
  if node.color:
    # Case when the node being deleted is red
    # This can only happen if the node has two leaf children (None),
    # otherwise the tree would be imbalanced
    if node == node.parent.left:
      node.parent.left = None
    else:
      node.parent.right = None
    return
  child = node.left if node.right is None else node.right
  if child is None:
    # If the child does not exist and the node is black (see above for red node case)
    # then it must only have leaf children and must be dealt with separately
    # the sibling cannot be a leaf since the
    # subtree of the parent with node has a black
    # height of two, so if the sibling is a leaf
    # the parent would be imbalanced
    rebalance_tree_after_delete(node)
    if node.parent:
      if node == node.parent.left:
        node.parent.left = None
      else:
        node.parent.right = None
    return
  # If the child exists, it must be red with only leaf children
  # or else the tree would be imbalanced. In this case just
  # replace the node with its child and repaint the child black
  replace_node(node, child)
  child.color = False


def red_black_delete(node, v):
  """
  Delete a value from a Red-Black tree

  """
  if v < node.value:
    red_black_delete(node.left, v)
  elif v > node.value:
    red_black_delete(node.right, v)
  else:
    if node.left and node.right:
      tmp = node.left
      while tmp.right is not None:
        tmp = tmp.right
      node.value = tmp.value
      delete_node_with_at_most_one_child(tmp)
    else:
      delete_node_with_at_most_one_child(node)
