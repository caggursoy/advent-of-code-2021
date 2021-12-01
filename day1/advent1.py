with open('day1-input.txt', 'r', encoding='utf-8') as file:
    inputList = list(map(int, file.readlines()))
# Part 1
increased = 0
for i in range(len(inputList)):
    # print(inputList[i])
    if i == 0:
        increased = 0
    else:
        if inputList[i] > inputList[i-1]:
            increased += 1

print(increased)

# Part 2
increased2 = 0
for i in range(len(inputList)):
    if i+3 < len(inputList):
        sum1 = inputList[i]+inputList[i+1]+inputList[i+2]
        sum2 = inputList[i+1]+inputList[i+2]+inputList[i+3]
        # print(sum1, sum2)
        if sum2 > sum1:
            increased2 += 1

print(increased2)
