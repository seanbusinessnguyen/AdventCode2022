fileInput = open('input.txt', 'r')

for line in fileInput:
    parsedLine = line.strip()
    print('The line is', parsedLine)
    print('The length of the line is', len(parsedLine))

    sequence = ''

    for letter in parsedLine:
        sequence += letter
        print('current sequence is', sequence)

        if len(sequence) == 14:
            print('checking', sequence)
            answer = set(sequence)
            print('The set equals', answer)

            if len(answer) == 14:
                break

        if len(sequence) > 13:
            sequence = sequence[1:]

print(sequence)

index = parsedLine.find(sequence)
index += 14

print(index)
