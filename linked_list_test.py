
import timeit
from LinkedList import Node
class ComparePythonAndLinkedList():
    def __init__(self) -> None:
        pass

    def python_insertion(self):
        print("*******Python List Insertion*************")
        python_test_code = '''
def test():
    listElement = []
    list.append("hello")
    list.append("there")
    list.append("test")
        '''
        time_taken=timeit.repeat(stmt=python_test_code,  repeat=5)
        print(time_taken)
        print(f'Python List Average time {sum(time_taken)/5}\n')

    def linked_list_insertion(self):
        print("*******Linked List Insertion*************")
    
        python_test_code = '''
def test():
    node = Node()
    node.insertAtBeg("hello")
    node.insertAtBeg("there")
    node.insertAtBeg("test")
        '''
        time_taken=timeit.repeat(stmt=python_test_code, setup="from LinkedList import Node", repeat=5)
        print(time_taken)
        print(f'linked List Average time {sum(time_taken)/5}')

    def test_insertion(self):
        self.python_insertion()
        self.linked_list_insertion()


    def python_find(self):
        print("*******Python List Find Element*************")
        list = []
        python_test_code = '''
def test():
    listElement = []
    list.append("hello")
    list.append("there")
    list.append("test")
    list.index(test)
        '''
        time_taken=timeit.repeat(stmt=python_test_code,  repeat=5)
        print(time_taken)
        print(f'Python List Average time {sum(time_taken)/5}\n')

    def linked_list_find(self):
        print("*******Linked List Find Element*************")
    
        python_test_code = '''
def test():
    node = Node()
    node.insertAtBeg("hello")
    node.insertAtBeg("there")
    node.insertAtBeg("test")
    node.indexOf("test")
        '''
        time_taken=timeit.repeat(stmt=python_test_code, setup="from LinkedList import Node", repeat=5)
        print(time_taken)
        print(f'linked List Average time {sum(time_taken)/5}')

    def test_find(self):
        self.python_find()
        self.linked_list_find()

    def python_delete(self):
        print("*******Python List Delete Element*************")
        list = []
        python_test_code = '''
def test():
    listElement = [] 
    list.append("hello")
    list.append("there")
    list.append("test")
    listElement.remove("test")
        '''
        time_taken=timeit.repeat(stmt=python_test_code,  repeat=5)
        print(time_taken)
        print(f'Python List Average time {sum(time_taken)/5}\n')

    def linked_list_delete(self):
        print("*******Linked List Delete Element*************")
    
        python_test_code = '''
def test():
    node = Node()
    node.insertAtBeg("hello")
    node.insertAtBeg("there")
    node.insertAtBeg("test")
    node.delVal("test")
        '''
        time_taken=timeit.repeat(stmt=python_test_code, setup="from LinkedList import Node", repeat=5)
        print(time_taken)
        print(f'linked List Average time {sum(time_taken)/5}')

    def test_delete(self):
        self.python_delete()
        self.linked_list_delete()


test_list = ComparePythonAndLinkedList()
test_list.test_delete()

# 0.23717257499993138