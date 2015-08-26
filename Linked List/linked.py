__author__ = 'Akshay'

class Node():

    def __init__(self):
        self.data = None
        self.next = None

    def getData(self):
        return self.data

    def setData(self,data):
        self.data = data

    def getNext(self):
        return self.next

    def setNext(self,next):
        self.next = next


class mylist():

    def __init__(self):
        self.head= None

    def create_list(self,data):
       new_node=Node()
       if(self.head==None):
            new_node.setData(data)
            self.head=new_node

    def insert_at_end(self,data):
        if(self.head==None):
            return self.create_list(data)
        else:
            new_node=Node()
            new_node.setData(data)
            current=self.head
            while current.getNext()!=None:
                current=current.getNext()
            current.setNext(new_node)

    def insert_at_beginning(self,data):
        new_node=Node()
        if(self.head==None):
            return self.create_list(data)
        else:
            new_node=Node()
            new_node.setData(data)
            new_node.setNext(self.head)
            self.head=new_node

    def listLength(self):
        current=self.head
        count=0
        while current!=None:
            count=count+1
            current=current.getNext()
        return count

    def insert_at_position(self,pos,data):
        length=self.listLength()
        if pos >length or pos<0:
            return None
        else:
            if pos == 0:
                return self.insert_at_beginning(data)
            else:
                if pos==length:
                    self.insert_at_end(data)
                else:
                    new_node=Node()
                    new_node.setData(data)
                    current=self.head
                    count=0
                    while count<pos-1:
                        count += 1
                        current=current.getNext()
                    new_node.setNext(current.getNext())
                    current.setNext(new_node)

    def delete_at_beginning(self):
        length=self.listLength()
        if length > 0:
            self.head=self.head.getNext()

    def delete_at_end(self):
        length=self.listLength()
        if length > 0:
            currentnode=self.head
            previousnode=self.head
            while currentnode.getNext()!=None:
                previousnode=currentnode
                currentnode=currentnode.getNext()
            previousnode.setNext(None)

    def delete_at_position(self,pos):
        length=self.listLength()
        if pos==0:
            return delete_at_beginning()
        if pos==length:
            return delete_at_end()
        else:
            currentnode=self.head
            previousnode=self.head
            count=0
            while count<pos-1:
                count += 1
                previousnode=currentnode
                currentnode=currentnode.getNext()
            previousnode.setNext(currentnode.getNext())
            currentnode.setNext(None)

    def printList(self):
        current=self.head
        while current!=None:
                print current.getData()
                current=current.getNext()





