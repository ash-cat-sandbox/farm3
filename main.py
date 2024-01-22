from actions import menu

def main():
    print('Welcome to the farm game. A text based game.' +
          ' Try to keep your crops alive and get money')
    
    while True:
        print('What would you like to do? \n')

        game = input('What would you like to do?\n' + 
                    '1. Start game\n' +
                    '2. Exit game\n')
        
        match game:
            case '1':
                menu()
            case '2':
                exit()






if __name__ == '__main__':
    main()