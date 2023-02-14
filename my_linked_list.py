class Node:
    def __init__(self, data = None, next = None):
       
        self.data = data
        self.next = next

    def __str__(self):
        return str(self.data)


class LinkedList():
    def __init__(self):
       
        self.head = None
        self.size = 0

    def __str__(self):
        temp = self.head
        out = ""
        while temp:
            out += str(temp.data) + " "
            temp = temp.next
        return out

#Takes a parameter and adds its value to the front of the list   
    def push_front(self, data):

        if self.head is None:
            self.head = Node(data)
        else:
            temp = self.head
            self.head = Node(data)
            self.head.next = temp
        self.size += 1


#Removes the item from the front of the list and ​returns ​its value 
#If the list is empty, return None    
    def pop_front(self):
       
        if self.head is None:
            return None
        else:
            temp = self.head
            self.head = self.head.next
            self.size -= 1
            return temp.data
        
#Takes a parameter and adds its value to the back of the list    
    def push_back(self, data):
       
        if self.head is None:
            self.head = Node(data)
        else:
            temp = self.head
            while temp.next is not None:
                temp = temp.next
            temp.next = Node(data)
        self.size += 1
  
  
#Removes the item from the back of the list and ​returns​ its value 
#If the list is empty, return None 
    def pop_back(self):
       
        if self.head is None:
            return None
        elif self.head.next is None:
            temp = self.head
            self.head = None
            self.size -= 1
            return temp.data
        else:
            temp = self.head
            while temp.next.next is not None:
                temp = temp.next
            temp.next = None
            self.size -= 1
            return temp.data
        
#Returns the number of items currently in the list 
    def get_size(self):
         
        return self.size

    

