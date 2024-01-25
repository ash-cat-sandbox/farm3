from actions import menu
from actions import planted_crops

def main():
    print('Welcome to the farm game. A text based game.' +
          ' Try to keep your crops alive and get money')

    game = input('What would you like to do?\n' + 
                    '1. Start game\n' +
                    '2. Exit game\n')
        
    match game:
        case '1':
            menu()
        case '2':
            exit()
    
    while True:
        for i in planted_crops:
            if i.name == "Potatoes":
                i.water += 1
            #if planted_crops[i].name == "Potatoes":
              #  print("Your Potato crop needs water")

        menu()






if __name__ == '__main__':
    main()