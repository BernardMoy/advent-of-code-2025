with open('input.txt', 'r') as f: 
    lines = f.read().split('\n') 

cur = 50 
ans = 0 
ans2 = 0 
for line in lines[:-1]: 
    num = int(line[1::])
    if line[0] == 'L': 
        if cur-num <= 0: 
            ans2 += ((100-cur)%100+num) // 100   # distance to 100 + number 
        cur = (cur-num)%100    # 100 because 99 is possible 
    else:  
        if cur+num > 99: 
            ans2 += (cur+num) // 100
        cur = (cur+num)%100
    if cur == 0: 
        ans += 1 

print(ans) 
print(ans2)