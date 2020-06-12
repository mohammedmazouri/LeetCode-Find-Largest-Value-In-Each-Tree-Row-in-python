class Node:
  def __init__(self,data):
    self.data=data
    self.left=None
    self.right=None
class tree:
  def __init__(self,RT):
    self.root=Node(RT)
    self.size=1

  def largestValues(self):
      """
      :type root: TreeNode
      :rtype: List[int]
      """
      result = []
      curr = [self.root]
      while any(curr):
          result.append(max(node.data for node in curr))
          curr = [child for node in curr for child in (node.left, node.right) if child]
      return result

def main():  # main method
   a=tree(1)
   a.root.right=Node(2)               #          1         level 0
   a.root.right.right = Node(9)       #       /    \
   a.root.left = Node(3)              #     3        2     level 1
   a.root.left.left = Node(5)         #   /   \       \
   a.root.left.right = Node(3)        #  5     3        9  level 2
   a.root.left.right.right= Node(7)   #          \
                                     #            7         level 3

   print(a.largestValues())             ## [1,3,9,7]
if __name__ == '__main__': main()  # call main method