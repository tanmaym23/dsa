# def linear_Search(list1, n, key):  
  
#     # Searching list1 sequentially  
#     for i in range(0, n):  
#         if (list1[i] == key):  
#             return i  
#     return -1  
  
  
# list1 = [1 ,3, 5, 4, 7, 9]  
# key = 7  
  
# n = len(list1)  
# res = linear_Search(list1, n, key)  
# def linear_Search(list1, n, key):  
  
#     # Searching list1 sequentially  
#     for i in range(0, n):  
#         if (list1[i] == key):  
#             return i  
#     return -1  
  
  
# list1 = [1 ,3, 5, 4, 7, 9]  
# key = 7  
  
# n = len(list1)  
# res = linear_Search(list1, n, key)  
# if(res == -1):  
#     print("Element not found")  
# else:  
#     print("Element found at index: ", res)


def locate_card(cards, query):
    position=0
    while position<len(cards):
        if cards[position]==query:
            return position
        position+=1
    return -1

card = [13, 11, 10, 7, 4, 3, 1, 0]
query =3
qwe=locate_card(card,query)
if(qwe == -1):  
    print("Element not found")  
else:  
    print("Element found at index: ", qwe)  