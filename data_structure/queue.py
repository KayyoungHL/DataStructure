class Queue :
    def __init__ (self, msg = True) :
        self.__items = []
        self.__first_index = 0
        self.__msg = msg
    
    def __repr__ (self):
        return self.__items[self.__first_index:]

    def __str__ (self) :
        return "Queue("+str(self.__items[self.__first_index:])+")"

    def __getitem__ (self, idx):
        if idx < 0 : return self.__items[idx] ## -1 인덱싱 할 때!
        else       : return self.__items[self.__first_index+idx]

    def __len__ (self) :
        return len(self.__items) - self.__first_index

    @property
    def items (self) : ## 아이템을 정리해준다. self.__first_index를 다시 0으로 시작할 수 있도록
        if not self.__first_index == 0 :
            self.__items = self.__items[self.__first_index:]
            self.__first_index = 0
        return self.__items

    def enqueue (self, val) :
        self.__items.append(val)
        
    def dequeue (self) :
        if len(self.__items) == self.__first_index : 
            if self.__msg : print("Queue is empty")
            return False
        self.__first_index += 1
        return self.__items[self.__first_index-1]

def __main () :
    x = Queue()
    print(x.dequeue())
    x.enqueue(1)
    x.enqueue(3)
    x.enqueue(7)
    x.enqueue(1)
    x.enqueue(-4)
    print(x.dequeue())
    print(x.dequeue())
    print(x)
    print(x[1])
    print(type(x))
    print(x[-1])
    print(x.items)
    print(len(x))
    y = [2,3]
    print(list(x)+y)
    print(str(x))
    print(x[0]+1)
    print(x[0:2])

if __name__=="__main__" :
    __main()



