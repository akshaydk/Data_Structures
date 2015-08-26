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

    def print_tree_preorder(self,node):
        while(node.get_data()!=None):
            print node.get_data()
            if(node.left_node()!=None):
                self.print_tree_preorder(node.left_node())
            else:
                return
            if(node.right_node()!=None):
                self.print_tree_preorder(node.right_node())
            else:
                return

            return

    def print_tree_inorder(self,node):
        while(node.get_data()!=None):
            if(node.left_node()!=None):
                self.print_tree_inorder(node.left_node())
                print node.get_data()
            else:
                print node.get_data()
                return
            if(node.right_node()!=None):
                self.print_tree_inorder(node.right_node())
            else:
                return

            return

    def print_tree_postorder(self,node):
        while(node.get_data()!=None):
            if(node.left_node()!=None):
                self.print_tree_postorder(node.left_node())
            else:
                print node.get_data()
                return
            if(node.right_node()!=None):
                self.print_tree_postorder(node.right_node())
            else:
                print node.get_data()
                return
            print(node.get_data())
            return

    def find_max_value(self,node,max_value):
         while(node.get_data()!=None):
             if(node.left_node()!=None):
                 self.find_max_value(node.left_node(),max_value)
                 if node.get_data() > max_value:
                     max_value=node.get_data()

             else:
                 if node.get_data() > max_value:
                     max_value = node.get_data()

             if(node.right_node()!=None):
                 self.find_max_value(node.right_node(),max_value)
                 if node.get_data() > max_value:
                     max_value=node.get_data()

             else:
                 if node.get_data() > max_value:
                     max_value=node.get_data()
             return max_value
         print max_value


if __name__=='__main__':
    new_tree=binary_tree()
    node = new_tree.create_root(1)
    new_tree.insert_element(node,2)
    new_tree.insert_element(node,3)

    max_value=0
    val = new_tree.find_max_value(node,max_value)
    print val


