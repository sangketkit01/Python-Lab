weigth = int(input("Enter weigth : "))
height = int(input("Enter height : "))
word1 = "อยู่ในเกณฑ์ :"
word2 = "ภาวะเสี่ยงต่อโรค :"

def Bmi(weigth,height) :
    return weigth / ((height/100)*(height/100))

def checkBmi(BMI) :
    if BMI < 18.5 :
        print("You BMI is : %.2f" %BMI)
        print(word1,"low weigth/skinny")
        print(word2,"More than normal people")

    elif 18.5 <= BMI <= 22.9 :
        print("You BMI is : %.2f" %BMI)
        print(word1,"Normal")
        print(word2,"Normal")

    elif 23 <= BMI <= 24.9 :
        print("You BMI is : %.2f" %BMI)
        print(word1,"Fat level 1")
        print(word2,"Dangerous level 2")

    elif 25<= BMI <= 29.9 :
        print("You BMI is : %.2f" %BMI)
        print(word1,"Fat level 2")
        print(word2,"Dangerous level 2")

    else :
       print("You BMI is : %.2f" %BMI)
       print(word1,"Fat level 3")
       print(word2,"Dangerous level 3")

BMI_Instace =  Bmi(weigth,height)
checkBmi(BMI_Instace)

