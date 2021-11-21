import re

class NodeD :
    def __init__ (self, key = None):
        self.__key = key
        self.__next = None
        self.__prev = None
    
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
        if (type(nn) == NodeD) or (nn is None) : self.__next = nn
        else : raise TypeError("can only point 'NodeD' type (not "+re.findall("\'.*\'|\s-\s.*",str(type(nn)))[0]+") as next Node")
    
    @property 
    def prev (self) : return self.__prev

    @prev.setter
    def prev (self, nn) :
        if (type(nn) == NodeD) or (nn is None) : self.__prev = nn
        else : raise TypeError("can only point 'NodeD' type (not "+re.findall("\'.*\'|\s-\s.*",str(type(nn)))[0]+") as previous Node")
    

class DoublyLinkedList :
    def __init__ (self) :
        self.__head = NodeD()
        self.__head.next = self.__head
        self.__head.prev = self.__head
        self.__size = 0
    
    def __repr__ (self):
        try : return {"Head":self.__head.next.key, "Tail":self.__head.prev.key, "Length":self.__size}
        except : return {"Head":self.__head.next, "Tail":self.__head.prev, "Length":self.__size}

    def __str__ (self) :
        try : return "DoublyLinkedList("+str({"Head":self.__head.next.key, "Tail":self.__head.prev.key, "Length":self.__size})+")"
        except : return "DoublyLinkedList("+str({"Head":self.__head.next, "Tail":self.__head.prev, "Length":self.__size})+")"

    def __len__ (self) :
        return self.__size
    
    def __getitem__ (self, idx) :
        if idx < 0 : idx = self.__size + idx
        if (idx >= self.__size) | (idx < 0) : raise IndexError("Out of inedx('"+str(idx)+"' is not in 0 ~ "+str(self.__size-1)+")")
        temp_Node = self.__head.next
        while idx > 0 :
            temp_Node = temp_Node.next
            idx -= 1
        return temp_Node
        
    # generator -> for loop을 돌리기 위한 작업
    def __iter__ (self) : # O(n)
        temp_Node = self.__head.next
        while temp_Node.key != None :
            yield temp_Node # yield는 return인가? 이해해 보자.
            temp_Node = temp_Node.next
        return StopIteration
    
    def splice (self, a, b, x) :
        ap, bn, xn = a.prev, b.next, x.next
        ap.next, bn.prev = bn, ap
        x.next, a.prev = a, x
        b.next, xn.prev = xn, b
    
    def moveafter (self, a, x) :
        self.splice(a, a, x)
    
    def movebefore (self, a, x) :
        self.splice(a, a, x.prev)
    
    def insertafter (self, x, key) :
        self.moveafter(NodeD(key), x)
        self.__size += 1
    
    def insertbefore (self, x, key) :
        self.movebefore(NodeD(key),x)
        self.__size += 1
    
    def pushfront (self, key) :
        self.insertafter(self.__head, key)
    
    def pushback (self, key) :
        self.insertbefore(self.__head, key)
    
    # def pushforward (self, ) : # 이거는 인덱스로 해야하나 아니면 키로 해야하나 햇갈리는구만!
    
    def remove (self, x) : # Node를 remove
        if (x == None) or (x == self.__head) : return
        x.prev.next = x.next
        x.next.prev = x.prev
        pop_node_key = x.key
        del x
        return pop_node_key
    
    def popfront (self) :
        return self.remove(self.__head.next)
    
    def popback (self) :
        return self.remove(self.__head.prev)

    def popforward (self, key) : # O(n)
        return self.remove(self.search(key))
    
    def popbackward (self, key) : # O(n)
        return self.remove(self.searchback(key))
    
    def search (self, key) : # O(n)
        temp_Node = self.__head
        while temp_Node.next != self.__head :
            if temp_Node.key == key : return temp_Node # Node를 리턴한다.
            temp_Node = temp_Node.next
        return None

    def searchback (self, key) : # O(n)
        temp_Node = self.__head
        while temp_Node.prev != self.__head :
            if temp_Node.key == key : return temp_Node # Node를 리턴한다.
            temp_Node = temp_Node.prev
        return None

    def index (self, key) : # O(n)
        temp_Node = self.__head.next
        index = 0
        while temp_Node.next != self.__head :
            if temp_Node.key == key : return index # 해당 키를 가진 첫 번째 index를 리턴한다.
            index += 1
            temp_Node = temp_Node.next
        return -1
    
    def join (self, dll) : 
        self.__head.prev.next = dll.__head.next
        dll.__head.next.prev = self.__head.prev
        self.__size += dll.__size 
        # del doublylinkedlist ## del을 해야하나? 굳이? 모르겠다. del을 하면 해당 값이 사라지는데, 혹시 쓸려고 마음 먹을 수도 있지 않을까?
        return self

    def split (self, idx) :
        new_dll = DoublyLinkedList()
        x = self[idx-1]
        new_dll.__head.next = x.next
        new_dll.__head.prev = self.__head.prev
        x.next = self.__head
        self.__head.prev = x
        new_dll.__size = self.__size - idx
        self.__size = idx
        return self, new_dll
        


def __main () :
    print("노드")
    a = NodeD(3)
    b = NodeD(9)
    c = NodeD(-1)
    print(type(b))
    a.next = b
    b.prev = a
    b.next = c
    c.prev = b
    print(a.next)
    print(b.next)
    print(c.prev)
    print(b.prev)

    print("링크리스트")
    l = DoublyLinkedList()
    print(l)
    


if __name__=="__main__" :
    __main()

