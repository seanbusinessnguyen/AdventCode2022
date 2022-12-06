fileInput = open('input.txt', 'r')

# test
# stack1 = ['Z', 'N']
# stack2 = ['M', 'C', 'D']
# stack3 = ['P']

#input
stack1 = ['F','D','B','Z','T','J','R','N']
stack2 = ['R','S','N','J','H']
stack3 = ['C','R','N','J','G','Z','F','Q']
stack4 = ['F','V','N','G','R','T','Q']
stack5 = ['L','T','Q','F']
stack6 = ['Q','C','W','Z','B','R','G','N']
stack7 = ['F','C','L','S','N','H','M']
stack8 = ['D','N','Q','M','T','J']
stack9 = ['P','G','S']

#mapping = {'1': stack1, '2': stack2, '3': stack3}

mapping = {'1': stack1, '2': stack2, '3': stack3, '4': stack4,
           '5': stack5,'6': stack6,'7': stack7,'8': stack8,
           '9': stack9,}

count = 0

def moveCrate(moveFrom, moveTo, moveAmt):
    global count
    count += 1

    print('working on step', count)
    print()

    crates = []
    for x in range(moveAmt):
        crate = mapping[moveFrom].pop()
        print('grabbing crate..', crate)
        crates.append(crate)

    print(crates)
    for crate in reversed(crates):
        print('adding', crates, 'to', mapping[moveTo])
        print()
        print(x)
        mapping[moveTo].append(crate)
        # print('updated stack')
        # print(mapping[moveTo])

    print('Crates after move')
    currentCrate()

def currentCrate():
    print("Stack1 = ", stack1)
    print("Stack2 = ", stack2)
    print("Stack3 = ", stack3)
    print("Stack4 = ", stack4)
    print("Stack5 = ", stack5)
    print("Stack6 = ", stack6)
    print("Stack7 = ", stack7)
    print("Stack8 = ", stack8)
    print("Stack9 = ", stack9)
    print()

# read in first line = top of stack
# find in = bottom of stack

for line in fileInput:
    parsedLine = line.strip().split()
    #print(parsedLine)

    moveAmt = int(parsedLine[1])
    moveFrom = parsedLine[3]
    moveTo = parsedLine[5]
    #print(moveAmt, moveFrom, moveTo)

    print('Current')
    currentCrate()
    moveCrate(moveFrom, moveTo, moveAmt)


currentCrate()

allStacks = mapping.values()
answer = ''
for x in allStacks:
    top = x[len(x)-1]
    answer += top

print(answer)