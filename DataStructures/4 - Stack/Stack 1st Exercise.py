# Write a function in python that can reverse a string using stack data structure. Use 4 - Stack class from the tutorial.
# reverse_string("We will conquer COVID-19") should return "91-DIVOC ereuqnoc lliw eW"
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
    data = "We will conquer COVID-19"
    for i in data:
        s.push(i)
    print("Original String: " + data)
    print("String after reversal: ", end='')
    for i in range(s.size()):
        print(s.pop(), end='')
