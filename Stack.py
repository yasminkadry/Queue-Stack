# 2- save a stack of nodes (1 side linked list ? push, pop for nodes ) 
# if the node is empty raise a message that the stack is empty

## node class 
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None


## stack class single forward LinkedList
class Stack:
    def __init__(self):
        self.tos = 0
        self.Head = None

    
    ##push function
    def push(self,data):
        ## creating the node
        nd = Node(data)
        
        ## empty stack
        if (self.Head == None):
            self.Head = nd
            self.tos += 1
        ## not empty Stack
        else:
            self.Head.next = nd
            nd.prev = self.Head
            self.Head = nd
            self.tos += 1
        return 'pushed successfully'
    
    ## pop function delete the last node (pop one node at once)
    def pop(self):
        ## empty stack
        if (self.Head == None):
            raise ValueError('The stack is empty, Nothing to be popped')

        ## not empty stack
        else:
            temp = self.Head
            self.Head = temp.prev
            temp.prev = None
            self.tos -= 1
            return temp.data

    ## display all nodes 
    def display(self):
         ## empty stack
        if (self.Head == None):
            raise ValueError('The stack is empty, Nothing to display')

        ## not empty stack
        else:
            temp = self.Head
            print("Data at the stack from the last one to the first one..")
            while(temp !=None):
                print(f"Data of Node: {temp.data}.")
                temp = temp.prev




s = Stack()
s.push(5)
s.push(1)
print(s.push(2))
s.display()
print(s.pop())
print(s.pop())
print(s.pop())
# print(s.pop())
