# direction= True so remove head False remove Tail
# _type = True remove index else remove Data
class Node:
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)

    def __init__(self, data):
        self.Data = data
        self.Next = None
        self.Previous = None


class LinkedList:
    Head = None
    Tail = None
    Size = 0
    __current = None

    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)

    def __init__(self, *args):
        if len(args) == 1:
            for i in args[0]:
                self.add_tail(i)

        if len(args) == 3:
            self.Head = args[0]
            self.Tail = args[1]
            self.Size = args[2]

    def __repr__(self) -> str:
        return f"{type(self).__name__}(Head={self.Head.Data}, Tail={self.Tail.Data},Size=({self.Size}) "

    @staticmethod
    def marge_lst(list1, list2):
        list1.Tail.Next = list2.Head
        return LinkedList(list1.Head, list2.Tail, list1.Size + list1.Size)

    def split(self, index):
        list1 = LinkedList.__new__(LinkedList)
        list2 = LinkedList.__new__(LinkedList)
        temp = self.Head
        for i in range(self.Size):
            if i <= index:
                list1.add_tail(temp.Data)
                temp = temp.Next
                continue
            list2.add_tail(temp.Data)
            temp = temp.Next
        return [list1, list2]

    def add_head(self, data):
        node = Node(data)
        if self.Head is None:
            self.Head = self.Tail = node
        else:
            node.Next = self.Head
            self.Head = node
        self.Size += 1

    def add_tail(self, data):
        node = Node(data)
        if self.Tail is None:
            self.Head = self.Tail = node
        else:

            self.Tail.Next = node
            self.Tail = node
        self.Size += 1

    def add_n_to(self, _to, _type, data):
        node = Node(data)
        self.find(_to, _type)
        node.Next = self.__current.Next
        self.__current.Next = node

    def print_list(self):
        node = self.Head
        while node:
            print(node.Data, end=' ')
            node = node.Next

    def find(self, data, direction: bool):
        temp = self.Head
        where = 0

        if direction:
            while temp:
                if data == where:
                    self.__current = temp
                    return True
                temp = temp.Next
                where += 1
            return False

        while temp:
            if data == temp.Data:
                self.__current = temp
                return True
            temp = temp.Next
        return False

    def remove(self, direction: bool):
        assert self.is_empty(), "the list is empty"
        self.Size -= 1
        if direction:
            if self.Head.Next is None:
                self.Head = None
                return None

            self.Head = self.Head.Next
            return

        temp = self.Head
        while temp.Next:
            if temp.Next == self.Tail:
                self.Tail = temp
                self.Tail.Next = None
                return
            temp = temp.Next

    def remove_loc(self, data):
        assert self.is_empty(), "Empty list"

        if data == self.Head.Data:
            self.remove(True)
            return
        if data == self.Tail.Data:
            self.remove(False)
            return
        prev = self.Head
        temp = prev.Next

        while True:
            if temp.Data == data:
                prev.Next = temp.Next
                temp.Next = None
                temp.Data = None
                return
            prev = temp
            temp = temp.Next

    def is_empty(self) -> bool:
        if self.Head or self.Tail:
            return True
        return False

    def push_back(self, arr):
        for i in arr:
            self.add_tail(i)

    def __del__(self):
        print(end='')


if __name__ == '__main__':
    lnklst2 = LinkedList([1, 2, 3, 4, 5, 6])
    lnklst2.add_n_to(3,False,20)
    lnklst2.print_list()
