__author__ = 'Akshay Kumar'

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


    def search_element(self,node,data):
        if node is None:
            return 0
        if node.get_data()== data:
            return 1
        else:
            temp=self.search_element(node.left_node(),data)
            if temp == 1:
                return temp
            else:
                return self.search_element(node.right_node(),data)

if __name__=='__main__':
    new_tree=binary_tree()
    node = new_tree.create_root(1)
    new_tree.insert_element(node,30)
    new_tree.insert_element(node,80)
    new_tree.insert_element(node,4)
    new_tree.insert_element(node,45)
    new_tree.insert_element(node,51)
    new_tree.insert_element(node,60)
    value = new_tree.search_element(node,100)
    if value==1:
        print 'element found'
    else:
        print 'element not found'


