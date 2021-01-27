# We can solve dynamic array memory allocation problem using Deque
# "self.container": it is a object of deque class
# using deque for stack functionality we will use append() and pop()
from collections import deque


class Stack:
    def __init__(self):
        self.container = deque()

    def push(self, val):
        self.container.append(val)

    def pop(self):
        return self.container.pop()

    def peek(self):
        return self.container[-1]

    def is_empty(self):
        return len(self.container) == 0

    def size(self):
        return len(self.container)


if __name__ == '__main__':
    s = Stack()
    s.push('Kagan')
    s.push('chanson')
    s.push('Ammo')
    print(s.container)
    s.pop()
    print(s.container)
    print(s.peek())
