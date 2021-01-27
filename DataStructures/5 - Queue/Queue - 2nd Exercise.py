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

    def front(self):
        return self.buffer[-1]


def produce_binary_numbers(n):
    binary_numbers_queue = Queue()
    binary_numbers_queue.enqueue('1')

    for i in range(n):
        # every time we are removing first added value[11, 10, 1], we will remove 0 so i will take 10 for next loop
        front = binary_numbers_queue.front()
        print("   ", front)
        binary_numbers_queue.enqueue(front + "0")
        binary_numbers_queue.enqueue(front + "1")

        binary_numbers_queue.dequeue()


if __name__ == '__main__':
    produce_binary_numbers(10)


