try:
    file = open("Lab15.txt", "r", encoding="utf-8")
    write_file = open("summary.txt","w",encoding="utf-8")
    lines = file.readlines()
    skip = []
    fruit = {}
    total = 0

    for count, line in enumerate(lines):
        newline = line.replace("#", " ").replace(  ",", " ").replace("฿", " ").split()
        list_of_fruit, price = newline[1:-1], newline[-1]
        if count == 0:
            continue
        try:
            assert newline[0].isdigit() and newline[-1].isdigit()
            for item in list_of_fruit:
                if item not in fruit:
                    fruit[item] = 1
                else:
                    fruit[item] += 1
            total += int(price)
        except AssertionError:
            skip.append(count+1)
            skip.append(line.strip())

    print(f"Cannot read the data at line {skip[0]} : {skip[1]}")
    write_file.write(f"Cannot read the data at line{skip[0]} : {skip[1]}\n")

    print("=====Fruit Report=====")
    write_file.write("=====Fruit Report=====\n")

    print("Quntity \t Fruit")
    print("="*23)
    write_file.write(f"Quntity \t Fruit\n{'='*23}\n")

    for key, value in sorted(fruit.items(), key=lambda item: [-item[1], item[0]]):
        print(f"{value} \t\t {key}")
        write_file.write(f"{value} \t\t {key}\n")

    print(f"Summary price : ฿{total:,}")
    write_file.write(f"Summary price : ฿{total:,}\n")

    file.close()
    write_file.close()
except IOError:
    print(f"Cannot open recipt.txt")
