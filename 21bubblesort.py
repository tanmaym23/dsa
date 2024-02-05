# time complexity=O(n2)
# space =O(1)
# trtaversing through each elememt and sort it. last element sorted first. no extra space required.

def bubbleSort(list):
    for i in range(len(list)-1):
        for j in range(len(list)-i-1):
            if list[j]>list[j+1]:
                list[j],list[j+1]=list[j+1],list[j]
    print (list)

custom_list=[2,5,1,8,3,7,4,6]
bubbleSort(custom_list)