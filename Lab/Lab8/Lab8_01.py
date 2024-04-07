countA = 0
countB = 0
other = 0
while True :
    AorB = input("")
    if AorB == "Y" :
        break
    elif AorB == "A" :
        countA += 1
    elif AorB == "B" :
        countB += 1
    else :
        other+=1

sum = other+countA+countB

print("Total A :",countA)
print("Total B :",countB)
print("Another : {}".format(sum-(countA+countB)))
