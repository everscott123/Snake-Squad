#Everett Scott

letter = input("Enter grades(Z terminates the list):"  )

count = 0

letter = letter.upper()

a = 4.0
b = 3.0
c = 2.0
d = 1.0
f = 0.0

totalA = 0
totalB = 0
totalC = 0
totalD = 0
totalF = 0


while letter != "Z":
    if letter == "A":
        totalA += 1
    if letter == "B":
        totalB += 1
    if letter == "C":
        totalC += 1
    if letter == "D":
        totalD += 1
    if letter == "F":
        totalF += 1
    letter = input().upper()

count = totalA + totalB + totalC + totalD + totalF


studentsFailing = totalF
studentsPassing = count - totalF

gpa = (totalA*a + totalB*b + totalC*c + totalD)/count

            
percentPass = studentsPassing/count*100
percentFail = studentsFailing/count*100

print("Students passing: ", studentsPassing,"{:.2f}%".format(percentPass))
print("Students falling: ", studentsFailing,"{:.2f}%".format(percentFail))
print("Class GPA: "), print("{:.2f}".format(gpa))
