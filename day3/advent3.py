import collections
with open('day3-input.txt', 'r', encoding='utf-8') as file:
    # inputList = list(map(int, file.readlines()))
    inputList = list(file.readlines())
# Part 1
# for inp in inputList:
#     print(collections.Counter(s).most_common(1)[0])

tpList = []
# str = ''
for x in zip(*inputList):
    str = ''
    for y in x:
        str += y
    tpList.append(str)

tpList = tpList[:-1]
mostCom = ''
leastCom = ''
for elem in tpList:
    mostCom += collections.Counter(elem).most_common()[0][0]
    leastCom += collections.Counter(elem).most_common()[-1][0]
    # print(mostCom)
print('MostCom:',mostCom, int(mostCom, 2), 'LeastCom:', leastCom, int(leastCom,2), 'Consumption:', int(mostCom,2)*int(leastCom,2))

# Part 2
