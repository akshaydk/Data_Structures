__author__ = 'Akshay Kumar'

def bubble_sort(a):
    for i in range(len(a)):
        for k in range(len(a)-1,i,-1):
            if(a[k]<a[k-1]):
                swap(a,k,k-1)

def swap(a,x,y):
    temp=a[x]
    a[x]=a[y]
    a[y]=temp

if __name__=='__main__':
    a=[19,0,25,1,6,34,64,123,5,665]
    bubble_sort(a)
    print(a)
