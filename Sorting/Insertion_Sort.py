__author__ = 'Akshay Kumar'

def insertion_sort(a):
    for i in range(1,len(a)):
        temp=a[i]
        k=i
        while k>0 and temp<a[k-1]:
            a[k]=a[k-1]
            k=k-1
        a[k]=temp

if __name__=='__main__':
     a=[1,2,3,4,5]
     insertion_sort(a)
     print(a)