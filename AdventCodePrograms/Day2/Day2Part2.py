# created by copying Day2.py

#first column is what the opponent will play

#second is what I play

#Score = Shape chose, 1 for Rock, 2 for paper, 3 for scissors, and the outcome
# Outcome = 0 if you lost, 3 if draw, 6 for win


fileIn = open('input.txt', 'r')
opponent = ''
player = ''

def determineWinner(opp, play):
    # A = Rock
    # B = Paper
    # C = Scissors

    # X for Rock
    # Y for Paper
    # Z for Scissors

    if opp == 'A':
        if play == 'X':
            score = 3
            return score
        elif play == 'Y':
            score = 6
            return score
        elif play == 'Z':
            score = 0
            return score

    if opp == 'B':
        if play == 'X':
            score = 0
            return score
        elif play == 'Y':
            score = 3
            return score
        elif play == 'Z':
            score = 6
            return score

    if opp == 'C':
        if play == 'X':
            score = 6
            return score
        elif play == 'Y':
            score = 0
            return score
        elif play == 'Z':
            score = 3
            return score

def scoreForPlay(play):
    # X for Rock
    # Y for Paper
    # Z for Scissors

    if play == 'X':
        score = 1
        return score
    elif play == 'Y':
        score = 2
        return score
    elif play == 'Z':
        score = 3
        return score

def part2Scorer(opp, play):
    # A = Rock
    # B = Paper
    # C = Scissors

    # X for Rock
    # Y for Paper
    # Z for Scissors

    score = 0
    if play == 'X':
        # need to lose
        if opp == 'A':
            # play scissors
            score += 3
            score += 0
            return score
        if opp == 'B':
            # play rock
            score += 1
            score += 0
            return score
        if opp == 'C':
            # play paper
            score += 2
            score += 0
            return score

    if play == 'Y':
        # need to end in draw
        if opp == 'A':
            # play rock
            score += 1
            score += 3
            return score
        if opp == 'B':
            # play paper
            score += 2
            score += 3
            return score
        if opp == 'C':
            # play scissors
            score += 3
            score += 3
            return score

    if play == 'Z':
        # need to end in win
        if opp == 'A':
            # play paper
            score += 2
            score += 6
            return score
        if opp == 'B':
            # play scissors
            score += 3
            score += 6
            return score
        if opp == 'C':
            # play rock
            score += 1
            score += 6
            return score


totalScore = 0

for line in fileIn:
    line = line.strip()
    line = line.split(' ')

    opponent = line.pop(0)
    winOrLose = line.pop(0)

    print('The opponent is', opponent, 'and the player is', winOrLose)

    score = part2Scorer(opponent, winOrLose)

    totalScore += score

print('Total score:', totalScore)


fileIn2 = open('input.txt', 'r')

for line in fileIn2:
    x, y = line.strip().split()
    print(x,y)
