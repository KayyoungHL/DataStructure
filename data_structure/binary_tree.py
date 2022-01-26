from abc import ABCMeta, abstractmethod
import warnings

# 추상클래스를 연습해보자.
class aBinaryTreeNode(metaclass=ABCMeta):
    """추상클래스 노드"""
    @property
    @abstractmethod
    def key(self):
        pass


    @property
    @abstractmethod
    def parent(self):
        pass


    @property
    @abstractmethod
    def left(self):
        pass


    @property
    @abstractmethod
    def right(self):
        pass


    @abstractmethod
    def split(self):
        pass


    @abstractmethod
    def find_root(self):
        pass

###########################################################################
class BinaryTreeNode(aBinaryTreeNode):
    """This class is to make binary tree node."""
    def __init__(self, value, parent=None, left=None, right=None):
        self.__parent = parent
        self.__left = left
        self.__right = right
        self.__key = value


    def __str__(self):
        return str(self.__key)  # or f"TreeNode(key = {self.__key})"


    def __repr__(self):
        return str(self.__key)


    @property
    def key(self): 
        return self.__key


    @key.setter
    def key(self, value):
        self.__key = value


    @property
    def parent(self):
        return self.__parent


    @parent.setter ## None으로 자르는 기능을 넣기 보다 split를 쓰게 만들까? 안 그러면 잘라낸 노드를 잃어버린다.
    def parent(self, node=None): 
        if (type(node) == BinaryTreeNode)|(node==None): 
            if not self.__parent == None:
                if node == None:
                    if (self.__parent.left == self): self.__parent.left = None
                    else: self.__parent.right = None
                    self.__parent = None
                else : raise ValueError("You can't specify parent node. Use 'left' or 'right' at argument node")
        else: raise TypeError(f"left Type MUST be BinaryTreeNode(not {type(node).__name__})")


    def split(self):
        """split function splits input node from parent node.
        return : input node as a root node, parent node's root node
        """
        x = self.__parent
        if not x == None:
            self.parent = None
            return self, x.find_root()
        else: raise ValueError("Unexpected input error. This node is root node. split function is only for node which has parent node(not root node)")


    def find_root(self, count=False):
        if count:
            count = 0
            while self.__parent != None: 
                self = self.__parent
                count += 1
            return self, count
        else:
            while self.__parent != None: 
                self = self.__parent
            return self


    @property
    def left(self):
        return self.__left


    @left.setter ## None으로 자르는 기능을 넣기 보다 split를 쓰게 만들까? 안 그러면 잘라낸 노드를 잃어버린다.
    def left(self, node):
        if (type(node) == BinaryTreeNode)|(node==None): 
            if node == None:
                if not self.__left == None: 
                    self.__left.__parent, self.__left  = None, None
            else:
                if not self.__left == None: self.__left.__parent = None
                if not node.__parent == None:
                    if node.__parent.__left == node: node.__parent.__left = None
                    else: node.__parent.__right = None
                node.__parent = self
                self.__left = node
        else: raise TypeError(f"left Type MUST be BinaryTreeNode(not {type(node).__name__})")


    @property
    def right(self):
        return self.__right


    @right.setter ## None으로 자르는 기능을 넣기 보다 split를 쓰게 만들까? 안 그러면 잘라낸 노드를 잃어버린다.
    def right(self, node):
        if (type(node) == type(self))|(node==None): 
            if node == None:
                if self.__right: self.__right.__parent, self.__right  = None, None
            else:
                if self.__right: self.__right.__parent = None
                if node.__parent:
                    if node.__parent.__left is node: node.__parent.__left = None
                    else: node.__parent.__right = None
                node.__parent = self
                self.__right = node
        else: raise TypeError(f"right Type MUST be BinaryTreeNode(not {type(node).__name__})")

###########################################################################
class aBinaryTree(metaclass=ABCMeta):
    @property
    @abstractmethod
    def root(self):
        pass


    @abstractmethod
    def traversal(self):
        pass

###########################################################################
class BinaryTree(aBinaryTree):
    """[summary]

    Attributes : root

    Methods : traversal(kind="inorder")
    """
    def __init__(self, node=None, set_root="find"):
        # set_root = "find"면 root를 찾아서 BT 생성
        # set_root = "split"면 부모노드와 분리한 후 해당 노드를 root로 만들고 BT 생성
        self.__set_root = set_root
        self.root = node


    def __str__(self):
        return f"BinaryTree({self.traversal()})"


    def __repr__(self): 
        return str(self.traversal())


    def __len__(self):
        return len(self.traversal())


    @property
    def set_root(self):
        return self.__set_root


    @set_root.setter
    def set_root(self, way):
        if way in ["find","split"]:
            self.__set_root = way


    @property
    def root(self):
        return self.__root


    def __check_type(self, node):
        return type(node) == BinaryTreeNode


    @root.setter
    def root(self, node):
        if (self.__check_type(node))|(node==None): 
            if node:
                if node.parent:
                    if self.__set_root == "find":
                        warnings.warn("This node has parent. Should find root node.",UserWarning)
                        node, count = node.find_root(count=True)
                        warnings.warn(f"To find root node, it has gone up {count} level",UserWarning)
                    elif self.__set_root == "split": ## 기존 루트 노드를 잃으면 어떡하지..? 방법을 찾아야하는데...
                        node.parent = None
                self.__root = node
            else: 
                self.__root = node
        else: raise TypeError(f"root Type MUST be BinaryTreeNode(not {type(node).__name__})")


    def traversal(self, kind="inorder") -> list:
        """[summary]

        Args:
            kind (str, optional): "inorder", "preorder", "postorder". Defaults to "inorder".

        Returns:
            list: list of traversed keys sorted by 'kind'
        """
        return_list = []
        command = {
            "inorder": self.__inorder,
            "preorder": self.__preorder,
            "postorder": self.__postorder
        }
        if self.__root:
            try:
                command[kind](self.__root, return_list)
            except:
                raise KeyError(f"Can't find key : '{kind}'. Key MUST be in ['inorder', 'preorder', 'postorder']")
        return return_list


    @classmethod
    def __inorder(cls, node, return_list):
        if node.left:
            cls.__inorder(node.left, return_list)
        return_list.append(node)
        if node.right:
            cls.__inorder(node.right, return_list)


    @classmethod
    def __preorder(cls, node, return_list):
        return_list.append(node)
        if node.left:
            cls.__preorder(node.left, return_list)
        if node.right:
            cls.__preorder(node.right, return_list)


    @classmethod
    def __postorder(cls, node, return_list):
        if node.left:
            cls.__postorder(node.left, return_list)
        if node.right:
            cls.__postorder(node.right, return_list)
        return_list.append(node)

###########################################################################
class BinarySearchTree(BinaryTree):
    """내일 만들거 생각해 봅시다.
    전제 - BST에 해당된 노드들은 BST class를 통하지 않으면 읽거나 변형할 수 없어야 한다.
    왜냐하면 size 정보가 있기 때문에 노드 자체적으로 길이가 변하게 되면 size를 매번 수정해 줘야 하는 번거로움이 있다.
    1. 노드를 입력받아 init 한다.(없으면 None으로 생성)
        1-1 init에서 root와 size가 attributes를 정의한다.
    2. 해당 노드가 1개인지, 여러개인지 확인한다.
    3. 1개라면 root노드로 정하고 그냥 만든다.
    4. 여러개라면 탐색(traversal)을 한다.
    5. 탐색한 값을 sorting하고(요부분이 쪼끔 걸린다... 다른 방법이 있을듯?) 해당 노드를 root 노드로 하는 이진탐색트리로 만든다.
        5-1 혹은 가불을 판단해서 이진탐색트리 형식이 아니라고 경고를 먼저 한 후 만든다?
    6. search 기능을 만든다.
    7. insert 기능을 만든다.
    8. delete 기능을 만든다.
    """
    def __init__(self, node=None):
        super().__init__(node) ## 이런식으로 노드를 받으면 당연히 BST 자료형이 아니다.
        self.__make_binary_search_tree() ## 현재 계획에서 5-1을 적용해야한다.. 쓰읍...
        self.__size = len(self.traversal())


    def __len__(self):
        return self.__size


    def __str__(self):
        return f"BinarySearchTree({self.traversal()})"


    @property
    def size(self):
        return self.__size


    def __make_binary_search_tree(self): 
        """이미 이진트리노드가 다른 노드와 연결 되어 있을 경우
        해당 이진트리를 이진탐색트리로 바꿔준다.
        1. 기존 트리를 traversal한 후 오름차순 정렬해서 list로 뽑는다.
        2. 중간 값을 root로 만든다.
        3. 모든 노드가 이진탐색트리 조건을 만족할 때까지 반복한다.
        시간이 오래걸리기 때문에 비추... 그냥 하나씩 추가 하는 것을 추천
        """
        node_list = self.traversal()
        sorted_node_list = sorted(node_list, key=lambda x : x.key)
        if not node_list == sorted_node_list: 
            n = len(node_list)
            self.set_root="split"
            self.root = sorted_node_list[n//2]
            self.__make_inorder(self.root, 0, n//2, n-1, sorted_node_list)


    @classmethod
    def __make_inorder(cls, node, start, mid, end, node_list):
        if start == mid:
            node.left = None
        else: 
            node.left = node_list[(start+mid)//2]
            cls.__make_inorder(node.left, start = start, mid = (start+mid)//2, end = mid-1, node_list = node_list)
        if mid == end:
            node.right = None
        else: 
            node.right = node_list[(mid+end)//2+1]
            cls.__make_inorder(node.right, start = mid+1, mid = (mid+end)//2+1, end = end, node_list = node_list)


    def find_loc(self, value):
        """
            value가 있으면 해당 노드를 return,
            value가 없으면 해당 노드를 생성할 자리의 부모 노드를 return
        """
        node = self.root
        if node:
            while node.key != value:
                if value > node.key:
                    if node.right:
                        node = node.right
                    else: 
                        return node
                elif value < node.key:
                    if node.left:
                        node = node.left
                    else: 
                        return node
        return node


    def search(self, value):
        node = self.find_loc(value)
        if node:
            if node.key == value:
                return node
        return None


    def __make_node(self, value):   ## 노드를 생성한다. overring 해서 사용할 것
        return BinaryTreeNode(value)


    def insert(self, value):
        new_node = self.__make_node(value)
        node = self.find_loc(value)
        node = self.__insert(new_node, node, value)
    
    def __insert(self, new_node, node, value):
        if node.key < value:
            right = node.right
            node.right = new_node
            new_node.right = right
        elif node.key >= value:
            left = node.left
            node.left = new_node
            new_node.left = left
        elif node is self.root:
            self.root = new_node
        self.__size += 1
        return node

    def delete(self, value):
        node = self.find_loc(value)
        if node:
            node, _ = self.__delete(node)
        else:
            raise ValueError(f"Value:{value} is not in Tree")
        return node
    
    def __delete(self, node):
        r"""
        node: 삭제할 노드
        x: 삭제할 노드의 자리를 대신 할 노드
        y: x의 왼쪽 서브트리의 head node
        z: x의 부모 노드

            node
           /    \
         ...    ...
           \ 
            z
           / \
         ...  x
             /
            y

        """
        if node.left:                           ### 1. 노드의 왼쪽이 None이 아니면
            x = node.left                       # x는 삭제할 노드의 자리를 대신 할 노드.
            while x.right: 
                x = x.right                     # 삭제할 노드보다 작은 수 중 가장 큰 수를 키로 갖는 노드 찾아 x가 참조한다.
            y = x.left                          # y는 x의 왼쪽 서브트리의 head
            z = x.parent                        # z는 옮기기 전 x의 부모 노드
            if z.right is x:
                z.right = y                     # 삭제할 노드자리로 옮길 노드(x)의 왼쪽 트리(y)를 부모노드(z)의 오른쪽에 붙인다.
            else:                               # 만약 x가 z의 왼쪽 노드라면 y를 z의 왼쪽으로 붙인다.
                z.left = y               
            x.left = node.left                  # 삭제할 노드의 왼쪽 트리를 x 노드의 왼쪽으로 붙인다.
            x.right = node.right                # 삭제할 노드의 오른쪽 트리를 x노드의 오른쪽으로 붙인다.

        elif node.right:                        ### 2. 노드의 왼쪽이 None이고 오른쪽이 None이 아니면
            x = node.right                      # 마찬가지로 x는 삭제할 노드의 자리를 대신 할 노드
            while x.left:                       # 삭제할 노드보다 큰 수 중 가장 작은 수를 키로 갖는 노드를 x
                x = x.left
            y = x.right                         # y는 x의 오른쪽 서브트리의 head
            z = x.parent
            if z.left is x:
                z.left = y                      # x의 오른쪽 트리 y를 z의 왼쪽에 붙인다.
            else:                               # 만약 x가 z의 오른쪽 노드라면 y를 z의 오른쪽으로 붙인다.
                z.right = y
            x.left = node.left                  # 반복
            x.right = node.right                # 반복
        
        else:                                   ### 3. 둘 다 None일 경우, 대체할 x가 없다. None을 반환
            x = None
            z = node.parent                     # z는 삭제할 노드의 부모노드가 된다.

        if node.parent is None: self.root = x
        elif node.parent.left is node: node.parent.left = x
        elif node.parent.right is node: node.parent.right = x
        # del node #del을 하던 return을 하던 마음대로!
        self.__size -= 1
        return node, z



###########################################################################
# AVL? 로테이션 돌리는 방식인가 그랬는데...
# • G.M. Adelson-Velskii, E.M. Landis
class AVLNode(BinaryTreeNode):
    def __init__(self, value, parent=None, left=None, right=None):
        super().__init__(value, parent, left, right)
        self.height_renew()


    def height_renew(self):
        if self.__left:
            height_left = self.__left.height
        else:
            height_left = 0
        if self.__right:
            height_right = self.__right.height
        else:
            height_right = 0
        self.__lr = height_left - height_right
        self.__height = max(height_left, height_right) + 1


    @property
    def lr(self):
        return self.__lr


    @property
    def height(self):
        return self.__height


class AVL(BinarySearchTree): 
    """
    높이 구하는 방법을 구하기 전 까지 풀 수 없다고 본다...
    집 가서 높이를 어떻게 구해서 어떻게 balance가 깨졌는 지 확인하는 지 알아보자.
    """
    def __str__(self):
        return f"AVL({self.traversal()})"


    def __check_type(self, node):
        return type(node) == AVLNode


    def __make_node(self, value):   ## 노드를 생성한다. overring 해서 사용할 것
        return AVLNode(value)
    

    def __make_balance(self, node):
        node.height_renew()
        while node.parent:
            node = node.parent
            node.height_renew()
            if (node.lr >= 2) | (node.lr <= -2):
                self.__rotation(node)

    
    def __rotation(self, node):
        ...
        
    
    def insert(self, value):
        new_node = self.__make_node(value)
        node = self.find_loc(value)
        node = self.__insert(new_node, node, value)
        self.__make_balance(node)


    def delete(self, value):
        node = self.find_loc(value)
        if node:
            node, node_bal = self.__delete(node)
            self.__make_balance(node_bal)
        else:
            raise ValueError(f"Value:{value} is not in Tree")
        return node



    
###########################################################################

def __main():
    x = BinaryTreeNode(1)
    x.left = BinaryTreeNode(2)
    x.left.left = BinaryTreeNode(4)
    x.left.right = BinaryTreeNode(5)
    x.left.right.left = BinaryTreeNode(7)
    x.right = BinaryTreeNode(3)
    x.right.right = BinaryTreeNode(6)
    x.right.right.left = BinaryTreeNode(8)
    x.right.right.right = BinaryTreeNode(9)
    k = BinaryTree()
    k.root = x.right.right.right
    print(k)
    print(list(map(lambda x:x.parent,k.traversal())))
    print(k.traversal(), type(k.traversal()), type(k.traversal()[0]))
    print(k.traversal(kind="preorder"))
    print(k.traversal(kind="postorder"))
    y = x.left
    y.parent = None
    k.root = x
    print(k)
    k.root = y
    print(k)
    x.left = y
    k.root = x
    print(k)
    z = x.right
    x.right = None
    print(k)
    k.root = z
    print(k)
    x.right = z
    k.root = x
    print(k)
    v = BinaryTree(set_root="split")
    v.root = y
    print(v, k)

def __main2():
    x = BinaryTreeNode(0)
    x.left = BinaryTreeNode(1)
    x.left.left = BinaryTreeNode(3)
    x.left.right = BinaryTreeNode(18)
    x.left.right.left = BinaryTreeNode(6)
    x.right = BinaryTreeNode(2)
    x.right.right = BinaryTreeNode(5)
    x.right.right.left = BinaryTreeNode(7)
    x.right.right.right = BinaryTreeNode(8)
    x.left.right.right = BinaryTreeNode(12) 
    x.left.left.left = BinaryTreeNode(15)
    x.left.left.left.right = BinaryTreeNode(21)
    k = BinarySearchTree(x)
    print(k)
    print(list(map(lambda x:x.parent,k.traversal())))
    print(k.root)
    print(len(k), k)
    print(type(k.search(12)))
    print(k.search(13), k.find_loc(13))
    k.insert(13)
    k.insert(4)
    print(len(k), k.traversal())
    k.delete(7)
    print(len(k), k.traversal())
    k.delete(4)
    k.delete(0)
    print(k.traversal())
    k.delete(21)
    print(list(map(lambda x:x.parent,k.traversal())))

    """
                ----------------7----------------
        -------3-------                 -------15-------
    ---1---         ---6---         ---12---        ---21---
           2       5                       13      18       

    """
    # print(k.traversal())
    # print(list(map(lambda x:x.parent,k.traversal())))

def __main3():
    x = BinaryTreeNode(0)
    x.left = BinaryTreeNode(1)
    x.left.left = BinaryTreeNode(3)
    x.right = BinaryTreeNode(2)
    x.right.right = BinaryTreeNode(5)
    x.right.right.left = BinaryTreeNode(7)
    k = BinarySearchTree(x)
    print(len(k), k.traversal())
    print(list(map(lambda x:x.parent,k.traversal())))
    k.delete(3)
    k.insert(3)
    print(len(k), k.traversal())
    print(list(map(lambda x:x.parent,k.traversal())))
    k.delete(7)
    print(len(k), k.traversal())
    print(list(map(lambda x:x.parent,k.traversal())))
    k.delete(2)
    print(len(k), k.traversal())
    k.delete(0)
    print(len(k), k.traversal())
    k.delete(5)
    print(len(k), k.traversal())
    k.delete(1)
    print(len(k), k.traversal())

if __name__ == "__main__":
    # __main()
    # __main2()
    __main3()