class Node:
    def __init__(self,value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def print(self):
        temp = self.head
        while(temp != None):
            print(temp.value)
            temp = temp.next


myList = LinkedList()
first = Node(10)
second = Node(20)
third = Node(30)
fourth = Node(40)


myList.head = first
first.next = second
second.next = third
third.next = fourth
myList.print()
