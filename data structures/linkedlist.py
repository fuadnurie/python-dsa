class Node:
    def __init__(self,value):
        self.value = value
        self.next = next 


    def __str__(self):
        return self.value


class LinkedList:
    def __init__(self):
        self.head = None 
    
    def insert(self,data):
        if self.head is not None:
            self.head = Node(data)
        else:
            node = self.head 
            while  node is not None:
                node = node.next 
            node = Node(data)

    def showLinedList(self):
        node = self.head 
        while node is not None:
            print(node.value)
            node = node.next 


a = LinkedList()

for i in range(5):
    a.insert(i)

a.showLinedList()
print(a.head.value)