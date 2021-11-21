import re

class NodeS :
    def __init__ (self, key = None):
        self.__key = key
        self.__next = None
    
    def __str__ (self) : return str(self.__key)
    
    def __repr__ (self) : return self.__key

    @property ## property! 데코레이터와 함께 개념을 정확히 공부하자.
    def key (self) : return self.__key
    
    @key.setter # 링크드 리스트에서 데이터를 바꾸는 기능을 넣는게 맞을까? 모르겠다.
    def key (self, key) : self.__key = key

    @property 
    def next (self) : return self.__next

    @next.setter
    def next (self, nn) :
        if (type(nn) == NodeS) or (nn is None) :
            self.__next = nn
        else : 
            # regex = "\'.*\'|\s-\s.*"
            raise TypeError("can only point 'NodeS' type (not "+re.findall("\'.*\'|\s-\s.*",str(type(nn)))[0]+") as next Node")


class SinglyLinkedList :
    def __init__ (self) :
        self.__head = None
        self.__tail = None
        self.__size = 0

    def __repr__ (self):
        try : return {"Head":self.__head.key, "Tail":self.__tail.key, "Length":self.__size}
        except : return {"Head":self.__head, "Tail":self.__tail, "Length":self.__size}

    def __str__ (self) :
        try : return "SinglyLinkedList("+str({"Head":self.__head.key, "Tail":self.__tail.key, "Length":self.__size})+")"
        except : return "SinglyLinkedList("+str({"Head":self.__head, "Tail":self.__tail, "Length":self.__size})+")"

    def __len__ (self) :
        return self.__size
    
    def __getitem__ (self, idx) :
        if idx >= self.__size  : 
            if self.__size == 0 : raise IndexError("List is empty")
            raise IndexError("Out of inedx('"+str(idx)+"' is not in 0 ~ "+str(self.__size-1)+")")
        elif idx < 0 : idx = self.__size + idx
        temp_Node = self.__head
        while idx > 0 :
            temp_Node = temp_Node.next
            idx -= 1
        return temp_Node
        
    # generator -> for loop을 돌리기 위한 작업
    def __iter__ (self) : # O(n)
        temp_Node = self.__head
        while temp_Node != None :
            yield temp_Node # yield는 return인가? 이해해 보자.
            temp_Node = temp_Node.next
        return StopIteration

    def pushfront (self, key) : # O(1)
        new_Node = NodeS(key)
        new_Node.next = self.__head # 현재 노드의 다음 노드 __head를 None으로
        self.__head = new_Node # __head를 현재 노드로
        if self.__size == 0 : self.__tail = new_Node
        self.__size += 1

    def pushback (self, key) : # O(1)
        new_Node = NodeS(key)
        if self.__size == 0 : self.__head = self.__tail = new_Node
        else : 
            self.__tail.next = new_Node
            self.__tail = new_Node
        self.__size += 1

    def push (self, idx, key) : # O(n)
        if   idx > self.__size  : raise IndexError("Out of inedx('"+str(idx)+"' is not in 0 ~ "+str(self.__size-1)+")")
        elif idx == 0           : return self.pushfront(key)
        elif idx == self.__size : return self.pushback(key)
        else :
            new_Node = NodeS(key)
            new_Node.next = self[idx]
            self[idx-1].next = new_Node
            self.__size += 1

    def popfront (self) : # O(1)
        if self.__size == 0 : print("List is empty") ; return
        x = self.__head
        pop_Node_key = x.key
        self.__head = self.__head.next
        self.__size -= 1
        if   self.__size == 1 : self.__tail = self.__head
        elif self.__size == 0 : self.__tail = None
        del x
        return pop_Node_key
    
    def popback (self) : # O(n)
        if self.__size == 0 : print("List is empty") ; return
        x = self.__tail
        pop_Node_key = x.key
        self.__size -= 1
        self.__tail = self[self.__size-1]
        if   self.__size == 1 : self.__head.next = None
        elif self.__size == 0 : self.__head = self.__tail = None
        else                  : self.__tail.next = None
        del x
        return pop_Node_key
    
    def pop (self, idx) : # O(n)
        if   self.__size == 0 : print("List is empty") ; return
        if   idx >= self.__size   : raise IndexError("Out of inedx('"+str(idx)+"' is not in 0 ~ "+str(self.__size-1)+")")
        elif idx == 0             : return self.popfront()
        elif idx == self.__size-1 : return self.popback()
        else :
            x_pre = self[idx-1]
            x = x_pre.next
            pop_Node_key = x.key
            x_pre.next = x.next
            self.__size -= 1
            del x
            return pop_Node_key

    def index (self, key) : # O(n)
        temp_Node = self.__head
        index = 0
        while temp_Node != None :
            if temp_Node.key == key : return index # 해당 키를 가진 첫 번째 index를 리턴한다.
            index += 1
            temp_Node = temp_Node.next
        return temp_Node 
    
    def search (self, key) : # O(n)
        temp_Node = self.__head
        while temp_Node != None :
            if temp_Node.key == key : return temp_Node # Node를 리턴한다.
            temp_Node = temp_Node.next
        return temp_Node 

def __main () :
    print("노드")
    a = NodeS(3)
    b = NodeS(9)
    c = NodeS(-1)
    print(type(b))
    a.next = b
    b.next = c
    print(a.next)
    print(b.next)
    print(c.next)

    print("링크리스트")
    l = SinglyLinkedList()
    l.pushfront(1)
    l.pushfront(3)
    l.pushfront(-1)
    l.pushback(2)
    l.push(-1,"x")
    print(l)
    print("iter start")
    for i in l :
        print(i)
    print("iter end")
    print("getitem l[1] =", l[1])
    print("       index(1) :", l.index(1))
    print(" type(index(1)) :", type(l.index(1)))
    print(" search(1) NodeS :", l.search(1))
    print("type(search(1)) :", type(l.search(1)))
    print(l)
    print(l.popfront())
    print(l.popback())
    print(l.pop(1))
    print(l.popfront())
    print(l.popback())
    print(l)
    print(l.popback())
    # print(l[0])


if __name__=="__main__" :
    __main()

