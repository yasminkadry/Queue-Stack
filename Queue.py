# 3- implement queue of nodes --> enqueue, dequeue the nodes in the queue 
# the queue has size --> nodes are employees(number, name, position)

class Node:
    def __init__(self,number,name,position):
        self.number = number
        self.name = name
        self.position = position



## Queue FIFO --> first in first out 

class Queue:
    ## constructor of the queue with a defualt size = 10 nodes
    def __init__(self,size=10):
        self.size = size
        self.Ar =[None]*self.size
        self.tos = 0

    ##enqueue --> add node at the end 
    def enqueue(self,number,name,position):
        employee = Node(number,name,position)
        enqueue = False
        ##check the queue is full
        if (self.tos == self.size):
            raise IndexError("the queue is full you can't add a new employee...")

        ## queue not full
        else:
            self.Ar[self.tos] = employee
            self.tos += 1
            enqueue = True

        return enqueue

    ## dequeue -->pop the node from the first
    def dequeue(self):
        dequeued = False
        ## check if the queue is empty
        if (self.tos ==0):
            raise ValueError("The queue is empty, nothing to be dequeued")
        
        ##queue not empty 
        else:
            dequeued = self.Ar.pop(0)
            self.tos -= 1
        return (f"({dequeued.number}, {dequeued.name}, {dequeued.position})")

    ## display all nodes in the queue
    def display(self):

        for i in range(self.tos):
            temp = self.Ar[i]
            print(f"Employee data: {temp.number}: {temp.name}: {temp.position}.")




q = Queue()
q.enqueue(1,'mohamed','ce')
q.enqueue(2,'yasmin','ce')
q.enqueue(3,'ahmed','ce')
q.enqueue(3,'ahmed','ce')
q.enqueue(3,'ahmed','ce')
q.enqueue(3,'ahmed','ce')
q.enqueue(1,'mona','ce')
q.enqueue(1,'mona','ce')
q.enqueue(1,'mona','ce')

q.enqueue(1,'mona','ce')
q.enqueue(1,'mona','ce')
q.enqueue(1,'ali','ce')
print(q.dequeue())

q.display()
            