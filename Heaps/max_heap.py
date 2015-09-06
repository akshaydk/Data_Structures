__author__ = 'Akshay Kumar'

class heap:
    def __init__(self):
        self.heaplist=[]
        self.size=0

    def parent(self,index):
        return index/2

    def left_child(self,index):
        return 2*index+1

    def reight_child(self,index):
        return 2*index+2

    def max_chld(self):
        if self.size==0:
            return -1
        else:
            return self.heaplist[0]

    def percolate_down(self,index):
        while (index*2)+1 <= self.size-1:
            maximum_child=self.max_child(index)
            if self.heaplist[index] < self.heaplist[maximum_child]:
                tmp=self.heaplist[index]
                self.heaplist[index]=self.heaplist[maximum_child]
                self.heaplist[maximum_child]=tmp
            index=maximum_child

    def max_child(self,index):
        if 2*index+2 > self.size-1:
            return 2*index+1
        else:
            if self.heaplist[2*index + 1] > self.heaplist[2*index + 2]:
                return 2*index + 1
            else:
                return 2*index+2

    def percolate_up(self,index):
        while index//2 > 0:
            if self.heaplist[index-1] > self.heaplist[(index // 2)-1]:
                tmp=self.heaplist[index-1]
                self.heaplist[index-1]=self.heaplist[(index // 2)-1]
                self.heaplist[(index // 2)-1]=tmp
            index= index // 2

    def insert_element(self,data):
        self.heaplist.append(data)
        self.size+=1
        self.percolate_up(self.size)

    def delete_max(self):
        retval=self.heaplist[0]
        self.heaplist[0]=self.heaplist[self.size-1]
        self.size= self.size-1
        self.heaplist.pop()
        self.percolate_down(0)
        return retval


    def print_heap(self):
        print self.heaplist

if __name__=='__main__':
    new_heap=heap()
    new_heap.insert_element(31)
    new_heap.insert_element(10)
    new_heap.insert_element(16)
    new_heap.insert_element(9)
    new_heap.insert_element(8)
    new_heap.insert_element(14)
    new_heap.insert_element(12)
    new_heap.insert_element(3)
    new_heap.insert_element(1)
    new_heap.insert_element(5)
    new_heap.insert_element(7)
    new_heap.insert_element(19)
    new_heap.delete_max()
    new_heap.print_heap()

    