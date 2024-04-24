alpha = input("")
count = 0

for i in range(len(alpha)) :
    if alpha[i].isdigit() :
        count += 1
    
if count == 0 :
    print("There's no digit")
else :
    print("There's is digit :",end="")
    for i in range(len(alpha)) :
        if alpha[i].isdigit() :
            if i == len(alpha)-1 :
               print(alpha[i])
            else :
               print(alpha[i],end=",") 

