def addVehicle() : 
    with open("Lab/Lab12/vehicles.txt",'a') as writeFile :
        vehicle = {1:"Sedan",2:"Van",3:"Truck"}
        id = input("Enter vehicle id : ") 
        type = int(input("Enter vehicle's type [1:Sedan , 2:Van , 3:Truck] : "))
        writeFile.write(f"{id}     {vehicle[type]}\n")
def show_all_vehicle() :
    with open("Lab/Lab12/vehicles.txt",'r') as readFile :
        lines = readFile.readlines()
        all_vehicle = []
        countVehicle = {'Sedan':0,'Van':0,'Truck':0}  
        for line in lines :
            all_vehicle.append(line.split())
        if len(all_vehicle) > 0 :
            print("ID     Type\n================")
            for i,j in all_vehicle :
                print(i,j)
                countVehicle[j] += 1
            print(f"The number of Sedan is : {countVehicle['Sedan']}\nThe number of van is : {countVehicle['Van']}\nThe number of Truck is : {countVehicle['Truck']}")
        else : print("Data is not found.")
        
def show_vanhicle_type() :
    with open("Lab/Lab12/vehicles.txt",'r') as readFile :
        lines = readFile.readlines()
        sedan,van,truck = {},{},{}
        all_type = {1:sedan.items(),2:van.items(),3:truck.items()}
        type = {"Sedan":sedan,"Van":van,"Truck":truck}
        for line in lines :
            vehicle = line.split() 
            for k,v in type.items() :
                if vehicle[1] == k :
                    v[vehicle[0]] = vehicle[1]
        group = int(input("Enter vehicle's type [1:Sedan , 2:Van , 3:Truck] : "))
        if group in all_type.keys() :
            for k,v  in sorted(all_type[group]) :
                print(f"ID : {k}")
            print(f"number of {v} is : {len(all_type[group])}")
        else : print("This id is not found.")
while 1 :
    print("=====Select Menu=====\n1.Add vehicle data\n2.Show all vehicle\n3.Show vehicle by type\n4.Exit")
    menu = int(input("Select menu number [1-4] : "))
    if menu == 1 :
        addVehicle()
    elif menu == 2 :
        show_all_vehicle()
    elif menu == 3 :
        show_vanhicle_type()
    elif menu == 4 :
        break