planted_crops = [{}]
def menu():
    choice = input('What would you like to do?\n' + 
                   '1. Add crop\n' +
                   '2. Crop status\n')
    
    match choice:
        case '1':
            crop = input("What crop would you like to plant?\n" +
                         '1. Potatoes\n' +
                         '2. Tomatoes\n')
            match crop:
                case '1':
                    print("\nYou decided to plant potatoes.")

            