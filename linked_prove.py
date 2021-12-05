class LinkedList:
    """ Constructing linked list object by creating the head and the tail 
    """
    class Node:
        """ A object within LinkedList to hold the value and the addresses of next and prev """
        def __init__(self, data):
            self.data = data
            self.next = None
            self.prev = None

    def __init__(self):
        self.head = None
        self.tail = None

    def insert_head(self, value):
        """ Insert a node at the head """
        # Create new node
        new = LinkedList.Node(value)

        # If the list is empty
        if self.head is None:
            self.head = new
            self.tail = new
        else:
            new.next = self.head
            self.head.prev = new
            self.head = new

    ###################
    # Start Problem 1 #
    ###################
    def insert_tail(self, value):
        """ Insert a node at the tail """

        pass