f_in = open("billboard.in", "r")
f_out = open("billboard.out", "w")

contents = f_in.readlines()

x1, y1, x2, y2 = map(int, contents[0].rstrip().split())
x3, y3, x4, y4 = map(int, contents[1].rstrip().split())

# trying to find x5, y5, x6, y6

# x2, x3
# three cases - not along the edges, outside the bounds,
# case 1 - x1 == x3 and x4 >= x2
# case 2 - x2 == x4 and x3 <= x1
# x3 <= x1 and x4 < x2
# y3 <= y1 and y4 < y2

area_of_cover = (y2-y1) * (x2-x1)

if x3 <= x1 and x4 >= x2: 
    if y3 > y1 and y4 < y2:
        area_of_cover = (y2-y1) * (x2-x1)
    elif y3 <= y1 and y4 >= y2:
        area_of_cover = 0
    elif y3 <= y1 and y1 < y4 < y2:
        area_of_cover = (x2-x1) * (y2-y4)
    elif y2 > y3 > y1 and y4 >= y2:
        area_of_cover = (x2-x1) * (y3-y1)
elif x3 > x1 and x4 < x2:
    area_of_cover = (y2-y1) * (x2-x1)
elif x3 <= x1 and x1 < x4 < x2:
    if y3 > y1 and y4 < y2:
        area_of_cover = (y2-y1) * (x2-x1)
    elif y3 <= y1 and y4 >= y2:
        area_of_cover = (x2-x3) * (y2-y1)
    elif y3 <= y1 and y1 < y4 < y2:
        area_of_cover = (y2-y1) * (x2-x1)
    elif y2 > y3 > y1 and y4 >= y2:
        area_of_cover = (y2-y1) * (x2-x1)  
elif x2 > x3 > x1 and x4 >= x2: 
    if y3 > y1 and y4 < y2:
        area_of_cover = (y2-y1) * (x2-x1)
    elif y3 <= y1 and y4 >= y2:
        area_of_cover = (x3-x1) * (y2-y1)
    elif y3 <= y1 and y1 < y4 < y2:
        area_of_cover = (y2-y1) * (x2-x1)
    elif y2 > y3 > y1 and y4 >= y2:
        area_of_cover = (y2-y1) * (x2-x1)

f_out.write(str(area_of_cover))

f_in.close()
f_out.close()


