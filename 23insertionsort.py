#  time complexity O(n2)
# space complexity O(1)

def insertionSort(list):
    for i in range(1,len(list)):
        key=list[i]
        j=i-1
        while j>=0 and key<list[j]:
            list[j+1]=list[j]
            j-=1
        list[j+1]=key
    print(list)        

custom_list=[4,5,3,1,2]
insertionSort(custom_list)