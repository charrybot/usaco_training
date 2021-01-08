import random

number = random.randint(1, 100)


def guess(number, count):
    """number is random, count is user input"""
    for i in range(count):
        user = int(input("guess a number"))
        if user > number:
            print("number is smaller")
        elif user < number:
            print("number is bigger")
        else:
            print("you got the answer")
            break

number_list = []

for i in range(100):
    num = int(random.randint(1, 100))
    number_list.append(num)
    number_list.sort()
    if i == 99:
        print(number_list)

if 61 in number_list:
    print("yes")
else:
    print("no")


# using binary search
def find_number(number_list, number):
    if len(number_list) == 0:
        print("we have a problem")
    if len(number_list) == 1:
        return number_list[0] == number
    elif len(number_list) == 2:
        return number_list[0] == number or number_list[1] == number
    middle = len(number_list)//2
    mid_number = number_list[middle]
    if number > mid_number:
        new_list = number_list[middle+1:]
        return find_number(new_list, number)
    elif number < mid_number:
        new_list = number_list[:middle-1]
        return find_number(new_list, number)
    else:
        return True

# define condition where it breaks








