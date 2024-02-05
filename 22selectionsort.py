# time complexity : O(n2)
# space complexity : O(1)

def selectionSort(list):
    for i in  range(len(list)):
        min_index=i
        for j in range (i+1,len(list)):
            if list[min_index] > list[j]:
                min_index = j
        list[i] , list[min_index]=list[min_index], list[i]
    print(list)
custom_list=[2,5,1,8,3,7,4,6]
selectionSort(custom_list)