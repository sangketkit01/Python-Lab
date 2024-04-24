from module import *

allData = data_list("Lab/Lab14/Lab14.txt")
round = 1 

print(f"Lab14.txt contain {len(allData)} lines")
for count,data in enumerate(allData) :
    print(f"line{count+1} : {data}")

word,most = most_word("Lab/Lab14/Lab14.txt")
print(f'Maximum occurred word is "{word}" ({most} times).')
