class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        self.first = None
        self.last = None
        self._size = 0

    def enqueue(self, data):
        node = Node(data)

        if not self.last:
            self.first = self.last = node
            self._size += 1
            return

        self.last.next = node
        self.last = node
        self._size += 1

    def dequeue(self):
        if not self.first:
            return None

        temp = self.first
        self.first = self.first.next
        self._size -= 1

        if not self.first:
            self.last = None

        return temp.data

    def peek(self):
        if not self.first:
            return None
        return self.first.data

    def is_empty(self):
        return self.first is None

    def display(self):
        if not self.first:
            print("Queue is empty.")
            return

        curr = self.first
        while curr:
            print(curr.data, end=" -> ")
            curr = curr.next
        print("None")

    
if __name__ == "__main__":
    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    q.enqueue(4)
    q.enqueue(5)
    q.enqueue(6)
    q.display()
    q.dequeue()
    q.dequeue()
    q.dequeue()
    q.dequeue()
    q.dequeue()
    q.dequeue()
    q.display()