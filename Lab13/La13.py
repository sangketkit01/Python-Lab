# หาผู้ท้าชิงโค้ดอ่านยากครับ
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
    lines = file.readlines()
    all_category, camping, kitchen, toilet = {}, [], [], []
    campingCount, kitchenCount, toiletCount, round, sumItem = 0, 0, 0, 0, 0
    for line in lines:
        category, name, quantity = line.split(", ")[1], line.split(
            ", ")[2], line.split(", ")[-1].replace("\n", "")
        round += 1
        if round == 1:
            continue
        if len(line.split(", ")) == 5:
            sumItem += int(quantity)
        if category == "Camping" and len(line.split(", ")) == 5:
            camping.append(name)
            campingCount += 1
        elif category == "Kitchen" and len(line.split(", ")) == 5:
            kitchen.append(name)
            kitchenCount += 1
        elif category == "Toilet" and len(line.split(", ")) == 5:
            toilet.append(name)
            toiletCount += 1
        if category not in all_category and len(line.split(", ")) == 5:
            if category == "Camping":
                all_category[category] = camping
            elif category == "Kitchen":
                all_category[category] = kitchen
            elif category == "Toilet":
                all_category[category] = toilet
    print(f"""The data in file contains {round} product
=================================================
There are {len(all_category)} categories.""")
    for k, v in all_category.items():
        if k == "Camping":
            print(f"Camping {campingCount} product : {','.join(v)}")
        elif k == "Kitchen":
            print(f"Kitchen {kitchenCount} product : {' , '.join(v)}")
        elif k == "Toilet":
            print(f"Toilet {toiletCount} product : {' , '.join(v)}")
    print(f"""=================================================
total contains {sumItem} items""")
