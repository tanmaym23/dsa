from array import *

arr1=array('i',[1,2,3,4,5])
arr2=array('d',[1.1,1.2,1.3])

print(arr1)
print(arr2)
arr1.insert(5,6)
arr1.insert(0,0)
print(arr1)

def traverse(array):
    for i in array:
        print(arr1)
traverse(arr1)

def accessElelent(array,index):
    if index>=len(array):
        print("no element in array")
    else:
        print("element:",array[index]) 
accessElelent(arr1,1)
print("......................")
accessElelent(arr2,3)

def search(array,value):
    for i in array:
        if i==value:
            return array.index(value)
    return "element doesnt exist"
e1=search(arr1,3)
print(e1)

arr1.remove(5)
print(arr1)