# Queues
* Big O Notation
* How queues work?
* Example code
* Sample problems

## Big O Notation
Before we go over queues, we need to understand the Big O

The big o referes to how long a function takes to complete on the amount of data given. Or the performance of an algorithim. It is represented as "O(n)" n being the units of time.

Each algorithim can be graphed to represent how long it would take.

### O(1)
When the performace is instant it is O(1). The performace does not change even if the data is extremely large.
![](images/1.png)

### O(n)
'for' loops are always O(n) 'n' being the size of the data.
![](images/n.png)

### O(n)^2
So a loop inside of a loop would be O(n) inside of O(n) which would be O(n)^2
![](images/n^2.png)

<br/>

## How do queues work?
Queues are like picking a ticket at the DMV and waiting your turn to be next in line.
![](images/90.jpeg)

When something is added to a queue, it is added to the end of the line waiting it's turn just to be reminded that they forgot some documents they needed to take the driver's ed test. 

It can also be thought as "First In First Out".

<br/>  

## Using code to represent a queue
`x = []`

In python, this is how you represent a list. We will treat this list as a queue. 

### Enqueue
When inserting into a queue, the value always goes at the end of the list. 

`x.append(value)`

Appending will always go to the end of the list.

What is the performance?

O(1) because the end is always known

### Dequeue
When deleting from a queue, the first value is always the first on the go.

`value = x[0]`

`del x[0]`

or

`value = x.pop(0)`

"value" needs to be saved into a variable in order to be returned if needed.

What is the performace?

O(n) because when the first item is dequeued, the rest of the list needs to be shifted foward.
<br/>

## Sample problems
[Problems](queue_prove.py)