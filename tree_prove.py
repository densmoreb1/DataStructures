class Tree:
    """ Constructing a tree by makeing the node and the root
    """
    class Node:
        """ A object within LinkedList to hold the value and the addresses of next and prev """
        def __init__(self, data):
            self.data = data
            self.left = None
            self.right = None

    def __init__(self):
       self.root = None

    def insert(self, data):
        """ 
        This function inserts a new node and starts at the root.
        """
        if self.root is None:
            self.root = Tree.Node(data)
        else:
            self._insert(data, self.root)  # Start at the root

    ###################
    # Start Problem 1 #
    ###################
    def _insert(self, data, node):
        """
        This function inserts a new node
        """
        # Step 1 compare if the data is greater than or less than
        # Step 2 compare if the node is None then set the node equal to the data
        # Step 3 if the node is not none then recurisvly call the function including the left or right node
        pass
    #################
    # End Problem 1 #
    #################



""" 
For our problem, we will be inserting the names of the apostles. 
The < and > signs work with strings and compare the length of them.
"""
tree = Tree()
tree.insert('Mark')
tree.insert('Matthew')
tree.insert('John')
tree.insert('Peter')
tree.insert('James')
tree.insert('Paul')

for x in tree:
    print(x)  