""" Scroll down for instructions """

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

    def insert_tail(self, value):
        """
        Someone who just comes in next and becomes the last person
        """
        # Create new node
        new_node = LinkedList.Node(value)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

    ###################
    # Start Problem 1 #
    ###################
    def insert_after(self, value, new_value):
        """
        This function inserts someone after another person
        """
        pass
    ###################
    # End Problem 1 #
    ###################


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
        output = "dmv_line["
        first = True
        for value in self:
            if first:
                first = False
            else:
                output += ", "
            output += str(value)
        output += "]"
        return output


""" 
We will be taking names and keeping order of people who come into the DMV.
They are able to take their own seat number but it is our job to take whoever is next in line.
To do so we will need a linked list
"""
dmv_line = LinkedList()

""" 
The DMV just opened at 9 A.M. There is already a line out the door. 
The first person becomes the head of the linked list and they choose seat 109.
More people fill the seats
"""
dmv_line.insert_front(109)
dmv_line.insert_tail(204)
dmv_line.insert_tail(246)
dmv_line.insert_tail(145)
dmv_line.insert_tail(50)
dmv_line.insert_tail(68)
dmv_line.insert_tail(223)
print(dmv_line)

"""
Now someone has an important task they need done before everyone else.
They need to be placed after the third person in line. (After seat #246)
Complete the insert_after function to insert them in the right place.
Their seat number is 37.
"""
dmv_line.insert_after(37, 246)
print(dmv_line) #dmv_line[109, 204, 246, 37, 145, 50, 68, 223]