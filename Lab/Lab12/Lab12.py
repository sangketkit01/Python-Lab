def show_vanhicle_type() :
    with open("Lab/Lab12/vehicles.txt",'r') as readFile :
        lines = readFile.readlines()
        sub_type = {}
        all_type = {1:"Sedan",2:"Van",3:"Truck"}
        group = int(input("Enter vehicle's type [1:Sedan , 2:Van , 3:Truck] : "))
        if group in all_type :
           for line in lines :
               vehicle = line.split() 
               if all_type[group] not in sub_type :
                   if vehicle[1] == all_type[group] :
                      sub_type[all_type[group]] = [vehicle[0]] 
               else :
                   if vehicle[1] == all_type[group]:
                        sub_type[all_type[group]].append(vehicle[0])
           for key,value in sorted(sub_type.items()) :
               for i in value :
                   print(f"ID : {i}")
               print(f"number of {key} is : {len(value)}")
        else :
            print("This id is not found")

show_vanhicle_type()