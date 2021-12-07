# Part 1
# crab_pos = [16,1,2,0,4,2,7,1,2,14]
with open('day7-input.txt', 'r', encoding='utf-8') as file:
    inputList = [int(line) for line in  file.read().split(',')]
crab_pos = inputList[:]

fuelList=[]
for pos in crab_pos:
    fuel = 0
    for crab in crab_pos:
        fuel += abs(pos-crab)
    fuelList.append(fuel)
print('Part 1:', min(fuelList))

# Part 2
print('Part 2:',min(sum(sum(range(1, abs(crab - i) + 1)) for crab in crab_pos) for i in range(min(crab_pos), max(crab_pos))))
