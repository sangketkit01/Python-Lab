scores = {"S321-6":87,"S321-9":54,"S321-7":67,"S321-4":65,"S321-1":77,"S321-5":91
          ,"S321-3":51,"S321-8":89,"S322-0":76,"S321-2":80}

evenId = []
evenNumber = 0
avg = 0
for k,v in scores.items() :
    id = k.split("-")
    if int(id[1]) % 2 == 0:
        evenNumber += 1
        evenId.append(k)
        avg += v

print("Number of even : {}".format(evenNumber))
print("Even id : ",   ",".join([x for x in sorted(evenId,reverse=True)]))
print("Average score of even id : {:.2f}".format(avg/len(evenId)))


print("Even id : ",end="")
for i in sorted(evenId,reverse=True) :
    if i == min(evenId) :
        print(i)
    else :
        print(i,end=",")