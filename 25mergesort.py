# time complexity O(NlogN)
#  space complexity O(n)

def merge(list, l, m, r): #left , middle, right
    n1=m-l+1 #first sub array
    n2=r-m #second sub array

    # two temp. arrays based on number of elements of n1 and n2
    L=[0]*(n1)
    R=[0]*(n2)

    #adding elements of n1 and n2 to L and R
    for i in range (0,n1):
        L[i]=list[l+i]

    for j in range (0,n2):
        R[j]=list[m+1+j]

    # merging back both temp arrays into a single list in sorted order
    i=0
    j=0
    k=l
    while i<n1 and j<n2:
        if L[i]<=R[j]:
            list[k]=L[i]
            i+=1
        else:
            list[k]=R[j]
            j+=1
        k+=1
    while i<n1:
        list[k]=L[i]
        i+=1
        k+=1
    while j<n2:
        list[k]=R[j]
        j+=1
        k+=1

def mergeSort(list,l,r):
    if l<r:
        m=(l+(r-1))//2
        mergeSort(list,l,m)
        mergeSort(list,m+1,r)
        merge(list,l,m,r)
    return(list)

custom_list=[2,5,1,8,3,7,4,6]
print(mergeSort(custom_list,0,7)) 