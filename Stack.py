from  LinkedList import Node

class Stack():
    def __init__(self, data=None) -> None:
        self.head = None
        self.length = 0
        if data:
            for data in data:
                self.push(data)

    def push(self, data):
        """
        Worst case Time Complexity is O(1) since we are inserting an element on top of the stack

        Space Complexity is O(1) since we are creating one temporary variable
        """
        node = Node()
        node.setData(data)
        node.setNext(self.head)
        self.head = node
        self.length += 1

    def pop(self):
        """
        Worst case Time Complexity is O(1) since we are removing an element on top of the stack

        Space Complexity is O(1) since we are creating one temporary variable
        """
        if self.head == None:
            raise IndexError
        else:
            data = self.head.getData()
            self.head = self.head.getNext()
            self.length -= 1
            return(data)

    def peek(self):
        if self.head == None:
            raise IndexError
        return self.head.getData()

    def all(self):
        all_list: list = []
        if self.head == None:
            raise IndexError
        current = self.head
        index: int = 0
        while index < self.length:
            all_list.append(current.getData())
            current = current.getNext()
            index += 1
        return all_list

# ourList = ["first", "second", "third", "fouth"]
# stack = Stack(ourList)
# stack.peek()
# stack.pop()
# print(stack.all())