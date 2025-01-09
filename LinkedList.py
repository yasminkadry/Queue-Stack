# 1- implement a linked list for nodes (node: have employee number, name, position)
    # 1- Insert data 
    # 2- update data 
    # 3- delete by (id)
    # 4- update by (id)
    # 5- display all
    # 6- delete all

## node has employee no , name , position
class Node:
    def __init__(self,number,name,position):
        self.number = number
        self.name = name
        self.position = position
        self.next = None
        self.prev = None



class LinkedList:
    def __init__(self):
        self.Head = None
        self.Tail = None
    
    ## 1- insert data of an employee at the end of the list as a new employee:
    def insert(self,number,name,position):
        employee = Node(number,name,position)

         ##empty list
        if (self.Head == None):
            self.Head = employee
            self.Tail = employee
        
         ## not empty list
        else:
            self.Tail.next = employee
            employee.prev = self.Tail
            self.Tail = employee
        return 'New employee inserted successfully'


    ## 2- update date of a specific employee using its location
    def update(self,loc,number,name,position):
          if(loc < 0):
            raise ValueError("The location can't be negative")

          else:
            ## empty list
            if (self.Head == None):
                print("The List is empty, do you need to insert new employee")
                ans = input("select y/n: ")
                if (ans.lower() == 'y'):
                    employee = Node(number,name,position)
                    self.Head = employee
                    self.Tail = employee
                    return 'New employee inserted successfully'

                else:
                    return "Data doesn't inserted"

            ### not empty list
            else:
                i = 0
                curr = self.Head
                while (i < loc and curr != None):
                    curr = curr.next
                    i += 1

                ## update the last Node
                if (curr !=None):
                    curr.number = number
                    curr.name = name
                    curr.position = position
                    return 'Employee data updated successfully'
                else:
                    return "The location is out of the range"

    ## 3- delete data of a specific employee using its id
    def delete(self,number):

        ## first check if the list is empty
        if (self.Head == None):
            raise ValueError("The list is empty...")

            ## not empty list
        else:
            curr = self.Head

            while(curr != None):
                if (curr.number == number):
                    ##curr at the first Node
                    if (curr == self.Head):
                        self.Head = curr.next
                        curr.next.prev = None
                    
                        ##node at the end                    
                    elif (curr ==self.Tail):
                        self.Tail = curr.prev
                        curr.prev.next = None
                    
                    ## the node at the middle
                    else:
                        curr.prev.next = curr.next
                        curr.next.prev = curr.prev
                    
                    return 'Employee deleted successfully'

                    ## if the curr.number != number passed to the function.
                else:
                    curr = curr.next

            else:
                raise ValueError("Employee number not found")
            
    ## 4- update by (id) first occurrence 
    def update_id(self,number,name,position):

        ##check if the list is empty 
        if (self.Head == None):
            print('the list is empty, would you like to insert your data..?')
            ans = input("select y/n")
            if (ans.lower() == 'y'):
                employee = Node(number,name,position)
                self.Head = employee
                self.Tail = employee
                return 'New employee inserted successfully'

            else:
                return "Data doesn't inserted"
        
        ## not empty
        else:
            curr = self.Head

            while(curr != None):

                if (curr.number == number):
                    curr.name = name
                    curr.position = position

                ## if the curr.number != number passed to the function.
                else:
                    curr = curr.next

                return "The data updated successfully.."
            ## curr == none --> out of list nodes
            else:
                raise ValueError("Employee number not found")

    ## # 5- display all
    def display_all(self):

        ## check if the list is empty
        if (self.Head == None):
            print("The list is empty...")
        
        ## not empty
        else:
            curr = self.Head

            while (curr != None):
                print(f"Employee Data: {curr.number}: {curr.name}: {curr.position}.")
                curr = curr.next

    # 6- delete all
    def delete_all(self):
        
        ## check if the list is empty
        if (self.Head == None):
            raise ValueError("The list is empty...Nothing to delete")
        
        ## not empty
        else:
            curr = self.Head
            temp = None
            while (curr != None):
                temp = curr.next
                if (temp != None):
                    temp.prev = None
                curr = temp

            self.Head = None
            self.Tail = None
            return "All employees deleted successfully"





ll = LinkedList()
ll.insert(0,'ali','ce')
ll.insert(1,'mone','ce')
ll.insert(2,'mohamed','ce')
ll.insert(3,"a'lla",'ce')
ll.update(5,4,'ahmed','ce')
ll.update(3,4,'ahmed','ce')
ll.delete(2)
ll.update_id(0,'yasmin','co')
ll.display_all()
print(ll.delete_all())
ll.display_all()
# ll.delete_all()