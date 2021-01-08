f_in = open("cbarn.in", "r")
f_out = open("cbarn.out", "w")

contents = f_in.readlines()

n = int(contents[0].rstrip())
rooms = []

for i in range(1, len(contents)):
    num_of_cows = int(contents[i].rstrip())
    rooms.append(num_of_cows)

distance_traveled = []
# nested for loop
for trials in range(n):
    result = 0
    for cow_constant in range(n):
        steps = (trials + cow_constant) % n
        result += (cow_constant * rooms[steps])
    distance_traveled.append(result)

answer = min(distance_traveled)

f_out.write(str(answer))

f_in.close()
f_out.close()



