from crops import Crop, Potatoes


planted_crops = []
potatoes = {}
field = {}

def menu():
    
    choice = input('What would you like to do?\n' + 
                   '1. Add crop\n' +
                   '2. Crop status\n' +
                   '4. Exit Game\n')
    
    if choice == '1':
        crop = input("What crop would you like to plant?\n" +
                         '1. Potatoes\n' +
                         '2. Tomatoes\n')
        if crop == '1':
            c1 = Potatoes('Potatoes', 'Temperate')
            # 
            c1.location = 1
            planted_crops.append(c1)
            print(f"\nYou decided to plant potatoes in field {c1.location}.")
            print(c1.name + " do well in a " + c1.region + " region")
                  
                    
    elif choice == '2':
        for i in planted_crops:
            print("You have planted: ", i.name, " in field", i.location)
                
            if i.name == "Potatoes":
                if i.water >= 2:
                    print("Your Potatoes look a little dry")
                else:
                    print("Your crops look great!")
    elif choice == '4':
        exit()
            
