class Node:
    def __init__(self, value:None) -> None:
        self.value = value
        self.next = None    

class LinkedList:
    def __init__(self):
        self.head = None
        self.__len = 0
    
    def length(self):
        return self.__len
        
    def insert_end(self, value) -> None:
        new_node = Node(value)
        
        if not self.head:
           self.head = new_node
           self.__len += 1 
           return
        
        temp = self.head
        while temp:
            prev = temp
            temp = temp.next
        prev.next = new_node
        self.__len += 1
        
    def display(self) -> None:
        if not self.head:
            print("Linked-List is empty.")
            return
     
        temp = self.head
        while temp:
            print(temp.value, end="-> ")
            temp = temp.next
        print("None")

    
    def pop(self):
        if not self.head:
            print("Linked List is empty")
            return

        if self.head.next is None:
            self.head = None
            self.__len -= 1
            return
        
        temp = self.head
        prev = None
        
        while temp.next:
            prev = temp
            temp = temp.next
        prev.next = None
        self.__len -= 1
        
        
        
if __name__ == "__main__":
    LL = LinkedList()
    LL.insert_end(5)
    LL.insert_end(10)
    LL.insert_end(15)
    LL.insert_end(20)
    LL.insert_end(25)
    LL.insert_end(30)
    
    LL.display()
    
    LL.pop()
    LL.pop()
    LL.pop()
    LL.pop()
    LL.pop()
    LL.pop()
    LL.pop()
   
    LL.display()
    print(LL.length())
