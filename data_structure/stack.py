class Stack : # 파이썬에서 스택은 리스트를 그대로 쓴다. 사실상 리스트의 기능을 제한한 것!
    # 내장 함수
    def __init__ (self, msg = True) :
        self.__items = []
        self.__msg = msg

    def __repr__ (self):
        return self.__items

    def __str__ (self) :
        return "Stack("+str(self.__items)+")"

    def __getitem__ (self, idx):
        return self.__items[idx]

    def __len__ (self) : ## self 의 길이를 리턴한다. len(Stack)을 하면 자동으로 self.__len__()을 실행한다.
        return len(self.__items)

    @property    # 내부 어트리뷰트 접근
    def items (self) : # 읽기 전용
        return self.__items

    def push (self, val) :
        self.__items.append(val)
    
    def pop (self) :
        try :
            return self.__items.pop()
        except :
            if self.__msg : print("Stack is empty")
            return False
        
    def top (self) :
        try :
            return self.__items[-1]
        except :
            if self.__msg : print("Stack is empty")
            return False

def __main () :
    x = Stack()
    x.push(1)
    x.push(3)
    x.push(7)
    x.push(1)
    x.push(-4)
    print(x.pop())
    print(x.pop())
    print(x)
    print(len(x))
    print(x.top())
    y = [2,3]
    print(list(x)+y)
    print(str(x))
    print(x[0]+1)

if __name__=="__main__" :
    __main()



