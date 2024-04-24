import math
number = int(input("Enter number : "))
for i in range(1) :
    if number == 2 : 
        print(str(number)+" เป็นจำนวนเฉพาะ")
    elif number != 2 and number % 2 == 0 :
        print(str(number)+" ไม่เป็นจำนวนเฉพาะ")
    elif number % 2 != 0 :
        if number % math.sqrt(number) == 0 :
            print(str(number)+" ไม่เป็นจำนวนเฉพาะ")
        else :print(str(number)+" เป็นจำนวนเฉพาะ")