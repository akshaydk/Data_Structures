__author__ = 'Akshay Kumar'

from queue_lib import queue

class binary_tree_node:

    def __init__(self):
        self.data=None
        self.left=None
        self.right=None

    def get_data(self):
        return self.data

    def set_data(self,data):
        self.data=data

    def left_node(self):
        return self.left

    def right_node(self):
        return self.right

class binary_tree:
    def __init__(self):
         self.root=None

    def create_root(self,data):
         new_node=binary_tree_node()
         new_node.set_data(data)
         self.root=new_node
         return self.root

    def insert_element(self,node,data):
        if(node.left_node()==None):
            new_node=binary_tree_node()
            new_node.set_data(data)
            node.left=new_node
            return

        elif(node.right_node()==None):
            new_node=binary_tree_node()
            new_node.set_data(data)
            node.right=new_node
            return
        else:
            self.insert_element(node.left_node(),data)


    def deepest_node(self,node):
        if node is None:
            return 0
        q=queue()
        q.enqueue(node)
        while q.is_empty()!=True:
            node=q.dequeue()
            if(node.left_node()!=None):
                q.enqueue(node.left_node())
            if(node.right_node()!=None):
                q.enqueue(node.right_node())
        return node.get_data()

if __name__=='__main__':
    new_tree=binary_tree()
    node = new_tree.create_root(1)
    new_tree.insert_element(node,2)
    new_tree.insert_element(node,3)
    new_tree.insert_element(node,4)
    new_tree.insert_element(node,5)
    deepest_node=new_tree.deepest_node(node)
    print 'deepest node is',deepest_node


