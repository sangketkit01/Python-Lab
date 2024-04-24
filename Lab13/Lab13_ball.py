from operator import le


l = 0
lis = []
des = {}
file = open("Lab/Lab13/product.txt", "r")
for line in file:
    l += 1
    if l == 1:
        continue
    data2 = line.strip().split(', ')
    print(data2)
    if len(data2) != 5:
        print(f"At line {l-1}, an invalid data is found, and it was skipped. [{line.strip()}]")
    else:
        R = data2[3].split(".")
        if R[1] != "99" :
            raise AssertionError(f"Check data at line {l} [{line.strip()}]")
        name = data2[0]
        if data2[1] not in des :
            des[data2[1]] = {data2[1]:[data2[2]]}
        else:
           des[data2[1]][data2[1]].append(data2[2])
for k,v in des.items() :
    print(k,v)

