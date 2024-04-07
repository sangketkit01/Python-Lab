text = "Information Technology Program, College of computing"
letter = {}
for i in text :
    if i.isalpha() :
        i = i.upper()
        if i not in letter :
            letter[i] = 1
        else : 
            letter[i] += 1

for k,v in sorted(letter.items(),key= lambda item : (-item[1],item[0])):
    print(k,":",v)
    






