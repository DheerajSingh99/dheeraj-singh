def register_vehicle(vehicles, vehicle_number, vehicle_type):
    vehicles[vehicle_number] = {"type": vehicle_type, "slot": None}
    print("Vehicle registered successfully.")


def show_slots(slots, vehicles):
    print("\n---------- PARKING SLOTS ----------")
    
    for slot, vehicle in slots.items():
        if vehicle is None:
            print(slot, "-> Available")
        else:
            print(slot, "->", vehicle, "(", vehicles[vehicle]["type"], ")")


def park_vehicle(vehicles, slots, vehicle_number):
    if vehicle_number not in vehicles:
        print("Vehicle is not registered.")
        return

    if vehicles[vehicle_number]["slot"] is not None:
        print("Vehicle is already parked.")
        return

    for slot in slots:
        if slots[slot] is None:
            slots[slot] = vehicle_number 
            vehicles[vehicle_number]["slot"] = slot 
            print("Vehicle parked successfully.")
            print("Parking Slot:", slot)
            return

    print("No parking slot available.")


def remove_vehicle(vehicles, slots, vehicle_number):
    if vehicle_number not in vehicles:
        print("Vehicle not found.")
        return None

    assigned_slot = vehicles[vehicle_number]["slot"]
    if assigned_slot is None:
        print("Vehicle is not parked.")
        return None
 
    slots[assigned_slot] = None
    vehicles[vehicle_number]["slot"] = None
    print("Vehicle removed from slot:", assigned_slot)
    return assigned_slot
