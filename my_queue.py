from array_deque import ArrayDeque
from my_linked_list import LinkedList

class Queue:
    def __init__(self):
        self.container = LinkedList()
     
    def add(self, data):
      self.container.push_back(data)  

    def remove(self):
     return self.container.pop_front()

    def get_size(self):
        return self.container.get_size()

    def __str__(self):
        return str(self.container)
