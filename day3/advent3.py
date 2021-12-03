import collections
with open('day3-input.txt', 'r', encoding='utf-8') as file:
    # inputList = list(map(int, file.readlines()))
    inputList = [line.rstrip() for line in file.readlines()]
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
oxy_rate = ''
co2_rate = ''

def transposeList(inputList):
    resList = []
    for x in zip(*inputList):
        str = ''
        for y in x:
            str += y
        resList.append(str)
    return(resList)

tpList2 = tpList
inputList2 = inputList
i = 0
while len(tpList[0])>1:
    elem = tpList[i]
    occ = collections.Counter(elem)
    if occ['1'] > occ['0']:
        oxyRating = [x for x in inputList if x[i]=='1']
        # co2Rating = [x for x in inputList if x[i]=='0']
        inputList = oxyRating
        tpList = transposeList(inputList)
    elif occ['1'] < occ['0']:
        oxyRating = [x for x in inputList if x[i]=='0']
        # co2Rating = [x for x in inputList if x[i]=='1']
        inputList = oxyRating
        tpList = transposeList(inputList)
    else:
        oxyRating = [x for x in inputList if x[i]=='1']
        # co2Rating = [x for x in inputList if x[i]=='0']
        inputList = oxyRating
        tpList = transposeList(inputList)
    i += 1

i = 0
while len(tpList2[0])>1:
    elem = tpList2[i]
    occ = collections.Counter(elem)
    if occ['1'] > occ['0']:
        co2Rating = [x for x in inputList2 if x[i]=='0']
        inputList2 = co2Rating
        tpList2 = transposeList(inputList2)
    elif occ['1'] < occ['0']:
        co2Rating = [x for x in inputList2 if x[i]=='1']
        inputList2 = co2Rating
        tpList2 = transposeList(inputList2)
    else:
        co2Rating = [x for x in inputList2 if x[i]=='0']
        inputList2 = co2Rating
        tpList2 = transposeList(inputList2)
    i += 1


print('Oxy rating:',int(oxyRating[0], 2), 'CO2 rating:',int(co2Rating[0], 2))
print('Answer is:', int(oxyRating[0], 2)*int(co2Rating[0], 2))
