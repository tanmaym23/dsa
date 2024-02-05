# # 1. number of days above the average temp
# numDays=int(input("enter number of days: "))
# total=0
# temp=[]
# for i in range (numDays):
#     nextDay= int(input("enter day "+str(i+1)+ "'s high temp: "))
#     temp.append(nextDay)
#     total += temp[i]
# avg=round(total/numDays,2)
# print("average: ", avg)

# above=0
# for i in temp:
#     if i>avg:
#         above+=1
# print(str(above)+" days above avg temp")

# # 2. missing number
# my_list=[1,2,3,4,5,7,8,9,10]
# def missingNum(list,n):
#     sum1=(n*(n+1))/2
#     sum2=sum(list)
#     miss_no=sum1-sum2
#     print("missing number is"+str(miss_no))

# missingNum(my_list,10)

# # 3. find distinct pairs thaat sum sum to target number
def pairs(list,target):
    for i in range (len(list)):
        for j in range (i+1,len(list)):
            if list[i]==list[j]:
                continue
            elif list[i]+list[j]==target:
                print (i,j)

# mylist=[1,2,3,2,3,4,5,6]
# pairs(mylist,7)

# # 4. find if number is there in array or not
import numpy as np

# def checkNum(arr,target):
#     for i in range(len(arr)):
#         if arr[i]==target:
#             print(i)

# myArr=np.array([1,2,3,4,5,6,7,8,9,10]) 
# checkNum(myArr,8)

# # 5. find max product of two integers in an array where all numberds are positive
# def maxProduct(arr):
#     max=0
#     for i in range (len(arr)):
#         for j in range(i+1,len(arr)):
#             if arr[i]*arr[j]>max:
#                 max=arr[i]*arr[j]
#                 pairs=str(arr[i])+","+str(arr[j])
#     print(max)
#     print(pairs)

# myArr=np.array([1,2,3,4,5,6,7,8,9])
# maxProduct(myArr)

# 6. find if all hnumbers in ana array are unique or not
# def unique(list):
#     for i in list:
#         for j in range (i+1,len(list)):
#             if list[i]==list[j]:
#                 print("numbers are not unique")

# def unique(list):
#     a=[]
#     for i in list:
#         if i in a:
#             print(i)
#             return False
#         else:
#             a.append(i)
#     return True

# my_list=[1,2,3,4,5,8,4,9,10]
# unique(my_list)
 