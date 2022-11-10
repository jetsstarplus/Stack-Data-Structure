class Node():
    def __init__(self) -> None:
        self.length = 0
        self.head= None
        self.data= None
        self.next= None
    
    def setData(self, data):
        self.data = data
    
    def getData(self):
        return self.data

    def setNext(self, next):
        self.next = next
    
    def getNext(self):
        return self.next

    def getAll(self):
        """
        Worst case Time Complexity is O(n) since we are traversing the whole node data structure

        Space Complexity is O(1) since we are creating one temporary variable
        """
        list_node = []
        if self.head == None:
            raise ValueError
        current: Node = self.head
        index: int = 0
        while index < self.length:
            list_node.append(current.getData())
            current = current.getNext()
            index += 1
        return list_node

    def insertAtBeg(self, data):
        """
        Worst case Time Complexity is O(1) since we are inserting at the beginning of the linkedList

        Space Complexity is O(1) since we are creating one temporary variable
        """
        newNode = Node()
        newNode.setData(data)
        
        if self.length != 0:
            self.head = newNode
        else:
            newNode.setNext(self.head)
            self.head = newNode
        self.length += 1

    def insertAtEnd(self, data):
        """
        Worst case Time Complexity is O(n) since we are inserting at the end of the linkedList that is we are traversing
        the whole list inorder for insertion

        Space Complexity is O(1) since we are creating one temporary variable
        """
        newNode = Node()
        newNode.setData(data)
        current = self.head
        while current.getNext() != None:
            current = self.getNext()
        
        current.setNext(newNode)
        self.length +=1

    def insertAtPos(self, data, pos):
        """
        Worst case Time Complexity is O(n) since we may insert at the last position of the linkedList that is we are traversing
        the whole list inorder for insertion

        Space Complexity is O(1) since we are creating one temporary variable
        """
        if pos> self.length or pos < 0:
            return None
        else:
            if pos == 0:
                self.insertAtBeg(data)
            else:                
                newNode = Node()
                newNode.setData(data)
                count = 0
                current = self.head
                while count < pos -1:
                    count +=1
                    current = current.getNext()
                newNode.setNext(current.getNext)
                current.setNext(newNode)
                self.length +=1
    
    def delAtBeg(self):
        """
        Worst case Time Complexity is O(1) since we are deleting at the first position of the linked list

        Space Complexity is O(1) since we are creating one temporary storage for the node to be deleted that is later
        dropped
        """
        if self.length == 0:
            raise IndexError
        else:
            self.head = self.head.getNext()
            self.length -= 1

    def delAtEnd(self):
        """
        Worst case Time Complexity is O(n) since we are deleting at the end of the linkedList that is we are traversing
        the whole list inorder for insertion

        Space Complexity is O(1) since we are creating one temporary variable
        """
        if self.length == 0:
            raise IndexError
        else:
            current = self.head
            index = 0
            while index < self.length - 1:
                index += 1
                current = current.getNext()
            current.setNext(None)
            self.length -= 1

    def delNode(self, node):
        """
        Worst case Time Complexity is O(n) since we are deleting at the end of the linkedList that is we are traversing
        the whole list inorder for insertion

        Space Complexity is O(1) since we are creating one temporary variable
        """
        if self.length == 0:
            raise ValueError("Empty List")
        else:
            current = self.head
            previous = None
            found = False

            while not found:
                if current == node:
                    found= True
                elif current is None:
                    raise(ValueError(f'Linked List does not have a node {node}'))
                else:
                    previous = current
                    current = current.getNext()
            if previous is None:
                self.head = current.getNext()
            else:
                previous.setNext(current.getNext())
            self.length -= 1

    def delVal(self, value):
        """
        Worst case Time Complexity is O(n) since we are deleting at the end of the linkedList that is we are traversing
        the whole list inorder for insertion

        Space Complexity is O(1) since we are creating one temporary variable
        """
        currnode= self.head
        prevnode= self.head

        while currnode.getNext() != None:
            if currnode.data == value:
                prevnode.setNext(currnode.getNext())
                self.length -= 1
                return
            else:
                prevnode = currnode
                currnode = currnode.getNext()
        raise ValueError

    def delAtPos(self, pos):
        """
        Worst case Time Complexity is O(n) since we are deleting at the end of the linkedList that is we are traversing
        the whole list inorder for insertion

        Space Complexity is O(1) since we are creating one temporary variable
        """
        index = 0
        currnode = self.head
        prevnode = self.head
        if self.length == 0:
            raise IndexError
        else:
            if pos < 0:
                pos = (self.length-1) + pos
            if pos > self.length -1 or pos < 0:
                raise IndexError
            else:
                while prevnode.next != None or index < pos:
                    index += 1
                    if index == pos:
                        prevnode.setNext(currnode.getNext())
                        self.length -= 1
                        return
                    else:
                        prevnode = currnode
                        currnode = currnode.getNext()

    def indexOf(self, value):
        """
        Worst case Time Complexity is O(n) since we can find an element at the end of the node

        Space Complexity is O(1) since we are creating one temporary variable
        """
        currnode= self.head
        index = 0
        while currnode.getNext() != None:
            if currnode.data == value:
                return index
            else:
                currnode = currnode.getNext()
                index += 1
        raise ValueError

    def valueOf(self, pos):
        """
        Worst case Time Complexity is O(n) since we can find an element at the end of the node

        Space Complexity is O(1) since we are creating one temporary variable
        """
        index = 0
        currnode = self.head
        if self.length == 0:
            raise IndexError
        else:
            if pos < 0:
                pos = (self.length-1) + pos
            if pos > self.length -1 or pos < 0:
                raise IndexError
            else:
                while currnode.next != None or index < pos:
                    index += 1
                    if index == pos:
                        return(currnode.getData())
                    else:
                        currnode = currnode.getNext()


