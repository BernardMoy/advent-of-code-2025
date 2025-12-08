with open('input.txt', 'r') as f: 
    lines = f.read().split('\n')[:-1]

from collections import defaultdict
groups = [] 
t = [] 
pairs = [] 

for line in lines: 
    t.append([int(x) for x in line.split(',')])

for i in range(len(t)): 
    for j in range(i+1, len(t)): 
        pairs.append(((
            (t[j][0]-t[i][0])**2 + (t[j][1]-t[i][1])**2 + (t[j][2]-t[i][2])**2 
        ), 
        (i,j)))

pairs.sort(key = lambda x: x[0])

parent = list(range(len(t)))
size = [1]*len(t) 

# Union find 
def find(x): 
    if parent[x] != x: 
        parent[x] = find(parent[x]) 
    return parent[x] 

def union(a,b): 
    ra = find(a) 
    rb = find(b) 
    if ra == rb: 
        return False  # not merged 
    
    if size[ra] < size[rb]: 
        ra, rb = rb, ra 
    parent[rb] = ra 
    size[ra] += size[rb] 

    # merged 
    return True 

count = 0 
for i in range(1000): 
    dist, tup = pairs[i] 
    a,b = tup 
    union(a,b)

d = defaultdict(int) 
for i in range(len(t)): 
    r = find(i) 
    d[r] += 1 

srt = sorted(d.values(), reverse=True) 
ans = srt[0]*srt[1]*srt[2] 
print(ans)




parent = list(range(len(t)))
size = [1]*len(t) 
ans2 = 0 
# instead of just 1000, merge all pairs
for i in range(len(pairs)): 
    dist, tup = pairs[i] 
    a,b = tup 
    if union(a,b): 
        # Keep track of the last merge occured
        ans2 = (t[a][0]*t[b][0])

print(ans2)