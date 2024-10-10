# Quang Tran - Student ID:001162701

import csv
import package
import truck
from hashtable import hashtable
from datetime import datetime, timedelta

#Read the distance file and make a 2-D list
with open('distances.csv',encoding='utf-8-sig') as distance_file:
    distance_data = list(csv.reader(distance_file))

#Read the address file and make a 2-D list
with open('addresses.csv',encoding='utf-8-sig') as address_file:
    address_data = list(csv.reader(address_file))

#Create the packages table
package_table = hashtable()

#Create truck objects with pre-selected packages
truck1 = truck.truck(1,0,datetime.strptime('08:00:00', '%H:%M:%S'),"4001 South 700 East",[1,2,4,5,13,14,15,16,19,20,29,30,31,34,37,40])
truck2 = truck.truck(2,0,datetime.strptime('09:05:00', '%H:%M:%S'),"4001 South 700 East",[3,6,7,8,10,11,18,25,28,32,36,38])
truck3 = truck.truck(3,0,None,"4001 South 700 East",[9,12,17,21,22,23,24,26,27,33,35,39])

#Create the list of trucks. Excludes truck 3 due to only having 2 drivers.
truck_list = [truck1,truck2]

#--------------------------------------------------------------------------------------------------------------------
""" def find_distance(package_id_current,package_id_next):

    #Initialize variables for addresses of the parameter package IDs
    address1 = package_table.search(package_id_current).address
    address2 = package_table.search(package_id_next).address

    # Below comment would check to see if any package addresses are empty
    # if package_table.search(package_id_current).address != '' and package_table.search(package_id_next).address != '':
    for address in address_data:
        #Get the values from addresses.csv 2D list, that correpsonds to the address parameter
        if address[2] == address1:
            lookup_x = int(address[0])
        if address[2] == address2:
            lookup_y = int(address[0])
    
    #Uses the lookup x and y values from addresses to find the distance between them in the the distances.csv file 2D array
    if distance_data[lookup_x][lookup_y] == '':
        #print(distance_data[lookup_y][lookup_x])
        return distance_data[lookup_y][lookup_x]
    else:
        #print(distance_data[lookup_x][lookup_y])
        return distance_data[lookup_x][lookup_y] """

""" def the_algo(trucks):
    for truck in trucks:
        truck.miles_traveled = 0
        sorted_list = []
        shortest_distance = 8000
        shortest_package = None
        
        #Set status of all packages in the truck to En route.
        for package in truck.package_list:
            package_table.search(package).status = "En route"

        while len(truck.package_list) > 0:
            for package in truck.package_list:
                if truck_find_distance(truck,package) < shortest_distance:
                    shortest_distance = truck_find_distance(truck,package)
                    shortest_package = package
            
            #Remove the next package to be delivered (is the closest) from the original list
            #Add the next package to the sorted-list that will be the delivery route
            #Update the truck's location to the next package
            truck.package_list.remove(shortest_package)
            sorted_list.append(shortest_package)
            truck.current_address = package_table.search(shortest_package).address
            package_table.search(shortest_package).status = "Delivered"

            #Adds the next package's distance to the truck's miles
            truck.miles_traveled += shortest_distance

            #TODO - add time miles code
            #Package delivery time = base time + truck total driving time at the time
            package_table.search(shortest_package).delivery_time = increment_time(truck.departure_time,(60*truck.miles_traveled)/18)

            shortest_distance = 8000
        
        #Truck returns to the hub. Set the truck's address to the hub.
        truck.miles_traveled += truck_return(truck,"4001 South 700 East")
        truck.current_address = "4001 South 700 East"
            
        print("List:",sorted_list)
        truck.package_list = sorted_list    """

#Creates package objects with data from packages.csv and inserts them into the hash table.
def load_package_info():
    filename = 'packages.csv'
    with open(filename, encoding='utf-8-sig') as package_file:
        package_data = csv.reader(package_file)
        for lines in package_data:
            package_id = int(lines[0])
            package_address = lines[1]
            package_city = lines[2]
            package_state = lines[3]
            package_zip = lines[4]
            package_deadline = lines[5]
            package_weight = lines[6]
            if lines[7] == '':
                package_notes = "No notes"
            else:    
                package_notes = lines[7]
            package_status = "At the hub"

            p = package.package(package_id,
                        package_address,
                        package_city,
                        package_state,
                        package_zip,
                        package_deadline,
                        package_weight,
                        package_notes,
                        package_status)
            package_table.insert(package_id, p)

#Returns the distance between the truck's current address and the next package to be delivered
def truck_find_distance(truck,package_id_next):

    #Initialize variables for addresses of the parameter package IDs
    address1 = truck.current_address
    address2 = package_table.search(package_id_next).address

    # Below comment would check to see if any package addresses are empty
    # if package_table.search(package_id_current).address != '' and package_table.search(package_id_next).address != '':
    for address in address_data:
        #Get the values from addresses.csv 2D list, that correpsonds to the address parameter
        if address[2] == address1:
            lookup_x = int(address[0])
        if address[2] == address2:
            lookup_y = int(address[0])
    
    #Uses the lookup x and y values from addresses to find the distance between them in the the distances.csv file 2D array
    if distance_data[lookup_x][lookup_y] == '':
        #print(distance_data[lookup_y][lookup_x])
        return float(distance_data[lookup_y][lookup_x])
    else:
        #print(distance_data[lookup_x][lookup_y])
        return float(distance_data[lookup_x][lookup_y])

#Returns the distance of the truck at its current address and the hub.
def truck_return(truck,hub_address):
    #Initialize variables for addresses of the parameter package IDs
    address1 = truck.current_address
    address2 = hub_address

    # Below comment would check to see if any package addresses are empty
    # if package_table.search(package_id_current).address != '' and package_table.search(package_id_next).address != '':
    for address in address_data:
        #Get the values from addresses.csv 2D list, that correpsonds to the address parameter
        if address[2] == address1:
            lookup_x = int(address[0])
        if address[2] == address2:
            lookup_y = int(address[0])
    
    #Uses the lookup x and y values from addresses to find the distance between them in the the distances.csv file 2D array
    if distance_data[lookup_x][lookup_y] == '':
        #print(distance_data[lookup_y][lookup_x])
        return float(distance_data[lookup_y][lookup_x])
    else:
        #print(distance_data[lookup_x][lookup_y])
        return float(distance_data[lookup_x][lookup_y])

#Looks up a specified package at the current moment (before or after deliveries are made)
def lookup_package_info(package_id):
    p = package_table.search(package_id)
    if p == None:
        print("\nPackage ID not found.")
    else:    
        print("\nPackage ID:",p.id)
        print("Address:",p.address)
        print("Deadline:",p.deadline)
        print("City:",p.city)
        print("ZIP Code:",p.zip)
        print("Weight:",p.weight)
        print("Status:",p.status)

        if p.status is not "At the hub":
            print("Departure time:",p.departure_time.time())

        if p.status == "Delivered":
            print("Delivered at:",p.delivery_time.time())

#Prints status of all packages on all trucks and their delivery times.
def timed_package_lookup(time):
    checked_time = datetime.strptime(time,'%H:%M')
    truck_miles = 0
    #Deliver packages
    deliver_trucks()

    trucks = [truck1,truck2,truck3]

    for truck in trucks:
        print("\n------------------------------------------------------------------------------")
        print("Truck:",truck.truck_number)
        for check_package in sorted(truck.package_list):
            p = package_table.search(check_package)

            ##Check if the truck left the hub and set package status and delivery time
            #If checking before the trucks have left.
            if checked_time < truck.departure_time:
                p.status = "At the hub"
                p.delivery_time = None
            #Check if the trucks have left AND if the input time is before the package delivery time.
            if (checked_time >= truck.departure_time) and (checked_time < p.delivery_time):
                p.status = "En route"
                p.delivery_time = None

            print("\nPackage ID:", p.id)
            print("Package status:",p.status)
            
            #Catches instances where there is no delivery time yet for some packages.
            if p.status == "At the hub" or p.status == "En route":
                print("Package delivery time: None")
            else:
                print("Package delivery time:",p.delivery_time.time())

        #Get truck miles driven caluclated at the checked time.
        if checked_time >= truck.departure_time:
            time_difference = checked_time - truck.departure_time
            driven_time = time_difference.total_seconds()
            truck_miles =.005 * driven_time

        #Compares the truck miles calculated to the actualy truck miles driven(limit) and prints whichever is lower.
        if truck_miles < truck.miles_traveled:
            print("")
            print("Truck",truck.truck_number,"miles traveled:",round(truck_miles,2))
        else:
            print("")
            print("Truck",truck.truck_number,"miles traveled:",round(truck.miles_traveled,2))
                  
#Displays total truck miles traveled at the current moment (before or after deliveries are made)
def get_truck_miles():
    if truck1.miles_traveled == 0 and truck2.miles_traveled == 0 and truck3.miles_traveled == 0:
        print("\nTruck miles before deliveries. To see truck miles after deliveries, first use Option 1 at the main menu and try again.\n")
        print("Truck 1:",round(truck1.miles_traveled,2),"miles")
        print("Truck 2:",round(truck2.miles_traveled,2),"miles")
        print("Truck 3:",round(truck3.miles_traveled,2),"miles")
        print("Total  :",round(truck1.miles_traveled+truck2.miles_traveled+truck3.miles_traveled,2),"miles")
    else:
        print("Truck miles after deliveries.\n")
        print("Truck 1:",round(truck1.miles_traveled,2),"miles")
        print("Truck 2:",round(truck2.miles_traveled,2),"miles")
        print("Truck 3:",round(truck3.miles_traveled,2),"miles")
        print("Total  :",round(truck1.miles_traveled+truck2.miles_traveled+truck3.miles_traveled,2),"miles")

#Calculates what time packages are delivered and when trucks finish deliveries.
def increment_time(base_time, total_truck_time):
    return base_time + timedelta(minutes=total_truck_time)

#Main algorithm. Finds truck route, marks packages as delivered, and updates time and distance tracking variables.
def deliver_packages(truck):
    #Sets these variables back to default/initial values so delivery datapoints don't stack in case of multiple deliveries of the same trucks and packages
    truck.miles_traveled = 0
    sorted_list = []
    shortest_distance = 8000
    shortest_package = None

    #Set status of all packages in the truck to En route.
    for package in truck.package_list:
        package_table.search(package).status = "En route"
        package_table.search(package).departure_time = truck.departure_time

    #Loop through all packages in the truck as long as there are any in it
    while len(truck.package_list) > 0:
        for package in truck.package_list:
            if truck_find_distance(truck,package) < shortest_distance:
                shortest_distance = truck_find_distance(truck,package)
                shortest_package = package
        
        #Remove the next package to be delivered (is the closest) from the original list
        #Add the next package to the sorted-list that will be the delivery route
        #Update the truck's location to the next package
        #Update the package's status
        truck.package_list.remove(shortest_package)
        sorted_list.append(shortest_package)
        truck.current_address = package_table.search(shortest_package).address
        package_table.search(shortest_package).status = "Delivered"

        #Adds the next package's distance to the truck's miles
        truck.miles_traveled += shortest_distance

        #Sets the package delivery time using the truck's departure time and the total distance the truck drove up to that package
        package_table.search(shortest_package).delivery_time = increment_time(truck.departure_time,(60*truck.miles_traveled)/18)
        
        #Reset the distance value for the next package check
        shortest_distance = 8000
    
    #Truck returns to the hub. Set the truck's address to the hub.
    truck.miles_traveled += truck_return(truck,"4001 South 700 East")
    truck.current_address = "4001 South 700 East"
    truck.return_time = increment_time(truck.departure_time,(60*truck.miles_traveled)/18)
    
    #Re-insert packages into each truck so they can be referenced even after delivery.
    truck.package_list = sorted_list

#Does deliveries for all 3 trucks
def deliver_trucks():
    #Delivers packages in truck 1 and truck 2
    for delivery_truck in truck_list:
        deliver_packages(delivery_truck)
    #When truck 1 and truck 2 return to hub, set truck 3's departure time, update package #9 address, and deliver
    if truck1.current_address == "4001 South 700 East" and truck2.current_address == "4001 South 700 East":
        #Truck 1 returns before truck 2 and it's AFTER 10:20. Set truck 3 to leave when truck 1 returns.
        if (truck1.return_time < truck2.return_time) and (truck1.return_time > datetime.strptime('10:20', '%H:%M')):
            truck3.departure_time = truck1.return_time
            package_table.search(9).address = "410 S State St"
            package_table.search(9).city = "Salt Lake City"
            package_table.search(9).state = "UT"
            package_table.search(9).zip = "84111"
            deliver_packages(truck3)
        #Truck 1 returns before truck 2 and it's BEFORE 10:20. Set truck 3 to leave at 10:20 after updating package 9 data.
        if (truck1.return_time < truck2.return_time) and (truck1.return_time < datetime.strptime('10:20', '%H:%M')):
            truck3.departure_time = datetime.strptime('10:20', '%H:%M')
            package_table.search(9).address = "410 S State St"
            package_table.search(9).city = "Salt Lake City"
            package_table.search(9).state = "UT"
            package_table.search(9).zip = "84111"
            deliver_packages(truck3)
        #Truck 2 returns before truck 1 and it's AFTER 10:20. Set truck 3 to leave when truck 2 returns.    
        if (truck2.return_time < truck1.return_time) and (truck2.return_time > datetime.strptime('10:20', '%H:%M')):
            truck3.departure_time = truck2.return_time
            package_table.search(9).address = "410 S State St"
            package_table.search(9).city = "Salt Lake City"
            package_table.search(9).state = "UT"
            package_table.search(9).zip = "84111"
            deliver_packages(truck3)
        #Truck 2 returns before truck 1 and it's BEFORE 10:20. Set truck 3 to leave at 10:20 after updating package 9 data.                     
        else: 
            truck3.departure_time = datetime.strptime('10:20', '%H:%M')
            package_table.search(9).address = "410 S State St"
            package_table.search(9).city = "Salt Lake City"
            package_table.search(9).state = "UT"
            package_table.search(9).zip = "84111"
            deliver_packages(truck3)        

#--------------------------------------------------------------------------------------------------------------------
class Main:
    load_package_info()
    running = True
    print("WGUPS Delivery System")
    while running:
        print("\nMAIN MENU")
        print("Select an option (type in the number to proceed):\n")
        print("1. Deliver packages              4. View total truck driving miles")
        print("2. Package lookup (Time)         5. Exit")
        print("3. Package lookup (ID)           6. Get all packages with deadlines (for project verification)")
        print("                                    (Deliver packages with option 1 first.)\n")

        choice = str(input())

        match choice:
            case "1":
                deliver_trucks()
            case "2":
                try:
                    print("\nEnter a time (format as 24 hour time, hh:mm):")
                    input_time = str(input())
                    timed_package_lookup(input_time)
                except ValueError:
                    print("\nError: invalid input. Make sure to use the format hh:mm.")
            case "3":
                try:
                    print("\nEnter a Package ID...")
                    lookup_id = int(input())
                    lookup_package_info(lookup_id)
                except ValueError:
                    print("\nError: invalid input. Type in an integer for the package ID.")
            case "4":
                get_truck_miles()
            case "5":
                print("Exiting...")
                running = False
                raise SystemExit
            case "6":
                lookup_package_info(15)
                lookup_package_info(6)
                lookup_package_info(25)
                lookup_package_info(20)
                lookup_package_info(16)
                lookup_package_info(14)
                lookup_package_info(1)
                lookup_package_info(13)
                lookup_package_info(29)
                lookup_package_info(30)
                lookup_package_info(31)
                lookup_package_info(34)
                lookup_package_info(37)
                lookup_package_info(40)
            case _:
                print("Please type a valid option.\n")