
from tokenize import String


class Node(object):
    """docstring for Node."""

    #data sera el que nos permitira almacenar la cadena y estado? si es que tiene o solo strings, no?
    def __init__(self, data=None, next=None, previous=None):
        self.data= data
        self.next= next
        self.previous = previous

class DoubledLinkedList(object):
    def __init__(self):
        self.head= None
        self.cola= None
        self.count= 0

    def insert(self, data):
        nodo= Node(data)

        if self.head is None:
            self.head = nodo
            self.cola = self.head
        else:
            nodo.previous=self.cola
            self.cola.next=nodo
            self.cola=nodo
            self.count+=1

    def rec(self):
        nodeAux= self.head
        while nodeAux:
            data=nodeAux.data
            nodeAux= nodeAux.next
            yield data

key=0
list=DoubledLinkedList()
list.insert("_")
list.insert("a")
list.insert("q0")
list.insert("a")
list.insert("_")

string = ""
for node in list.rec():
    string= string + node
print(string)