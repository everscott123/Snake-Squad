#Everett Scott
#Lab 1



days_list = []
numDays = 0

userDate = input()
userDate = userDate.split(' ')
userMonth, userYear = int(userDate[0]), int(userDate[1])
i = 0

nameMonths = ('January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', \
              'September', 'October', 'November', 'December') # header for all 12 months 
dias = ('Su Mo Tu We Th Fr Sa')
print(' ' * ((len(dias) - len(nameMonths[userMonth - 1] + ' ' + str(userYear))) // 2) \
      + nameMonths[userMonth - 1] + ' ' + str(userYear) + '\n' + dias) 

shortMonths = (4, 6, 9, 12) # short months of the year
if userMonth == 2:
    if (userYear % 4 == 0 and userYear % 100 != 0) or userYear % 400 == 0:
        numDays = 29
    else:
        numDays = 28
elif userMonth in shortMonths:
    numDays = 30
else:
    numDays = 31

if userMonth <= 2:
    userMonth += 12
    userYear -= 1    
firstDay = int(1 + int((13 * (userMonth + 1)) / 5) + userYear + int(userYear / 4) \
               - int(userYear / 100) + int(userYear / 400)) % 7 # used Zeller's Congruence
for dayNums in range(1, numDays + 1):
    if dayNums < 10:
        days_list.append(' ' + str(dayNums))
    else:
        days_list.append(str(dayNums))
if firstDay == 0:
    firstDay += 6
else:
    firstDay -= 1
print('   ' * firstDay, end='')
i += firstDay

lines = 0
for dias in days_list:
    if i == 6:
        print(str(dias) + '\n', end='')
        lines += 1
        i = 0
    elif dias == days_list[numDays - 1]:
        print(str(dias).strip(' '), end='')
    else:
        print(str(dias) + ' ', end='')
        i += 1
while lines < 6:
    print('\n', end='')
    lines += 1