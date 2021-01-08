f_in = open("paint.in", "r")
f_out = open("paint.out", "w")

contents = f_in.readlines()
a, b = map(int, contents[0].rstrip().split())
c, d = map(int, contents[1].rstrip().split())

total = (b-a) + (d-c)
intersection = max(min(b, d)-max(a, c), 0)
answer = total - intersection

f_out.write(str(answer))

f_in.close()
f_out.close()


