class Node:
    def __init__(self, data) -> None:
        self.data = data 
        self.memory = None
        
class Stack:
    def __init__(self) -> None:
        self.head = None
        self._size = 0
    
    def push(self, data) -> None:
        node = Node(data)     
        node.memory = self.head
        self.head = node
        self._size += 1
        
    def pop(self):
        if not self.head:
            raise Exception ("Stack is empty")
        
        top = self.head
        self.head = self.head.memory
        self._size -= 1
        return top.data
    
    def peek(self):
        if not self.head:
            raise Exception ("Stack is empty")
        
        return self.head.data
    
    def size(self):
        return self._size
    
    def display(self) -> None:
        if not self.head:
            print("Stack is empty") 
            return
        
        curr = self.head
        while curr:
            print(curr.data, end="-> ")
            curr = curr.memory    
        print("None")
        
    def is_empty(self):
        return self.head is None
            
if __name__ == "__main__":
    
    ss = Stack()
    ss.push(1)
    ss.push(2)
    ss.push(3)
    ss.push(4)
    ss.push(5)
    ss.push(9)
    print(ss.size())
    print(ss.peek())
    print(ss.pop())
    print(ss.size())
    ss.display()