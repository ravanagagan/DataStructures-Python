# We are using deque to implement queue
# This will solve memory allocation problem
# "self.buffer": it is a object of deque class
# using deque for queue functionality we will use appendleft() and pop()
from collections import deque


class Queue:
    def __init__(self):
        self.buffer = deque()

    def enqueue(self, val):  # enqueue: means insert
        self.buffer.appendleft(val)

    def dequeue(self):  # deque: means delete
        return self.buffer.pop()

    def is_empty(self):
        return len(self.buffer) == 0

    def size(self):
        return len(self.buffer)


if __name__ == '__main__':
    q = Queue()
    q.enqueue(10)
    q.enqueue(20)
    print(q.buffer)

    print(q.dequeue())
    q.enqueue(30)
    q.enqueue(40)
    print(q.buffer)
    print(q.size())
    print(q.is_empty())

    q.dequeue()
    q.dequeue()
    q.dequeue()
    print('After popping all the items from deque :', q.is_empty())

