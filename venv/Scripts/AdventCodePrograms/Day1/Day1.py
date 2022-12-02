fileIn = open('input.txt', 'r')

caloriesList = []
totalCalories = 0

for line in fileIn:
    if line.strip() == '':
        caloriesList.append(totalCalories)
        totalCalories = 0
        continue
    else:
        totalCalories += int(line)

for x in caloriesList:
    print(x)

firstMostCalories = max(caloriesList)
print('The 1st most calories is', firstMostCalories)

#########################################
#Part 2

caloriesList.remove(firstMostCalories)
secondostCalories = max(caloriesList)
print('The 2nd most calories is', secondostCalories)

caloriesList.remove(secondostCalories)
thirdMostCalories = max(caloriesList)
print('The 3rd most calories is', thirdMostCalories)

topThreeCalories = firstMostCalories + secondostCalories + thirdMostCalories

print('Top 3 Calorie total =', topThreeCalories)