# # def linear_Search(list1, n, key):  
  
# #     # Searching list1 sequentially  
# #     for i in range(0, n):  
# #         if (list1[i] == key):  
# #             return i  
# #     return -1  
  
  
# # list1 = [1 ,3, 5, 4, 7, 9]  
# # key = 7  
  
# # n = len(list1)  
# # res = linear_Search(list1, n, key)  
# # def linear_Search(list1, n, key):  
  
# #     # Searching list1 sequentially  
# #     for i in range(0, n):  
# #         if (list1[i] == key):  
# #             return i  
# #     return -1  
  
  
# # list1 = [1 ,3, 5, 4, 7, 9]  
# # key = 7  
  
# # n = len(list1)  
# # res = linear_Search(list1, n, key)  
# # if(res == -1):  
# #     print("Element not found")  
# # else:  
# #     print("Element found at index: ", res)


# class node:
#     def __init__(self,value=None):
#         self.value=value
#         self.next=None

# class linklist:
#     def __init__(self):
#         self.head=None
#         self.tail=None

#     def __iter__(self):
#         node=self.head
#         while node:
#             yield node
#             node=node.next

#     def insertion(self,value,location):
#         newnode=node(value)
#         if self.head is None:
#             self.head=newnode
#             self.tail=newnode
#         else:
#             if location==0:
#                 newnode.next=self.head
#                 self.head=newnode
#             # elif location==1:
#             #     newnode.next=None
#             #     self.tail.next=newnode
#             #     self.tail=newnode
#             else:
#                 temp=self.head
#                 index=0
#                 while index<location-1:
#                     temp=temp.next 
#                     index += 1
#                 nextnode=temp.next
#                 temp.next=newnode
#                 newnode.next=nextnode

# ll=linklist()
# # node1=node(0)
# # node2=node(10)
# # node3=node(20)

# # ll.head=node1
# # ll.head.next=node2
# # node2.next=node3
# # ll.tail=node3

# ll.insertion(0.1,0)
# ll.insertion(30,1)
# ll.insertion(50,2)

# print([node.value for node in ll])
x = range(3, 20, 2)

for n in x:
    print(n)
