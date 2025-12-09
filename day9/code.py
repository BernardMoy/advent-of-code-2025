with open('input.txt', 'r') as f: 
    lines = f.read().split('\n')[:-1]

pos = [[int(x) for x in line.split(',')] for line in lines]

ans = 0 
for i in range(len(pos)): 
    for j in range(i, len(pos)): 
        first = pos[i] 
        second = pos[j] 
        ans = max(ans, (abs(first[0]-second[0])+1)*(abs(first[1]-second[1])+1))

print(ans)

from shapely import Polygon, Point

# Construct outer polygon that contains all valid spaces 
outer = Polygon(pos) 

# for each pair of pos, generate the 4 corners of the rect 
ans2 = 0 
for i in range(len(pos)): 
    for j in range(i, len(pos)): 
        first = pos[i] 
        second = pos[j] 
        tl = [min(first[0], second[0]), min(first[1], second[1])]
        tr = [max(first[0], second[0]), min(first[1], second[1])]
        bl = [min(first[0], second[0]), max(first[1], second[1])]
        br = [max(first[0], second[0]), max(first[1], second[1])]

        # if all(outer.covers(Point(x[0], x[1])) for x in [tl, tr, bl, br]): 
        #     ans2 = max(ans2, abs(pos[i][0]-pos[j][0]+1)*abs(pos[i][1]-pos[j][1]+1))

        inner = Polygon([tl, tr, br, bl])   # continuous
        if outer.contains(inner):  
            ans2 = max(ans2, (abs(first[0]-second[0])+1)*(abs(first[1]-second[1])+1))


print(ans2)