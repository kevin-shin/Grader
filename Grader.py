newGrades = {}
weightGrade = int(input("Enter weighted grade: "))
totalGrade = int(input("Enter total grade: "))
numProb = int(input("Enter number of problems: "))


flag = True

while flag:
    name = input("Student Name (Last, First): ")
    accum = 0
    for i in range(numProb):
        grade = int(input("Problem "+ str(i+1) + ": "))
        accum += grade
    score = round((accum*(weightGrade/totalGrade)),2)
    newGrades[name] = score
    isDone = input("Done? ")
    if isDone == "Yes":
        flag = False

for key in sorted(newGrades.iterkeys()):
    print("{}: {}".format(key, newGrades[key]))

