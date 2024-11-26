class Stack:
    def __init__(self):
        self.stack = []

    def is_empty(self):
        return len(self.stack) == 0

    def push(self, item):
        self.stack.append(item)
        print(f"Pushed {item} to the stack")

    def pop(self):
        if self.is_empty():
            return "Stack is empty"
        return self.stack.pop()

    def peek(self):
        if self.is_empty():
            return "Stack is empty"
        return self.stack[-1]

    def size(self):
        return len(self.stack)

    def display(self):
        print("Stack:", self.stack)

if __name__ == "__main__":
    s = Stack()
    s.push(10)
    s.push(20)
    s.push(30)
    s.display()
    print("Top item:", s.peek())
    print("Popped item:", s.pop())
    s.display()
    print("Stack size:", s.size())
    s.pop()
    s.pop()
    print("Popped item:", s.pop())
