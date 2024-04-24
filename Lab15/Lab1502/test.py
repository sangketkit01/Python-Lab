file = open("Lab/Lab15/Lab1502/test.txt","r")
data = file.read(30)
file.seek(50, 1)  # การย้ายตำแหน่งไป 50 ตำแหน่งข้างหน้าจากตำแหน่งปัจจุบัน
f = file.read(10)  # อ่านอีก 10 ตำแหน่ง
print(data)
print(f)




    
