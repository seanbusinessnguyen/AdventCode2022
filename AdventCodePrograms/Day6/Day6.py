fileInput = open('input.txt', 'r')

for line in fileInput:
    parsedLine = line.strip()
    print('The line is', parsedLine)
    print('The length of the line is', len(parsedLine))

    sequence = ''

    for letter in parsedLine:
        sequence += letter
        print('current sequence is', sequence)

        if len(sequence) == 4:
            print('checking', sequence)
            answer = set(sequence)
            print('The set equals', answer)

            if len(answer) == 4:
                break

        if len(sequence) > 3:
            sequence = sequence[1:]

print(sequence)

index = parsedLine.find(sequence)
index += 4

print(index)
