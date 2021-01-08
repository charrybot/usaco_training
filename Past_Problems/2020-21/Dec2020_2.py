N = int(input(""))
flower_list = []

flower_list = [int(x) for x in input("").split()]

"""for flowers in range(N):
    flower = int(input(""))
    flower_list.append(flower)"""

avg_P = round(sum(flower_list)/N)

photos_list = []

for i in range(N):
    for j in range(N):
        tup_list = []
        if 0 <= i <= j <= N:
            for k in range(i, j+1):
                # print("i is {} j is {} k is {}".format(i, j, k))
                if i==j:
                    tup_list.append(flower_list[k])
                    tup_list.append(flower_list[k])
                else:
                    tup_list.append(flower_list[k]) # (1,1)?
            photos_list.append(tuple(tup_list))

count = 0
for photos in range(len(photos_list)):
    if avg_P in photos_list[photos]:
        count += 1

# print(photos_list)

print(count)


