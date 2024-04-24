dict_student = {
    "001" : {"gender":"F","GPA":3.50},
    "002" : {"gender":"M","GPA":2.67},
    "003" : {"gender":"M","GPA":3.28},
    "004" : {"gender":"M","GPA":2.75},
    "005" : {"gender":"F","GPA":3.21},
    "006" : {"gender":"M","GPA":2.62},
    "007" : {"gender":"F","GPA":3.00},
    "008" : {"gender":"F","GPA":2.30}
}
Male = 0
Female = 0
count = 0
all_Grade = []
for studentId,information in dict_student.items() :
    for k,v in information.items() :
        if k == "gender" :
            if v == "F" :
                Female += 1
            elif v == "M" :
                Male += 1
        if k == "GPA" :
            all_Grade.append(v)
            if float(v) < 3.00 :
                count += 1

print(f"""There are {count} student who have GPA less than 3.00
Female = {Female}
Male = {Male}
Max GPA = {max(all_Grade):.2f}""")

