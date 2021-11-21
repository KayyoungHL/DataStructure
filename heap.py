class Heap :
    def __init__ (self, lst) :
        self.__list = lst
        self.__make_heap()

    def __str__ (self) -> str :
        return str(self.__list)
    
    def __repr__ (self) -> list :
        return self.__list

    def __len__(self) -> int :
        return len(self.__list)

    def __make_heap (self) : # O(n*log(n)) or O(n)
        n = len(self.__list)
        for k in range(n//2-1, -1, -1) :
            self.__heapify_down(k)

    def __heapify_down (self, k) : # O(log(n))
        n = len(self.__list)
        while k < n//2 :
            if k*2+2 <= n-1 : index_max = max([k,2*k+1,2*k+2], key = lambda i: self.__list[i])
            else : index_max = max([k,2*k+1], key = lambda i: self.__list[i])
            if not index_max == k : 
                self.__list[index_max], self.__list[k] = self.__list[k], self.__list[index_max]
                k = index_max
            else : break
    
    def __heapify_up (self, k) : # O(log(n))
        while k > 0 :
            if self.__list[k] > self.__list[(k-1)//2] : 
                self.__list[k], self.__list[(k-1)//2] = self.__list[(k-1)//2], self.__list[k]
                k = (k-1)//2
            else : break

    def insert (self, value) : # O(log(n))
        k = len(self.__list)
        self.__list.append(value)
        self.__heapify_up(k)
    
    def find_max (self) -> int : # O(1)
        return self.__list[0]
    
    def delete_max (self) -> int : # O(log(n))
        self.__list[0], self.__list[-1] = self.__list[-1], self.__list[0]
        return_val = self.__list.pop()
        self.__heapify_down(0)
        return return_val
    
    def heap_sort (self, reverse=False) -> list : # O(n*log(n))
        n = len(self.__list) # O(1)
        __list = self.__list[:] # O(n). 얕은 복사
        temp = [None] * n # O(1)
        if reverse : 
            for i in range(n) : temp[i] = self.delete_max() # O(n*log(n))
        else :
            for i in range(n-1,-1,-1) : temp[i] = self.delete_max() # O(n*log(n))
        self.__list = __list # O(1)
        return temp

    def heap_plot (self) : # 나중에 그려봅시다.
        pass

def __main() :
    lst = [0,10,3,7,11,13,30,6,12]
    x = Heap(lst)
    print(x)
    x.insert(50)
    print(x)
    x.insert(70)
    print(x)
    print(x.delete_max())
    print(x)
    print(x.delete_max())
    print(x)
    print(x.find_max())
    print(x.heap_sort())
    print(x.heap_sort(reverse=True))
    print(x)

def __timechk () : # 그냥 sorted가 왜 더 빠를까?! 힙 의미가 있을까?? 최대값을 하나씩 제외할 때 의미가 있을 지도
    from datetime import datetime
    lst = list(range(1000000))
    start = datetime.now()
    print(sorted(lst,reverse=True)[0])
    end = datetime.now()
    print(end - start)
    start = datetime.now()
    k = Heap(lst)
    print(k.find_max())
    end = datetime.now()
    print(end - start)


if __name__ == "__main__" :
    __main()
    # __timechk()