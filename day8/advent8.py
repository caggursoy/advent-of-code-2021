# Part 1
# crab_pos = [16,1,2,0,4,2,7,1,2,14]
with open('day8-input.txt', 'r', encoding='utf-8') as file:
    inputList = [(line.strip('\n').split('|')[0], line.strip('\n').split('|')[1]) for line in file.readlines()]

def seg_choose(inp):
    out_seg = -1
    if len(inp) == 2:
        out_seg = 1
    elif len(inp) == 3:
        out_seg = 7
    elif len(inp) == 4:
        out_seg = 4
    elif len(inp) == 7:
        out_seg = 8
    elif len(inp) == 1:
        out_seg = -1
    else: #  len = 5&6
        out_seg = -2
    
    return out_seg

def unique_chars(str1, str2):
    # a_set = set(list(str1))
    # b_set = set(list(str2))
    return ''.join(map(str, list(set(list(str1)) - set(list(str2)))))

# def seg_loc(segments_list):
#     segments = [0,0,0,0,0,0,0]
#     for seg in segments_list:
#         if seg[1] == 1:
            

# inputList = inputList[0]
segments_list = []

for input in inputList:
    input = inputList[0]
    print(input)
    for inp in input:
        for i in inp.split(' '):
            # print(i, seg_choose(i))
            if seg_choose(i) > 0:
                segments_list.append((i, seg_choose(i)))
    break
        
print(segments_list)

for i in range(len(segments_list)-1):
    print(segments_list[i][0],'=',segments_list[i][1], segments_list[i+1][0],'=',segments_list[i+1][1],'uniques:', unique_chars(segments_list[i][0], segments_list[i+1][0]))
    
    