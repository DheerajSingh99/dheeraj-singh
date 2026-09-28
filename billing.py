def calculate_bill(hours, vehicle_type):
    if vehicle_type == "Car":
        rate = 100
    elif vehicle_type == "Bike":
        rate = 50
    else:
        rate = 30

    return hours * rate


def show_bill(vehicle_number, vehicle_type, hours, amount):
    print("\n========== PARKING BILL ==========")
    print("Vehicle Number :", vehicle_number)
    print("Vehicle Type   :", vehicle_type)
    print("Parking Hours  :", hours)
    print("Total Amount   : ₹", amount)
    print("==================================")
