from queue import LifoQueue

# Part 1: Using LIFO stacks saves lives
with open('day10-input.txt', 'r', encoding='utf-8') as file:
    # arr = [line.strip().split() for line in file]
    arr = [[i for i in line.strip()] for line in file]
    
rule_dict = {')':3, ']':57, '}':1197, '>':25137}
rule_pairs = {'(':')', '[':']', '{':'}', '<':'>'}
starts = {'(', '[', '{', '<'}
stack = LifoQueue()
fails = []
scores = []

for line in arr:
    for char in line: # traverse chars
        if char in starts: # if it is an 'opening char'
            stack.put(char) # put it to stack
        else: # not 'opening char'
            if char != rule_pairs[stack.get()]: # if the current char does not pair
                fails.append(char) # append to fails list
                stack = LifoQueue() # reset the stack
                break
    result = sum(rule_dict[err] for err in fails) # sum the score rules
    
print('Part 1:', result)

# Part 2: LIFO stacks again
rule_dict = {')':3, ']':57, '}':1197, '>':25137}
rule_pairs = {'(':')', '[':']', '{':'}', '<':'>'}
starts = {'(', '[', '{', '<'}
stack = LifoQueue()
scores = []

def part2_score(stack): # score calculator function
    score = 0
    part2_rules = {')': 1, ']': 2, '}': 3, '>': 4}
    while stack.qsize() != 0: # while stack not empty
        score *= 5
        score += part2_rules[rule_pairs[stack.get()]] # multiply by 5 and add the score of corresponding rule
    return score

for line in arr:
    for char in line: # traverse chars
        if char in starts: # if it is an 'opening char'
            stack.put(char) # put it to stack
        else: # not 'opening char'
            if char != rule_pairs[stack.get()]: # if the current char does not pair
                stack = LifoQueue() # reset the stack
                break
    if stack.qsize() != 0:
        scores.append(part2_score(stack)) # calculate & append
    stack = LifoQueue()

print('Part 2:', sorted(scores)[int((len(scores)-1)/2)]) # print the middle score