def checkFile():
    try:
        file = open("Lab/Lab13/product.txt")
    except IOError:
        print(f"Cannot open product.txt")


def notComplete():
    file = open("Lab/Lab13/product.txt")
    lines, round = file.readlines(), 0
    for line in lines:
        round += 1
        line.split(", ")[-1] = line.split(", ")[-1].replace("\n", "")
        price = line.split(", ")[3]
        if round == 1:
            continue
        if len(line.split(", ")) != 5:
            print(
                f"At line {round},an invalid data is found and it was skipped. {line.split(', ')}")
        try:
            assert price.endswith("99") or len(
                line.split(", ")) != 5, "The price shoud be .99"
        except AssertionError:
            print(f"Check data at line {round} {line.split(', ')}")


def complete():
    file = open("Lab/Lab13/product.txt")
    all_category = {}
    round, sumItem = 0, 0
    for line in file.readlines():
        category, name, quantity = (
             line.split(", ")[1], line.split( ", ")[2],
               line.split(", ")[-1].strip()
            )
        round += 1
        if round == 1 or len(line.split(", ")) !=5:
            continue
        if len(line.split(", ")) == 5:
            sumItem += int(quantity)
        if category not in all_category :
            all_category[category] = {category:[name],category+"s":1}
        else :
            all_category[category][category+"s"] += 1
            all_category[category][category].append(name)
    print(f"""The data in file contains {round-1} product
=================================================
There are {len(all_category)} categories.""")
    for key,value in all_category.items() :
        print(f"{key} {value[key+'s']} product : {', '.join(value[key])}")
    print(f"""=================================================
total contains {sumItem} items""")
            
checkFile()
notComplete()
complete()

