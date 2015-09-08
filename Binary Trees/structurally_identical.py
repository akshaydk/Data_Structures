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

    def struct_identical(self,node1,node2):
            if (node1.left_node()!=None and node2.left_node()==None) or (node1.left_node()==None and node2.left_node()!=None) or \
                (node1.right_node()!=None and node2.right_node()==None) or (node1.right_node()==None and node2.right_node()!=None) or \
                (node1.get_data() != node2.get_data()):
                   return False
            if (node1.left_node()==None and node2.left_node()==None) or (node1.right_node()==None and node2.right_node()==None):
                return True
            if (node1.left_node()!=None and node2.left_node()!=None):
                left=self.struct_identical(node1.left_node(),node2.left_node())
            if (node1.right_node()!=None and node2.right_node()!=None) :
                right=self.struct_identical(node1.right_node(),node2.right_node())
            return left and right

if __name__=='__main__':
    new_tree=binary_tree()
    node1 = new_tree.create_root(1)
    new_tree.insert_element(node1,2)
    new_tree.insert_element(node1,3)
    new_tree.insert_element(node1,4)
    new_tree.insert_element(node1,5)

    node2 = new_tree.create_root(1)
    new_tree.insert_element(node2,2)
    new_tree.insert_element(node2,3)
    new_tree.insert_element(node2,4)

    value=new_tree.struct_identical(node1,node2)
    if value==False:
        print 'not identical'
    else:
        print 'idenitcal'




