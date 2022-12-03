fileInput = open('input.txt', 'r')

total = 0

for line in fileInput:
    line = line.strip()
    half = len(line) // 2
    print(half)
    sliceValue = slice(half)

    firstSack = line[sliceValue]
    print(firstSack)

    sliceValueSecond = slice(half, len(line))
    secondSack = line[sliceValueSecond]
    print(secondSack)

    # print(line)
    # print(firstSack+secondSack)

    dupes = set()
    for letter in firstSack:
        for letter2 in secondSack:
            if letter == letter2:
                dupes.add(letter)
    print(dupes)

    #lower case = ord() - 96
    #upper case = ord() - 38

    # print(ord('a')-96)
    # print(ord('z')-96)
    # print(ord('A')-38)
    # print(ord('Z')-38)

    for letter in dupes:
        if letter.isupper():
            total += ord(letter) - 38
        elif letter.islower():
            total += ord(letter) - 96

    print(total)




