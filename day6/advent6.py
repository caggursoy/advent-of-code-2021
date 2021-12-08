import collections
import numpy as np

fishList=[5,1,1,4,1,1,4,1,1,1,1,1,1,1,
1,1,1,1,4,2,1,1,1,3,5,1,1,1,5,4,1,1,1,2,2,1,1,1,2,1,1,1,2,5,2,1,2,2,3,1,1,1,1,1,1,1,1,5,1,
1,4,1,1,1,5,4,1,1,3,3,2,1,1,1,5,1,1,4,1,1,5,1,1,5,1,2,3,1,5,1,3,2,1,3,1,1,4,1,1,1,1,2,1,2,
1,1,2,1,1,1,4,4,1,5,1,1,3,5,1,1,5,1,4,1,1,1,1,1,1,1,1,1,2,2,3,1,1,1,1,1,2,1,1,1,1,1,1,2,1,1,
1,5,1,1,1,1,4,1,1,1,1,4,1,1,1,1,3,1,2,1,2,1,3,1,3,4,1,1,1,1,1,1,1,5,1,1,1,1,1,1,1,1,4,1,1,2,2,
1,2,4,1,1,3,1,1,1,5,1,3,1,1,1,5,5,1,1,1,1,2,3,4,1,1,1,1,1,1,1,1,1,1,1,1,5,1,4,3,1,1,1,2,1,1,1,1,
1,1,1,1,2,1,1,1,1,1,1,1,1,1,1,1,3,3,1,2,2,1,4,1,5,1,5,1,1,1,1,1,1,1,2,1,1,1,1,1,1,1,1,1,1,1,5,1,
1,1,4,3,1,1,4]

# fishList = [3,4,3,1,2]

# Part 1: Brute Force FTW!!
# day = 1
# part1 = True
# if part1:
#     for day in range(1,257):
#         for i in range(len(fishList)):
#             fish = fishList[i]
#             if fish-1 >= 0:
#                 fishList[i] = fish-1
#             else:
#                 fishList[i] = 6
#                 fishList.append(8)
#         # print(day, len(fishList))
#
#     print('Part 1:', day, len(fishList))

part1 = 80
part2 = 256

# Part 2: Goodbye Brute Force :(

def solver(fishList, part):
    num_fish = np.zeros((9,), dtype=np.longlong) # there're only 9 states 0-8
    fish_arr = np.array(fishList) # convert it to numpy array for convenience
    for i in range(9):
        num_fish[i] = np.count_nonzero(fish_arr == i) # count amount of fish in each state

    for i in range(part):
            new_fish = num_fish[0]
            num_fish[0:8] = num_fish[1:9] # -1 operation, shift one left
            num_fish[6] += new_fish # add new_fish amount of new fish
            num_fish[8] = new_fish # set new_fish amount as this will be reset in every state
    return sum(num_fish)
print('Part 1:', solver(fishList,part1), '\nPart 2:', solver(fishList,part2))
