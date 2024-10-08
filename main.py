# Quang Tran - Student ID:001162701

import csv
import package
import truck
import HashTable
from datetime import datetime, timedelta

#Create the packages table
package_table = HashTable.ChainingHashTable()

#Read the distance file and make a 2-D list
with open('distances.csv',encoding='utf-8-sig') as distance_file:
    distance_data = list(csv.reader(distance_file))

#Read the address file and make a 2-D list
with open('addresses.csv',encoding='utf-8-sig') as address_file:
    address_data = list(csv.reader(address_file))

#Time set in seconds from 00:00, assuminng delivery time won't last 24 hours or more.
truck1 = truck.truck(1,0,28800,"4001 South 700 East",[1,2,4,5,13,14,15,16,19,20,29,30,31,35,37,40])
truck2 = truck.truck(2,0,32700,"4001 South 700 East",[3,6,7,8,10,11,18,25,28,32,36,38])
truck3 = truck.truck(3,0,0,"4001 South 700 East",[9,12,17,21,22,23,24,26,27,33,35,39])

truck_list = [truck1,truck2]

#--------------------------------------------------------------------------------------------------------------------

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

def find_distance(package_id_current,package_id_next):

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
        return distance_data[lookup_x][lookup_y]

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

        if p.status == "Delivered":
            print("Delivered at:",p.delivery_time)

#TODO - maybe can print all packages instead of specific. don't need ID param anymore
def timed_package_lookup(time): #TODO - MAKE
    print("TODO")

def get_truck_miles(time): #TODO - FIX
    print("Truck 1:",truck1.miles_traveled,"miles")
    print("Truck 2:",truck2.miles_traveled,"miles")
    print("Truck 3:",truck3.miles_traveled,"miles")
    print("Total  :",truck1.miles_traveled+truck2.miles_traveled+truck3.miles_traveled,"miles")

def the_algo(trucks):
    for truck in trucks:
        #truck.miles_traveled = 0
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

            shortest_distance = 8000
        
        #Truck returns to the hub. Set the truck's address to the hub.
        truck.miles_traveled += truck_return(truck,"4001 South 700 East")
        truck.current_address = "4001 South 700 East"
            
        print("List:",sorted_list)    
        #truck.package_list = sorted_list
                
            


    
class Main:
    load_package_info()
    running = True
    print("WGUPS Delivery System")
    while running:
        print("\nSelect an option (type in the number to proceed):\n")
        print("1. Deliver packages              4. def find distance")
        print("2. distance data                 5. View total truck driving miles")
        print("3. Lookup package info           6. Exit\n")

        choice = str(input())

        match choice:
            case "1":
                the_algo(truck_list)
            case "2":
                print(distance_data)          
            case "3":
                #MAYBE add in an exit condition so you can stay in case 3 if input is invalid
                print("\nType in a Package ID...")
                lookup_id = int(input())
                lookup_package_info(lookup_id)
            case "4":
                print(find_distance(1,15))
            case "5":
                get_truck_miles(0)
            case "6":
                print("Exiting...")
                running = False
                raise SystemExit
            case _:
                print("Please type a valid option.\n")