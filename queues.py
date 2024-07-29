# Question: Implement a circular queue using a fixed-size array in Python.

class CircularQueue:
    def __init__(self, capacity):
        self.capacity = capacity
        self.queue = [None] * capacity
        self.front = self.rear = -1
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def is_full(self):
        return self.size == self.capacity

    def enqueue(self, item):
        if self.is_full():
            return True
        
        if self.is_empty():
            self.front = self.rear = 0
        else:
            self.rear = (self.rear + 1) % self.capacity
        
        self.queue[self.rear] = item
        self.size += 1

    def dequeue(self):
        if self.is_empty():
            return False
        
        item = self.queue[self.front]
        if self.size == 1:
            self.front = self.rear = -1
        else:
            self.front = (self.front + 1) % self.capacity
        
        self.size -= 1
        return item

    def front_item(self):
        if self.is_empty():
            return False
        return self.queue[self.front]

    def __str__(self):
        if self.is_empty():
            return "Queue: []"
        items = []
        index = self.front
        for _ in range(self.size):
            items.append(str(self.queue[index]))
            index = (index + 1) % self.capacity
        return "Queue: [" + ", ".join(items) + "]"


cq = CircularQueue(5)


cq.enqueue(1)
cq.enqueue(2)
cq.enqueue(3)
print(cq)


print(cq.dequeue())


cq.enqueue(4)
cq.enqueue(5)
print(cq)  

print(cq.dequeue())

print(cq) 
