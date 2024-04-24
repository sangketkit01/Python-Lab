tax = 0 
for i in range(5):
    car = int(input("ป้อนประเภทรถยนต์(1=รถยนต์ส่วนบุคคล,2=รถตู้,3=รถโดยสาร,4=รถบรรทุก)"))
    if car == 1 :
        tax += 40
    elif car == 2 :
        tax += 60
    elif car == 3 :
        tax += 80 
    elif car == 4 :
        tax += 100

print("all tax : {}".format(tax))
