from wordData import WordData

class OrderedSet:

    class LNode:
        def __init__(self, data=None, next= None, prev= None):
            self.data = data
            self.next = next
            self.prev = prev

    # # QUESTION: maybe an iterator class...
    # # QUESTION: maybe an exception class...


    def __init__(self, other=None):
        self.size = 0
        self.first = None
        self.last = None
        if other:
            n = other.first
            while n != None:
                self.insertLast(n.data)
                n = n.next


    def insert(self, wd):
        if self.size == 0:
            return self.__insertFirst(wd)
        if wd > self.last.data:
            return self.__insertLast(wd)
        if wd < self.last.data:
            return self.__insertFirst(wd)
        if self.find(wd):
            return False
        nn = self.LNode()
        if nn == None:
            return
        nn.data = wd
        nx = self.first
        while nx.data < wd:
            nx = nx.next
        pv = myfirst.prev
        nn.prev = pv
        nx.prev = nn
        pv.next = nn
        nn.next = nx
        self.size += 1
        return True

    def __insertFirst(self, value):
        np = self.LNode()
        if np == None:
            return False
        np.data = value
        np.next = self.first
        self.first = np
        self.size+= 1
        return True

    def __insertLast(self, value):
        if self.size == 0:
            return self.__insertFirst(value)
        np = self.first
        mid = None
        while np != None:
            mid = np
            np = np.next
        last = self.LNode()
        if last == None:
            return False
        mid.next = last
        last.next = None
        last.data = value
        self.size += 1
        return True

    def delete(self, wd):
        if self.size == 1:
            return self.__deleteFirst()
        elif wd == self.last.data:
            return self.__deleteLast()
        elif wd == self.first.data:
            return self.__deleteFirst()
        elif not self.find(wd):
            return False
        else:
            # self.find() will return the value it finds else None
            # deleteMe = self.find(wd)
            pass
    def __deleteFirst(self):
        if self.first == None:
            return False
        np = self.first
        self.first = self.first.next
        self.size -= 1
        return True

    def __deleteLast(self):
        if self.size == 0:
            return False
        if self.size == 1:
            return self.__deleteFirst()
        n = self.first
        p = LNode()
        while n.next != None:
            p = n
            n = n.next
        p.next = None
        self.size -= 1
        return True

    def __eq__(self, other):
        if self.size != other.size:
            return False
        myfirst = self.first
        otherFirst = other.first
        while myfirst != None:
            if myfirst.data != otherFirst.data:
                return False
            myfirst = myfirst.next
            otherFirst = otherFirst.next
        return True

    def CopySet(self, other):
        if self is other:
            return self
        while self.first:
            self.__deleteFirst()
        n = other.first
        while n != None:
            self.__insertLast(n.data)
            n = n.next
        return self

    def printSet(self):
        np = self.first
        while np != None:
            print(np.data)
            np = np.next

    def find():
        n = self.first
        while n != None:
            if n.data == value:
                return True
        return False
    def __add__(self, other):
        myCopy = self.CopySet(self)
        s2 = OrderedSet()
        Union = self
        for i in other:
            s2.insert(i)
        if self.size >= other.size():
            for i in other:
                Union.insert(i)
            return Union
        else:
            for i in self:
                s2.insert(i)
            return s2

    def __mul__(self, other):
        intersection = OrderedSet()
        myCopy = self.CopySet(self)
        intersection2 = OrderedSet()
        for i in other:
            intersection.insert(i)
        if self.size >= other.size:
            for i in other:
                if intersection.find(i):
                    myCopy.insert(i)
        else:
            i = 0
            while i < self.size:
                if intersection2.find(myCopy[i]):
                    intersection.insert(myCopy[i])
                i += 1
        return intersection
    def __getItem__(self, key):
        if key < 0:
            return None
        if index >= self.size:
            return None
        n = self.first
        i = 0
        while i < key:
            n = n.next
        return n.data
