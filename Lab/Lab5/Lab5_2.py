number = int(input("Enter number")) 
if number > 0 and number < 100 :
    print("Total :",number)
else : 
    print("Total(plus VAT) %.2f" % (number+number*0.07)) 