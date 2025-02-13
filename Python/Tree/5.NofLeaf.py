class Node:
    """
    Class which represent a tree as a node, it use more or less the same notation as we used in prolog,
    the only difference is that here we omit the nil value when there is an empty node.
    """

    def __init__(self, value, left=None, right=None):
        """
        Constructor for a node, the sub-trees can be omitted if there is no value for these.
        :param value: The node payload.
        :param left: the left sub-tree (defined as another Node)
        :param right: the right sub-tree (defined as another Node)
        """
        self.left = left
        self.right = right
        self.value = value



def number_leaves(tree: Node):
    if not tree:
        return 0
    if tree.value and not tree.right and not tree.left:
        return 1
    return number_leaves(tree.left) + number_leaves(tree.right)

if __name__ == "__main__":
    print(number_leaves(Node(1,Node(1),Node(1,Node(1,Node(1),Node(1))))))