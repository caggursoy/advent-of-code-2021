with open('day2-input.txt', 'r', encoding='utf-8') as file:
    # inputList = list(map(int, file.readlines()))
    inputList = list(file.readlines())
# Part 1
ver_loc = 0
hor_loc = 0
for inp in inputList:
    # print(inp)
    if 'forward' in inp:
        move = int(inp[inp.find('forward')+8:])
        hor_loc += move
    elif 'down' in inp:
        move = int(inp[inp.find('down')+5:])
        ver_loc += move
    elif 'up' in inp:
        move = int(inp[inp.find('up')+3:])
        ver_loc -= move

print('Part 1:',hor_loc, ver_loc, hor_loc*ver_loc)

# Part 2
ver_loc = 0
hor_loc = 0
aim = 0
for inp in inputList:
    # print(inp)
    if 'forward' in inp:
        move = int(inp[inp.find('forward')+8:])
        hor_loc += move
        ver_loc += aim*move
    elif 'down' in inp:
        move = int(inp[inp.find('down')+5:])
        aim += move
    elif 'up' in inp:
        move = int(inp[inp.find('up')+3:])
        aim -= move
        
print('Part 2:',hor_loc, ver_loc, hor_loc*ver_loc)
