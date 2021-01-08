q, w, e, r, t, y, u = map(int, input("").split())

A_B_C = max(q, w, e, r, t, y, u) # == A+B+C
A = min(q, w, e, r, t, y, u) # == A
B_C = max(q, w, e, r, t, y, u) - min(q, w, e, r, t, y, u) # == B+C
number_list = [q, w, e, r, t, y, u]
number_list.sort()
A_C = number_list[-3] # == A+C
C = B_C + A_C - A_B_C
B = A_B_C - A - C

print("{} {} {}".format(A, B, C))
