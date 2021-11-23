# Programmers: Sebastian Silguero
# Course: CS151, Dr. Rajeev
# Programming Assignment: 5
# Program Inputs: Two trip files, function, date, payment method, longitude and latitude, max distance from chosen location, file name, and choice of continuation.
# Program Outputs: Average cost from cash or credit card, total amount of trips from specific date, created file containing the output

# Importing math module
import math

# Declare the index file
ID = 1
StartTime = 2
EndTime = 3
Duration = 4
Distance = 5
TotalCost = 6
PaymentMethod = 7
Company = 8
LatitudePickUp = 9
LongitudePickUp = 10
LatitudeDropOff = 11
LongitudeDropOff = 12


# Make list of list
def list_of_list(filename):
    taxi_info = []
    try:
        file = open(filename, "r")
        line_count = 1
        for line in file:
            try:
                line_count += 1

                line_data = line.split(",")

                line_data[ID] = (line_data[ID])
                line_data[StartTime] = int(line_data[StartTime])
                line_data[EndTime] = int(line_data[EndTime])
                line_data[TotalCost] = float(line_data[TotalCost])
                line_data[PaymentMethod] = line_data[PaymentMethod].strip()
                line_data[Company] = int(line_data[Company])
                line_data[LatitudePickUp] = float(line_data[LatitudePickUp])
                line_data[LongitudePickUp] = float(line_data[LongitudePickUp])
                line_data[LatitudeDropOff] = float(line_data[LatitudeDropOff])
                line_data[LongitudeDropOff] = float(line_data[LongitudeDropOff])

                taxi_info.append(line_data)
            except ValueError:
                print(line_data)
        file.close()
    except FileNotFoundError:
        print("error: File", filename, "not found")
    return taxi_info


def average_cost(list_of_list, payment_method):
    total_cost = 0
    line_counter = 0

    for line in list_of_list:
        if list_of_list[7][PaymentMethod] == payment_method:
            cost_of_trip = list_of_list[7][TotalCost]
            total_cost += cost_of_trip
            line_counter += 1

    average_cost = total_cost / line_counter
    average_cost = round(average_cost, 2)
    return average_cost


def trip_tracker(list_of_list, date):
    day_trips = 0
    line_counter = 0

    for line in list_of_list:
        if line[StartTime] == line[EndTime] == date:
            day_trips += 1
            line_counter += 1

    return day_trips


def find_distance(lat1, lon1, lat2, lon2):
    lat1 = float(lat1)
    lon1 = float(lon1)
    lat2 = float(lat2)
    lon2 = float(lon2)
    lat1 = math.radians(lat1)
    lat2 = math.radians(lat2)
    lon1 = math.radians(lon1)
    lon2 = math.radians(lon2)
    total_distance = math.acos(
        math.sin(lat1) * math.sin(lat2) + math.cos(lat1) * math.cos(lat2) * math.cos(lon1 - lon2)) * 3959

    return total_distance


def total_distance(list_of_list):
    starting_distance = float(input("How many miles is the trip? >"))

    lat1 = float(input("Where is your starting latitude? >"))
    lon1 = float(input("Where is your starting longitude? >"))

    if not (starting_distance >= 0):
        print("Error: This is an invalid input")
        starting_distance = float(input("How many miles is the trip? >"))

    if not (-90 <= lat1 <= 90):
        print("This is an invalid input")
        lat1 = float(input("Where is your starting latitude? >"))

    if not (-90 <= lon1 <= 90):
        print("This is an invalid input")
        lon1 = float(input("Where is your starting longitude? >"))

    user_file = input("What would you like to name this file: ")


def main():
    choice = input("Would you like to load data from September or October? >")
    choice = choice.lower().strip()

    if choice == "september":
        taxi_month = list_of_list("2016_09.csv")
    elif choice == "october":
        taxi_month = list_of_list("2016_10.csv")
    else:
        print("Error: Invalid month")

    print("Average Cost, Total Distance, Specific Date")
    task = input("Which part of the data would you like to find? > ")
    task = task.strip().lower()

    if task == "average cost":
        payment_method = input("Cash or Credit Card: ")
        average_cost(list_of_list, payment_method)
    elif task == "total distance":
        total_distance(list_of_list)
    elif task == "specific date":
        date = input("Please input a date (year/month/day")
        trip_tracker(list_of_list, date)

    second_task = input("Would you like to do something else? >")
    second_task = second_task.strip().lower()

    if second_task == "yes":
        task = input("Which part of the data would you like to find? > ")
        task = task.strip().lower()
    elif second_task == "no":
        print("Thanks for using code")
    else:
        second_task = input("Would you like to do something else? >")
        second_task = second_task.strip().lower()


main()
