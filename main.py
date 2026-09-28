from validation import vehicle_number, menu_choice
from parking import register_vehicle, show_slots, park_vehicle, remove_vehicle
from billing import calculate_bill, show_bill


def main():
    vehicles = {}
    slots = {"P1": None, "P2": None, "P3": None, "P4": None, "P5": None}

    while True:
        print("\n================================")
        print("    PARKING MANAGEMENT SYSTEM")
        print("================================")
        print("1. Register Vehicle")
        print("2. Park Vehicle")
        print("3. Show Parking Slots")
        print("4. Vehicle Exit")
        print("5. Exit")
        print("================================")

        choice = menu_choice("Enter your choice: ", 1, 5)

        if choice == 1:
            plate_number = input("Enter vehicle number (e.g. MP04BA4321): ").strip().upper()

            if not vehicle_number(plate_number):
                print("Invalid vehicle number.")
                continue

            if plate_number in vehicles:
                print("Vehicle already registered.")
                continue

            print("\n1. Car\n2. Bike\n3. Auto")
            vehicle_choice = menu_choice("Select vehicle type: ", 1, 3)

            if vehicle_choice == 1:
                vehicle_type = "Car"
            elif vehicle_choice == 2:
                vehicle_type = "Bike"
            else:
                vehicle_type = "Auto"

            register_vehicle(vehicles, plate_number, vehicle_type)

    
        elif choice == 2:
                        plate_number = input("Enter vehicle number: ").strip().upper()
                        park_vehicle(vehicles, slots, plate_number)
            

        elif choice == 3:
            show_slots(slots, vehicles)


        elif choice == 4:
            plate_number = input("Enter vehicle number: ").strip().upper()

            if plate_number not in vehicles:
                print("Vehicle not found.")
                continue

            vehicle = vehicles[plate_number]

            if vehicle["slot"] is None:
                print("Vehicle is not parked.")
                continue

            hours_input = input("Enter parking duration in hours: ")

            if hours_input.replace('.', '', 1).isdigit():
                hours = float(hours_input)
                if hours <= 0:
                    print("Hours must be greater than zero.")
                    continue
            else:
                print("Please enter a valid number.")
                continue

            amount = calculate_bill(hours, vehicle["type"])
            slot = remove_vehicle(vehicles, slots, plate_number)

            if slot is not None:
                show_bill(plate_number, vehicle["type"], hours, amount)
                print("Released Slot:", slot)

        elif choice == 5:
            print("\nThank you for using Parking Management System!")
            break


if __name__ == "__main__":
    main()
