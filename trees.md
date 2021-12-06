# Trees
* Recursion
* How trees work?
* Example code
* Sample problems

## Recursion
![](images/giphy.gif)

Recusion is like living the same day over and over.

![](images/ground_hod.jpg)

Much like the movie, Groundhog Day, the same function is being called over and over in an infinite loop until something happens.

    def say_hello():  
        print("Hello")
        say_hello()  # This is the recursive call

This code will continue to say hello forever.

It is important when using recursion to have a 'base case'. A base case is when you finally become a good person you are released from the infinite loop. 

In code, a base case is when you set a condition for the function to hit. For example, adding a count.

    def say_hello(count):
	    if count <= 0:  # Base Case
		    return
        else:
            print("Hello")
            say_hello(count-1)  # Smaller Problem

Now the function takes in a number and says 'hello' until the count is reached.
