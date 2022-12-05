fileInput = open('input.txt', 'r')

stack1 = ['Z', 'N']
stack2 = ['M', 'C', 'D']
stack3 = ['P']

mapping = {'1': stack1, '2': stack2, '3': stack3}

def moveCrate(moveFrom, moveTo, moveAmt):
    for x in range(moveAmt):
        crate = mapping[moveFrom].pop()
        mapping[moveTo].append(crate)
        # print('updated stack')
        # print(mapping[moveTo])

    print('Crates after move')
    currentCrate()

def currentCrate():
    print("Stack1 = ", stack1)
    print("Stack2 = ", stack2)
    print("Stack3 = ", stack3)
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