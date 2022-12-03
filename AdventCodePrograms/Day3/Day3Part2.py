fileInput = open('input.txt', 'r')

lines = []
dupes = set()
total = 0

for line in fileInput:
    lines.append(line.strip())
    if len(lines) == 3:
        print(lines)

        for letter in lines[0]:
            for letter2 in lines[1]:
                for letter3 in lines[2]:
                    if letter == letter2 and letter2 == letter3:
                        dupes.add(letter)
                        print(dupes)

        lines = []

        for letter in dupes:
            if letter.isupper():
                total += ord(letter) - 38
            elif letter.islower():
                total += ord(letter) - 96

        dupes = set()

print(total)
