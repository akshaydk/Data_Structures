__author__ = 'Akshay Kumar'

def selection_sort(a):
    for i in range(len(a)):
        least=i
        for k in range(i+1,len(a)):
            if a[k]<a[least]:
                least=k
        swap(a,least,i)

def swap(a,x,y):
    temp=a[x]
    a[x]=a[y]
    a[y]=temp

if __name__=='__main__':
     a=[19,0,25,1,6,34,64,123,5,665]
     selection_sort(a)
     print(a)

