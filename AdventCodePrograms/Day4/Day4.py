fileInput = open('input.txt', 'r')

count = 0

for line in fileInput:
    parsedLine = line.strip().split(',')

    firstElf = parsedLine.pop(0)
    secondElf = parsedLine.pop(0)

    firstStart = firstElf.split('-')
    firstStartInt = int(firstStart[0])

    firstEndInt = int(firstStart[1])

    firstSequence = []
    for number in range (firstStartInt, firstEndInt + 1):
        firstSequence.append(number)

    secondStart = secondElf.split('-')
    secondStartInt = int(secondStart[0])

    secondEndInt = int(secondStart[1])

    secondSequence = []
    for number in range (secondStartInt, secondEndInt + 1):
        secondSequence.append(number)

    setFirst = set(firstSequence)
    setSecond = set(secondSequence)
    #print(firstSequence, secondSequence)
    if setFirst.issubset(setSecond) or setSecond.issubset(setFirst):
        count += 1

print(count)