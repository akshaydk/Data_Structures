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


    def find_count(self,node):
        if node is None:
            return 0
        my_list=[]
        count=0
        my_list.append(node)
        while len(my_list)!=0:
            element=my_list.pop()
            count +=1
            if(element.left_node()!=None):
                my_list.append(element.left_node())
            if(element.right_node()!=None):
                my_list.append(element.right_node())
        return count
if __name__=='__main__':
    new_tree=binary_tree()
    node = new_tree.create_root(1)
    new_tree.insert_element(node,30)
    new_tree.insert_element(node,80)
    new_tree.insert_element(node,4)
    new_tree.insert_element(node,45)
    new_tree.insert_element(node,51)
    new_tree.insert_element(node,60)
    value = new_tree.find_count(node)
    print value
