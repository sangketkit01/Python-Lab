number = []
count = 0
sum = 0
while True :
    x = int(input(""))
    if x == 0 :
        break
    else : 
        number.append(x)
        sum += x
        count += 1
print("Min number is",min(number))
print("Max number is",max(number))
print("Avereage is {}".format(sum/count))
