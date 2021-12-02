class Queue:
    
    def __init__(self):
        """ The contructs an empty queue """
        self.queue = []

    def enqueue(self, value):
        """ This function add something to the queue """
        pass

    def dequeue(self):
        """ This function removes the next item """
        pass


# Tests
queue = Queue()

# Adding to the queue
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
queue.enqueue(4)
queue.enqueue(0)
queue.enqueue(9)

print(queue) # [1,2,3,4,0,9]

# Dequeueing
queue.dequeue()
queue.dequeue()
queue.dequeue()
queue.dequeue()
queue.enqueue(45)

print(queue) # [0,9,45]