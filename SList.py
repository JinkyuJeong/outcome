class SingleLinkedList:
    class Node:                                 # 노드생성 (데이터와 next값을 가리키는 링크)
        def __init__(self, data, next):
            self.data = data
            self.next = next

    def __init__(self):
        self.head = None        # 헤드생성

    ## 오름차순 정렬 메서드
    def add(self, word):
        newNode = self.Node(word, None)  

        if self.head == None:               # 값이 하나도 존재하지 않는 경우
            self.head = newNode
        elif word < self.head.data:         # 값이 헤드보다 작아서 맨 앞에 들어가 새로운 헤드가 되는 경우
            newNode.next = self.head
            self.head = newNode
        else:
            temp = self.head
            before = temp
            while word > temp.data:         # 새로운값이 temp값보다 작을 때 까지 반복
                if temp.next == None:       # temp.next가 None이 됐을 경우는 가장 큰 값이 들어오는 경우이므로
                    temp.next = newNode     # 새로운 값을 맨 뒤에 넣고 리턴하여 함수종료
                    return
                else:                       # before(이전)와 temp(현재)에 값을 넣어     
                    before = temp           # 새로운값이 temp값보다 작으면 while문 탈출
                    temp = temp.next    

            newNode.next = temp             # before(이전)와 temp(현재) 사이에 값을 넣음
            before.next = newNode        

    ## 순서 상관없이 무조건 맨 앞에 값을 넣는 메서드   
    def firstInsert(self, word):
        if self.head == None:
            newNode = self.Node(word, None)
            self.head = newNode
        else:
            newNode = self.Node(word, self.head)
            self.head = newNode

    ## 삭제 메서드    
    def delete(self, word):
        if self.head == None:
            return                             # 지울려는 값이 아예 없는경우
        elif self.match(self.head.data, word):
            self.head = self.head.next         # 지울려는 값이 헤드일 경우 헤드 다음값을 헤드로 지정                     
        else:
            temp = self.head
            before = temp
            while temp != None:
                if self.match(temp.data, word):
                   before.next = temp.next     # 지울려는 데이터의 다음 값을 가리키게함
                   break                     
                else:
                    before = temp
                    temp = temp.next           # 이전값에 템프를 저장하고 템프는 다음값을 지정

    ## 찾기 메서드
    def find(self, word):
        temp = self.head
        while temp != None:
            if self.match(temp.data, word):
                return temp.data
            else:
                temp = temp.next
        return "없어요"

    ## 해당 노드의 위치값을 반환하는 메서드
    def serch(self, word):      
        temp = self.head
        count = 0
        while temp != None:
            if self.match(temp.data, word):
                return count
            else:
                temp = temp.next
                count+=1
        return "없어요"

    ## 값 일치 여부 메서드
    def match(self, long, short):
        for i in range(len(short)):
            if long[i] != short[i]:
                return False
        return True

    ## SList 출력
    def printAll(self):
        temp=self.head
        while temp != None:
            print(temp.data)
            temp = temp.next

    ## SList 반대로 출력
    def Rprint(self):
        self.RprintRecurssive(self.head)

    def RprintRecurssive(self,temp : Node):
        if temp == None :
            return
        else:
            self.RprintRecurssive(temp.next)
            print(temp.data)

## 두 개의 SList를 오름차순으로 합병정렬
## 두 리스트의 헤드를 매개변수로 받음
def mergy(l1 : SingleLinkedList.Node, l2 : SingleLinkedList.Node):  
    ret = SingleLinkedList.Node(None, None)     # 합병을 위한 새로운 노드 생성
    
    # 두 리스트값 중 한 쪽 값이 비워져 있으면 반대쪽 리스트가 리턴됨
    if l1 == None:
        return l2
    if l2 == None:
        return l1
    
    # 두 리스트값을 비교해서 오름차순으로 차곡차곡 넣는작업 (Recurssive 활용)
    if l1.data < l2.data:
        ret = l1
        ret.next = mergy(l1.next, l2)
    else:
        ret = l2
        ret.next = mergy(l1, l2.next)
    
    return ret              

    
note = SingleLinkedList()
note.add("java : 자바")
note.add("apple : 사과")
note.add("single : 싱글")
note.add("blue : 파랑")

note2 = SingleLinkedList()
note2.add("java1 : 자바")
note2.add("apple1 : 사과")
note2.add("single1: 싱글")
note2.add("blue1 : 파랑")

note3 = SingleLinkedList()
note3.head = mergy(note.head, note2.head)
note3.printAll()
