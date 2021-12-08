from collections import Counter 

# Part 1
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
    return ''.join(map(str, list(set(list(str1)) - set(list(str2)))))

segments_list = []

for input in inputList:
    for inp in input[1].split(' '):
        if seg_choose(inp) > 0:
            item = seg_choose(inp)
            segments_list.append(item)

print('Part 1:', len(segments_list))

## Part 2

ssd = {'abcefg': '0', 'cf': '1', 'acdeg': '2', 'acdfg': '3', 'bcdf': '4', 'abdfg': '5', 'abdefg': '6', 'acf': '7', 'abcdefg': '8', 'abcdfg': '9'}

translated = []
for line in inputList:
        counts = Counter(line[0].replace(' ',''))
        dynamic = {x[0]: {4:'e',6:'b',9:'f'}[x[1]]for x in counts.items() if x[1] in (4,6,9)}

        for ln in line[0].split():
            if len(ln) == 2:
                dynamic.update({seg: 'c' for seg in ln if seg not in dynamic})
        
        dynamic.update({x[0]: 'a' for x in counts.items() if x[1] == 8 and x[0] not in dynamic})

        for ln in line[0].split():
            if len(ln) == 4:
                dynamic.update({seg: 'd' for seg in ln if seg not in dynamic})

        dynamic.update({x[0]: 'g' for x in counts.items() if x[1] == 7 and x[0] not in dynamic})
        deciphered = line[1].translate(str.maketrans(dynamic)).split()

        translated.append(int(''.join([ssd[''.join(sorted(term))] for term in deciphered])))

print('Part 2:', sum(translated))