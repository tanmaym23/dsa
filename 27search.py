# LINEAR SEARCH

# time complexity=O(n)
# space =O(1)

def linearSearch(array,value):
    for i in array:
        if array[i]==value:
            return i
    return -1
        
# print(linearSearch([1,2,3,4,5,6],5))


# BINARY SEARCH
# ==> works only on sorted array

# time complexity = O(logN)
# space = O(1)
import math

def binarySearch(array,value):
    start=0
    end=len(array)-1
    middle=math.floor((start+end)/2)

    while array[middle]!=value and start<=end:
        if value<middle:
            end=middle-1
        else :
            start=middle+1
        middle=math.floor((start+end)/2)
    if array[middle]==value:
        return (middle)
    else:
        return -1
    
print(binarySearch([1,2,3,4,5,6],5))

  