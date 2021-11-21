import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__)))) # 상위 폴더 추가
from data_structure.stack import *
# from ..data_structure.stack import *

class Calculator :
    def __init__ (self) : 
        self.outstack = Stack(msg = False)
        self.opstack = Stack(msg = False)
        self.__opsq = ("(","+","-","*","/","^",")")

    def start (self) : 
        self.__set(sys.stdin.readline().replace(" ",""))
        return self.__calculate()
    
    def __set (self, x) :
        k = ""
        for i in range(len(x)) :
            if (x[i].isdigit()) or (x[i] == ".") : 
                k += x[i]
                if not (i+1 == len(x)) : 
                    if (x[i+1].isdigit()) or (x[i+1] == ".") : continue
                self.outstack.push(k)
                k = ""
            elif x[i] == "(" : self.opstack.push(0)
            elif x[i] == ")" : 
                while self.opstack.top() != 0 : self.outstack.push(self.__opsq[self.opstack.pop()])
                self.opstack.pop()
            elif (x[i] == "+") or (x[i] == "-") :
                if (i == 0) or (x[i-1] == "(") or (x[i-1] == "^") : k += x[i] ; continue ## 가장 처음 또는 ( 또는 ^ 다음 + or -가 나오면 수에 포함.
                while True :
                    if self.opstack.top() <= 2 : self.opstack.push(self.__opsq.index(x[i])) ; break
                    else : self.outstack.push(self.__opsq[self.opstack.pop()])
            elif (x[i] == "*") : 
                while True :
                    if self.opstack.top() <= 3 : self.opstack.push(self.__opsq.index(x[i])) ; break
                    else : self.outstack.push(self.__opsq[self.opstack.pop()])
            elif (x[i] == "/") : 
                while True :
                    if self.opstack.top() <= 4 : self.opstack.push(self.__opsq.index(x[i])) ; break
                    else : self.outstack.push(self.__opsq[self.opstack.pop()])
            elif (x[i] == "^") : self.opstack.push(self.__opsq.index(x[i]))

        while len(self.opstack) :
            self.outstack.push(self.__opsq[self.opstack.pop()])

    def __calculate (self) :
        i = self.outstack.pop()
        if   i == "*" : return self.__calculate() * self.__calculate()
        elif i == "/" : return round(1/self.__calculate() * self.__calculate(),10)
        elif i == "+" : return self.__calculate() + self.__calculate()
        elif i == "-" : return - self.__calculate() + self.__calculate()
        elif i == "^" : 
            a = self.__calculate()
            b = self.__calculate()
            return b**a
        else : return float(i)

def __main () :
    print("main start")
    x = Calculator()
    print(x.start())
    print("main end")

if __name__ == "__main__" :
    __main()
    # print(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
    # print(os.path.abspath(os.path.dirname(__file__)))
    # print(os.path.dirname(__file__))