__author__ = 'Akshay Kumar'

def selection_sort(a):                      // selection_sort function declaration 
    for i in range(len(a)):
        least=i
        for k in range(i+1,len(a)):
            if a[k]<a[least]:               //change the logical operator to shift from asec to desc
                least=k
        swap(a,least,i)

def swap(a,x,y):                            //  swap function to swap the elements in the list
    temp=a[x]
    a[x]=a[y]
    a[y]=temp

if __name__=='__main__':
     a=[19,0,25,1,6,34,64,123,5,665]        // list to be sorted    
     selection_sort(a)
     print(a)                               // printing the sorted list

