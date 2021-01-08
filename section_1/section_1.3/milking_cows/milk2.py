"""
LANG: PYTHON3
PROG: milk2
"""
# f_in = open("/Users/harold/usaco_training/section_1/section_1.3/milking_cows/milk2.in", "r")
f_in = open("milk2.in", "r")
f_out = open("milk2.out", "w")

contents = f_in.readlines()
N = int(contents[0].rstrip())

dict = {}
start_time = []
end_time = []
farmer_time = []
# for loop over N farmers
for farmer in range(1, N+1):
    start, end = (contents[farmer].rstrip()).split()
    start = int(start)
    end = int(end)
    farmer_time.append(end-start)
    start_time.append(start)
    end_time.append(end)
    dict[farmer] = [start, end]


# calculating continuous
if N == 1:
    continuous = dict[1][1] - dict[1][0]
elif N > 1:
    number = 1
    while dict[number+1][0] <= dict[number][1]:
        number += 1
    continuous = dict[number][1] - dict[1][0]

if max(farmer_time) >= continuous:
    continuous = max(farmer_time)


# calculating missing
if N == 1:
    time_missing = 0
elif N > 1:
    list = []
    for farmer_num in range(1, N):
        if dict[farmer_num+1][0] > dict[farmer_num][1]:
            list.append(dict[farmer_num+1][0] - dict[farmer_num][1])
    time_missing = max(list)

time_range = max(end_time) - min(start_time)


f_out.write("{} {}\n".format(continuous, time_missing))

f_in.close()
f_out.close()



