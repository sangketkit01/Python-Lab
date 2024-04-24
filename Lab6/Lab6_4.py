start = int(input("Enter start : "))
stop = int(input("Enter stop : "))
count = 0 
for i in range(start,stop) :
    if i % 2 != 0 :
        count +=1 

print("number between "+str(start)+" to "+str(stop)+" is : "+str(count))