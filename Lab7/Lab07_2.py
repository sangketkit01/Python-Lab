sumGrade = 0
sumWeight = 0
while True:
    weight = int(input("Enter weight : "))
    grade = float(input("Enter grade : "))
    if int(grade) == 0 or weight == 0:
        break
    else:
        sumGrade += (weight*grade)
        sumWeight += weight

AvgGrade = sumGrade/sumWeight
print("Average grade is : %.2f" % AvgGrade)
