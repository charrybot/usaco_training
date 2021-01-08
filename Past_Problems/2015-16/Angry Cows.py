f_in = open("angry.in", "r")
f_out = open("angry.out", "w")

contents = f_in.readlines()
N = int(contents[0].rstrip())

hay_position = []
for line in range(1, N+1):
    hay = int(contents[line].rstrip())
    hay_position.append(hay)

hay_position.sort()


def count_exploded_right(location):
    ranges = [x for x in range(1, N)]
    count = 0
    for position in hay_position:
        if location < position <= location + range:
            range += 1
            count += 1
            count_exploded_right(position)
        else:
            return count

    return count



for shot in range(1, N+1):
    hays_exploded = []
    hay_target = hay_position[shot]



