class Stack():
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def is_empty(self):
        return self.items == []

    def peek(self):
        if not self.is_empty():
            return self.items[-1]

    def get_stack(self):
        return self.items

s = Stack()
print(s.is_empty())
s.push("1")
s.push("6")
s.push("3")
s.push("8")
print(s.get_stack())
s.pop()
print(s.get_stack())
s.push("60")
print(s.get_stack())

#-------------------------------------------
#How does __Init__ work?









