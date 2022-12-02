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

totalScore = 0

for line in fileIn:
    line = line.strip()
    line = line.split(' ')

    opponent = line.pop(0)
    player = line.pop(0)

    print('The opponent is', opponent, 'and the player is', player)

    score = determineWinner(opponent, player)

    score += scoreForPlay(player)

    totalScore += score

print('Total score:', totalScore)


