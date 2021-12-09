# from collections import Counter 
import numpy as np
from scipy.ndimage import measurements

# Part 1
with open('day9-input.txt', 'r', encoding='utf-8') as file:
    # arr = [line.strip().split() for line in file]
    arr = [[i for i in line.strip()] for line in file]
    
mins_list = []
mins_pos = []

# A cumbersome method to traverse in the maze, but i like maze traversing so here's my solution
for i in range(len(arr)): # i:row, j:col
    for j in range(len(arr[0])):
        # print('row',i,'col',j)
        if i-1 < 0 and j-1 < 0:
            if arr[i][j] < arr[i+1][j] and arr[i][j] < arr[i][j+1]:
                mins_list.append(int(arr[i][j]))
                mins_pos.append([i,j])
        elif i-1 < 0 and j+1 > len(arr[0])-1:
            if arr[i][j] < arr[i+1][j] and arr[i][j] < arr[i][j-1]:
                mins_list.append(int(arr[i][j]))
                mins_pos.append([i,j])
        elif i+1 > len(arr)-1 and j+1 > len(arr[0])-1:
            if arr[i][j] < arr[i-1][j] and arr[i][j] < arr[i][j-1]:
                mins_list.append(int(arr[i][j]))
                mins_pos.append([i,j])
        elif i-1 < 0:
            if arr[i][j] < arr[i+1][j] and arr[i][j] < arr[i][j+1] and arr[i][j] < arr[i][j-1]:
                mins_list.append(int(arr[i][j]))
                mins_pos.append([i,j])
        elif i+1 > len(arr)-1:
            if arr[i][j] < arr[i-1][j] and arr[i][j] < arr[i][j+1] and arr[i][j] < arr[i][j-1]:
                mins_list.append(int(arr[i][j]))
                mins_pos.append([i,j])
        elif j-1 < 0:
            if arr[i][j] < arr[i+1][j] and arr[i][j] < arr[i][j+1] and arr[i][j] < arr[i-1][j]:
                mins_list.append(int(arr[i][j]))
                mins_pos.append([i,j])
        elif j+1 > len(arr[0])-1:
            if arr[i][j] < arr[i-1][j] and arr[i][j] < arr[i+1][j] and arr[i][j] < arr[i][j-1]:
                mins_list.append(int(arr[i][j]))
                mins_pos.append([i,j])
        else:
            if arr[i][j] < arr[i-1][j] and arr[i][j] < arr[i+1][j] and arr[i][j] < arr[i][j-1] and arr[i][j] < arr[i][j+1]:
                mins_list.append(int(arr[i][j]))
                mins_pos.append([i,j])
        
        
print('Part 1:', sum(mins_list)+len(mins_list)*1)

# Part 2: basically cheating because rules implied that basins are surrounded by 9s. So get the input to np array and convert to 9s and non-9s

# read the data as str and then make some god awful operations to have a nice array
data = np.loadtxt('day9-input.txt',dtype=str)
data = np.array([np.array(list(i)) for i in data]).astype(int)
data = np.pad(data,pad_width=1,constant_values=9)

data[data != 9] = 1 # non 9s
data[data == 9] = 0 # 9s
              
lw, num = measurements.label(data) # again cheating with using scipy methods and labeling basins
area = measurements.sum(data, lw, index=np.arange(lw.max() + 1)) # sum everything
print('Part 2:', int(np.product(np.sort(area)[-3:]))) # and get the product
                