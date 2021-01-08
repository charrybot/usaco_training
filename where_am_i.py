import re
f_in = open("whereami.in", "r")
f_out = open("whereami.out", "w")
contents = f_in.readlines()
N = int(contents[0].rstrip())
Sequence = str(contents[0].rstrip())

set = set()
unique = []
# finding unique letters
for alphabet in Sequence:
    set.add(alphabet)
for element in set:
    unique.append(element)


def check_same(list_of_str):
    """takes a list of str and returns true if some are the same"""
    for i in range(len(list_of_str)):
        new_list = list_of_str.pop(i)
        if element[i] in new_list:
            return True
    return False

answers = []
for letter in unique:
    finding = re.finditer(letter, Sequence)
    positions = [letter.start() for letter in finding] # using re module
    subseq_list = [Sequence[x] for x in positions]
    for position in positions:
        k = 1
    while check_same(subseq_list):
        k += 1
        subseq_list = []
        for x in positions:
            if x+k-1 > len(Sequence):
                subseq_list.append(Sequence[x:])
            else:
                subseq_list.append(Sequence[x:x+k])
    answers.append(k)


# search all positions
# Sequence[positions[i]:positions[i] + k]
answer = max(answers)

f_out.write(str(answer)+"\n")

f_in.close()
f_out.close()




