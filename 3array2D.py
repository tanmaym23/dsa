import numpy as np

arr1=np.array([[1,2,3,4],[5,6,7,8],[11,12,13,14],[15,16,17,18]])
print(arr1)

newArr=np.insert(arr1,0,[[99,98,97,96]],axis=0) #TO ADD NEW ROW
print(newArr)
newArr=np.insert(arr1,0,[[99,98,97,96]],axis=1) #TO ADD NEW COLUMN
print(newArr)
# (ARRAY NAME,WHERE TO ADFD NEW ROW/COLUMN, WHAT TO ADD, ROW/COLUMN)

newarr=np.append(arr1,[[50,61,52,53]],axis=0)
print(newarr)

def accessElement(array,rowIndex,columnIndex):
    if rowIndex>=len(array) and columnIndex>=len(array[0]):
        # ....(TO ACCESS ROWS)............(TO ACCESS COLUMNS)
        print("invalid index")
    else:
        print("your element:",array[rowIndex][columnIndex])
e1=accessElement(arr1,2,3)

# def traverse(array):
#     for i in range(len(array)):
#         for j in range(len(array[0])):
#             print(array[i][j])
# traverse(arr1)

def Lsearch(array,element):
    for i in range(len(array)):
        for j in range(len(array[0])):
            if array[i][j]==element:
                print("element found at index:",i,j)
    print("element not found")
Lsearch(arr1,4)

dltAry=np.delete(arr1,1,axis=0) #OR AXIS=1 TO DLT COLUMN
print(dltAry)
