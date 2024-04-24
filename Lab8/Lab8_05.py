number = input("")
print("รหัสแบบมีขีด :",number[0:-2]+"-"+number[-1])



card = []
for i in number :
    card.append(i)
card.insert(-1,"-")

print("รหัสแบบมีขีด :",end=" ")
for i in card :
    print(i,end="")
