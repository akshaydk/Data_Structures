__author__ = 'Akshay'

class Node():

    def __init__(self):
        self.data = None
        self.next = None

    def get_data(self):
        return self.data

    def set_data(self,data):
        self.data = data

    def get_next(self):
        return self.next

    def set_next(self,next):
        self.next = next


class queue():

    def __init__(self):
        self.head= None

    def enqueue(self,data):
        new_node=Node()
        if(self.head==None):
            new_node.set_data(data)
            self.head=new_node
            new_node.set_next(None)
        else:
            new_node.set_data(data)
            current=self.head
            while current.get_next()!=None:
                current=current.get_next()
            current.set_next(new_node)
            new_node.set_next(None)

    def queue_length(self):
        current=self.head
        count=0
        while current!=None:
            count=count+1
            current=current.get_next()
        return count

    def is_empty(self):
        current=self.head
        count=0
        while current!=None:
            count=count+1
            current=current.get_next()
        if count==0:
            return True


    def dequeue(self):
        length=self.queue_length()
        if length > 0:
            temp=self.head.get_data()
            self.head=self.head.get_next()
            return temp


    def print_queue(self):
        current=self.head
        while current!=None:
                print current.get_data()
                current=current.get_next()








