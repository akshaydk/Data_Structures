__author__ = 'Akshay Kumar'

def bubble_sort(a):                             //bubble_sort function declaration for sorting the data in ascending order
    for i in range(len(a)):     
        for k in range(len(a)-1,i,-1):
            if(a[k]<a[k-1]):                    // changing the logical operator will change the order form asec/decs
                swap(a,k,k-1)

def swap(a,x,y):                                // swap funtion that swap to data values in given list
    temp=a[x]
    a[x]=a[y]
    a[y]=temp

if __name__=='__main__':
    a=[19,0,25,1,6,34,64,123,5,665]     // creating a list in python 
    bubble_sort(a)                      // calling the bubble sort function
    print(a)                            // printing
