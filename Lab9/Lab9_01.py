sublist = []
print("""=====ฟังก์ชั่นการทำงาน=====
a : เพิ่มรายวิชา
d : ลบรายวิชา
p : พิมพ์รายวิชา
y : จบการทำงาน""")
while True :
    option = input("ฟังก์ชั่นการทำงาน : ")
    if option == 'a' :
        addsub = input("กรอกวิชาที่ต้องการเพิ่ม : ")
        sublist.append(addsub)
    elif option == 'd' :
        removesub = input("กรอกวิชาที่ต้องการลบ : ")
        sublist.remove(removesub)
    elif option == 'p' :
        print("วิชาทั้งหมด :",sublist)
    elif option == 'y' :
        print("จบการทำงาน")
        break