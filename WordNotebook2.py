class WordNotebookSorted:
    def __init__(self):
        self.words=[];
    
    def add(self, word):
        self.addRecurssive(word, 0, len(self.words)-1)
    
    def addRecurssive(self, word, start, end):
        if start > end :
            self.words.insert(start, word)
        else:
            middle = int((start + end) / 2)
            if word < self.words[middle]:
                self.addRecurssive(word, start, middle - 1)
            else:
                self.addRecurssive(word, middle+1, end)
    
    def delete(self, word):
        self.deleteRecurssive(word, 0, len(self.words)-1)
    
    def deleteRecurssive(self, word, start, end):
        if start > end:
            print("입력한 단어가 해당 단어배열에 없어 삭제할 수 없습니다.")
            return
        else:
            middle = int((start+end) / 2)
            if self.match(self.words[middle], word):
                return self.words.pop(middle)
            elif word < self.words[middle]:
                self.deleteRecurssive(word, start, middle-1)
            else:
                self.deleteRecurssive(word, middle+1, end)

    def find(self, word):
        return self.findRecurssive(word, 0, len(self.words)-1)

    def findRecurssive(self, word, start, end):
        if start > end:
            print("찾고자 하는 단어가 없습니다.")
            return 
        else:
            middle = int((start+end) / 2)
            if self.match(self.words[middle], word):
                return self.words[middle]
            elif word < self.words[middle]:
                self.findRecurssive(word, start, middle-1)
            else:
                self.findRecurssive(word, middle+1, end)
                

    def match(self, long, short):
        for i in range(0, len(short)):
            if long[i] != short[i]:
             return False
        return True

    def printAll(self):
        for w in self.words:
            print(w)

note = WordNotebookSorted()

note.add("python : 파이썬")
note.add("java : 자바")
note.add("apple : 사과")
note.add("structure : 구조체")
note.add("data : 데이터")

note.printAll()
print()
note.delete("t")
print()
note.printAll()
print("")
print(note.find("c"))
