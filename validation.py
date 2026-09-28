import re


def vehicle_number(number):
    if not isinstance(number, str):
        return False

    number = number.strip().upper()
    return bool(re.fullmatch(r"[A-Z]{2}[0-9]{2}[A-Z]{2}[0-9]{4}", number))


def menu_choice(message, minimum, maximum):
    while True:
        choice = input(message)
        
        if choice.isdigit():
            choice = int(choice)
            
            if minimum <= choice <= maximum:
                return choice
            else:
                print("Enter a choice between", minimum, "and", maximum)
        else:
            print("Please enter a valid number.")