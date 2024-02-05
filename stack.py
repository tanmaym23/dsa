# from collections import deque
from queue import LifoQueue

# # implimentation using list(time complexity is O(n))
# stack=[]
# stack.append("@")
# stack.append(23.25)
# stack.append(23)
# stack.append("tanmay")
# print(stack)
# print(stack.pop())
# print(stack)

# # implimentation using deque(time complexity is O(1)... so it is faster than list and prefered over list)
# stack=deque()
# stack.append("@")
# stack.append(23.25)
# stack.append(23)
# stack.append("tanmay")
# print(stack)
# print(stack.pop())
# print(stack)

# implimentation using queue
# stack=LifoQueue()
# stack.put("@")
# stack.put(2.3)
# stack.put("Tanmay")
# print(stack())
# print(stack.qsize())
# print(stack.full()) #will show false as queue is not full 
# print(stack.get())
# print(stack)