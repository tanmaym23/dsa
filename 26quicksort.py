# time complexity O(NlogN)
#  space complexity O(n)

def partition(list,low,high):
    i=low-1 
    pivot=list[high]
    for j in range(low,high):
        if list[j]<=pivot:
            i+=1
            list[i] , list[j]=list[j],list[i]
    
    list[i+1],list[high]= list[high],list[i+1]
    return (i+1)

def quickSort(list,low,high):
    if low<high:
        pi=partition(list,low,high)
        quickSort(list,low,pi-1)
        quickSort(list,pi+1,high)

custom_list=[2,3,1,4,5]
quickSort(custom_list,0,4)
print(custom_list)