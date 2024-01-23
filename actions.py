from crops import Crop, Potatoes


planted_crops = []

def menu():
    if planted_crops: 
        for i in planted_crops:
            i.water += 1
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
                    c1 = Potatoes('Potatoes', 'Temperate')
                    planted_crops.append(c1)
                    print(c1.name + " do well in a " + c1.region + " region")
                    planted_crops.append(c1)
            
