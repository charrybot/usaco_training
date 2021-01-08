f_in = open("mowing.in", "r")
f_out = open("mowing.out", "w")

contents = f_in.readlines()
N = int(contents[0].rstrip())

possible_xs = []
"""Don't use coordinate system just have a variable x and y to record position"""








def move(list_of_coordinates, direction, steps, time):
    global possible_xs
    current = list_of_coordinates[-1]
    current_x = current[0]
    current_y = current[1]
    move_result = []
    x = 0
    y = 0
    if direction == "N":
        for movement in range(1, steps+1):
            y += current_y + movement
            time += 1
            if (current_x, y) in list_of_coordinates:
                possible_xs.append(time - (list_of_coordinates.index((current_x, y))+1))
            move_result.append((current_x, y))
    elif direction == "S":
        for movement in range(1, steps+1):
            y += current_y - movement
            time += 1
            if (current_x, y) in list_of_coordinates:
                possible_xs.append(time - (list_of_coordinates.index((current_x, y))+1))
            move_result.append((current_x, y))
    elif direction == "E":
        for movement in range(1, steps+1):
            x += current_x + movement
            time += 1
            if (x, current_y) in list_of_coordinates:
                possible_xs.append(time - (list_of_coordinates.index((x, current_y))+1))
            move_result.append((x, current_y))
    elif direction == "W":
        for movement in range(1, steps+1):
            x += current_x - movement
            time += 1
            if (x, current_y) in list_of_coordinates:
                possible_xs.append(time - (list_of_coordinates.index((x, current_y))+1))
            move_result.append((x, current_y))

    coordinates = list_of_coordinates + move_result
    return coordinates, time


coordinates = [(0,0)]
t = 0

for line in range(1, N+1):
    direction, steps = contents[line].rstrip().split()
    steps = int(steps)
    coordinates, t = move(coordinates, direction, steps, t)

if len(possible_xs) == 0:
    answer = -1
else:
    answer = max(possible_xs)

f_out.write(str(answer))

f_in.close()
f_out.close()


