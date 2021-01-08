from collections import *

list = []
for i in range(5):
    list.append(i)

list.pop() # removes or calls last element in list
print(list)

list = []
for i in range(5):
    list.append(i) # adds element to the end of the list

list.pop(0) # removes or calls first element in list
print(list.pop(0))

# pop() method returns the last in first out --> Stacks

queue = deque()


queue.append(1)
queue.pop()


# maps =. python dictionaries


# stack
# push = append
# pop = pop
# peek = list[-1]


# queue
# add = append()
# remove from front = pop(0)
# peek = list[0]



