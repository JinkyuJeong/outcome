class WordNotebook():
    def __init__(self):
        self.notebook=[]

    def add(self,word):
        self.notebook.append(word)

    def delete(self,word):
        index=0
        for w in self.notebook:
            if self.match(w,word):
                self.notebook=self.notebook[0:index]+self.notebook[index+1:]
                break
            index+=1

    def find(self,word):
        for w in self.notebook:
            if self.match(w,word):
                return w
        return "없어요"

    def match(self,longs,short):
        for i in range(0,len(short)):
            if longs[i] != short[i]:
                return False
        return True     

    def printAll(self):
        for w in self.notebook:
            print(w)

note = WordNotebook()

note.add("python : 파이썬")
note.add("java : 자바")
note.add("structure : 구조체")
note.add("data : 데이터")
print(note.find("java"))

note.printAll()
note.delete("python")
print("")
note.printAll()
print("")
print(note.find("java"))