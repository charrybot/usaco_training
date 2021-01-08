f_in = open("speeding.in", "r")
f_out = open("speeding.out", "w")

contents = f_in.readlines()
N, M = contents[0].split() # N is road, M is Bessie the cow
N = int(N)
M = int(M)

speed_limit = []
for i in range(1, N+1):
    l, s = contents[i].split()
    l = int(l)
    s = int(s)
    for i in range(l):
        speed_limit.append(s)

bessie_speed = []
for i in range(N+1, N+M+1):
    l, s = contents[i].split()
    l = int(l)
    s = int(s)
    for i in range(l):
        bessie_speed.append(s)

# calculating
speed_difference = []
for minute in range(100):
    speed_difference.append(bessie_speed[minute]-speed_limit[minute])

answer = max(speed_difference)
if answer < 0:
    answer = 0

f_out.write(str(answer) + "\n")

f_in.close()
f_out.close()











