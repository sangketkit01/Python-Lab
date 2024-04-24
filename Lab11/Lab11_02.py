def findLost(x : list[int]) -> str :
    lost = []
    for i in range(min(x),max(x)+1) :
        if i not in x :
            lost.append(i)
    return ",".join(str(num) for num in lost)

num = [10,11,15,12,9,14,7]
print("Lost number contain =",findLost(num))
