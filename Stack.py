class Stack:
    class Node:
        def __init__(self, word, prev):
            self.word = word
            self.prev = prev

    def __init__(self):
        self.top = None
    
    def push(self, word):
        newNode = self.Node(word, self.top)
        self.top = newNode
    
    def pop(self):
        if self.top == None:
            return
        else:
            temp = self.top.word
            self.top = self.top.prev
            return temp

    def print(self):
        temp = self.top
        while temp != None:
            print(temp.word)
            temp = temp.prev

s = Stack()
s.push("java")
s.push("python")
s.push("spring")
s.print()
print()
print(s.pop())
print()
s.print()   
