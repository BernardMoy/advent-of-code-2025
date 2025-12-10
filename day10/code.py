with open('input.txt', 'r') as f: 
    lines = f.read().split('\n')[:-1]
from itertools import combinations
import numpy as np 

# [.###.#] (0,1,2,3,4) (0,3,4) (0,1,2,4,5) (1,2)
# (0,3,4) (0,1,2,4,5)
arr = [] 
for line in lines: 
    pattern = [0 if x == '.' else 1 for x in line.split(' ')[0][1:-1]]
    pairs = [tuple(map(int, item.strip("()").split(","))) for item in line.split(' ')[1:-1]]
    num_list = [int(x) for x in line.split(' ')[-1].strip('{}').split(',')] 

    # Convert the target pattern into masks 
    target = 0
    for b in pattern:
        target= (target << 1) | b

    cur = float('inf')
    for i in range(len(pairs)+1): 
        subsets = combinations(pairs, i) 
        
        for subset in subsets: 
            initial = 0 
            step = 0 
            for group in subset: 
                for pos in group: 
                    initial ^= (1<<(len(pattern)-1-pos))  # XOR to flip. << start from the right side
                step += 1 
            
            if initial == target: 
                cur = min(cur, step) 
    
    arr.append(cur) 




    # # Build a weight matrix for the system of linear equations 
    # A = [] 
    # N = len(num_list) 

    # for pair in pairs: 
    #     # if the pair increases a certain index, set the entry to 1 
    #     A.append([1 if i in pair else 0 for i in range(N)])

    # A = np.array(A).T
    # C = np.array(num_list) 

    # print(A.shape, C.shape) 
    # x = np.linalg.lstsq(A, C, rcond=None)[0]
    # print(x) 


print(sum(arr))

