""" 
We will be taking names and keeping order of people who come into the DMV.
They are able to take their own seat number but it is our job to take whoever is next in line.
To do so we will need a linked list
"""

class LinkedList:
    """ Constructing linked list object by creating the head and the tail """
    class Node:
        """ A object within LinkedList to hold the value and the addresses of next and prev """
        def __init__(self, data):
            self.data = data
            self.next = None
            self.prev = None

    def __init__(self):
        self.head = None
        self.tail = None

    def insert_front(self, value):
        """
        If someone has a very urgent appointment at the DMV they can be in the front.
        """
        # Create the new node
        new_person = LinkedList.Node(value)  
        
        if self.head is None:
            self.head = new_person
            self.tail = new_person
        else:
            new_person.next = self.head # Connect new node to the previous head
            self.head.prev = new_person # Connect the previous head to the new node
            self.head = new_person      # Update the head to point to the new node

    ###################
    # Start Problem 1 #
    ###################
    def insert_tail(self, value):
        """
        Insert a new node at the back (i.e. the tail) of the 
        linked list.
        """
        # Create new node
        new_node = LinkedList.Node(value)
    
    #################
    # End Problem 1 #
    #################

    def __iter__(self):
        """
        Iterate foward through the Linked List
        """
        curr = self.head  # Start at the begining since this is a forward iteration.
        while curr is not None:
            yield curr.data  # Provide (yield) each item to the user
            curr = curr.next # Go forward in the linked list

    def __str__(self):
        """
        Return a string representation of the linked list.
        """
        output = "linkedlist["
        first = True
        for value in self:
            if first:
                first = False
            else:
                output += ", "
            output += str(value)
        output += "]"
        return output
