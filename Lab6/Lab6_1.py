while True : 
    grade = input("Enter score")
    if grade == "n" :
        break
    elif int(grade) >= 80 and int(grade) < 100 :
        print("Your grade is A")
    elif int(grade) >=75 and int(grade) < 80 :
        print("Your grade is B+")
    elif int(grade) >= 70 and int(grade) < 75 :
        print("Your grade is B")
    elif int(grade) >=65 and int(grade) < 70 :
        print("Your grade is C+")
    elif int(grade) >= 60 and int(grade) < 65 :
        print("Your grade is C")
    elif int(grade) >=55 and int(grade) < 60 :
        print("Your grade is D+")
    elif int(grade) >= 50 and int(grade) < 55 :
        print("Your grade is D")
    elif int(grade) < 50 :
        print("Your grade is F")
    