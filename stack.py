from typing import Deque


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
        return len(self.container)==0
    
    def size(self):
        return len(self.container)

def reverse_string(s):
    stack = Stack()

    for i in s:
        stack.push(i)

    reverse_str = ''

    while stack.size() != 0:
        reverse_str += stack.pop()

    return reverse_str


    if __name__ == '__main__':
        print(reverse_string("We will conquere COVI-19"))
        print(reverse_string("I am the king"))
            