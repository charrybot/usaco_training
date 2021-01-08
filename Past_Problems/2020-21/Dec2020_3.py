N = int(input(""))
cow_directions = []
current_loc = []
cow_locations = []
cow_steps = {}

for i in range(N):
    direc, x, y = input("").split()
    x = int(x)
    y = int(y)
    # current location of cow
    current_loc.append(x)
    current_loc.append(y)
    # accumulative locations of cow
    cow_locations.append((x, y))
    # direction of cow
    cow_directions.append(direc)
    # steps
    cow_steps[i] = 1

step_end = {}
for i in range(100):
    for n in range(N):
        if 2*n+1 <= len(current_loc):
            cur_x = current_loc[2*n]
            cur_y = current_loc[2*n+1]
            if cow_directions[n] == "E":
                cur_x += 1
                if (cur_x, cur_y) in (cow_locations[-6:-1] or cow_locations[-1]):
                    cow_locations.append((cur_x, cur_y))
                    cow_steps[n] += 1
                    current_loc[2 * n] = cur_x
                elif (cur_x, cur_y) in cow_locations:
                    step_end[n] = cow_steps[n]
                else:
                    cow_locations.append((cur_x, cur_y))
                    cow_steps[n] += 1
                    current_loc[2*n] = cur_x
            else:
                cur_y += 1
                if (cur_x, cur_y) in (cow_locations[-6:-1] or cow_locations[-1]):
                    cow_locations.append((cur_x, cur_y))
                    cow_steps[n] += 1
                    current_loc[2*n+1] = cur_y
                elif (cur_x, cur_y) in cow_locations:
                    step_end[n] = cow_steps[n]
                else:
                    cow_locations.append((cur_x, cur_y))
                    cow_steps[n] += 1
                    current_loc[2*n+1] = cur_y

for i in range(N):
    try:
        print(step_end[i])
    except KeyError:
        print("Infinity")
# 2n, 2n+1 --- 2n+1 <= len(cow_locations)


