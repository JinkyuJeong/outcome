class DList:
    class Node:
        def __init__(self,data,prev,next):
            self.data = data
            self.prev = prev
            self.next = next
    
    def __init__(self):
        self.head = None
        self.tail = None

    def add(self, word):
        newNode = self.Node(word,self.tail, None)
            
        if self.head == None:
            self.head = newNode
            self.tail = newNode
        else:
            self.tail.next = newNode
            self.tail = newNode

    def delete(self,word):
        if self.head == self.tail:
            if self.match(self.head.data, word):
                self.head = None
                self.tail = None
        elif self.match(self.head.data, word):
            self.head = self.head.next
            self.head.prev = None
        elif self.match(self.tail.data, word):
            self.tail = self.tail.prev
            self.tail.next = None
        else:
            temp = self.head
            while temp != None:
                if self.match(temp.data, word):
                    temp.next.prev = temp.prev
                    temp.prev.next = temp.next
                    break
                else:
                    temp = temp.next
        

    def match(self, long, short):
        for i in range(len(short)):
            if long[i] != short[i]:
                return False
        return True

    def printAll(self):
        temp=self.head
        while temp != None:
            print(temp.data)
            temp = temp.next

    def Rprint(self):
        temp = self.tail
        while temp != None:
            print(temp.data)
            temp = temp.prev

n = DList()

n.add("java : 자바")
n.add("python : 파이썬")
n.add("c : c언어")
n.printAll()
n.delete("python")
n.printAll()